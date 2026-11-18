# Tools

Scripts that build each patch page's GitHub README and SVG graphics. Run them from anywhere with Python 3, BeautifulSoup and Pillow installed.

| Script | What it does |
|---|---|
| `make_md.py <patch>/index.html <patch>` | Builds the core page README and the tier board and build card SVGs from the core `index.html` and `builds.py` |
| `make_support.py <patch>/index.html <patch>/supports <link to core page>` | Builds the support page `index.html`, README and SVGs from `support_data.py`, reusing the core page's styles |
| `builds.py` | Pos 1 build data |
| `support_data.py` | Pos 4 and pos 5 tiers, builds, items, neutrals and support changes |
| `svgkit.py` | Shared drawing code for the tier boards and build cards |

The core page's tier boards live directly in `<patch>/index.html`. Edit them there, then rerun `make_md.py`.

To rebuild 7.42 from the repo root:

```
python3 tools/make_md.py 7.42/index.html 7.42
python3 tools/make_support.py 7.42/index.html 7.42/supports https://github.com/Tachanks/dota2-patches/tree/main/7.42
```
