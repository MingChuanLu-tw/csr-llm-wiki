"""
Build a single browsable HTML page from the wiki, so it can be published and
linked (the assignment asks for a Wiki link, and 19 markdown files are not one).

No markdown library is installed, so this converts the subset the wiki actually
uses: headings, tables, lists, blockquotes, fenced code, bold/italic/code,
links, [[wikilinks]], horizontal rules, and $...$ / $$...$$ left untouched for
KaTeX. The wiki is written by us, so the subset is known and closed.

Output: 繳交/wiki.html  (self-contained apart from the KaTeX scripts on cdnjs,
which the artifact CSP allows; the stylesheet is inlined from the deck build.)

Run:  python3 scripts/build_wiki_site.py
"""

import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
OUT = ROOT / "繳交" / "wiki.html"
DECK = ROOT / "slides_html" / "index.html"

ORDER = ["overview", "index", "Kopel2021-CSR", "first-mover-advantage",
         "csr-spillovers", "appropriability", "competition-intensity",
         "strategic-commitment", "rival-exclusion", "csr-modelling-choices",
         "glossary", "equations", "numbers", "sources", "open-questions",
         "Chen2021-OptimalCSR", "HiroseMatsumura2022-CommonOwnershipECSR",
         "BarcenaRuizSagasta2021-CrossOwnershipCSR", "XingLee2023-EnvironmentalRD"]

GROUP = {
    "Start here": ["overview", "index"],
    "Source pages": ["Kopel2021-CSR", "Chen2021-OptimalCSR",
                     "HiroseMatsumura2022-CommonOwnershipECSR",
                     "BarcenaRuizSagasta2021-CrossOwnershipCSR",
                     "XingLee2023-EnvironmentalRD"],
    "Concepts": ["first-mover-advantage", "csr-spillovers", "appropriability",
                 "competition-intensity", "strategic-commitment",
                 "rival-exclusion", "csr-modelling-choices"],
    "Registers": ["glossary", "equations", "numbers", "sources",
                  "open-questions"],
}

pages = {p.stem: p.read_text(encoding="utf-8") for p in WIKI.rglob("*.md")}
missing = set(pages) - set(ORDER)
assert not missing, f"page not in ORDER: {missing}"

MATH = []


def stash_math(t):
    def keep(m):
        MATH.append(m.group(0))
        return f"\x00M{len(MATH)-1}\x00"
    t = re.sub(r"\$\$.+?\$\$", keep, t, flags=re.S)
    t = re.sub(r"(?<!\$)\$[^$\n]+\$(?!\$)", keep, t)
    return t


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", lambda m: f"<code>{m.group(1)}</code>", t)
    t = re.sub(r"\[\[([^\]]+)\]\]",
               lambda m: f'<a href="#{m.group(1).strip()}">{m.group(1).strip()}</a>', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
               lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", lambda m: f"<strong>{m.group(1)}</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", lambda m: f"<em>{m.group(1)}</em>", t)
    t = re.sub(r"~~([^~]+)~~", lambda m: f"<del>{m.group(1)}</del>", t)
    return t


def md(src):
    src = stash_math(src)
    out, lines, i = [], src.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            j = i + 1
            buf = []
            while j < len(lines) and not lines[j].startswith("```"):
                buf.append(html.escape(lines[j], quote=False)); j += 1
            out.append("<pre><code>" + "\n".join(buf) + "</code></pre>")
            i = j + 1; continue
        if re.match(r"^\s*\|", ln) and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i+1]):
            hdr = [c.strip() for c in ln.strip().strip("|").split("|")]
            rows, j = [], i + 2
            while j < len(lines) and re.match(r"^\s*\|", lines[j]):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")]); j += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in hdr)
            tb = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>")
            i = j; continue
        m = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if m:
            lv = len(m.group(1))
            out.append(f"<h{lv}>{inline(m.group(2))}</h{lv}>"); i += 1; continue
        if re.match(r"^---+\s*$", ln):
            out.append("<hr>"); i += 1; continue
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").strip()); i += 1
            out.append("<blockquote>" + md("\n".join(buf)) + "</blockquote>"); continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", ln)
        if m:
            ordered = not m.group(2) in ("-", "*")
            tag = "ol" if ordered else "ul"
            items, j = [], i
            while j < len(lines):
                mm = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", lines[j])
                if not mm: break
                items.append(inline(mm.group(3))); j += 1
            out.append(f"<{tag}>" + "".join(f"<li>{x}</li>" for x in items) + f"</{tag}>")
            i = j; continue
        if not ln.strip():
            i += 1; continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|>|```|\s*\||\s*([-*]|\d+\.)\s|---+\s*$)", lines[i]):
            buf.append(lines[i]); i += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>")
    return "\n".join(out)


body = []
for name in ORDER:
    body.append(f'<article id="{name}" class="page"><div class="slug">{name}.md</div>'
                + md(pages[name]) + "</article>")

nav = []
for grp, names in GROUP.items():
    nav.append(f'<div class="grp">{grp}</div><ul>')
    for n in names:
        nav.append(f'<li><a href="#{n}">{n}</a></li>')
    nav.append("</ul>")

# reuse the KaTeX CSS already inlined into the deck
deck = DECK.read_text(encoding="utf-8")
m = re.search(r"<style>/\* KaTeX .*?</style>", deck, re.S)
katex_css = m.group(0) if m else ""
if not katex_css:
    print("  WARNING: KaTeX css not found in the deck; run b9_inline_katex.py first")

doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CSR Leadership — LLM Wiki</title>
{katex_css}
<style>
:root{{--ink:#1b2733;--muted:#5b6b7a;--faint:#8a99a8;--accent:#b3261e;--rule:#e3e8ec;--panel:#f7f9fa}}
*{{box-sizing:border-box}}
body{{margin:0;display:flex;color:var(--ink);background:#fff;
 font:16px/1.62 "Charter","Iowan Old Style",Georgia,serif}}
nav{{width:270px;flex:none;height:100vh;overflow:auto;padding:26px 18px 40px;
 border-right:1px solid var(--rule);background:var(--panel);
 font:14px/1.5 ui-sans-serif,system-ui,sans-serif;position:sticky;top:0}}
nav h1{{font-size:15px;margin:0 0 4px;letter-spacing:-.01em}}
nav .sub{{color:var(--faint);font-size:12.5px;margin-bottom:20px;line-height:1.45}}
.grp{{font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--faint);
 margin:18px 0 6px}}
nav ul{{list-style:none;margin:0;padding:0}}
nav li a{{display:block;padding:3.5px 8px;margin-left:-8px;border-radius:4px;
 color:var(--muted);text-decoration:none;word-break:break-all}}
nav li a:hover{{background:#eceff2;color:var(--ink)}}
main{{flex:1;min-width:0;padding:44px 7vw 120px;max-width:980px}}
.page{{padding-bottom:40px;margin-bottom:40px;border-bottom:1px solid var(--rule)}}
.slug{{font:12px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--faint);
 margin-bottom:14px}}
h1{{font-size:30px;line-height:1.2;margin:.2em 0 .5em;letter-spacing:-.01em}}
h2{{font-size:22px;margin:1.5em 0 .5em;letter-spacing:-.005em}}
h3{{font-size:17.5px;margin:1.3em 0 .4em}}
p,li{{font-size:16px}}
ul,ol{{padding-left:1.3em}}
li{{margin:.26em 0}}
a{{color:var(--accent)}}
code{{font:13.5px ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--panel);
 padding:.1em .34em;border-radius:3px}}
pre{{background:var(--panel);padding:14px 16px;border-radius:6px;overflow:auto}}
pre code{{background:none;padding:0;font-size:13px;line-height:1.5}}
blockquote{{border-left:3px solid var(--rule);margin:.6em 0;padding:.1em 0 .1em 1.1em;
 color:var(--ink)}}
blockquote p{{margin:.35em 0}}
table{{border-collapse:collapse;margin:.7em 0;font-size:14.5px;width:100%}}
th,td{{text-align:left;padding:.45em .8em .45em 0;border-bottom:1px solid var(--rule);
 vertical-align:top}}
th{{color:var(--muted);font-size:13px;font-weight:650}}
hr{{border:0;border-top:1px solid var(--rule);margin:1.6em 0}}
del{{color:var(--faint)}}
.katex{{font-size:1.02em}}
@media (max-width:860px){{body{{display:block}} nav{{width:auto;height:auto;position:static}} main{{padding:28px 6vw 80px}}}}
</style></head><body>
<nav>
<h1>CSR Leadership — LLM Wiki</h1>
<div class="sub">Built from 5 duopoly-CSR papers. Kopel (2021) at full depth —
equations re-derived symbolically and twice independently reviewed; the other
four read and summarised only.</div>
{''.join(nav)}
</nav>
<main>
{''.join(body)}
</main>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>
if (window.renderMathInElement) renderMathInElement(document.body, {{
  delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],
  throwOnError:false
}});
</script>
</body></html>"""

# restore maths
for k, v in enumerate(MATH):
    doc = doc.replace(f"\x00M{k}\x00", v)

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(doc, encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)} — {len(doc)/1024:.0f} KB, {len(ORDER)} pages")
