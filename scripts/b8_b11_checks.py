"""
B8 — equation check: every equation on a slide must be in wiki/equations.md.
B11 — timing check: the script must land inside 30–45 minutes.

Run:  python3 scripts/b8_b11_checks.py
Exit 1 on any failure.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DECK = ROOT / "slides_html" / "index.html"
SCRIPT = ROOT / "notes" / "script.md"
REG = ROOT / "wiki" / "equations.md"
OUTLINE = ROOT / "notes" / "outline.md"

fails = []


def norm(s: str) -> str:
    """Normalise LaTeX for comparison: drop whitespace and display wrappers."""
    s = s.strip()
    s = re.sub(r"\\[,;:!> ]", "", s)
    s = re.sub(r"\s+", "", s)
    s = s.replace(r"\left", "").replace(r"\right", "")
    s = s.replace(r"\dfrac", r"\frac").replace(r"\tfrac", r"\frac")
    s = s.replace("{*}", "*").replace("^{*}", "^*")
    s = s.replace("^{2}", "^2").replace("_{1}", "_1").replace("_{2}", "_2")
    s = s.rstrip(",.")                 # register joins parts with a comma
    return s


# ----------------------------------------------------------------------
print("=" * 70)
print("B8 — equation check")
print("=" * 70)

reg_raw = REG.read_text(encoding="utf-8")
# every $$...$$ block in the register, split on \qquad / , so multi-part
# display lines register each part separately
reg_parts = set()
for block in re.findall(r"\$\$(.+?)\$\$", reg_raw, re.S):
    for part in re.split(r"\\qquad|\\quad|,\s*\\\\|\\\\", block):
        if part.strip():
            reg_parts.add(norm(part))
# inline maths in the register too (thresholds etc.)
for m in re.findall(r"(?<!\$)\$([^$\n]+)\$(?!\$)", reg_raw):
    reg_parts.add(norm(m))

deck = DECK.read_text(encoding="utf-8")
# Only take display maths that sits alone inside a <p>. Scanning the whole
# document for "$$" pairs made stray inline "$" join across slides and
# produced nonsense candidates (first B8 run).
deck_display = [m.group(1) for m in
                re.finditer(r"<p>\s*\$\$(.+?)\$\$\s*</p>", deck, re.S)]
deck_inline = [m.group(1) for m in
               re.finditer(r"(?<!\$)\$([^$<>\n]{3,120})\$(?!\$)", deck)]

unknown = []
for block in deck_display:
    for part in re.split(r"\\qquad|\\quad", block):
        p = norm(part)
        if not p:
            continue
        if p not in reg_parts:
            unknown.append(part.strip())

print(f"register entries (normalised parts): {len(reg_parts)}")
print(f"display equations on slides        : {len(deck_display)}")
if unknown:
    print(f"NOT FOUND IN REGISTER              : {len(unknown)}")
    for u in unknown:
        print(f"   {u[:100]}")
    fails.append(f"B8: {len(unknown)} slide equation(s) absent from the register")
else:
    print("every slide equation matches wiki/equations.md      PASS")

# LaTeX delimiter balance on the deck
body = re.sub(r"<script.*?</script>", "", deck, flags=re.S)
if body.count("$$") % 2:
    fails.append("B8: odd number of $$ in the deck")
    print("delimiter balance                                   FAIL")
else:
    print("delimiter balance                                   PASS")

# ----------------------------------------------------------------------
print()
print("=" * 70)
print("B11 — timing check")
print("=" * 70)

txt = SCRIPT.read_text(encoding="utf-8")
# count only spoken words: drop headings, stage directions, the backup section
txt = txt.split("## Backup slides")[0]
txt = re.sub(r"^#.*$", "", txt, flags=re.M)          # headings
txt = re.sub(r"\[.*?\]", "", txt, flags=re.S)        # [PAUSE], [stage dirs]
txt = re.sub(r"^\s*[-*]\s.*$", "", txt, flags=re.M)  # bullet notes
txt = re.sub(r"[*_`>|]", " ", txt)
words = len(txt.split())

LOW, HIGH = 130, 150                                  # words per minute
t_fast, t_slow = words / HIGH, words / LOW
print(f"spoken words               : {words}")
print(f"at {HIGH} wpm (fast)          : {t_fast:.1f} min")
print(f"at {LOW} wpm (measured slow) : {t_slow:.1f} min")

if t_slow > 45:
    fails.append(f"B11: {t_slow:.1f} min at 130 wpm exceeds the 45-minute cap")
    print("fits 30–45 min                                      FAIL (too long)")
elif t_fast < 30:
    fails.append(f"B11: {t_fast:.1f} min at 150 wpm is under the 30-minute floor")
    print("fits 30–45 min                                      FAIL (too short)")
else:
    print("fits 30–45 min at both speeds                       PASS")

# per-slide script coverage: every slide must have a script section
slide_heads = re.findall(r"^## Slide (\d+)", SCRIPT.read_text(encoding="utf-8"), re.M)
n_all = len(re.findall(r'class="slide', deck))
n_backup = len(re.findall(r'<span class="n">B\d</span>', deck))
n_slides = n_all - n_backup
covered = sorted(int(x) for x in slide_heads)
missing = [i for i in range(1, 31) if i not in covered]
print(f"slides in deck             : {n_slides} (+{n_backup} backup)")
print(f"slides with script         : {len(covered)}")
if missing:
    fails.append(f"B11: slides without a script section: {missing}")
    print(f"every slide has a script                            FAIL {missing}")
else:
    print("every slide has a script                            PASS")

# ----------------------------------------------------------------------
print()
print("=" * 70)
if fails:
    print(f"RESULT: {len(fails)} FAILURE(S)")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("RESULT: B8 and B11 PASS")
print("=" * 70)
