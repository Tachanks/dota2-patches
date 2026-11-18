"""Builds a colorful GitHub README for a patch folder: SVG tier boards, SVG build cards, emoji markers and GitHub alerts.

Usage: python3 -I make_md.py <index_html> <out_dir>
Writes <out_dir>/README.md and <out_dir>/img/*.svg
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from builds import BUILDS  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from PIL import ImageFont  # noqa: E402

index_html, out_dir = sys.argv[1:3]
img_dir = os.path.join(out_dir, "img")
os.makedirs(os.path.join(img_dir, "builds"), exist_ok=True)

soup = BeautifulSoup(open(index_html, encoding="utf-8").read(), "html.parser")

FONT_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
_fonts = {}


def tw(text, size):
    """Approximate rendered width of bold sans text, padded for Segoe/Helvetica differences."""
    if size not in _fonts:
        _fonts[size] = ImageFont.truetype(FONT_B, size)
    return _fonts[size].getlength(text) * 1.07


def esc(s):
    return html.escape(s, quote=True)


TIER_FILL = {"S": "#cf462e", "A": "#e09a2e", "B": "#4f9440", "C": "#4279a8", "X": "#757b84"}
TIER_INK = {"S": "#ffffff", "A": "#1c1406", "B": "#ffffff", "C": "#ffffff", "X": "#ffffff"}

SVG_STYLE = """<style>
.card{fill:#ffffff;stroke:#d8dbd5}
.pill{fill:#f2f3f0;stroke:#d8dbd5}
.ink{fill:#16191d}
.muted{fill:#5b6168}
.sep{stroke:#d8dbd5}
.up{fill:#2d8540}.down{fill:#b8352a}.steady{fill:#687079}.rework{fill:#7448ab}
.rec{fill:#2d8540}.alt{fill:#3c6f9a}
.arrow{stroke:#8a9099;fill:none}
@media (prefers-color-scheme: dark){
.card{fill:#1a1d22;stroke:#2b3037}
.pill{fill:#111317;stroke:#2b3037}
.ink{fill:#e6e8eb}
.muted{fill:#9ba2ab}
.sep{stroke:#2b3037}
.up{fill:#5cc46f}.down{fill:#ef6c60}.steady{fill:#9ba2ab}.rework{fill:#ad8ae3}
.rec{fill:#3f9a52}.alt{fill:#4f88b8}
.arrow{stroke:#6f767f}
}
text{font-family:'Segoe UI',Helvetica,Arial,sans-serif;font-weight:700}
</style>"""


def trend_shape(kind, cx, cy):
    if kind == "up":
        return f'<path class="up" d="M{cx-6},{cy+5} L{cx},{cy-6} L{cx+6},{cy+5} Z"/>'
    if kind == "down":
        return f'<path class="down" d="M{cx-6},{cy-5} L{cx},{cy+6} L{cx+6},{cy-5} Z"/>'
    if kind == "steady":
        return f'<circle class="steady" cx="{cx}" cy="{cy}" r="5"/>'
    return (f'<path class="rework" d="M{cx},{cy-7} L{cx+2},{cy-2} L{cx+7},{cy} L{cx+2},{cy+2} '
            f'L{cx},{cy+7} L{cx-2},{cy+2} L{cx-7},{cy} L{cx-2},{cy-2} Z"/>')


# ---------------- Tier board SVGs ----------------
W = 960


def tier_board_svg(sec_id, title):
    sec = soup.select_one(f"#{sec_id}")
    rows = []
    for tier in sec.select(".tier"):
        letter = [c for c in tier["class"] if c != "tier"][0]
        heroes = []
        for h in tier.select(".hero"):
            kind = [c for c in h.select_one(".tag")["class"] if c != "tag"][0]
            heroes.append((h.select_one(".nm").get_text(strip=True), kind))
        rows.append((letter, heroes))

    LEFT, PADX, PADY, PH, GAP, RGAP = 66, 14, 12, 34, 8, 10
    parts, y = [], 0
    for letter, heroes in rows:
        # wrap pills
        x0 = LEFT + PADX
        maxx = W - PADX
        lines, cur, x = [], [], x0
        for name, kind in heroes:
            pw = 14 + tw(name, 15) + 8 + 14 + 12
            if cur and x + pw > maxx:
                lines.append(cur)
                cur, x = [], x0
            cur.append((name, kind, x, pw))
            x += pw + GAP
        if cur:
            lines.append(cur)
        rh = max(70, PADY * 2 + len(lines) * PH + (len(lines) - 1) * GAP)
        parts.append(f'<rect class="card" x="0.5" y="{y+0.5}" width="{W-1}" height="{rh-1}" rx="10"/>')
        fill, ink = TIER_FILL[letter], TIER_INK[letter]
        parts.append(f'<path fill="{fill}" d="M10.5,{y+0.5} H{LEFT} V{y+rh-0.5} H10.5 A10,10 0 0 1 0.5,{y+rh-10.5} V{y+10.5} A10,10 0 0 1 10.5,{y+0.5} Z"/>')
        if letter == "X":
            cx, cy = LEFT / 2, y + rh / 2
            parts.append(f'<text x="{cx}" y="{cy}" fill="{ink}" font-size="15" letter-spacing="2" text-anchor="middle" dominant-baseline="central" transform="rotate(-90 {cx} {cy})">AVOID</text>')
        else:
            parts.append(f'<text x="{LEFT/2}" y="{y+rh/2}" fill="{ink}" font-size="36" text-anchor="middle" dominant-baseline="central">{letter}</text>')
        for i, line in enumerate(lines):
            py = y + PADY + i * (PH + GAP)
            for name, kind, px, pw in line:
                parts.append(f'<rect class="pill" x="{px:.1f}" y="{py}" width="{pw:.1f}" height="{PH}" rx="{PH/2}"/>')
                parts.append(f'<text class="ink" x="{px+14:.1f}" y="{py+PH/2}" font-size="15" dominant-baseline="central">{esc(name)}</text>')
                parts.append(trend_shape(kind, round(px + pw - 20, 1), py + PH / 2))
        y += rh + RGAP

    # legend
    lx = 4
    ly = y + 12
    for kind, label in (("up", "Up"), ("down", "Down"), ("steady", "Steady"), ("rework", "Rework")):
        parts.append(trend_shape(kind, lx + 7, ly))
        parts.append(f'<text class="muted" x="{lx+20}" y="{ly}" font-size="13" dominant-baseline="central">{label}</text>')
        lx += 20 + tw(label, 13) + 22
    H = ly + 14
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
           f'aria-label="{esc(title)}"><title>{esc(title)}</title>{SVG_STYLE}{"".join(parts)}</svg>')
    return svg


for sec_id, fname, title in (("carry", "pos1-tiers.svg", "Position 1 tier list for patch 7.42"),
                             ("mid", "pos2-tiers.svg", "Position 2 tier list for patch 7.42"),
                             ("off", "pos3-tiers.svg", "Position 3 tier list for patch 7.42")):
    open(os.path.join(img_dir, fname), "w", encoding="utf-8").write(tier_board_svg(sec_id, title))


# ---------------- Build card SVGs ----------------
def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def arrow(x, cy):
    return f'<path class="arrow" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="M{x},{cy} H{x+12} M{x+8},{cy-4} L{x+12},{cy} L{x+8},{cy+4}"/>'


def build_svg(b):
    PAD, PH, GAP, AW = 16, 30, 6, 22
    parts = []
    y = PAD
    fill, ink = TIER_FILL[b["tier"]], TIER_INK[b["tier"]]
    parts.append(f'<rect x="{PAD}" y="{y}" width="30" height="30" rx="6" fill="{fill}"/>')
    parts.append(f'<text x="{PAD+15}" y="{y+15}" fill="{ink}" font-size="19" text-anchor="middle" dominant-baseline="central">{b["tier"]}</text>')
    parts.append(f'<text class="ink" x="{PAD+42}" y="{y+15}" font-size="22" dominant-baseline="central">{esc(b["hero"])}</text>')
    y += 30 + 14
    for key, label, cls in (("rec", "RECOMMENDED", "rec"), ("alt", "ALTERNATIVE", "alt")):
        p = b[key]
        parts.append(f'<line class="sep" x1="{PAD}" x2="{W-PAD}" y1="{y}" y2="{y}"/>')
        y += 12
        tagw = tw(label, 12) + 18
        parts.append(f'<rect class="{cls}" x="{PAD}" y="{y}" width="{tagw:.1f}" height="24" rx="5"/>')
        parts.append(f'<text x="{PAD+tagw/2:.1f}" y="{y+12}" fill="#ffffff" font-size="12" letter-spacing="0.6" text-anchor="middle" dominant-baseline="central">{label}</text>')
        parts.append(f'<text class="ink" x="{PAD+tagw+10:.1f}" y="{y+12}" font-size="16" dominant-baseline="central">{esc(p["name"])}</text>')
        y += 24 + 10
        x = PAD
        for i, item in enumerate(p["items"]):
            pw = tw(item, 14) + 24
            need = pw + (AW if i else 0)
            if x + need > W - PAD and x > PAD:
                x = PAD
                y += PH + GAP
            elif i:
                parts.append(arrow(x + 5, y + PH / 2))
                x += AW
            parts.append(f'<rect class="pill" x="{x:.1f}" y="{y}" width="{pw:.1f}" height="{PH}" rx="{PH/2}"/>')
            parts.append(f'<text class="ink" x="{x+12:.1f}" y="{y+PH/2}" font-size="14" dominant-baseline="central">{esc(item)}</text>')
            x += pw
        y += PH + 14
    H = y + 2
    card = f'<rect class="card" x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10"/>'
    title = f'{b["hero"]} builds for patch 7.42'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="{esc(title)}"><title>{esc(title)}</title>{SVG_STYLE}{card}{"".join(parts)}</svg>')


for b in BUILDS:
    open(os.path.join(img_dir, "builds", slug(b["hero"]) + ".svg"), "w", encoding="utf-8").write(build_svg(b))


# ---------------- Markdown ----------------
def txt(el):
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).replace(" ,", ",").replace(" .", ".").strip()


TIER_SQ = {"S": "🟥", "A": "🟧", "B": "🟩", "C": "🟦", "X": "⬛"}
TREND = {"up": "🟢 ▲ Up", "down": "🔴 ▼ Down", "steady": "⚪ ● Steady", "rework": "🟣 ✦ Rework"}

md = []
md.append(f"# {txt(soup.h1)}\n")
md.append(txt(soup.select_one(".lede")) + "\n")
md.append(" ".join(f"`{txt(c)}`" for c in soup.select(".chips span.chip")) + "\n")
md.append("**Jump to:** [Short version](#the-short-version) · [Pos 1](#position-1) · [Pos 1 builds](#pos-1-builds) · "
          "[Pos 2](#position-2) · [Pos 3](#position-3) · [Items](#items) · [Neutrals](#neutral-items) · "
          "[Patch breakdown](#patch-breakdown) · [Sources](#sources-and-method) · [Support tier list (pos 4–5)](supports/README.md)\n")
md.append("> [!NOTE]\n> `index.html` in this folder is the same guide as a standalone page. Download it and open it in a browser if you want it offline.\n")

# Short version
s = soup.select_one("#short")
md.append(f"## {txt(s.h2)}\n")
md.append(txt(s.select_one(".sub")) + "\n")
for i, p in enumerate(s.select(".short .pt"), 1):
    md.append(f"{i}. {txt(p)}")
md.append("")
md.append("> [!IMPORTANT]\n> **First picks**  ")
picks = [f"**{txt(pk.select_one('.role')).replace(' first picks', '')}:** {txt(pk.select_one('.names'))}" for pk in s.select(".pick")]
md.append("\n".join("> " + p + "  " for p in picks))
md.append("")


def tier_section(sec_id, img):
    sec = soup.select_one(f"#{sec_id}")
    out = [f"## {txt(sec.h2)}\n", txt(sec.select_one(".sub")) + "\n",
           f"![{txt(sec.h2)} tier list overview](img/{img})\n",
           "<sub>🟢 ▲ Up = better than in 7.41f · 🔴 ▼ Down = worse · ⚪ ● Steady = small or offsetting changes · 🟣 ✦ Rework = test before ranked</sub>\n"]
    for tier in sec.select(".tier"):
        letter = [c for c in tier["class"] if c != "tier"][0]
        heading = "Avoid" if letter == "X" else f"{letter} tier"
        out.append(f"### {TIER_SQ[letter]} {heading}\n")
        for h in tier.select(".hero"):
            kind = [c for c in h.select_one(".tag")["class"] if c != "tag"][0]
            out.append(f"- **{txt(h.select_one('.nm'))}** · {TREND[kind]} · <sub>{txt(h.select_one('.base'))}</sub>  \n  {txt(h.select_one('p'))}")
        out.append("")
    co = sec.select_one(".callout")
    if co:
        body = txt(co).replace("Test in unranked first:", "").strip()
        out.append(f"> [!WARNING]\n> **Test in unranked first.** {body}\n")
    return out


md += tier_section("carry", "pos1-tiers.svg")

# Builds
bs = soup.select_one("#builds")
md.append("## Pos 1 builds\n")
md.append(txt(bs.select_one(".sub")) + "\n")
for b in BUILDS:
    md.append(f"### {TIER_SQ[b['tier']]} {b['hero']}\n")
    md.append(f"![{b['hero']} recommended and alternative builds](img/builds/{slug(b['hero'])}.svg)\n")
    md.append(f"**Start:** {b['start']}\n")
    md.append(f"🟢 **Recommended, {b['rec']['name']}.** {b['rec']['note']}\n")
    md.append(f"🔵 **Alternative, {b['alt']['name']}.** {b['alt']['note']}\n")

md += tier_section("mid", "pos2-tiers.svg")
md += tier_section("off", "pos3-tiers.svg")

# Items
it = soup.select_one("#items")
md.append(f"## {txt(it.h2)}\n")
md.append(txt(it.select_one(".sub")) + "\n")
PANEL_MARK = {"Pos 1: buy more": "🟢", "Pos 2": "🔵", "Got worse": "🔴", "Pos 3": "🟠"}
for panel in it.select(".panel"):
    for child in panel.find_all(["h3", "ul"], recursive=False):
        if child.name == "h3":
            small = child.find("small")
            small_txt = txt(small) if small else ""
            if small:
                small.extract()
            head = txt(child)
            mark = PANEL_MARK.get(head, "")
            md.append(f"### {mark} {head}".replace("  ", " ") + (f" <sub>({small_txt})</sub>" if small_txt else "") + "\n")
        else:
            for li in child.select("li"):
                name = txt(li.select_one(".iname"))
                cost = li.select_one(".cost")
                body = re.sub(r"\s+", " ", li.get_text(" ", strip=True))[len(name):].strip()
                if cost:
                    body = body[len(txt(cost)):].strip()
                cost_txt = f" `{txt(cost)}`" if cost else ""
                md.append(f"- **{name}**{cost_txt}: {body}")
            md.append("")

# Neutrals
ne = soup.select_one("#neutrals")
md.append(f"## {txt(ne.h2)}\n")
md.append(txt(ne.select_one(".sub")) + "\n")
tbl = ne.select_one("table.pools")
heads = [txt(th) for th in tbl.select("thead th")]
md.append("| " + " | ".join(heads) + " |")
md.append("|" + "---|" * len(heads))
for i, tr in enumerate(tbl.select("tbody tr")):
    cells = []
    for j, cell in enumerate(tr.find_all(["th", "td"])):
        for b_ in cell.find_all("b"):
            b_.replace_with(f"**{b_.get_text()}**")
        c = re.sub(r"\s+", " ", cell.get_text(" ", strip=True))
        cells.append(f"**{c}**" if j == 0 else c)
    md.append("| " + " | ".join(cells) + " |")
md.append("\n<sub>Bold entries are the best picks for cores.</sub>\n")


def sys_block(blk):
    out = [f"### {txt(blk.h3)}\n"]
    for child in blk.find_all(["p", "ul", "div", "table"], recursive=False):
        if child.name == "p":
            t = txt(child)
            if "foryou" in (child.get("class") or []):
                out.append("> [!TIP]\n> " + t.replace("For you:", "**For you:**", 1) + "\n")
            else:
                out.append(t + "\n")
        elif child.name == "ul":
            for li in child.select("li"):
                out.append(f"- {txt(li)}")
            out.append("")
        else:
            t = child if child.name == "table" else child.find("table")
            if t is None:
                continue
            hs = [txt(th) for th in t.select("thead th")]
            out.append("| " + " | ".join(hs) + " |")
            out.append("|" + "|".join("---:" if k >= 2 else "---" for k in range(len(hs))) + "|")
            for tr in t.select("tbody tr"):
                tds = [txt(td) for td in tr.find_all("td")]
                out.append("| " + " | ".join(tds) + " |")
            out.append("")
    return out


for blk in ne.select(".sys"):
    md += sys_block(blk)

pb = soup.select_one("#patch")
md.append(f"## {txt(pb.h2)}\n")
md.append(txt(pb.select_one(".sub")) + "\n")
for blk in pb.select(".sys"):
    md += sys_block(blk)

ft = soup.select_one("#sources")
md.append(f"## {txt(ft.h2)}\n")
md.append(txt(ft.find('p')) + "\n")
for a in ft.select("li a"):
    md.append(f"- [{txt(a)}]({a['href']})")
md.append("")

text = re.sub(r"\n{3,}", "\n\n", "\n".join(md))
open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8").write(text)
print("ok", len(text))
