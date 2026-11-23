"""
A5 lint — mechanical health checks on the wiki.

Deterministic checks only. The judgement half of A5 (cross-page contradictions
that need reading) is done by an independent reviewer agent, not here.

Run:  python3 scripts/a5_lint.py
Writes a summary to stdout; the caller saves it to checks/.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

problems = []   # (severity, check, file, line, message)


def fail(sev, check, file, line, msg):
    problems.append((sev, check, str(file), line, msg))


def rel(p):
    return str(Path(p).relative_to(ROOT))


pages = sorted(WIKI.rglob("*.md"))
stems = {p.stem for p in pages}
text = {p: p.read_text(encoding="utf-8") for p in pages}
lines = {p: text[p].splitlines() for p in pages}

print("=" * 72)
print(f"A5 LINT — {len(pages)} wiki pages")
print("=" * 72)

# ----------------------------------------------------------------------
# L1 wikilinks resolve
# ----------------------------------------------------------------------
LINK = re.compile(r"\[\[([^\]]+)\]\]")
linked_to = defaultdict(set)
for p in pages:
    for i, ln in enumerate(lines[p], 1):
        for m in LINK.finditer(ln):
            target = m.group(1).strip()
            linked_to[target].add(p.stem)
            if target not in stems:
                fail("blocker", "L1 link", rel(p), i,
                     f"[[{target}]] does not resolve to a page")
print(f"L1 wikilinks resolve           : "
      f"{'PASS' if not any(x[1]=='L1 link' for x in problems) else 'FAIL'}")

# ----------------------------------------------------------------------
# L2 orphans (no inbound link). overview is the documented root.
# ----------------------------------------------------------------------
ROOTS = {"overview"}
orphans = [p.stem for p in pages
           if p.stem not in ROOTS and not (linked_to[p.stem] - {p.stem})]
for o in orphans:
    fail("should-fix", "L2 orphan", f"wiki/**/{o}.md", 0,
         "no page links to it")
print(f"L2 no orphan pages             : {'PASS' if not orphans else 'FAIL ' + str(orphans)}")

# ----------------------------------------------------------------------
# L3 index agrees with disk
# ----------------------------------------------------------------------
idx = WIKI / "index.md"
idx_links = {m.group(1).strip() for m in LINK.finditer(text[idx])}
missing_from_index = sorted(stems - idx_links - {"index"})
for s in missing_from_index:
    fail("should-fix", "L3 index", "wiki/index.md", 0,
         f"page '{s}' exists on disk but is not listed in the index")
print(f"L3 index lists every page      : "
      f"{'PASS' if not missing_from_index else 'FAIL ' + str(missing_from_index)}")

# ----------------------------------------------------------------------
# L4 markdown table integrity
#    A table run is >=2 consecutive lines starting with '|'.
#    The 2nd line of a run must be a separator (|---|---|).
#    A run whose 2nd line is not a separator is an orphaned fragment --
#    usually prose dropped into the middle of a table.
# ----------------------------------------------------------------------
SEP = re.compile(r"^\|[\s:|-]+\|\s*$")
bad_tables = 0
for p in pages:
    # blank out fenced code so pipes inside it are not mistaken for tables
    ls = []
    in_fence = False
    for ln in lines[p]:
        if ln.lstrip().startswith("```"):
            in_fence = not in_fence
            ls.append("")
            continue
        ls.append("" if in_fence else ln)
    i = 0
    while i < len(ls):
        if ls[i].lstrip().startswith("|"):
            start = i
            while i < len(ls) and ls[i].lstrip().startswith("|"):
                i += 1
            run = ls[start:i]
            # A single pipe-line is never a valid table: markdown needs at
            # least a header plus a separator. This catches a row orphaned
            # from its table by inserted prose -- the A5-03 defect, which the
            # original run>=2 rule could not see.
            if len(run) == 1:
                bad_tables += 1
                fail("blocker", "L4 table", rel(p), start + 1,
                     "lone table row, separated from its table — will render "
                     "as literal pipe-separated text")
            elif not SEP.match(run[1].strip()):
                bad_tables += 1
                fail("blocker", "L4 table", rel(p), start + 1,
                     f"table run of {len(run)} lines has no separator row — "
                     f"rows will render as literal text")
        else:
            i += 1
print(f"L4 markdown tables well-formed : {'PASS' if not bad_tables else f'FAIL ({bad_tables})'}")

# ----------------------------------------------------------------------
# L5 LaTeX delimiters balanced
# ----------------------------------------------------------------------
latex_bad = 0
for p in pages:
    body = text[p]
    # strip fenced code
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    if body.count("$$") % 2:
        latex_bad += 1
        fail("blocker", "L5 latex", rel(p), 0,
             f"odd number of $$ delimiters ({body.count('$$')})")
    inline = re.sub(r"\$\$.*?\$\$", "", body, flags=re.S)
    if inline.count("$") % 2:
        latex_bad += 1
        fail("blocker", "L5 latex", rel(p), 0,
             f"odd number of inline $ delimiters ({inline.count('$')})")
    # Only braces are checked. Square brackets are NOT balanced in correct
    # maths: half-open intervals like $[0,1)$ are legitimate, and checking
    # them produced only false positives (A5 run 1).
    for i, ln in enumerate(lines[p], 1):
        seg = "".join(re.findall(r"\$[^$]*\$", ln))
        if seg.count("{") != seg.count("}"):
            latex_bad += 1
            fail("minor", "L5 latex", rel(p), i,
                 "unbalanced brace inside inline math")
print(f"L5 LaTeX delimiters balanced   : {'PASS' if not latex_bad else f'FAIL ({latex_bad})'}")

# ----------------------------------------------------------------------
# L6 key constants consistent across pages
#    Any numeric string close to a canonical value but not equal to it
#    is a contradiction between pages.
# ----------------------------------------------------------------------
CANON = {
    # Kopel (2021) -- the full-depth source
    "gamma_max":  ["0.810736", "0.8107358771", "0.8107359", "0.8107358771227719"],
    "turning":    ["0.531963", "0.5319633163"],
    "theta_fol":  ["0.202167", "0.2021670", "0.2021670222", "0.2021669652"],
    "theta_lead": ["0.229499", "0.2294985", "0.2294985504", "0.2294985134"],
    # Light-depth sources. Listed so they are not mistaken for Kopel's --
    # note Hirose & Matsumura's delta** = 0.531 is NOT Kopel's 0.531963.
    # See open-questions Q9.
    "hm_delta2":  ["0.531"],
    "hm_delta1":  ["0.862"],
    "br_beta":    ["0.3819"],
    "chen_e":     ["0.085", "0.125", "0.876", "1.142"],
}
PREFIX = {"gamma_max": "0.810", "turning": "0.531", "theta_fol": "0.202",
          "theta_lead": "0.2294", "hm_delta1": "0.862", "br_beta": "0.381"}
ACCEPTED = {v for forms in CANON.values() for v in forms}
NUM = re.compile(r"\b0\.\d{3,}\b")
const_bad = 0
for p in pages:
    for i, ln in enumerate(lines[p], 1):
        for m in NUM.finditer(ln):
            v = m.group(0)
            if v in ACCEPTED:
                continue        # a known constant from any source
            for key, pre in PREFIX.items():
                if v.startswith(pre):
                    const_bad += 1
                    fail("should-fix", "L6 constant", rel(p), i,
                         f"'{v}' looks like {key} but matches no registered "
                         f"constant; nearest accepted: {CANON[key]}")
                    break
print(f"L6 key constants consistent    : {'PASS' if not const_bad else f'FAIL ({const_bad})'}")

# ----------------------------------------------------------------------
# L7 every claim-bearing section carries a page citation OR a marking tag
#    Heuristic: a section (## or ###) in a concept/source page whose body
#    has >40 words and contains neither (p. NNN) nor a marking tag.
# ----------------------------------------------------------------------
CITE = re.compile(r"\(p{1,2}\.\s*\d|\bp\.\s*\d|fn\.\s*\d")
TAG = re.compile(r"\[our reading\]|\[own calculation\]|🔎|⚠️")
SKIP_PAGES = {"index", "sources", "glossary", "open-questions", "numbers",
              "equations", "overview"}
# Sections that are process metadata, not claims about the source. These
# legitimately carry no page citation.
META_HEAD = re.compile(
    r"verification status|^#+ *A[0-9] —|remaining gaps|verification queue",
    re.I)
uncited = 0
for p in pages:
    if p.stem in SKIP_PAGES:
        continue
    ls = lines[p]
    heads = [i for i, ln in enumerate(ls) if re.match(r"^#{2,3} ", ln)]
    meta_from = next((i for i, ln in enumerate(ls)
                      if re.match(r"^## .*[Vv]erification status", ln)), None)
    for j, h in enumerate(heads):
        if meta_from is not None and h >= meta_from:
            continue
        if META_HEAD.search(ls[h]):
            continue
        end = heads[j + 1] if j + 1 < len(heads) else len(ls)
        body = "\n".join(ls[h + 1:end])
        words = len(body.split())
        if words > 40 and not CITE.search(body) and not TAG.search(body):
            uncited += 1
            fail("should-fix", "L7 citation", rel(p), h + 1,
                 f"section '{ls[h].strip()[:48]}' has {words} words, "
                 f"no page citation and no marking tag")
print(f"L7 sections cited or tagged    : {'PASS' if not uncited else f'FAIL ({uncited})'}")

# ----------------------------------------------------------------------
# L8 every source in sources.md has a wiki/papers page, and vice versa
# ----------------------------------------------------------------------
paper_pages = {p.stem for p in (WIKI / "papers").glob("*.md")}
raw_pdfs = {f.stem for f in (ROOT / "raw" / "papers").glob("*.pdf")}
l8 = 0
for s in raw_pdfs - paper_pages:
    l8 += 1
    fail("should-fix", "L8 source", "wiki/papers/", 0,
         f"raw/papers/{s}.pdf has no wiki page")
for s in paper_pages - raw_pdfs:
    l8 += 1
    fail("should-fix", "L8 source", f"wiki/papers/{s}.md", 0,
         "wiki page has no matching PDF in raw/papers/")
print(f"L8 raw/ and wiki/papers/ match : {'PASS' if not l8 else f'FAIL ({l8})'}")

# ----------------------------------------------------------------------
# L9 referenced check/script files exist
# ----------------------------------------------------------------------
PATHREF = re.compile(r"`((?:checks|scripts)/[A-Za-z0-9_.\-]+)`")
l9 = 0
for p in pages:
    for i, ln in enumerate(lines[p], 1):
        for m in PATHREF.finditer(ln):
            if not (ROOT / m.group(1)).exists():
                l9 += 1
                fail("should-fix", "L9 path", rel(p), i,
                     f"references {m.group(1)}, which does not exist")
print(f"L9 referenced files exist      : {'PASS' if not l9 else f'FAIL ({l9})'}")

# ----------------------------------------------------------------------
# L10 index counts match reality
# ----------------------------------------------------------------------
concept_n = len(list((WIKI / "concepts").glob("*.md")))
m = re.search(r"Concept pages:\s*\**(\d+)", text[idx])
l10 = 0
if m and int(m.group(1)) != concept_n:
    l10 += 1
    fail("minor", "L10 counts", "wiki/index.md", 0,
         f"index says {m.group(1)} concept pages; disk has {concept_n}")
print(f"L10 index counts accurate      : {'PASS' if not l10 else 'FAIL'}")

# ----------------------------------------------------------------------
print("=" * 72)
by_sev = defaultdict(int)
for sev, *_ in problems:
    by_sev[sev] += 1
print(f"TOTAL: {len(problems)} problems — "
      f"{by_sev['blocker']} blocker, {by_sev['should-fix']} should-fix, "
      f"{by_sev['minor']} minor")
print("=" * 72)
for sev in ("blocker", "should-fix", "minor"):
    rows = [x for x in problems if x[0] == sev]
    if rows:
        print(f"\n### {sev.upper()}")
        for _, check, f, line, msg in rows:
            loc = f"{f}:{line}" if line else f
            print(f"  [{check}] {loc}\n      {msg}")

sys.exit(1 if by_sev["blocker"] else 0)
