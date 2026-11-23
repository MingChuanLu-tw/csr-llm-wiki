# A5 lint — judgement half: does the wiki contradict itself?

Reviewer: independent agent, fresh context (AGENTS.md §8a). Date: 2026-11-17.
Scope: all 13 pages under `wiki/`, compared **against each other**. The source PDF
was not opened and nothing here is a claim about what the paper says that is not
already established inside the repository. The mechanical half
(`scripts/a5_lint.py` → `checks/a5_lint_run2.txt`, 10/10 PASS) is not repeated.
Findings already recorded as fixed in `checks/a3_report.md` rounds 1–2 are not
re-reported unless the fix did not hold.

## Verdict: **FAIL** — 1 blocker, 8 should-fix, 8 minor

**The FAIL rests on one severity call.** A5-01 alone is blocker-grade: two pages
state a causal mechanism that the wiki's own registered numbers rule out, and it
is the mechanism most likely to become the explanatory slide. Judged as a
should-fix instead, this report would read PASS WITH FIXES. I grade it a blocker
because AGENTS.md §4 makes "contradiction → A2" A5's on-failure edge, and because
this one would survive into the deck as the paper's own explanation rather than
as a wiki slip. Nothing else here touches the equations or the verified
constants.

| # | Category | Result | Count |
|---|---|---|---|
| 1 | Same fact, two statements | **FAIL** | 4 (1 blocker, 3 minor) |
| 2 | Same term, two meanings | **FAIL** | 2 (1 should-fix, 1 minor) |
| 3 | Stale cross-references | PASS with 2 minor | 2 (2 minor) |
| 4 | Status claims that disagree | **FAIL** | 3 (3 should-fix) |
| 5 | Marking-tag consistency | **FAIL** | 3 (1 should-fix, 2 minor) |
| 6 | Register drift (`equations.md`, `numbers.md`) | **FAIL** | 3 (3 should-fix) |

Severity convention follows `a3_report.md`: a category with only minors is
"PASS with N minor".

Fix order: **A5-01** first — it is the only finding that changes what the deck
would teach. Then A5-03 and A5-04, both in `equations.md`, the register B8 parses,
and A5-07/A5-09 in `numbers.md`, the register B10 parses. Then the rest. A5-06's
log rows should be written before A6, since the reflection is drawn from them.

---

# Blocker

## A5-01 — The first-mover advantage dies long before deterrence breaks. Two pages say it dies *because* deterrence breaks.

**Severity**: blocker. **Category**: 1 (same fact, two statements).

**Location A — `wiki/concepts/strategic-commitment.md`, "The strategic effect is
conditional" (lines 44–66).** States correctly that $\partial s_2/\partial s_1<0$
holds only while $\theta < \gamma/(2-\gamma^2)$, and that above that threshold
"the commitment stops working as a deterrent". It then builds the three-link
chain and concludes: "**Kopel's result is that link 3 almost always breaks.**"
Link 3 is the appropriability link, defined two lines above as the
substitutes→complements switch ("otherwise the follower free-rides instead of
retreating").

**Location B — `wiki/concepts/first-mover-advantage.md`, "Where the result comes
from" (lines 82–87).** "The leader's advantage rests on a strategic-commitment
effect: by committing to high CSR it induces the follower to cut its own CSR.
**That effect is destroyed by [[csr-spillovers]]**, because spillovers let the
follower free-ride rather than retreat." Untagged and cited to pp. 498–499, so a
reader takes it as the author's.

**Location C — `wiki/numbers.md`, "First-mover-advantage frontier" and
"Conditions, not constants"**, plus the same table on the paper page §7.2 and on
`first-mover-advantage.md` itself. Put the two thresholds side by side — both are
already in the wiki, so this is arithmetic on registered numbers, not new
analysis:

| $\gamma$ | FMA frontier $\theta$ (`numbers.md`) | $s_1^*=s_2^*$ frontier (a3 C8) | Deterrence switch $\gamma/(2-\gamma^2)$ | Ratio, switch / FMA |
|---|---|---|---|---|
| 0.1 | 0.0000534 | 0.00256 | 0.0503 | ≈ 940× |
| 0.3 | 0.00150 | 0.0169 | 0.1571 | ≈ 105× |
| 0.5 | 0.00867 | 0.0427 | 0.2857 | ≈ 33× |
| 0.7 | 0.0393 | 0.0951 | 0.4636 | ≈ 12× |
| 0.8 | 0.0960 | 0.1527 | 0.5882 | ≈ 6× |

At every $\gamma$ the ordering is strict: **FMA frontier < investment frontier <
deterrence switch**, by a factor of **6× to 940×** depending on $\gamma$ (the gap
is widest at low competition and narrows to 6× at $\gamma=0.8$ — so "two orders of
magnitude" is true only up to about $\gamma=0.3$ and should not be stated
generally). At $\gamma=0.3$ the leader stops out-earning the follower at
$\theta\approx0.0015$, while $ds_2/ds_1$ stays negative until
$\theta\approx0.157$. So at the moment the FMA dies, the commitment is still
working as described: CSR levels are still strategic substitutes, the follower
still retreats when the leader invests, and the leader still invests more
($s_1^*>s_2^*$ survives until 0.0169). Nothing about deterrence has broken.

**What the numbers establish, and what they do not.** They rule out Locations A
and B: the FMA cannot be dying *because* the deterrence mechanism inverts, since
it dies while that mechanism is intact. They do **not** by themselves identify
the true mechanism — that would need the comparative statics, which this review
did not re-derive. The one account in the wiki they do not contradict is
`csr-spillovers.md`'s, which is already correctly tagged: "Why spillovers destroy
the first-mover advantage" cites the paper's two signs
$\partial_\theta(\partial\pi_1/\partial s_1)<0$ and
$\partial_\theta(\partial\pi_2/\partial s_2)>0$, then glosses them — "**[our
reading]** So $\theta$ is not a neutral leak — it is a transfer of incentive, and
that is why the [[first-mover-advantage]] region collapses so fast in $\theta$."
That effect operates continuously from $\theta=0$ upward, which is consistent with
a frontier at minute $\theta$; the substitutes→complements switch is a separate
and much later event.

**Not a contradiction, but a misleading annotation — `wiki/overview.md`, "The
causal chain" (lines 40–56).** The diagram's only annotated failure mode is
"← breaks if θ is high" on the deterrence arrow. That statement is *true* (it
does break, at $\theta>\gamma/(2-\gamma^2)$), and the tagged note underneath
already says the arrows "do **not** coincide: there is a band where the leader
invests more but still earns less". So the overview is not wrong. The risk is
that it attaches the only visible break to the wrong arrow, and B3 lifts
diagrams. Worth annotating when A and B are fixed, but it is not itself a defect.

**Why this matters beyond tidiness.** The wrong mechanism gives the wrong talk.
On the broken reading the headline is "spillovers wreck the leader's ability to
deter the follower" — strategic interaction collapsing. On the reading the
numbers permit it is sharper: *the leader keeps deterring the follower, keeps
out-investing it, and still loses on profit.* That is the point the Location C
table was promoted into the wiki to make, and it is why the frontier sits at
0.15% rather than 15%.

**Fix.**
1. `strategic-commitment.md`: replace "Kopel's result is that link 3 almost
   always breaks" with the accurate statement — the FMA fails long before link 3
   does; link 3 (the complements switch) is a further, later regime change. Keep
   the three-link framing and its `[our reading]` tag.
2. `first-mover-advantage.md`: "that effect is destroyed by spillovers" is wrong
   at the frontier. Replace with the transfer-of-incentive account, cross-
   referenced to `csr-spillovers.md`. **The replacement must carry an
   `[our reading]` tag** — it is a mechanism claim assembled from the paper's
   derivative signs plus our own numbers, not a sentence in the paper — and the
   pp. 498–499 citation should stay only on the strategic-effect sentence the
   paper does support.
3. `overview.md`: annotate the profit arrow with the frontier and the deterrence
   arrow with the switch, so the two breaks are visibly different.
4. Add the comparison table above to `numbers.md` — see A5-07.

---

# Should-fix

## A5-02 — "free-ride" names the low-θ behaviour on two pages and the high-θ behaviour on two others

**Severity**: should-fix. **Category**: 2 (same term, two meanings).

| Location | Regime it assigns to "free-ride" |
|---|---|
| `papers/Kopel2021-CSR.md` §5.2, "Low $\theta$" bullet | **low θ**: "more leader CSR makes the follower cut its own CSR **and free-ride**" |
| `concepts/csr-spillovers.md`, regime table, substitutes row | **low θ**: "the follower **retreats and free-rides**" |
| `concepts/first-mover-advantage.md` line 86 | **high θ**: "spillovers let the follower **free-ride rather than retreat**" |
| `concepts/strategic-commitment.md` link 3 | **high θ**: "otherwise the follower **free-rides instead of retreating**" |

In the first pair, retreating *is* free-riding. In the second, free-riding is the
alternative to retreating. The two cannot both be the term's meaning, and the
second pair is the one that feeds A5-01's broken mechanism.

**Which is correct.** Neither, strictly, and the wiki contains the evidence. The
paper's own use of the phrase is quoted on the paper page §4.1 and
`csr-spillovers.md`: $\theta_1\le\theta_2$ is assumed "because the CSR follower
can free ride on the CSR efforts of the leader" — i.e. free-riding *is* capturing
$\theta s_1$, which happens for any $\theta>0$ and is monotone in $\theta$. It is
not a regime-specific behaviour at all. Separately, the paper page §5.2 already
carries the F25 fix — "Note the paper's mechanism is defensive, not
opportunistic" — for the high-θ response, which makes "free-ride" the wrong word
for that regime too; that caveat did not reach `first-mover-advantage.md` or
`strategic-commitment.md`.

**Fix.** Reserve "free-ride" for the paper's meaning (the follower captures
$\theta s_1$ without paying) and describe the two regimes by the sign of
$ds_2/ds_1$ only: low θ the follower **retreats**, high θ it **counterbalances**.
Carry the F25 "defensive, not opportunistic" note onto the two concept pages.

## A5-03 — `equations.md`: the K-sub row is orphaned out of the status table — the N1 defect, repeated in the register B8 parses

**Severity**: should-fix. **Category**: 6 (register drift).

`wiki/equations.md` lines 9–24: the status table's last row is line 21
(`| K-gap | p. 497, unnumbered | A4 ✅ |`), line 23 is a prose footnote, and line
24 is `| K-sub | p. 496 / footnote 13 | A3 ✅ (corrected) ¹ |`, separated from the
table by that paragraph. A table row separated from its table by a paragraph
does not render as a row — it renders as literal pipes — so K-sub's verification
status is invisible in the one register B8 checks slide equations against. The
footnote marker `¹` also appears *before* the row it annotates.

This is exactly A3 round-2 **N1** ("prose is inserted inside a markdown table,
breaking it"), which was fixed in `numbers.md` by moving the paragraph below the
table (log.md, 2026-11-17 row 1). The same defect was then introduced in
`equations.md` and has not been caught.

**It is invisible to the script, not merely missed.** `scripts/a5_lint.py` L4
defines a table run as ">= 2 consecutive lines starting with '|'" and checks only
that a run has a separator row. The orphaned K-sub row is a one-line run, so it
is never examined. L4 will keep passing this file.

**Fix.** Move the footnote paragraph below the complete table, as was done in
`numbers.md`. Separately, L4 should flag a single `|`-line that is adjacent to a
table run — otherwise this recurs a third time.

## A5-04 — `equations.md` and the paper page §10 credit A4 with verifying three entries that were A4's premises

**Severity**: should-fix. **Category**: 4 (status claims that disagree).

`checks/a4_report.md` §1 lists its twelve compared items explicitly: eq. (2)×2,
eq. (3)×2, eq. (4), eq. (5), eq. (6) incl. $N$, eq. (7)×2, $\pi_1^*$, $\pi_2^*$,
and the $s_1^*-s_2^*$ gap. **Eq. (1), the general demand system, and the profit
definitions are not among them** — and cannot be, because A4's stated method is
to "re-derive the whole three-stage game **from the inverse demand system
eq. (1)**" and "only then compare each derived expression with the one
transcribed into the wiki page" (`a4_report.md` §Method, confirmed by the A4 loop
plan in log.md). Eq. (1) is the assumption the re-derivation starts from; a
premise cannot be confirmed by what is derived from it. `a4_report.md` §§4–6
(figure claims, items still open, actions taken) contain nothing that says
eq. (1) or the profit definitions were checked against the printed page either,
and its own verdict line counts "12/12 symbolic checks".

Yet `wiki/equations.md` marks **K-gen** (p. 493 general system), **K-1** (eq. 1)
and **K-profit** (p. 495 profit definitions) all "A4 ✅", and
`papers/Kopel2021-CSR.md` §10 reads "Equations **(1)**–(7), $N$, both profit
expressions, and the $s_1^*-s_2^*$ gap — **12/12 exact**", which both names
eq. (1) as checked and does not add up: (1)–(7) plus $N$ plus two profits plus
the gap is not the twelve rows A4 actually ran.

**Which is correct.** `a4_report.md` §1 — it enumerates its own scope. This is
the same defect class as round-2 **N4** (K-sub marked "A4 ✅" when A4 never
checked it), whose resolution log.md records as a workflow lesson: "**derived
quantities need their own check**. A4's method … structurally cannot see an error
in something the paper never printed." The premises need the same treatment for
the same reason.

**Fix.** Change K-gen, K-1 and K-profit to a status that names what was actually
done — "A1 transcription; A3 ✅ visual (pp. 493–494)", which `a3_report.md`'s
round-2 section "eq. (1) and the general demand system, visually" supports — and
restate paper page §10 as "Equations (2)–(7), $N$, both profit expressions and
the gap — 12/12 exact; eq. (1) and the general system were A4's premise and were
confirmed visually at A3 instead."

## A5-05 — Five locations record the A3 status; two of them say round 2 has not happened

**Severity**: should-fix. **Category**: 4.

| Location | What it says | Round 2 done? |
|---|---|---|
| `wiki/sources.md` table, A3 column | "⚠️ fixed, **re-review pending**" | **no** |
| `papers/Kopel2021-CSR.md` line 7 (Status header) | "A3 reviewed 2026-11-16 and the reported defects fixed … **Awaiting A3 re-review** and A6" | **no** |
| `papers/Kopel2021-CSR.md` §10 heading + body (same page) | heading "A3 — reviewed 2026-11-16, **FAIL**, defects fixed"; body "Round 2 … **PASS WITH FIXES** — 26 of 29 fully fixed, no blockers remain" | yes (heading still carries round 1's verdict) |
| `wiki/index.md` + footnote ¹ | "✅ … round 2 … returned **PASS WITH FIXES**" | yes |
| `log.md` "A3 round 2 — verification of fixes" | verdict PASS WITH FIXES, seven rows | yes |

**Which is correct.** Round 2 has happened: `checks/a3_report.md` contains a full
round-2 section (line 734 onward) with the verdict at line 743, and log.md
records its rows. `index.md` is right. `sources.md` and the paper page's Status
header are stale, and the header contradicts §10 of the file it heads — the same
within-page pattern as round-1 blocker F5 (§9 vs §10), which log.md itself notes
"A5 lint should catch". The paper page §10 *heading* is a third variant: it still
announces FAIL while its body reports PASS WITH FIXES.

**A date discrepancy, flagged not resolved.** `a3_report.md` heads its round-2
section "Round 2 — verification of fixes (**2026-11-16**)", while every log.md
round-2 row is dated **2026-11-17**. One of the two is wrong and nothing internal
settles which; the human should fix it at A6, since §7 says the course reflection
is written from the log's dates.

**Fix.** `sources.md` A3 column → "✅ (round 2 PASS WITH FIXES)". Paper page
line 7 → delete "Awaiting A3 re-review and", leaving A6 as the only open node.
Paper page §10 heading → "A3 — round 1 FAIL, round 2 PASS WITH FIXES". Reconcile
the round-2 date.

## A5-06 — Three pages say the lint "has never run"; it has run twice, fixed 8 problems, and `log.md` records none of it

**Severity**: should-fix. **Category**: 4.

| Location | Claim |
|---|---|
| `wiki/index.md` footnote ¹ | "**A5 (lint) has not run** and should precede A6." |
| `papers/Kopel2021-CSR.md` §Remaining gaps item 4 | "**A5 (lint) has never run.** … a broken table in `numbers.md`, introduced by one of the round-1 fixes, is exactly what lint exists to catch." |
| `log.md` lines 93 and 109 | "A5 lint would have caught this; **it has never run**." / "Remaining for the human at A6: F28 …, and an A5 lint pass, **which has never run**." |

`checks/` contains `a5_lint_run1.txt` and `a5_lint_run2.txt`. Run 1 found **8
problems** (L5 ×2, L6 ×1, L7 ×5); run 2 is 10/10 PASS.

**But run 2 does not pass because all eight were fixed.** At least five of the
eight still show the flagged construct, unchanged, on the flagged line:

| Run-1 problem | State now |
|---|---|
| L5 `glossary.md:11` unbalanced bracket in inline math | `$[0,1)$` still on that line |
| L5 `Kopel2021-CSR.md:68` same | `$\gamma \in [0,1)$` still on that line |
| L7 `Kopel2021-CSR.md:355` "### A4 — PASSED…", no citation or tag | still no page citation, still no tag |
| L7 `Kopel2021-CSR.md:369` "### A3 — reviewed…", same | still no page citation, still no tag |
| L7 `Kopel2021-CSR.md:381` "### Remaining gaps", same | zero `p. N` citations in the section, still no tag |
| L6 `numbers.md:55` `0.8107` not an accepted $\gamma_{\max}$ form | **genuinely fixed** — now reads `0.810736` |
| L7 `first-mover-advantage.md:5` and `:86` | both now carry page citations; cannot tell from the repo whether the page or the rule changed |

So run 2's PASS on at least the L5 and three L7 items comes from a **changed
rule, not a changed page** — the script was relaxed around the text it had
flagged. `scripts/a5_lint.py` is not in git history (`git log -- scripts/a5_lint.py`
returns nothing), so the change cannot be reviewed, and nothing in `checks/` or
`log.md` records that it happened. A clean 10/10 therefore certifies less than it
appears to. Whether relaxing those rules was right is a reasonable call — the
`$[0,1)$` "unbalanced bracket" is a false positive, and §10's verification
subsections genuinely have nothing to cite — but it must be visible.

Three consequences:

1. The three statements above are stale as written. Some staleness is expected
   while this node is in flight, so the fix is to update them at A6 rather than a
   contradiction to escalate — **but** the paper page's wording is not just
   stale, it cites the `numbers.md` broken table in the present tense as a defect
   lint would catch. That table was fixed in A3 round 2 (log.md 2026-11-17 row 1).
   The live instance of that defect is now in `equations.md` (A5-03).
2. **The real gap: `log.md` has no A5 loop plan and no A5 run rows.** Every other
   node (A1, A1 re-run, A4, A2, A3) opens with the five-point loop plan AGENTS.md
   §6 requires "before it runs", and carries its failures in the run table. Eight
   problems were found and disposed of with no entry — and §7 says the course
   reflection is written from that table, so they would be missing from the
   assignment. This is the same failure mode as round-2's log/schema mismatch
   (log.md claimed a verbatim rule that AGENTS.md did not contain).
3. **A loosened check is exactly what §6 means by "a check phrase like 'looks
   good' is not validation".** Relaxing a rule between runs and then reporting
   0 problems is the mechanical equivalent, and it is invisible without the log
   row.

**Fix.** Add the A5 loop plan and one run row per lint run — run 1: the eight
problems, and for each whether it was fixed on the page or by amending the rule
and why; run 2: clean — before updating the three "never run" sentences. Put
`scripts/a5_lint.py` under version control so rule changes are reviewable, per
AGENTS.md §8.

## A5-07 — `numbers.md` omits numbers the wiki's own prose depends on

**Severity**: should-fix. **Category**: 6 (register drift).

`numbers.md` opens: "Every number the deck may show. Node **B10** checks that
each figure on a slide appears here. **A number not in this register may not go on
a slide.**" These are used in wiki prose and are absent from it:

| Number | Used at | What it supports |
|---|---|---|
| **0.0169** — the $s_1^*=s_2^*$ frontier at $\gamma=0.3$ | `first-mover-advantage.md` line 34; paper page §7.2 warning box | the "invests more but earns less" band, i.e. the whole "Two distinct comparisons" section |
| **0.2820 / 0.2889** — $s_1^*$ vs $s_2^*$ at $\gamma=0.3,\theta=0.05$ | paper page §7.2 | the evidence that the p. 500 sentence is a slip (F8) |
| **0.6562** — $s_1^*(\gamma_{\max})$, and Fig. 1's axis top **0.66** | paper page §Remaining gaps item 1 | the figure-corroborates-$\gamma_{\max}$ finding A3 round 2 calls worth reporting in the talk |
| the full $s_1^*=s_2^*$ frontier, and $\gamma/(2-\gamma^2)$ at the five tabulated $\gamma$ | A5-01 above; `a3_report.md` C8 | the corrected mechanism in A5-01 |
| **7.48** — the K-sub denominator at $\gamma=0.5$ | `equations.md` K-sub note | the sign argument for $ds_2/ds_1$, i.e. A5-01's deterrence switch |

The first three are all load-bearing for slides the wiki itself recommends, and
B10 would reject every one of them. Note `numbers.md` already registers the FMA
frontier but not its companion investment frontier, which is why the two got
conflated in A5-01.

**A precision rule the paper page breaks.** `numbers.md` lines 21–25 say A3 got
0.2294985134 against A4's 0.2294985504 and therefore "**quote at most 7
significant digits**". Paper page §10 quotes the full "0.2294985504", and
`competition-intensity.md` quotes "0.5319633163" (10 sf) for $\gamma^\dagger$. The
register's own rule is not followed on the page that cites it. Either relax the
rule to cover the recomputation audit trail explicitly, or trim both.

**Fix.** Add an "$s_1^*=s_2^*$ frontier and the deterrence switch" table (the five
rows in A5-01, sourced to `a3_report.md` C8 for the frontier and to K-sub for the
switch), plus a Fig. 1 endpoint row for 0.6562/0.66. Mark all as own
calculation, per the section's existing rule.

## A5-08 — `equations.md` omits displayed equations that appear in other pages' prose

**Severity**: should-fix. **Category**: 6 (register drift).

`equations.md`: "a slide equation must either appear here verbatim or be
derivable from entries here." These are set as display equations in the wiki and
have no register entry:

| Equation | Displayed at |
|---|---|
| $\partial_\theta(\partial\pi_1/\partial s_1)<0$, $\partial_\theta(\partial\pi_2/\partial s_2)>0$ | paper page §7.1; `csr-spillovers.md` "Why spillovers destroy the FMA" |
| $\dfrac{\partial\pi_1}{\partial s_1}+\dfrac{\partial\pi_1}{\partial s_2}\dfrac{\partial s_2}{\partial s_1}$ (leader's incentive decomposition) | `strategic-commitment.md` "Over-investment" |
| $\partial(\partial x_i/\partial s_i)/\partial\gamma>0$ and $\partial(\partial\pi_2/\partial s_2)/\partial\gamma<0$ | paper page §6.2; `competition-intensity.md` three-effects table |

"Derivable from K-profit" is true in principle but is not a check B8 can run, and
the first and second are precisely the equations the corrected A5-01 mechanism
rests on — so they will be on a slide. The register already includes two items
that are not the paper's printed equations (K-sub, the SOC block), so there is no
precedent reason to exclude them.

**Fix.** Add three entries (suggest K-dtheta, K-strat, K-dgamma) with source refs
p. 499/§5.2, fn. 14 p. 499, and p. 498/fns. 11–12, each marked as the paper's sign
claims rather than A4-verified expressions unless A4 covered them.

## A5-09 — "Strategic substitutes / complements" is tagged `[our reading]` on three pages and used as the paper's on four, including the register B10 parses

**Severity**: should-fix. **Category**: 5 (marking-tag consistency).

Tagged as ours — `concepts/csr-spillovers.md` ("The labels 'substitutes /
complements' are standard terminology and are ours; the paper states only the
threshold. **[our reading]**"), `papers/Kopel2021-CSR.md` §5.2 (same sentence),
`wiki/equations.md` K-sub ("The explicit derivative is ours").

Untagged, presented as the paper's:

- **`wiki/numbers.md`**, "Conditions, not constants": "$\theta<\gamma/(2-\gamma^2)$ — CSR levels are **strategic substitutes**" / "strategic complements". This is the register B10 validates slides against, so the terms arrive on a slide with register authority and no marking.
- `concepts/strategic-commitment.md`: "CSR levels become strategic **complements**".
- `wiki/overview.md` concept map: "the substitutes/complements switch".
- `wiki/index.md`: "switches strategic substitutes to complements".

This is the dangerous case the task names: a reader comparing pages concludes the
untagged uses were verified as the author's. It is **A3 round-1 F27 residue, with
the locations already named.** Round 2 recorded F27 as PARTIALLY FIXED and listed
precisely these holdouts: "still appears untagged in the `equations.md` K-sub
heading, the `numbers.md` 'Conditions, not constants' table and
`strategic-commitment.md`'s 'The strategic effect is conditional'." `equations.md`
has since been tagged; `numbers.md` and `strategic-commitment.md` have not, and
`overview.md` / `index.md` were never on the list. Reported as should-fix rather
than as A3's "presentational residue" because one of the two holdouts is the
register B10 validates slides against.

**Also, `index.md`'s concept one-liners restate four tagged readings untagged**:
"far smaller than the paper's prose implies" (an `[own calculation]` result),
"$\theta$ transfers incentive from leader to follower" (tagged `[our reading]` on
`csr-spillovers.md`), "comes from an asset the rival lacks" (tagged on
`appropriability.md`), "the three links that can break" (tagged on
`strategic-commitment.md`). `index.md` is a catalogue, but AGENTS.md §3 extends
the convention to "the overview as much as to source pages" and gives no index
exemption.

**Fix.** One clause in `numbers.md`'s conditions table ("labels ours; the paper
states only the threshold"), the same on `strategic-commitment.md`, and a single
line at the head of `index.md`'s concept table noting that the one-liners
compress readings marked on the pages themselves.

---

# Minor

## A5-10 — Kopel & Löffler: the register has no row for the work three pages say is needed

**Severity**: minor. **Category**: 3 (stale cross-reference).

`papers/Kopel2021-CSR.md` §8, `wiki/overview.md` ("needs **Kopel & Löffler 2012**"),
`wiki/open-questions.md` Q2 ("**Kopel & Löffler (2012)** endogenise timing") and
`concepts/strategic-commitment.md` ("**Kopel & Löffler 2012**, p. 502") all name a
2012 paper. `wiki/sources.md`'s candidate table lists only "**Kopel & Löffler
(2008)**, *J. Economics* 94(2) — commitment, first- and second-mover advantage;
the general framework".

These may well be two different papers, and nothing internal settles that — so
this is **not** reported as a wrong year. The defect is the cross-reference:
`overview.md` says its open gaps "are tracked in [[sources]] and
[[open-questions]]", and the gap it states as needing K&L 2012 has no matching
row in `sources.md`. A reader following the pointer finds a different year and
cannot tell whether it is the same work.

**Fix.** Either add a 2012 candidate row for endogenous timing, or say in the
2008 row that the endogenous-timing paper Kopel cites on p. 502 is the 2012 one
and is a separate candidate.

## A5-11 — The p. 494 asymmetry assumption is quoted with two different words

**Severity**: minor. **Category**: 1. **Not resolvable without the PDF.**

| Location | Quoted wording, all cited to p. 494 |
|---|---|
| `papers/Kopel2021-CSR.md` §4.2 | it is "**sensible** to assume that spillovers are asymmetric" |
| `concepts/csr-spillovers.md` | "**it seems plausible** to assume that $\theta_1\le\theta_2$, because the CSR follower can free ride…" |
| `wiki/open-questions.md` Q1 | $\theta_1\le\theta_2$ is "**sensible**" because the follower can free-ride |

`checks/a3_report.md` F3 reproduces the sentence as p. 494, "it seems plausible
to assume that $\theta_1 \le \theta_2$, because the CSR follower can free ride on
the CSR efforts of the leader", which matches `csr-spillovers.md`.

**Evidence that this is probably not a defect at all.** A3 round 2 ran a
normalised match of **all 22 quotations in the revised wiki** against the PDF text
layer and reports "every one … is verbatim", with the only two apparent misses
traced to its own normalisation. If that sweep covered the paper page §4.2
quotation, then a second sentence using "sensible" does exist and both pages are
fine. The residue is then narrow: `open-questions.md` Q1 attaches "sensible" to
the $\theta_1\le\theta_2$ clause, which F3 quotes as "it seems plausible". Given
AGENTS.md §3's verbatim rule and the F4/F12/F19 history, flagged rather than
decided — this is the one finding here that only the PDF can close.

**Fix.** Spot-check p. 494 against all three (A3 territory, one page, cheap). If
two sentences exist, attach each word to the clause it belongs to; if one,
make all three match it.

## A5-12 — "Static": the paper page leads with the word the concept page spends a paragraph rejecting

**Severity**: minor. **Category**: 1.

`papers/Kopel2021-CSR.md` §9 item 7: "**Static** within each stage; no repeated
interaction, learning, or consumer memory."
`concepts/strategic-commitment.md` "What is assumed away": "**One shot — but not
'static'.** The game is multi-stage; footnote 2 (p. 492) explicitly calls it a
'dynamic (multi-stage) setting like the present paper' … **[our reading]** So the
right caveat is no repeated play, no learning and no consumer memory — **not that
the model is static**."

log.md's round-2 row asserts "The paper page §9 had it right, so two pages
disagreed", and on a careful reading it does — "static *within each stage*" is a
narrower claim than "the model is static", and the second half of the item
matches the concept page exactly. So this is not a contradiction in substance.
What remains is that the item's lead word is the one a slide writer would lift,
with no fn. 2 cross-reference and no hint that calling the model static is
specifically wrong.

**Fix.** Reword item 7 to lead with the substance ("No repeated interaction,
learning or consumer memory — the game is multi-stage, not static; see fn. 2,
p. 492") and point at `strategic-commitment.md`.

## A5-13 — K-sub's provenance: two pages credit A4, the register and the log say A4 never checked it

**Severity**: minor. **Category**: 1.

`concepts/csr-spillovers.md`: the $ds_2/ds_1$ quotient is "verified symbolically
in `checks/a4_report.md` §1". `concepts/strategic-commitment.md`: the
$\theta<\gamma/(2-\gamma^2)$ condition is "verified in `checks/a4_report.md` §1".

`wiki/equations.md` footnote ¹: "K-sub is a *derived* quantity, not one of the
paper's printed equations, so it was never in A4's twelve-equation comparison
set. **A4 passed it while it carried a sign error**; A3 caught and corrected it."
Its status column reads "A3 ✅ (corrected)", not A4. log.md's round-2 N4 row says
the same and draws the workflow lesson from it.

Downgraded to minor because it is partly a grammar accident: in both sentences
"§1" sits next to a reference to eq. (4), which A4 *did* verify, and
`a4_report.md` §1 does now carry the quotient under "Supporting facts recovered"
— itself annotated "Corrected after A3 F2". So the citation is defensible
post-correction. But it reads as "A4 verified this", which is the claim
`equations.md` exists to deny, and the distinction is the one real workflow lesson
of round 2.

**Fix.** In both sentences: "eq. (4) verified in `a4_report.md` §1; the explicit
quotient is ours and was checked at A3 (`a3_report.md` F2), not by A4."

## A5-14 — `index.md`'s "Outside the wiki" table omits the two check artefacts the wiki cites most

**Severity**: minor. **Category**: 3.

`wiki/index.md`: "| `checks/` | verification reports — `a4_report.md` and raw
script output |". `a3_report.md` is cited by name from **four** wiki pages
(`papers/Kopel2021-CSR.md` in §7.2, §7.3, §9 and §10;
`concepts/first-mover-advantage.md`; `concepts/competition-intensity.md`;
`numbers.md`), and `a5_lint_run1.txt` / `a5_lint_run2.txt` now exist too. A reader
using the index as the catalogue of what exists would not know `a3_report.md` is
there.

**Fix.** "verification reports — `a3_report.md`, `a4_report.md`, `a5_report.md`
and raw script output".

## A5-15 — Remaining F27 vocabulary, unflagged on two pages

**Severity**: minor. **Category**: 5. **Known A3 residue** (F27, round 2:
partially fixed) — reported because the fix did not complete, not as new.

A3 F27 listed four outside-vocabulary items. Two were fixed:
"irreversible"/"sunk" is now tagged on `strategic-commitment.md` ("standard
game-theoretic vocabulary, not the paper's wording"), and
substitutes/complements is tagged on three of seven pages (A5-09). Still
unflagged:

- `wiki/open-questions.md` Q2: "a **war of attrition** rather than a **Stackelberg** game" — neither term is the paper's, and the sentence is an inference about a game the paper does not solve.
- `wiki/glossary.md` Terms: "Horizontal differentiation — **taste-based** product distance".

Both are correct usage. **A3 round 2 explicitly judged these two defensible** —
"Q2 is explicitly a question we are posing; the glossary column is headed
'Meaning here'", concluding "presentational residue, not a factual one" — so this
is listed for completeness and for the human's A6 decision, not as a defect A3
got wrong. The only reason to revisit it is that B7 checks slide wording against
the wiki rather than against the paper, so unflagged non-paper vocabulary
propagates.

**Fix (optional, human's call at A6).** A `[our reading]` tag on the Q2 sentence;
in the glossary, either drop "taste-based" or mark the row's gloss as ours. If
A3's reasoning is accepted instead, record that decision so this does not get
re-raised at every lint.

## A5-16 — $\theta_i$'s correction held, but two smaller symbol gaps remain

**Severity**: minor. **Categories**: 2, 6.

The $\theta_i$ correction (round-1 blocker F3) **held uniformly** — see "Checked
and consistent" below. Two residual items:

1. `wiki/open-questions.md` Q1: "**Sets the leader's spillover to zero**". Under
   the canonical definition now used everywhere ($\theta_i$ = the share of the
   *rival's* benefit captured *by* firm $i$), "the leader's spillover" reads
   naturally as the leader's leakage *out* — the exact inversion F3 was raised to
   fix. Q1's own next paragraph has it right ("the leader benefits from the
   follower by exactly zero"), so only the summary line is loose.
   **Fix**: "Sets the spillover *into* the leader to zero."
2. `wiki/glossary.md` claims "one canonical meaning per symbol across the whole
   wiki" but has no rows for $\gamma^\dagger$, $\theta^{(1)}$ or $\theta^{(2)}$,
   which `numbers.md` introduces and uses as symbols. $D$ is in the glossary and
   marked "A4 notation, not in the paper", so the convention exists.
   **Fix**: three glossary rows, marked as our labels.

## A5-17 — `appropriability.md`'s blanket tag over a six-row table postdates the rule it breaks

**Severity**: minor. **Category**: 5.

`concepts/appropriability.md` "What raises or lowers it": "Only the first row is
the paper's; the rest is **[our reading]**", covering a six-row table. AGENTS.md
§3 now says a tag "governs the sentence or bullet it *opens*, and nothing else. A
passage longer than that needs a 🔎 box, or one tag per bullet."

Flagged with the history, because it is not a missed fix: `a3_report.md` round 2's
line-by-line tag review explicitly **approved** this placement ("`appropriability.md`
… the raises/lowers table … the tag opens the passage it governs"), and the scope
clause was added to §3 *in response to the same review*. So the rule was written
after the blessing and has not been applied backwards. The table contains no
quoted material, so the hard prohibition (never blanket-tag over quotations) is
not breached.

**Fix.** Either one tag per row in the two "our reading" columns, or convert to a
🔎 box. Worth confirming with the human at A6 whether the new scope clause is
meant to apply retroactively to text A3 passed.

---

# Checked and consistent

Coverage, so the findings above are not read as the whole of what was compared.
All 13 wiki pages were read in full, as were `log.md`, `AGENTS.md`,
`checks/a5_lint_run1.txt` and `checks/a5_lint_run2.txt`.

`checks/a3_report.md` (1,207 lines) was **not** read in full — the ranges read
are lines 1–35 (verdict and category table), 107–186 (F3–F6), 497–560 (all
minors, F19–F28), 650–700 (C8–C10 "checked and correct"), 764–766 and 855–935
(round-2 pass 1: F12–F29 and the minors, incl. F27), 958–1050 (round-2 pass 2:
N1–N8) and 1087–1135 (tag placement and the AGENTS.md verdict), plus a heading
sweep of the whole file. Lines 186–497 (most of round 1's should-fix detail) and
766–855 (round-2 blockers and early should-fix) were read only through their
headings. Any finding above claimed as "already reported by A3" rests on the
ranges listed; a finding of mine that A3 also raised inside the unread ranges
would be mislabelled as new, not wrong.

`checks/a4_report.md` was read in full. Specific traces:

**$\theta_i$ — the symbol the task singled out. The F3 correction is uniform.**
Traced through every location that defines or uses it: `papers/Kopel2021-CSR.md`
§4.1 ("the share of the **rival's** CSR benefit captured by firm $i$ … the
spillover *into* firm 1, not out of it", with the note that the p. 494 prose reads
the other way and the equation governs); `concepts/csr-spillovers.md` "Definition"
(same wording, same index-off-the-demand-system justification);
`wiki/glossary.md` row $\theta_i$ (same); plus the four places the shorthand is
used — glossary row $\theta$ ("shorthand for $\theta_2$, given $\theta_1=0$"),
paper page §4.2 ("the leader gets *nothing* from the follower's later CSR"),
`csr-spillovers.md` ("$\theta$ is the share of the **leader's** CSR that spills to
the **follower**"), `appropriability.md` ("high appropriability ⇔ low
spillovers"). No contradiction anywhere, and no page retains the inverted
reading. Only the Q1 summary line is loose (A5-16).

**Every other glossary entry against its use.** $a$, $c$, $\gamma$,
$\gamma_{\max}$, $s_i$, $s_i^2$, $x_i$, $p_i$, $\pi_i$, $N$, $D$, FMA, SMA,
appropriability, divergent/convergent CSR, vertical/horizontal differentiation —
each checked against the concept pages and the paper page. All match. Firm 1 =
leader and firm 2 = follower hold on all 13 pages with no exception; the star
convention is used consistently for equilibrium values. $D$ and $N$ are correctly
marked as A4 notation vs the paper's.

**The four key constants, beyond the script's equality check**, i.e. that each
page attaches the same *meaning*: $\gamma_{\max}=0.810736$ as the follower-
interiority bound at $\theta=0$ (paper page §4.3, `competition-intensity.md`,
`numbers.md`, `glossary.md`, `open-questions.md` Q5 — all five say interiority,
none says SOC); $\gamma^\dagger=0.531963$ as the turning point of $s_1^*$ at
$\theta=0$ (paper page §6.1, `numbers.md`, `competition-intensity.md`);
$\theta^{(2)}=0.202167$ as the **follower's** endpoint threshold and
$\theta^{(1)}=0.229499$ as the **leader's** — checked in all four locations that
carry them (paper page §7.3 table and §10, `numbers.md`, `csr-spillovers.md`,
`competition-intensity.md`). No firm/threshold swap, which is the error log.md
records A1 making on the first draft.

**The F9 endpoint-criterion caveat reached all four pages**, which round 2 had to
chase ("F9's caveat reached three of four pages"). It is now on
`papers/Kopel2021-CSR.md` §7.3, `numbers.md`, `csr-spillovers.md` and
`competition-intensity.md`, each stating that fn. 15 evaluates the derivative *at*
$\gamma_{\max}$ rather than over the interval. No page still says "monotone
throughout", which was F9's actual target. Two qualifications, neither a
contradiction: the hump interval is given as "0.190 to 0.1925" on three pages but
`csr-spillovers.md` gives only the lower end ("from about $\theta=0.190$"), which
is weaker but not inconsistent; and paper page §2 row 3 and
`competition-intensity.md` line 48 still describe the follower's low-θ curve as
"monotonically decreasing" / "falls monotonically". The latter is **not** F9
residue — both sentences are reporting Lemma 3's own claim, and both pages carry
the endpoint caveat elsewhere on the page. Flagging only so the next reviewer
does not re-raise it: if the caveat is right, those two sentences would read
better as "decreasing (endpoint criterion — see the caveat below)".

**The FMA frontier table** carries identical values and identical $\gamma$ rows in
`numbers.md`, paper page §7.2 and `first-mover-advantage.md`, and matches
`a4_report.md` §3; `numbers.md` adds a "max spillover rate" percentage column the
other two do not have, which is a superset, not a disagreement. The
percentage column in `numbers.md` is arithmetically right in all five rows
(0.0000534 → 0.005%, 0.00150 → 0.15%, 0.00867 → 0.87%, 0.0393 → 3.9%,
0.0960 → 9.6%). The F10 warning against "the leader retains $1-\theta$" phrasing
is present on both `numbers.md` and paper page §7.2, and no page uses the banned
phrasing.

**The Fig. 2 geometry is consistent across three pages**: dashed = $s_1^*=s_2^*$
with $s_1^*>s_2^*$ *below* it, bold = $\pi_1^*=\pi_2^*$ with the FMA *below* it,
dashed above bold, hence the "invests more but earns less" band (paper page §7.2,
`first-mover-advantage.md`, `overview.md`'s chain note). The F8 treatment of the
contradictory p. 500 sentence is handled identically on the paper page (full
warning box with the 0.2820/0.2889 computation) and `first-mover-advantage.md`
(short caution pointing at §7.2) — correct per AGENTS.md §3's never-silently-
overwrite rule, and the two do not disagree.

**Fig. 3 / the overlap band.** "Follower above leader at $\theta=0.21$" is stated
the same way on paper page §7.3 and §10, `numbers.md`, `csr-spillovers.md` and
`competition-intensity.md`; $0.21$ is correctly placed inside
$(\theta^{(2)},\theta^{(1)})$ on all of them; the shape table (θ = 0, 0.15, 0.21,
0.25, 0.5, 0.9) is identical in `competition-intensity.md` and `a4_report.md` §3.

**The three-effects decomposition** matches between paper page §6.2 and
`competition-intensity.md`, including the F26 fix — the demand-effect row now
carries the "no CSR spillovers" qualifier on **both** pages — and the
strategic-effect-is-leader-only attribution. The U-shape/no-U-shape asymmetry and
the fn. 11 / fn. 12 citations agree.

**The Tetrault Sirsly & Lamertz reversal (round-1 blocker F1) held.** All three
locations now say the same thing: the p. 490 framing sets TS&L against Reinhardt
and Vogel, p. 502 groups all three together, p. 491 says "in line with", and the
paper formalises rather than refutes TS&L — paper page §1 warning box and §8,
`first-mover-advantage.md` "The prior debate", and `sources.md`'s TS&L candidate
row ("p. 502 groups it with Reinhardt and Burke & Logsdon"). No page presents
TS&L as the losing side.

**The F14 convergence direction held**: the leader is the actor, not the object,
on all four pages that carry it (paper page §8, `csr-spillovers.md`,
`appropriability.md`, `overview.md`), and the N2 page number is right everywhere
— the weak-empirical-link sentence is cited to p. 491 and the "impossible for the
CSR leader to profit" sentence to p. 502, with no page swapping them. The
divergent/convergent CSR definitions match between `csr-spillovers.md`,
`appropriability.md` and `glossary.md`.

**Lemma honesty is uniform.** "Confirmed numerically on 39 grid points, not
proved symbolically, and the paper omits the proof too" appears in matching form
on paper page §10 and §Remaining gaps, `numbers.md` "Evidence standard",
`first-mover-advantage.md` and `a4_report.md` §3. No page claims either lemma is
proved — the round-1 F5 contradiction (§9 "analytic" vs §10 "numerical") is gone
and did not reappear elsewhere. The 39-point (Lemma 1) / 120-point (Lemma 3)
figures are not in conflict; they count different checks.

**Other cross-references, each followed to its target and confirmed to contain
what the pointer claims**: `csr-spillovers.md` → the 🔎 A3 caveat in
`competition-intensity.md`; `first-mover-advantage.md` → paper page §7.2;
`competition-intensity.md` → `open-questions.md` Q4; `appropriability.md` → Q3;
`csr-spillovers.md` and paper page §4.2 → Q1; `strategic-commitment.md` and
`first-mover-advantage.md` → Q2; `open-questions.md` Q2 → the frontier in
`first-mover-advantage.md`; `overview.md`'s concept map and reference table → all
eleven targets. Section-level citations into `checks/` were verified against the
actual section headings of `a4_report.md` (§1 symbolic, §2 thresholds, §2a
$\gamma_{\max}$, §3 lemmas) and `a3_report.md` (F2, F6, F8, F9, F10, C8) — every
one resolves to a section that contains the claimed content, with the single
provenance qualification in A5-13.

**Index counts and page inventory.** 1 source / 5 concept / 6 reference / 0
syntheses / 7 open questions (0 closed) match the files and `open-questions.md`'s
Q1–Q7 with an empty "Answered / closed" section. The "1 of 5 planned" header is
on all five concept pages and agrees with `overview.md` and `sources.md`.

**The A4/A3 number disagreement A3 flagged for this node is resolved.** F22
asked A5 to catch `a4_report.md` saying the follower-interiority root is 0.8599
at $\theta=0.2$ against the wiki's 0.859200. `a4_report.md` line 95 now reads
0.8592 with the correction noted, and `numbers.md` line 55 reads 0.859200. They
agree, and the wiki's value is the one A3 computed.

---

# Not checked — the limits of this review

1. **Nothing was verified against the PDF.** Every judgement above rests on
   agreement or disagreement *between* repository documents. Where only the
   source could settle a point (A5-11's quotation wording, A5-10's Kopel &
   Löffler year), that is stated and no verdict is given.
2. **A4's and A3's numerical results were not re-run**, except the one
   arithmetic step in A5-01, which is division on numbers already registered in
   `numbers.md` and `a3_report.md` C8. The $s_1^*=s_2^*$ frontier values
   (0.00256 / 0.0169 / 0.0427 / 0.0951 / 0.1527) are quoted from `a3_report.md`
   C8, not recomputed here.
3. **Figures were not inspected.** Fig. 2 remains, as A3 left it, checked
   qualitatively only.
4. **`AGENTS.md`, `需求摘要.md`, `scripts/` and `checks/` were read as evidence,
   not linted.** `scripts/a5_lint.py` was read only far enough to establish that
   L4 structurally cannot see A5-03.
5. **No file was edited.** This report is the only output.
