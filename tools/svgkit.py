import re
import html
from PIL import ImageFont

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


def tier_board_svg(rows, title):

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


