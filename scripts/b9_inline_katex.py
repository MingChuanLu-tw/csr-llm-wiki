"""
B9 build step — make the deck self-contained.

The artifact viewer's content security policy admits stylesheets only from the
artifact's own files and Google Fonts, so KaTeX's stylesheet on cdnjs is blocked
and every equation renders unstyled. This fetches KaTeX's CSS and the woff2
fonts it references, inlines the fonts as data: URIs inside the CSS, and inlines
the CSS into the page. The KaTeX *scripts* stay on cdnjs, which the policy does
allow.

Output: slides_html/index.html is rewritten in place, self-contained.
Run:  python3 scripts/b9_inline_katex.py
"""

import base64
import pathlib
import re
import sys
import urllib.request

VER = "0.16.9"
BASE = f"https://cdnjs.cloudflare.com/ajax/libs/KaTeX/{VER}"
ROOT = pathlib.Path(__file__).resolve().parent.parent
DECK = ROOT / "slides_html" / "index.html"
CACHE = ROOT / "slides_html" / ".katex-cache"
CACHE.mkdir(exist_ok=True)


def get(url: str) -> bytes:
    name = CACHE / url.rsplit("/", 1)[-1]
    if name.exists():
        return name.read_bytes()
    print(f"  fetching {url.rsplit('/', 1)[-1]}")
    req = urllib.request.Request(url, headers={"User-Agent": "deck-build"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    name.write_bytes(data)
    return data


print("Inlining KaTeX into the deck")
css = get(f"{BASE}/katex.min.css").decode("utf-8")

# KaTeX ships woff2, woff and ttf for each face. Keep woff2 only: every browser
# that runs this deck supports it, and the other two triple the page size.
fonts = sorted(set(re.findall(r"fonts/(KaTeX_[\w-]+\.woff2)", css)))
print(f"  {len(fonts)} woff2 faces referenced")

total = 0
for f in fonts:
    data = get(f"{BASE}/fonts/{f}")
    total += len(data)
    uri = "data:font/woff2;base64," + base64.b64encode(data).decode("ascii")
    css = css.replace(f"fonts/{f}", uri)

# drop the now-unreachable woff and ttf sources from each @font-face
css = re.sub(r",url\(fonts/KaTeX_[\w-]+\.(?:woff|ttf)\)format\(\"(?:woff|truetype)\"\)", "", css)

print(f"  fonts inlined: {total/1024:.0f} KB raw, CSS now {len(css)/1024:.0f} KB")

deck = DECK.read_text(encoding="utf-8")
link = re.search(r'<link rel="stylesheet" href="https://cdnjs[^>]*KaTeX[^>]*>', deck)
if not link:
    if "KaTeX inlined by scripts/b9_inline_katex.py" in deck:
        print("  already inlined — nothing to do")
        sys.exit(0)
    sys.exit("could not find the KaTeX stylesheet link in the deck")

deck = deck.replace(
    link.group(0),
    "<style>/* KaTeX " + VER + " inlined by scripts/b9_inline_katex.py "
    "— the artifact CSP blocks third-party stylesheets */\n" + css + "</style>",
)
DECK.write_text(deck, encoding="utf-8")
print(f"  wrote {DECK.relative_to(ROOT)} — {len(deck)/1024:.0f} KB, self-contained")
