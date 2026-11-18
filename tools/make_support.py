"""Builds the 7.42 support page: HTML, GitHub README and SVG graphics.

Usage: python3 -I make_support.py <core_index_html> <out_dir> <core_link_for_html>
Writes <out_dir>/index.html, <out_dir>/README.md, <out_dir>/img/*.svg
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import support_data as D  # noqa: E402
from svgkit import tier_board_svg, build_svg, slug  # noqa: E402

core_html, out_dir, core_link = sys.argv[1:4]
os.makedirs(os.path.join(out_dir, "img", "builds"), exist_ok=True)


def e(s):
    return html.escape(s, quote=False)


TREND_TAG = {"up": ("up", "▲ Up"), "down": ("down", "▼ Down"), "steady": ("steady", "● Steady"), "rework": ("rework", "✦ Rework")}
TIER_ORDER = ["S", "A", "B", "C", "X"]

# ---------- HTML ----------
style = re.search(r"<style>.*?</style>", open(core_html, encoding="utf-8").read(), re.S).group(0)
style = style.replace("</style>", """
.callout.fill { border-color: var(--b); border-style: solid; border-left-width: 4px; }
.callout.fill b { color: var(--b); }
</style>""")


def board_html(tiers):
    rows = []
    for t in TIER_ORDER:
        heroes = tiers.get(t, [])
        if not heroes:
            continue
        cards = []
        for name, kind, base, why in heroes:
            cls, label = TREND_TAG[kind]
            cards.append(f'      <div class="hero"><div class="hd"><span class="nm">{e(name)}</span><span class="tag {cls}">{label}</span></div>'
                         f'<div class="base">{e(base)}</div><p>{e(why)}</p></div>')
        letter = "Avoid" if t == "X" else t
        rows.append(f'    <div class="tier {t}"><div class="letter">{letter}</div><div class="heroes">\n' + "\n".join(cards) + "\n    </div></div>")
    return '  <div class="board">\n' + "\n\n".join(rows) + "\n  </div>"


def chain(items):
    return '<ol class="chain">' + "".join(f"<li><span>{e(i)}</span></li>" for i in items) + "</ol>"


def builds_html(builds):
    out = []
    for b in builds:
        out.append(f'''    <article class="build">
      <div class="bh"><span class="tierchip {b["tier"]}" title="{b["tier"]} tier">{b["tier"]}</span><h3>{e(b["hero"])}</h3></div>
      <div class="start"><b>Start:</b> {e(b["start"])}</div>
      <div class="path rec"><div class="plabel"><span>Recommended</span> · {e(b["rec"]["name"])}</div>{chain(b["rec"]["items"])}<p>{e(b["rec"]["note"])}</p></div>
      <div class="path alt"><div class="plabel"><span>Alternative</span> · {e(b["alt"]["name"])}</div>{chain(b["alt"]["items"])}<p>{e(b["alt"]["note"])}</p></div>
    </article>''')
    return '  <div class="buildgrid">\n' + "\n".join(out) + "\n  </div>"


LEGEND = '''  <div class="legend">
    <span><span class="tag up">▲ Up</span> better than in 7.41f</span>
    <span><span class="tag down">▼ Down</span> worse than in 7.41f</span>
    <span><span class="tag steady">● Steady</span> small or offsetting changes</span>
    <span><span class="tag rework">✦ Rework</span> needs testing before ranked</span>
  </div>'''


def md_bold_to_html(s):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e(s))


items_html = []
for title, small, entries in D.ITEMS:
    lis = "".join(f'<li><span class="iname">{e(n)}</span>' + (f'<span class="cost">{e(c)}</span>' if c else "") + f"<br>{e(t)}</li>" for n, c, t in entries)
    items_html.append(f'    <div class="panel">\n      <h3>{e(title)} <small>{e(small)}</small></h3>\n      <ul class="items">{lis}</ul>\n    </div>')

pool_rows = "".join(f"<tr><th>{e(t)}</th>" + "".join(f"<td>{md_bold_to_html(c)}</td>" for c in cols) + "</tr>" for t, cols in D.NEUTRAL_POOLS)
neutral_notes = "".join(f'<div class="sys"><h3>{e(h)}</h3><ul>' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul></div>" for h, items in D.NEUTRAL_NOTES)

sys_html = []
for h, paras, bullets, foryou in D.SYSTEMS:
    block = f'    <div class="sys">\n      <h3>{e(h)}</h3>\n' + "".join(f"      <p>{e(p)}</p>\n" for p in paras)
    if bullets:
        block += "      <ul>" + "".join(f"<li>{e(b)}</li>" for b in bullets) + "</ul>\n"
    block += f'      <p class="foryou">{e(foryou)}</p>\n    </div>'
    sys_html.append(block)

LEDE = ("A day-one read of 7.42 for pos 4 and pos 5, written for a core player who fills support. The tiers start from where each hero "
        "stood at the end of 7.41f in high-MMR pubs, then move up or down based on what the 7.42 notes changed. Real 7.42 win rates "
        "need a few days of games, so check the stats again by the weekend.")

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Patch 7.42 Support Tier List</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
{style}
</head>
<body>

<header class="top">
  <div class="wrap">
    <div class="kicker">Patch 7.41f to 7.42 · Support roles</div>
    <h1>Patch 7.42 Support Tier List</h1>
    <p class="lede">{e(LEDE)}</p>
    <div class="chips">
      <span class="chip">7.42 released Nov 18, 2026</span>
      <span class="chip">7.41f baseline: Dota2ProTracker, 7000+ MMR, last 8 days</span>
      <span class="chip">Focus: pos 4 and pos 5</span>
      <a class="chip" href="{e(core_link)}">Core tier list (pos 1–3)</a>
    </div>
  </div>
</header>

<nav class="jump" aria-label="Sections">
  <div class="wrap">
    <a href="#short">Short version</a>
    <a href="#pos4">Pos 4</a>
    <a href="#pos4-builds">Pos 4 builds</a>
    <a href="#pos5">Pos 5</a>
    <a href="#pos5-builds">Pos 5 builds</a>
    <a href="#items">Items</a>
    <a href="#neutrals">Neutrals</a>
    <a href="#changes">Support changes</a>
    <a href="#sources">Sources</a>
  </div>
</nav>

<main class="wrap">

<section id="short">
  <h2>The short version</h2>
  <p class="sub">Six things that change how you play support this patch, and the picks I would queue first.</p>
  <div class="short">
{chr(10).join(f'    <div class="pt"><p>{e(t)}</p></div>' for t in D.SHORT)}
  </div>
  <div class="picks">
{chr(10).join(f'    <div class="pick"><div class="role">{e(r)}</div><div class="names">{e(n)}</div></div>' for r, n in D.PICKS)}
  </div>
  <div class="callout fill"><b>Filling support?</b> {e(D.FILL_NOTE)}</div>
</section>

<section id="pos4">
  <h2>Position 4</h2>
  <p class="sub">Soft support and roamer. Baselines are pos 4 numbers from the last 8 days of 7.41f at 7000+ MMR, with D2PT's 0–100 rating where it had one.</p>
{LEGEND}
{board_html(D.POS4)}
</section>

<section id="pos4-builds">
  <h2>Pos 4 builds</h2>
  <p class="sub">{e(D.BUILD_NOTE)}</p>
{builds_html(D.BUILDS4)}
</section>

<section id="pos5">
  <h2>Position 5</h2>
  <p class="sub">Hard support. Baselines are pos 5 numbers from the same 7.41f window.</p>
{board_html(D.POS5)}
  <div class="callout"><b>Test in unranked first:</b> {e(D.CALLOUT)}</div>
</section>

<section id="pos5-builds">
  <h2>Pos 5 builds</h2>
  <p class="sub">Same format as pos 4. Venomancer, Grimstroke and Ringmaster are also fine at pos 4 with the same builds.</p>
{builds_html(D.BUILDS5)}
</section>

<section id="items">
  <h2>Support items</h2>
  <p class="sub">Two new items are aimed at supports, and most of the save and aura items got cheaper or stronger. Spell amp and cast range items went the other way.</p>
  <div class="itemgrid">
{chr(10).join(items_html)}
  </div>
</section>

<section id="neutrals">
  <h2>Neutral items</h2>
  <p class="sub">Artifact tiers unlock at 0:00, 15:00, 30:00 and 50:00. Each game picks one artifact from each pool, so you'll see four options per tier. The bold ones are the best for supports.</p>
  <div class="tablewrap">
  <table class="pools">
    <thead><tr><th>Tier</th><th>Pool 1</th><th>Pool 2</th><th>Pool 3</th><th>Pool 4</th></tr></thead>
    <tbody>{pool_rows}</tbody>
  </table>
  </div>
  <div class="split" style="margin-top:14px">{neutral_notes}</div>
</section>

<section id="changes">
  <h2>Support changes in 7.42</h2>
  <p class="sub">The system changes behind the tiers, and what each one means when you're the support.</p>
  <div class="split">
{chr(10).join(sys_html)}
  </div>
</section>

<footer id="sources">
  <h2 style="color:var(--ink)">Sources and method</h2>
  <p>7.41f baselines come from Dota2ProTracker's meta page at 7000+ MMR for pos 4 and pos 5 over the last 8 days of 7.41f, read on November 18, 2026 just before 7.42 data replaced it. These are high-MMR numbers, and small samples are noted on each card. Tiers are my reading of the 7.42 notes on top of those baselines, so check them against real 7.42 data once a few days of games are in.</p>
  <ul>
    <li><a href="https://www.dota2.com/patches/7.42">Dota 2 patch notes, 7.42</a></li>
    <li><a href="https://www.dota2.com/patches/7.41f">Dota 2 patch notes, 7.41f</a></li>
    <li><a href="https://dota2protracker.com/meta">Dota2ProTracker meta (7.41f, 7000+ MMR)</a></li>
    <li><a href="{e(core_link)}">Patch 7.42 core tier list (pos 1–3)</a></li>
  </ul>
</footer>

</main>
</body>
</html>
'''
open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(page)

# ---------- SVGs ----------
def rows(tiers):
    return [(t, [(n, k) for n, k, _, _ in tiers[t]]) for t in TIER_ORDER if tiers.get(t)]


open(os.path.join(out_dir, "img", "pos4-tiers.svg"), "w", encoding="utf-8").write(tier_board_svg(rows(D.POS4), "Position 4 tier list for patch 7.42"))
open(os.path.join(out_dir, "img", "pos5-tiers.svg"), "w", encoding="utf-8").write(tier_board_svg(rows(D.POS5), "Position 5 tier list for patch 7.42"))
for b in D.BUILDS4 + D.BUILDS5:
    open(os.path.join(out_dir, "img", "builds", slug(b["hero"]) + ".svg"), "w", encoding="utf-8").write(build_svg(b))

# ---------- README ----------
TIER_SQ = {"S": "🟥", "A": "🟧", "B": "🟩", "C": "🟦", "X": "⬛"}
TREND_MD = {"up": "🟢 ▲ Up", "down": "🔴 ▼ Down", "steady": "⚪ ● Steady", "rework": "🟣 ✦ Rework"}
md = ["# Patch 7.42 Support Tier List\n", LEDE + "\n",
      "`7.42 released Nov 18, 2026` `7.41f baseline: Dota2ProTracker, 7000+ MMR, last 8 days` `Focus: pos 4 and pos 5`\n",
      "**Jump to:** [Short version](#the-short-version) · [Pos 4](#position-4) · [Pos 4 builds](#pos-4-builds) · [Pos 5](#position-5) · "
      "[Pos 5 builds](#pos-5-builds) · [Items](#support-items) · [Neutrals](#neutral-items) · [Support changes](#support-changes-in-742) · "
      "[Sources](#sources-and-method) · [Core tier list (pos 1–3)](../README.md)\n",
      "> [!NOTE]\n> `index.html` in this folder is the same guide as a standalone page. Download it and open it in a browser if you want it offline.\n",
      "## The short version\n", "Six things that change how you play support this patch, and the picks I would queue first.\n"]
md += [f"{i}. {t}" for i, t in enumerate(D.SHORT, 1)] + [""]
md.append("> [!IMPORTANT]\n> **First picks**  \n" + "\n".join(f"> **{r.replace(' first picks', '')}:** {n}  " for r, n in D.PICKS) + "\n")
md.append(f"> [!TIP]\n> **Filling support?** {D.FILL_NOTE}\n")


def tier_md(title, sub, tiers, img):
    out = [f"## {title}\n", sub + "\n", f"![{title} tier list overview](img/{img})\n",
           "<sub>🟢 ▲ Up = better than in 7.41f · 🔴 ▼ Down = worse · ⚪ ● Steady = small or offsetting changes · 🟣 ✦ Rework = test before ranked</sub>\n"]
    for t in TIER_ORDER:
        if not tiers.get(t):
            continue
        out.append(f"### {TIER_SQ[t]} {'Avoid' if t == 'X' else t + ' tier'}\n")
        for n, k, base, why in tiers[t]:
            out.append(f"- **{n}** · {TREND_MD[k]} · <sub>{base}</sub>  \n  {why}")
        out.append("")
    return out


def builds_md(title, sub, builds):
    out = [f"## {title}\n", sub + "\n"]
    for b in builds:
        out += [f"### {TIER_SQ[b['tier']]} {b['hero']}\n",
                f"![{b['hero']} recommended and alternative builds](img/builds/{slug(b['hero'])}.svg)\n",
                f"**Start:** {b['start']}\n",
                f"🟢 **Recommended, {b['rec']['name']}.** {b['rec']['note']}\n",
                f"🔵 **Alternative, {b['alt']['name']}.** {b['alt']['note']}\n"]
    return out


md += tier_md("Position 4", "Soft support and roamer. Baselines are pos 4 numbers from the last 8 days of 7.41f at 7000+ MMR, with D2PT's 0–100 rating where it had one.", D.POS4, "pos4-tiers.svg")
md += builds_md("Pos 4 builds", D.BUILD_NOTE, D.BUILDS4)
md += tier_md("Position 5", "Hard support. Baselines are pos 5 numbers from the same 7.41f window.", D.POS5, "pos5-tiers.svg")
md.append(f"> [!WARNING]\n> **Test in unranked first.** {D.CALLOUT}\n")
md += builds_md("Pos 5 builds", "Same format as pos 4. Venomancer, Grimstroke and Ringmaster are also fine at pos 4 with the same builds.", D.BUILDS5)

md.append("## Support items\n")
md.append("Two new items are aimed at supports, and most of the save and aura items got cheaper or stronger. Spell amp and cast range items went the other way.\n")
for title, small, entries in D.ITEMS:
    mark = "🟢" if title == "Buy more" else "🔴"
    md.append(f"### {mark} {title} <sub>({small})</sub>\n")
    md += [f"- **{n}**" + (f" `{c}`" if c else "") + f": {t}" for n, c, t in entries] + [""]

md.append("## Neutral items\n")
md.append("Artifact tiers unlock at 0:00, 15:00, 30:00 and 50:00. Each game picks one artifact from each pool, so you'll see four options per tier. The bold ones are the best for supports.\n")
md.append("| Tier | Pool 1 | Pool 2 | Pool 3 | Pool 4 |")
md.append("|---|---|---|---|---|")
md += [f"| **{t}** | " + " | ".join(cols) + " |" for t, cols in D.NEUTRAL_POOLS] + [""]
for h, items in D.NEUTRAL_NOTES:
    md += [f"### {h}\n"] + [f"- {x}" for x in items] + [""]

md.append("## Support changes in 7.42\n")
md.append("The system changes behind the tiers, and what each one means when you're the support.\n")
for h, paras, bullets, foryou in D.SYSTEMS:
    md.append(f"### {h}\n")
    md += [p + "\n" for p in paras]
    if bullets:
        md += [f"- {b}" for b in bullets] + [""]
    md.append("> [!TIP]\n> " + foryou.replace("For you:", "**For you:**", 1) + "\n")

md.append("## Sources and method\n")
md.append("7.41f baselines come from Dota2ProTracker's meta page at 7000+ MMR for pos 4 and pos 5 over the last 8 days of 7.41f, read on November 18, 2026 just before 7.42 data replaced it. These are high-MMR numbers, and small samples are noted on each card. Tiers are my reading of the 7.42 notes on top of those baselines, so check them against real 7.42 data once a few days of games are in.\n")
md += ["- [Dota 2 patch notes, 7.42](https://www.dota2.com/patches/7.42)",
       "- [Dota 2 patch notes, 7.41f](https://www.dota2.com/patches/7.41f)",
       "- [Dota2ProTracker meta (7.41f, 7000+ MMR)](https://dota2protracker.com/meta)",
       "- [Patch 7.42 core tier list (pos 1–3)](../README.md)", ""]
open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8").write(re.sub(r"\n{3,}", "\n\n", "\n".join(md)))
print("ok")
