"""Rewrites the core page's tier boards, picks, callout and pos 1 builds from core_data.py and builds.py.

Usage: python3 -I update_core.py <patch>/index.html
Edits the file in place. Run make_md.py afterwards to rebuild the README and graphics.
"""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core_data as C  # noqa: E402
from builds import BUILDS  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402

path = sys.argv[1]
soup = BeautifulSoup(open(path, encoding="utf-8").read(), "html.parser")


def e(s):
    return html.escape(s, quote=False)


TREND_TAG = {"up": ("up", "▲ Up"), "down": ("down", "▼ Down"), "steady": ("steady", "● Steady"), "new": ("rework", "✦ New")}


def frag(markup):
    return BeautifulSoup(markup, "html.parser")


def board(tiers):
    rows = []
    for t in ["S", "A", "B", "C", "X"]:
        if not tiers.get(t):
            continue
        cards = []
        for name, kind, base, why in tiers[t]:
            cls, label = TREND_TAG[kind]
            cards.append(f'<div class="hero"><div class="hd"><span class="nm">{e(name)}</span><span class="tag {cls}">{label}</span></div>'
                         f'<div class="base">{e(base)}</div><p>{e(why)}</p></div>')
        rows.append(f'<div class="tier {t}"><div class="letter">{"Avoid" if t == "X" else t}</div><div class="heroes">' + "".join(cards) + "</div></div>")
    return '<div class="board">' + "".join(rows) + "</div>"


for sec, tiers in (("carry", C.POS1), ("mid", C.POS2), ("off", C.POS3)):
    soup.select_one(f"#{sec} .board").replace_with(frag(board(tiers)))

LEGEND = ('<div class="legend">'
          '<span><span class="tag up">▲ Up</span> moved up since the day-one list</span>'
          '<span><span class="tag down">▼ Down</span> moved down</span>'
          '<span><span class="tag steady">● Steady</span> same tier</span>'
          '<span><span class="tag rework">✦ New</span> added to the list</span></div>')
soup.select_one("#carry .legend").replace_with(frag(LEGEND))

picks = soup.select_one("#short .picks")
picks.replace_with(frag('<div class="picks">' + "".join(
    f'<div class="pick"><div class="role">{e(r)}</div><div class="names">{e(n)}</div></div>' for r, n in C.PICKS) + "</div>"))

soup.select_one("#off .callout").replace_with(frag(f'<div class="callout"><b>{e(C.CALLOUT_LABEL)}</b> {e(C.CALLOUT)}</div>'))


def chain(items):
    return '<ol class="chain">' + "".join(f"<li><span>{e(i)}</span></li>" for i in items) + "</ol>"


cards = []
for b in BUILDS:
    cards.append(f'<article class="build"><div class="bh"><span class="tierchip {b["tier"]}" title="{b["tier"]} tier">{b["tier"]}</span><h3>{e(b["hero"])}</h3></div>'
                 f'<div class="start"><b>Start:</b> {e(b["start"])}</div>'
                 f'<div class="path rec"><div class="plabel"><span>Recommended</span> · {e(b["rec"]["name"])}</div>{chain(b["rec"]["items"])}<p>{e(b["rec"]["note"])}</p></div>'
                 f'<div class="path alt"><div class="plabel"><span>Alternative</span> · {e(b["alt"]["name"])}</div>{chain(b["alt"]["items"])}<p>{e(b["alt"]["note"])}</p></div></article>')
soup.select_one("#builds .buildgrid").replace_with(frag('<div class="buildgrid">' + "".join(cards) + "</div>"))
soup.select_one("#builds .sub").string = C.BUILDS_SUB

soup.select_one("header .kicker").string = C.KICKER
soup.select_one("header .lede").string = C.LEDE
chips = soup.select_one("header .chips")
links = [str(a) for a in chips.select("a.chip")]
chips.replace_with(frag('<div class="chips">' + "".join(f'<span class="chip">{e(c)}</span>' for c in C.CHIPS) + "".join(links) + "</div>"))
for sec in ("carry", "mid", "off"):
    soup.select_one(f"#{sec} .sub").string = C.SUBS[sec]
soup.select_one("#sources p").string = C.METHOD
for a in soup.select("#sources li a"):
    if "dota2protracker" in a.get("href", ""):
        a.string = "Dota2ProTracker meta (7.42, 7000+ MMR)"

style = soup.find("style")
if ".tierchip.C" not in style.string:
    style.string = style.string.replace(".build .start {", ".tierchip.C { background: var(--c); color: var(--c-ink); }\n.build .start {")

open(path, "w", encoding="utf-8").write(str(soup))
print("ok")
