# Run log

Format: Date | Node | Symptom | Cause | Change made | Did it change the workflow? (yes/no + why)

## Loop plan: A1 Read source (Kopel2021-CSR)

1. **Goal**: one English summary page `wiki/papers/Kopel2021-CSR.md` covering the whole paper (model, timing, equilibrium, lemmas, figures, discussion), with page and equation citations and LaTeX equations.
2. **Limits**: write only `wiki/papers/Kopel2021-CSR.md`. Do not edit `raw/`, other wiki pages, or slides. No outside knowledge.
3. **Done criteria** (checked later by A3/A4, not by self-review): every claim has a page citation; every equation has its paper equation number; numerical thresholds are labelled as numerical; all sections of the paper are covered.
4. **Stop conditions**: maximum 3 rounds. If a page or equation cannot be read reliably, stop and record it rather than guess.
5. **Trigger**: human instruction "start A1" (2026-11-16).

## Run entries

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-16 | A1 | — | first run | — | — |

## Loop plan: A1 re-run (Kopel2021-CSR) — Opus 5

1. **Goal**: replace the Haiku draft with a page that transcribes equations (1)–(7) in full LaTeX, covers every section of the paper, and separates the author's claims from A1's own observations.
2. **Limits**: write only `wiki/papers/Kopel2021-CSR.md` and `log.md`. No outside knowledge.
3. **Done criteria**: all equations present; every claim cited to a page; §9 marked as not the author's words; verification queue written for A3/A4.
4. **Stop conditions**: max 3 rounds. Do not guess values that cannot be read from the PDF — record them as gaps instead.
5. **Trigger**: human instruction after switching the main session to Opus 5 (2026-11-16).

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-16 | A1 | Draft transcribed only eq. (1)–(2); eq. (3)–(7) left as page pointers. | Haiku 5.5 judged long equations too error-prone to transcribe from page images and deferred them to A4. | Re-ran A1 on Opus 5; all equations now transcribed inline. | yes — model policy added to AGENTS.md §10 (Opus for judgement, Haiku for mechanical steps). |
| 2026-11-16 | A1 | Draft stated "for θ < 0.202167 … the leader's CSR falls and then rises" but attached the 0.202167 threshold to the wrong firm and mis-summarised Fig. 3. | Lemma 3 names two thresholds governing different firms; the draft collapsed them. | Rewrote §7.3 with a threshold table and identified the 0.202167–0.229499 overlap band where both firms are U-shaped (which is the case Fig. 3 plots, θ = 0.21). | no — but added an explicit A3 check for this item. |
| 2026-11-16 | A1 | Draft claimed Fig. 3 CSR levels are "higher than in Fig. 1 for most γ". | Read off rendered plot images; axis maxima differ (0.66 vs 0.4), so the comparison was unsupported. | Claim removed. Added rule: no quantitative claim from reading figures; must come from A4 recomputation. | yes — added to the "Known gaps" section of the page. |

## Loop plan: A4 numerical/symbolic verification (Kopel2021-CSR)

1. **Goal**: confirm every equation and numerical threshold on the A1 page by re-deriving the model from eq. (1), not by plugging numbers into the paper's own formulas.
2. **Limits**: write only `scripts/`, `checks/`, and verified corrections to `wiki/papers/Kopel2021-CSR.md`. Never modify `raw/`.
3. **Done criteria**: all transcribed equations match a symbolic re-derivation; all three numerical thresholds reproduced to the precision the paper reports; Lemmas 1 and 3 confirmed.
4. **Stop conditions**: max 3 runs. If a threshold cannot be reproduced, record it as an open finding rather than adjusting the model to fit.
5. **Trigger**: human instruction "先跑 A4" (2026-11-16).

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-16 | A4 | `python3 -I` could not import sympy. | sympy is installed in user site-packages, which `-I` excludes. | Ran from the scratchpad with an absolute script path instead, so cwd is still not on the import path. | no |
| 2026-11-16 | A4 | gamma_max = 0.810736 did not match the denominator D (0.830176) or either second-order condition (0.830176, 0.932526). | The paper says only "interior equilibrium and all second-order conditions", without naming the binding one. | Swept every equilibrium object for a boundary crossing (`a4_gammamax_hunt.py`), found the follower's interiority at theta=0, then confirmed it is the root of N(gamma,0) at 0.8107358771 (`a4_gammamax_confirm.py`). Added to the wiki page as a finding not in the paper. | no — but it shows A4 must hunt for the binding condition, not assume one. Worth stating in the reflection. |
| 2026-11-16 | A4 | — | — | Lemma 2's FMA frontier computed numerically; the paper only describes it qualitatively. At gamma=0.3 the leader needs theta < 0.0015. Added to the wiki page as a candidate headline slide. | no |
| 2026-11-16 | A4 | A1's §5.4 flagged the pi1*/pi2* asymmetry as a possible transcription error. | It is genuine: the leader's stage-1 FOC lets one factor of s1* be substituted out. | Flag resolved and the explanation recorded. | no — the A1 habit of flagging doubts for A4 worked as intended. |

## Loop plan: A2 concept layer (after Kopel2021-CSR ingest)

1. **Goal**: build the concept layer the paper page links to, plus the reference registers that Graph B's checks need, and the overview/index that make the wiki navigable.
2. **Limits**: write `wiki/concepts/*`, `wiki/overview.md`, `wiki/index.md`, `wiki/{glossary,equations,numbers,sources,open-questions}.md`, and `AGENTS.md` §2. Do not touch `raw/` or `wiki/papers/`.
3. **Done criteria**: every `[[link]]` resolves; no orphan pages; every concept page states how many sources back it; every number on `numbers.md` carries provenance and verification status.
4. **Stop conditions**: max 3 rounds. Do not invent cross-source claims — with one source, concept pages say so.
5. **Trigger**: human instruction "先做 A2" (2026-11-16), after A4 passed.

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-16 | A2 | `index.md` was an orphan — nothing linked to it. | Wrote index as a leaf catalogue; only outbound links. | Added `[[index]]` to the overview reference table. Caught by an inline link check before commit. | yes — moved the link check earlier. It belongs in A5 (lint), but running it at the end of A2 catches breakage before it is committed, which is cheaper. Recorded for the reflection. |
| 2026-11-16 | A2 | Concept pages risk being restatements of the single source. | Only one paper ingested, so there is nothing to compare against. | Each concept page carries a "Sources so far: 1 of 5 planned" header, and `sources.md` lists eight candidates drawn from Kopel's own reference list so the next sources argue with the same question rather than adding unrelated CSR papers. | no |
| 2026-11-16 | A2 | A4's findings (gamma_max origin, FMA frontier) exist only in `checks/`, which Graph B is not allowed to read. | `AGENTS.md` §3 restricts slides to `raw/` and approved `wiki/` pages. | Folded both findings into the wiki proper (`competition-intensity`, `first-mover-advantage`, `numbers`), each marked as own calculation rather than the author's claim. | no — but it shows verification output must be promoted into the wiki, not left in `checks/`, or the deck cannot use it. |

## Loop plan: A3 independent review + fixes (Kopel2021-CSR)

1. **Goal**: have a reviewer with fresh context check the wiki against the PDF, then fix exactly what it marks as failed.
2. **Limits**: the reviewer writes only `checks/a3_report.md` and may not edit the wiki. The writer fixes only reported items — no opportunistic rewriting.
3. **Done criteria**: every blocker and should-fix addressed or explicitly declined with a reason; links still resolve; re-review scheduled.
4. **Stop conditions**: max 2 review rounds, then ask the human.
5. **Trigger**: human instruction "跑 A3 審查" (2026-11-16).

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-16 | A3 | Reviewer agent terminated with HTTP 429 — Opus 5-hour limit. | Two long Opus sessions (writer + reviewer) in one evening. | None needed: the report was already complete on disk, including the sections the agent was still editing. Committed as-is. | yes — check `checks/` for partial output before re-running a failed agent. Re-running would have cost a second full review and hit the same limit. |
| 2026-11-16 | A3 | **F1 (blocker)**: the wiki said Kopel argues *against* Tetrault Sirsly & Lamertz. p. 502 groups TS&L *with* Burke & Logsdon and Reinhardt; p. 491 says "in line with Tetrault Sirsly and Lamertz (2008) I find that a first-mover advantage exists". | A1 read the p. 490 framing ("in contrast to") and carried it into the conclusion without checking p. 502. | Rewrote §1, §8, `first-mover-advantage.md` and `sources.md`; added a warning box noting the framing and the conclusion differ. | no |
| 2026-11-16 | A3 | **F3 (blocker)**: $\theta_i$ defined as the share of firm *i*'s CSR that leaks *out*. The demand system puts $\theta_1$ on $s_2$ inside $p_1$, so it is the share flowing *in*. §4.1 contradicted §4.2 of the same page. | The paper's prose on p. 494 ("abilities to protect their CSR investments") reads the wiki's way; A1 followed the prose instead of the equation. | Corrected in the paper page, `csr-spillovers.md` and `glossary.md`, with a note that the equation governs. | no — but it shows prose and equations must be cross-checked, not read in isolation. |
| 2026-11-16 | A3 | **F2 (blocker)**: `equations.md` K-sub had $ds_2/ds_1 \propto -(\gamma^2-2)(\ldots)$ — sign inverted, so the stated implication was false. | A1 copied sympy's factored output and dropped the sign of its denominator, which sympy had printed in the reversed form $(\gamma^6-8\gamma^4+20\gamma^2-12)$. | Replaced with the explicit quotient. Verified independently: true value −0.1169 at $\gamma=0.5,\theta=0$ vs the wiki's +0.875. Corrected in `csr-spillovers.md` and `a4_report.md` too. | yes — **A4 could not have caught this.** A4 compared the wiki against A4's own re-derivation, and this expression was not one of the paper's equations, so it was never in the comparison set. Derived quantities need their own check. |
| 2026-11-16 | A3 | **F4 (blocker)**: a quotation marked `(p. 491)` that appears nowhere in the paper. | A1 compressed the real sentence into a paraphrase but kept the quotation marks. | Replaced with the verbatim sentence; also restored "in fact" and the capital W in the §2 quote. | yes — quotation marks now require a verbatim match, checked at A3, not a plausible gist. |
| 2026-11-16 | A3 | **F5 (blocker)**: §9 claimed Lemmas 1 and 2 "are analytic" while §10 of the same page said they are confirmed numerically and the paper omits both proofs. | Two sections written at different times; no internal consistency pass. | Deleted the claim; §9 item 4 replaced by the homogeneity argument (F6). | no — A5 lint should catch within-page contradictions. |
| 2026-11-16 | A3 | **F6**: the $a-c=1$ caveat was unnecessary — $(a-c)$ is a bare factor in eqs. (5)–(6), so all orderings and derivative signs are independent of it. | Over-caution: A4 flagged a limitation that the algebra rules out. | Replaced the caveat with the homogeneity argument and removed the corresponding "remaining gap". | no |
| 2026-11-16 | A3 | **F8**: the wiki silently reversed a sentence on p. 500 that contradicts Fig. 2's own labels. The wiki's reading is right. | No rule existed for what to do when the source contradicts itself. | Stated our reading plus the contradiction and the evidence. Added a rule to `AGENTS.md` §3. | yes — new rule: never silently overwrite the source. |
| 2026-11-16 | A3 | **F9**: "monotone throughout below $\theta=0.202167$" overstates footnote 15, whose criterion is the derivative *at the endpoint*. The follower's curve develops an interior hump from about $\theta=0.190$. | A4's shape classifier sampled a grid and reported the band; it reproduced the paper's number without interrogating what the number measures. | Stated footnote 15's actual criterion in three places and recorded the hump as a discussion point. | yes — reproducing a published number is not the same as understanding it. |
| 2026-11-16 | A3 | **F16**: seven passages on the concept pages read as the author's claims but are our inferences. The paper page had a marking convention; the concept pages had none. | A2 inherited no convention from A1. | Added **[our reading]** / **[own calculation]** tags throughout and wrote the convention into `AGENTS.md` §3. | yes — the convention is now a schema rule, not a habit. |
| 2026-11-16 | A3 | F7, F10–F15, F17–F18, F29 and minors F19–F27 | various: wrong page numbers, a non-verbatim blockquote, a characterisation of a cited work beyond what Kopel says, missing citations on narrative sections. | Fixed individually. | no |

## A3 round 2 — verification of fixes

Same reviewer, resumed with its round-1 context. Verdict **PASS WITH FIXES**: 26 of 29
findings fully fixed, 0 blockers remain. Both mathematical claims added in response to
round 1 (the K-sub quotient and the $a-c$ homogeneity argument) were confirmed correct
under independent re-derivation. Both gaps the reviewer had carried forward are closed.

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-17 | A3 r2 | **My F9 fix broke a markdown table.** The explanatory paragraph was dropped between two rows of `numbers.md`, so the last two rows stopped rendering as a table — in the one register B10 parses. | Edited a table by inserting prose without re-reading the rendered block. | Paragraph moved below the table. | yes — a fix is not done until the file is re-read. A5 lint would have caught this; it has never run. |
| 2026-11-17 | A3 r2 | **My F14 fix introduced a new wrong page number** in `csr-spillovers.md` (weak-empirical-link is p. 491, not p. 502). | Rewrote a paragraph and carried the old citation onto a new clause. | Corrected, with the p. 491 sentence quoted. | no — but two of my own fixes created new defects, which is the argument for re-review being mandatory, not optional. |
| 2026-11-17 | A3 r2 | **F9's caveat reached three of four pages.** `csr-spillovers.md` still said the follower's CSR "falls monotonically", so the four pages carrying the thresholds disagreed with each other. | Fixed the locations the finding named without searching for every page that carried the claim. | Added the endpoint-criterion wording and a cross-reference. | yes — when a finding lists locations, grep for the claim rather than trusting the list. |
| 2026-11-17 | A3 r2 | `equations.md` marked K-sub "A4 ✅" although A4 never checked it. | K-sub is a *derived* quantity, not one of the paper's printed equations, so it fell outside A4's twelve-equation comparison set. | Status changed to "A3 ✅ (corrected)" with a footnote explaining why. | yes — **derived quantities need their own check**. A4's method (compare the wiki against a re-derivation of the paper) structurally cannot see an error in something the paper never printed. |
| 2026-11-17 | A3 r2 | `strategic-commitment.md` called the model "static"; fn. 2 (p. 492) calls it a "dynamic (multi-stage) setting like the present paper". The paper page §9 had it right, so two pages disagreed. | A blanket tag over three bullets hid the problem — per the reviewer, it "would have surfaced" with per-bullet marking. | Reworded to "one shot — but not static", with fn. 2 cited; tags moved per bullet. | yes — tag scope is now defined in `AGENTS.md` §3. |
| 2026-11-17 | A3 r2 | `log.md` claimed a verbatim-quotation workflow rule that `AGENTS.md` §3 did not contain. | I recorded an intention in the log instead of writing the rule into the schema. | Rule added to §3. | yes — the reflection table is written from this log, so a claimed rule that does not exist would have gone into the assignment. |
| 2026-11-17 | A3 r2 | N4–N10, three tag placements, "All are now fixed" self-assessment. | various | Fixed individually. | no |

**Closed by round 2, and worth reporting in the talk**: Figs. 1 and 3 were compared
curve-to-curve for the first time in this pipeline. Fig. 1's axis top of 0.66 matches the
computed $s_1^*(\gamma_{\max}) = 0.6562$, and its dashed curve hits zero exactly at the
right-hand edge — **the printed figure independently corroborates the A4 $\gamma_{\max}$
interiority finding.** The figure had been showing it all along. Pages 493–494 were also
rendered, confirming the corrected $\theta_i$ indexing visually.

**Remaining for the human at A6**: F28 (an optional speaker note about a slip on p. 499),
and an A5 lint pass, which has never run.

## Loop plan: A5 lint (written retrospectively — see the first row below)

1. **Goal**: mechanical health checks on the wiki (links, orphans, index/disk agreement, table structure, LaTeX delimiters, constant consistency, citation coverage) plus an independent cross-page contradiction check.
2. **Limits**: the script writes only to stdout/`checks/`; the reviewer agent writes only `checks/a5_report.md`. The writer fixes only reported items.
3. **Done criteria**: script exits 0 with no problems; every judgement finding fixed or declined with a reason.
4. **Stop conditions**: max 3 script runs; one reviewer round.
5. **Trigger**: human instruction "跑 A5 lint" (2026-11-17).

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-17 | A5 | **No loop plan was written before the run**, although AGENTS.md §6 requires it. Caught by the A5 reviewer, not by me. | I treated a lint pass as too mechanical to need one. | Plan written retrospectively and marked as such. | yes — §6 applies to every node, including the ones that feel procedural. The reflection table is built from this log, so a missing plan is a missing row. |
| 2026-11-17 | A5 | **The clean 10/10 certifies less than it looks.** Of run 1's 8 problems, only 3 were fixed in the pages; **5 were fixed by relaxing the script** — 2 L5 hits (`$[0,1)$` is correct half-open interval notation; my check counted `[` against `)`) and 3 L7 hits (verification-status sections are process metadata and legitimately carry no page citation). | Both relaxations are defensible, but reporting "10/10 pass" without saying which checks moved overstates the result. | Recorded here and in `checks/a5_report.md`; the script is now committed so the relaxations are reviewable in the diff. | yes — **when a check is changed in response to its own output, say so.** A passing test that was loosened to pass is not the same as a passing test. |
| 2026-11-17 | A5 | `scripts/a5_lint.py` was **not in git** when it was being cited as evidence. | Written and run in the same turn, never staged. | Committed. | yes — a check's output is only evidence if the check itself is under version control. |
| 2026-11-17 | A5 | **A5-01 (blocker): two pages said the first-mover advantage dies *because* the leader's deterrence breaks.** Arithmetic on numbers already in the wiki: the substitutes→complements switch $\gamma/(2-\gamma^2)$ sits **6×–940×** above the FMA frontier. At $\gamma=0.3$ the FMA is gone at $\theta\approx0.0015$ while deterrence holds to $\theta\approx0.157$. | A plausible causal story was assembled from two true facts that sit at completely different scales. Nobody had put the two thresholds side by side — A3 checked the wiki against the paper, not the wiki against itself. | Rewrote `strategic-commitment.md` and `first-mover-advantage.md`; added a "Three thresholds" table to `numbers.md`; annotated the overview's causal chain with all three break points. | yes — **wiki↔source checking cannot find wiki↔wiki contradictions.** The two checks are not substitutes. Also: this is now the sharpest point in the deck, and it came out of a consistency check, not a content pass. |
| 2026-11-17 | A5 | **A5-03: the N1 table defect recurred in `equations.md`** — I put the K-sub footnote between K-gap and K-sub, orphaning the row from the register B8 parses, one turn after fixing the identical defect in `numbers.md`. L4 could not see it because it only examined runs of ≥2 pipe-lines. | Same editing habit, same blind spot in the check. | Footnote moved below the table. L4 extended to flag a lone pipe-line; verified against the pre-fix file that the new rule catches it. | yes — when a defect recurs, fix the **check**, not just the instance. |
| 2026-11-17 | A5 | **A5-04: `equations.md` credited A4 with verifying K-gen, K-1 and K-profit — A4's own premises.** A4 re-derives everything *from* eq. (1), so it cannot confirm eq. (1). | Same class as the K-sub error: a method cannot validate its own starting point. | Status changed to "A3 ✅ (page image)" with a footnote; A3 round 2 did render pp. 493–495. | no — but it is the second instance of the same structural blind spot, which is worth saying in the reflection. |
| 2026-11-17 | A5 | A5-02: "free-ride" named the low-θ behaviour on two pages and the high-θ behaviour on two others — opposite responses sharing a word. | No terminology note existed. | Terminology box added to `strategic-commitment.md`. | no |
| 2026-11-17 | A5 | A5-05/A5-06: five locations recorded node status; two still said A5 had never run. | Status is duplicated across index, sources, the paper page and the log. | All updated. | no — but duplicated status is a standing lint risk; L-checks for it would be a sensible addition. |

## Loop plan: light ingest of sources 2–5

1. **Goal**: meet the assignment's 5-source requirement *and* give the concept layer something to compare against, without pretending to the verification depth of source 1.
2. **Limits**: read and summarise only — no A4 symbolic verification, no per-paper A3 review. Every page must say so. `raw/` is read-only; no downloading.
3. **Done criteria**: 5 sources registered; each paper page states its depth; at least one concept page that was impossible with one source; A5 lint passes; assurance levels never mixed.
4. **Stop conditions**: 4 papers, one pass each. If a paper turns out not to be on the same question, drop it rather than force a connection.
5. **Trigger**: human instruction "輕量補 4 篇" (2026-11-17).

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-17 | A1 light | The four extra PDFs were already in the same folder as source 1; the plan had assumed they would have to be supplied. | I had only looked for the one filename the human named, and `sources.md` had been written around candidates from Kopel's reference list that are not available locally. | Picked the 4 of 7 local papers that model strategic CSR in a duopoly; recorded the 3 rejected and why. | no — but "check what is already in the folder" would have saved a planning round. |
| 2026-11-17 | A1 light | Two assurance levels now coexist in one wiki, and nothing stopped a light-depth number reaching a slide. | A new failure mode: with one source, "verified" was unambiguous. | Depth column in `sources.md`, a ⚠️ banner on each light page, a rule that a light number may not go on a slide unchecked, and depth shown in `index.md`. | yes — **mixed assurance is itself a risk**, and the wiki now has to carry provenance of *confidence*, not just of claims. |
| 2026-11-17 | A2 | Four summaries alone would have added nothing — five disconnected pages. | A concept layer needs a comparison, not a pile. | Wrote two cross-source pages that were impossible with one paper: [[rival-exclusion]] (three models independently drive a rival to zero) and [[csr-modelling-choices]] (the five papers formalise "CSR" five different ways, so results do not transfer). | no — this is what the 5-source requirement is actually for. |
| 2026-11-17 | A2 | $\theta$ means "spillover rate" in Kopel and "CSR level" in Bárcena-Ruiz; $\beta$ means "CSR level" in Chen and "cross-ownership share" in Bárcena-Ruiz. | Independent literatures reusing letters. | Symbol-clash table added to `glossary.md`. | yes — the glossary's "other sources' notation" column existed from A2 but was empty; multi-source ingest is what makes it load-bearing. |
| 2026-11-17 | A5 | Lint flagged Hirose & Matsumura's $\delta^{**} \approx 0.531$ as a malformed version of Kopel's $0.531963$. | L6 matched on a numeric prefix with only Kopel's constants registered. | Registered the light sources' constants separately and switched L6 to "accepted by any source, else flag". **The near-collision is real and is now logged as [[open-questions]] Q9** — the two numbers are not known to be the same object and must not be presented as a finding. | yes — the lint's own false positive surfaced a genuine trap. |
| 2026-11-17 | A5 | Seven new sections carried no page citation. | New pages written before the L7 rule was in mind. | Citations added. | no — the check did its job on first contact with new material. |

## A6 signed off — 2026-11-17

MingLu signed off Graph A. All nodes complete: A1 → A2 → A3 (2 rounds) → A4 → A5.
Recorded in `wiki/sources.md` and `wiki/index.md`.

## Loop plan: Graph B, nodes B1–B4

1. **Goal**: an evidence-backed 30-slide outline for a 30–45 minute English seminar, ready for human review at B5.
2. **Limits**: write only `notes/`. Slides may draw **only** on `notes/cards/`; cards may draw only on verified wiki pages. No new claims.
3. **Done criteria**: every slide has a card reference; the coverage gate script passes; act structure fits the time budget; assurance levels flagged where light sources are used.
4. **Stop conditions**: **stop at B5.** Do not draft slides or script before the human confirms the outline.
5. **Trigger**: human instruction "簽核，開始 Graph B" (2026-11-17).

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-17 | B3 | Cards risked being a pointless copy of the wiki. | With a wiki this well cited, "evidence cards" look redundant. | Kept them, because their job is an **information barrier**, not a summary: B4 may use only cards, so a fact that did not survive carding cannot reach a slide. 79 facts carded; 6 deliberately unused. | no — but it clarified *why* the node exists. Merging B3 into B4 would have removed the barrier while looking tidier. |
| 2026-11-17 | B2 | — | — | Wrote the coverage gate as a script, not a judgement: it parses card IDs out of `notes/cards/` and out of `notes/outline.md` and fails if the outline cites an ID that no card defines. Passes 30/30. | yes — the gate is now mechanical and will re-run on every outline edit. |
| 2026-11-17 | B4 | The obvious running order put our own strongest result last. | Habit: save the best for the end. | Moved the three-thresholds result to slides 22–23 of 30, so the talk ends on the room's questions rather than on our arithmetic. Two honesty slides (14, 24) are in the main deck, not the backup. | no — a presentation decision, recorded because it is the kind of thing to revisit if the talk runs long. |

## Loop plan: Graph B, nodes B6–B11

1. **Goal**: a 30-slide English HTML deck and a speaker script that lands inside 30–45 minutes, both drawing only on the cards.
2. **Limits**: write `slides_html/`, `notes/`, `scripts/`. No new claims; anything not on a card may not appear.
3. **Done criteria**: B8 (every slide equation in the register), B10 (no slide overflows), B11 (timing inside the window, every slide scripted) all pass; then B7 independent faithfulness review.
4. **Stop conditions**: max 3 rounds per check.
5. **Trigger**: human confirmed the outline at B5 (2026-11-17).

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-17 | B9 | The preview pane served the deck as a `data:` snapshot, so JS and the KaTeX CDN never ran — nothing about the rendered deck could be verified. | Local files outside the served root are snapshotted, not hosted. | Served `slides_html/` over a local HTTP server and checked against that origin instead. | yes — **a render check against a snapshot is not a render check.** Verify at a real origin or not at all. |
| 2026-11-17 | B10 | Content overflowed the slide and ran under the footer at the pane's size; layout changed with every viewport. | The deck used viewport-relative `clamp()` type, so there was no canonical layout to check. | Rebuilt as a fixed 1280×720 stage scaled to fit. Layout is now identical everywhere, so the overflow check means something. **0/30 slides overflow.** | yes — a responsive deck cannot be mechanically checked for overflow; a fixed stage can. |
| 2026-11-17 | B8 | The first run reported 5 missing equations; 3 were real, 2 were the checker mis-parsing — stray inline `$` joined across slides into fake `$$` pairs. | The extractor scanned the whole document for `$$` pairs. | Restricted it to display maths alone inside a `<p>`, and normalised trailing commas (the register joins parts with `, \qquad`). Then added the three genuinely missing entries to the register: the generic profit form, **K-fma** (the FMA definition), and **K-theta** (the two opposite-signed derivatives). | yes — the register was missing the definition the whole talk rests on. B8 found that, which is exactly its job. |
| 2026-11-17 | B11 | The first script ran **24–28 minutes** — below the 30-minute floor. | I wrote to the slide count, not to the clock. | Expanded by ~900 words where a graduate audience would actually want more: the backward-induction sketch, why the strategic effect is a two-negatives story, a walk-through of the three-threshold figure, and the Hirose & Matsumura contrast. Now 30.2–34.8 min. | yes — **write the script to the clock, not to the slides.** A timing check after drafting is too late to be cheap. |
| 2026-11-17 | B6 | — | — | Figures plotted from the A4-verified expressions rather than copied from the PDF (outline decision 5), so the curve is provably the one that was checked, and can be annotated. | no |

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-17 | B7 | **Blocker: the slide-4 Economist quotation was untraceable in the card chain.** The card carried only the final clause; the slide showed all three sentences. | B3 carded a shorter span than the wiki page held, and B6 then drew on the wiki habit rather than the card. | **I checked p. 490 directly: the three-sentence quotation is verbatim and correct.** So the deck was right and the *card* was wrong. Expanded C1.7 to carry the full quotation. | yes — and this is the sharpest lesson of the node. B7 could not see the PDF by design, so "unsupported by the chain" was the correct verdict on the evidence available, even though the content was sound. **A card that carries less than the wiki silently narrows what the deck is allowed to say** — and B3 had no check for that. |
| 2026-11-17 | B7 | Slide 23, the climax, said the follower "captures part of the leader's demand shift" — re-importing the subtraction reading that C5.5 forbids and slides 10 and 20 explicitly disclaim. Untagged, under a footer reading "mechanism from Kopel". | Writing the same idea a third time, the careful phrasing eroded. | Reworded to "receives a demand shift it did not pay for", tagged `our reading`, and scoped the claim to θ between 0.0015 and 0.0169. | no — but it shows a rule obeyed on two slides can still fail on the third. |
| 2026-11-17 | B7 | Lemma 2 was labelled verbatim with two of four sentences missing — and the omitted half is Kopel separating the profit and CSR-level comparisons himself, which is the distinction slide 22 is built on. | C5.2 summarised instead of quoting. | Card and slide now carry Lemma 2 in full. | yes — "verbatim" on a card must mean the whole statement, not the part that was convenient. |
| 2026-11-17 | B7 | The script told the room to look at slide 16 for "the axis labelled 0.66" — a feature of *Kopel's* Figure 1, not of our replot, which the deck never shows. | Outline decision 5 (replot rather than copy) was taken after the script's framing was drafted. | Script now distinguishes our replot from Kopel's figure. | no |
| 2026-11-17 | B7 | The script promised seven backup slides that did not exist in the deck. | The outline specified them; B6 wrote the script's references but not the slides. | Seven backup slides added (B1–B7), and the B11 checker now counts backups separately so it cannot be fooled by the slide total. | yes — a promise in the script is a deliverable; the check should catch it. |
| 2026-11-17 | B7 | 17 minors: dropped ellipses in quotations, our arithmetic spoken untagged, a claim about the author's motivation, an intensified verb ("collapses" for "falls so much that"). | Ordinary drift over a long draft. | All fixed. | no |

## 交件文件 — 2026-11-17

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-17 | 交件 | The deck's KaTeX stylesheet is on cdnjs, which the **artifact CSP blocks** — every equation would have rendered unstyled for anyone opening the published link. Caught by the publish result's own warning, not by B10 (which tested a local origin where the CDN works). | B9/B10 verified at `127.0.0.1`, where third-party stylesheets load fine. The published environment is stricter than the test environment. | Wrote `scripts/b9_inline_katex.py`: fetches KaTeX's CSS, inlines the 254 KB of woff2 faces as data URIs, and drops the unreachable woff/ttf sources. Deck is now self-contained (402 KB) and was republished. | yes — **test in the environment you ship to.** A render check at a more permissive origin can pass while the real one fails. |
| 2026-11-17 | 交件 | 19 markdown files are not a "link", which the assignment asks for. | The wiki was built for agents to read, not for a human to browse. | Wrote `scripts/build_wiki_site.py` — a markdown subset converter (no library available) producing one browsable page: 19 pages, 644 rendered equations, 42 tables, 0 broken anchors. Published. | no |
| 2026-11-17 | 交件 | **Three of the counts in my own submission document were wrong** — reports, scripts, commits. | Written from memory of a long session rather than counted. | Counted them with a script and corrected; recorded in the reflection material, because a verification project miscounting its own artefacts is the point. | yes — **never write a count you did not just measure**, whatever the subject. |

## Loop plan: 第六節反思 ＋ 獨立審查（補寫，見下方倒數第二列）

1. **Goal**: 第六節直接回答作業的三個問題，每個主張都有可查證的一手出處。
2. **Limits**: 只寫 `繳交/繳交內容.md` 第六節、`log.md`，以及審查要求的連帶更正（§5、附件清單）。判斷必須是 MingLu 的，不代筆。
3. **Done criteria**: 獨立審查的每一項 A 類與 B 類發現都已修正或明確拒絕並附理由。
4. **Stop conditions**: 每件產出最多 2 輪審查（§8a），之後停下來交給人。
5. **Trigger**: 人工指示「一起討論寫」，以及 MingLu 指出三個問題必須被直接回答（2026-11-17）。

## 第六節反思 — 獨立審查（2026-11-17）

兩位獨立 reviewer（Opus，新 context）查核 `繳交/繳交內容.md` 第六節的每一條事實主張。
判定 **FAIL**，8 項必改。報告：`checks/section6_review.md`、`checks/section6_review_appendix.md`。
三個答案的方向都成立，但其中兩個答案的**主證據**是錯的。

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-17 | 反思 | **問題一的 blocker 歸屬表把 A4 寫出來的兩個 blocker（F2 符號反、F4 捏造引文）算給了 A1。** 審查者用 `git log -S` 查字串首次進 repo 的 commit：兩者都在 `39bd252`（A4），而 `git show 5acf804:wiki/papers/Kopel2021-CSR.md ｜ grep -c 'must be very low'` → 0。 | 我照 `log.md` 的 Cause 欄歸因，而 Cause 欄是事後憑記憶寫的。 | 改成 A1→3、A4→2、A2→1、B3→1。答案（A1 單一節點最高）不變。並補上分母偏誤的說明：只有 A3/A5/B7 做嚴重度分級，腳本節點結構上為零。 | yes — **歸因要查 git，不要查自己的紀錄欄。** 一份用來寫反思的 log，它的 Cause 欄本身未經驗證。 |
| 2026-11-17 | 反思 | **「A4 結構上不可能抓到 F2」的理由不完整。** 我寫的「不在 12 條方程式比對清單裡」本身是真的（`log.md` A3 r2 那列就這麼記），但漏了更直接的一層：**那條式子就是 A4 自己寫的**。 | 沒查 F2 的出處就解釋它，所以只看到比對清單這一層。 | 兩層理由並列，結論改寫成「一個節點無法稽核自己的輸出」。第五節原本只印舊理由，補上了交互參照。 | no — 但這是全節最尖銳的一句，而我原本寫的是較弱的版本。 |
| 2026-11-17 | 反思 | **問題三「結構性修改四項」有三項存在於初始 commit**（§8a 獨立審查、B3 證據卡、A3/A5 拆分），而 B3 那列的 log 自己填 `no`。`AGENTS.md` §5 開頭也自己寫著：相對於老師的示範 graph，本專案加的是 **B8 與 B11**。 | 憑印象說「新增」，沒跑 `git show de8d030:AGENTS.md`。 | 換成四項真正的 schema 修改（§10 model policy、§2 四張登錄表、§3 兩次規則新增），各附 commit。另把兩層保證水準降級為「做了但沒進 schema」（`grep -i assurance AGENTS.md` → 0）。 | yes — **「有沒有改流程」要用 `git diff` 回答，不是用印象。** |
| 2026-11-17 | 反思 | **A4 的 schema 擴權從未被當成問題記錄。** `AGENTS.md` A4 列的 Writes 只有 `pass/fail report`，但 A4 的 loop plan 自己放寬成「verified corrections to the wiki page」，並在 `39bd252` 寫了一個帶引文的 🔎 box 進 `wiki/papers/` —— 那個 box 裡就是 F4。 | 擴權當時被記錄成 loop plan 的一行，沒有人問「一個腳本節點開始寫散文會怎樣」。 | 寫進反思，並定為下一版 schema 要補的第一項：驗證節點不得寫入 wiki 正文，發現必須經過一次明確的提升步驟。 | yes — **擴權有記錄不等於擴權有評估。** 這是七個 blocker 之一的直接成因。 |
| 2026-11-17 | 反思 | **「57 筆／30 筆」實際是 60 筆／32 筆。** 57 = 60 減掉交件三列。（我原本寫「恰好是 §5 節點表的加總」也不對：那張表自己漏了 B3，加總是 56。） | 用自己整理的表當母體去數，而不是數 `log.md` 本身。 | 重數並改正；§5 節點表補上 B3 與交件列。 | yes — 又一次「憑既有整理而非原始檔案」。與上面三筆同一類錯誤。 |
| 2026-11-17 | 反思 | **「三個門檻相差約 105 倍」違反 `wiki/numbers.md` 自己登錄的規則**（該比值不得以單一數字陳述）。105× 只在 γ=0.3；§5 寫的「6 到 940 倍」則是表格從 γ=0.1 起算的產物，比值隨 γ→0 發散。 | 把一個隨參數變化的量寫成一個數字。 | 兩處都改成趨勢敘述並附樣本點。 | yes — **我違反的是我自己寫進 wiki 的規則**，而 lint 沒有檢查「散文是否遵守登錄表的使用限制」。 |
| 2026-11-17 | 反思 | **§5 的「B10 渲染 PASS — 37 頁零溢出」沒有任何 artefact。** `log.md` 只記過 0/30，七張備用頁是之後才加的；`checks/` 裡沒有任何溢出檢查輸出。 | B10 當時是在瀏覽器裡臨時跑的 JS，結果沒有落檔。 | 重跑並涵蓋 37 頁，寫成 `scripts/b10_overflow_check.js` ＋ `checks/b10_run5_37slides.txt`。結果 **0/37，最窄餘裕 27 px**，所以原本的宣稱是真的——**只是當時無從查證**。重跑時第一版判準把 37 頁全判失敗（拿 padding box 比，而 `.foot` 依設計就在 padding 區），修正判準後才正確；另有一個 wrapped inline 造成的假陽性。 | yes — **一個沒有落檔的檢查等於沒跑過。** 腳本節點的輸出必須進 `checks/`，否則下一輪無法複驗。 |
| 2026-11-17 | 反思 | 「人是 graph 裡唯一沒有被規範輸入輸出的節點」寫錯：A6／B5 的 Reads 欄與失敗邊都有寫，而 `A6_簽核清單.md`（183 行）正是「人該看什麼、抽查幾項、何時退回」。 | 只看了 Writes 欄就下全稱結論。 | 改成真正的缺口：人工程序寫在一次性清單裡、沒進 schema（不會被下一輪繼承），且兩個人工節點只做了 A6 一個，**B5 連清單都沒有**。 | no — 但缺口的描述從「沒規範」變成「沒繼承」，是不同的修法。 |
| 2026-11-17 | 反思 | 「新想法只被允許待在 open-questions」被本文件自己的最佳發現否證——三門檻是 `[own calculation]`，已上投影片 22–23。 | 把「被擋下」和「需要新算一輪才做得到」混為一談。 | 改成：能通行的是「用既有工具重整既有數字」，被擋死的是「需要新解一次模型」。Q1（$0<\theta_1<\theta_2$ 重解模型）確實整輪未執行——八支腳本沒有一支把 θ₁ 當自由變數。 | no |
| 2026-11-17 | 反思 | 其餘 B 類：「修正是第二名」沒有一致度量（用 blocker 算是 0）、「下游每道檢查都會回報通過」對 F3/F5 不成立（同頁矛盾，A5 本該抓到）、「A2 的唯一輸入」與 schema 寫的「A1 page + existing concept pages」不符、A5「改了 3 個頁面」實為 3 個問題分佈在 2 個檔案、Q1 被誤述為「比較靜態」、Haiku 版 A1 的缺陷只有自述為證（草稿未進版控）。 | 多為措辭過寬或換了度量。 | 逐項加上限定語或改正。 | no |

### 第六節 — 審查第二輪（2026-11-17）

同一位審查者，帶著第一輪 context 續跑。判定 **PASS WITH FIXES**：A 類 8 項中 7 項
完全修好、1 項部分（計數）；B 類 10 項中 9 項完全修好。報告：`checks/section6_review_round2.md`。
已確認不必再動的部分：blocker 歸屬、四項 schema 修改的 commit 落點（逐一驗證無誤，且
`git log e2d664a..HEAD -- AGENTS.md` 為空，證明那張表是完整的）、七個 commit hash、
70／37 兩種數法一致、12 張表格結構零告警（犯過兩次的表格缺陷沒有第三次）。
審查者並從論文 eq. (1) 獨立重解賽局，三個取樣倍數全部重現（6.13／104.6／940.5），
γ→0 發散確認，`ds₂/ds₁` 與論文 eq. (4) 經 sympy 判定相等。

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? |
|---|---|---|---|---|---|
| 2026-11-17 | 反思 r2 | **改寫時把「`numbers.md` 由 B10 解析」換成了 B8。** 舊版寫的是 B10，是對的。 | 重寫整段時憑記憶填節點編號。 | 改回 B10（`AGENTS.md` 第 29 行）。 | yes — 這與 A3 F14「把舊引用帶到新句子上」是同一類；**重寫一段文字會破壞段內原本正確的細節**，不只是修正會。 |
| 2026-11-17 | 反思 r2 | **「零 KaTeX 錯誤」整個 repo 沒有任何 artefact**，卻和有 artefact 的溢出數字共用同一個指標。 | B10 當時肉眼看過就寫下來，溢出腳本不驗這一項。 | 第五節明白標成未驗證。 | yes — **一個有 artefact 的數字會把可信度借給旁邊沒有 artefact 的數字。** 這跟 F4 把真句子壓成假引文同構：形式正確，來源沒有。 |
| 2026-11-17 | 反思 r2 | 「渲染檢查已移到發布環境」落實程度寫得太滿：`checks/b10_run5_37slides.txt` 的 origin 至今仍是 `127.0.0.1`。 | 把「問題修好了」當成「檢查搬家了」。 | 改成「半套」，並說明差別。 | no — 但這正是（甲）表要分落實程度的理由。 |
| 2026-11-17 | 反思 r2 | **「這些錯沒有一個是我自己發現的」是反方向的過度宣稱**：三個計數是我自己抓的（commit `8d0f2fe`，早於任何第六節審查）。 | 寫到結尾時為了收束而誇大。 | 補上分界：自己抓得到「知道該去數的東西」，抓不到「以為已經查證過的東西」。 | yes — **自我批評也要受同一個查核標準**，否則它只是另一種沒查證的敘事。 |
| 2026-11-17 | 反思 r2 | 問題三引用了「`AGENTS.md` §5 說本專案加的是 B8／B11」當論據——**那句話在初始 commit `de8d030` 就存在**，所以它不能用來證明本輪改了什麼；而且「那兩個我一個字都沒提」被同一節的（甲）表自己否證（B11 就在表裡）。 | 這句是第一輪審查報告的論據，我照抄進文件，沒有自己再查一次。 | 整句刪除。 | yes — **審查報告也是二手資料。** 照抄審查者的論據而不自己驗證，和照抄自己 Cause 欄的錯誤性質相同。 |
| 2026-11-17 | 反思 r2 | **`log.md` 又一次缺 `AGENTS.md` §6 要求的 loop plan**（這次是寫反思這個節點本身）。A5 那一輪已經記過同一個缺失。 | 又一次把「寫文件」當成不需要 loop plan 的工作。 | 補寫在上方並標明是補寫。 | yes — 同一缺失第二次發生，所以不該只補這一次：**§6 的五項應該變成寫入 `log.md` 時的必填欄位，而不是靠記得。** 列為下一版要補的項目。 |
| 2026-11-17 | 反思 r2 | 「57 恰好是 §5 節點表的加總」算錯：那張表漏了 B3，加總是 56；57 是 60 減掉交件三列。 | 連解釋計數錯誤的那句話本身也沒驗算。 | 改正。 | no — 但很值得記：**在解釋一個計數錯誤時又算錯一次。** |
| 2026-11-17 | 反思 r2 | 其餘不精確：「推翻答案」應為「推翻證據」、「八支腳本」應為「八支 Python 腳本」、`a4_verify_kopel2021.py`「把 θ₁ 寫死為 0」不準（符號清單裡根本沒有 θ₁）、4／8／15 需加時間錨點、「2 個檔案」是審查的推論。 | 措辭過寬。 | 逐項加限定語。 | no |
| 2026-11-17 | 反思 r2 | 審查者自己也先解錯一次——把第三階段當成 Cournot，算出的倍數是 21.6× 而非 6×，差點把一個有外部錨點的正確數字判成缺陷；改用價格競爭後全部對上。 | — | 記錄下來。 | yes — **獨立審查者也會錯，所以審查意見要能被原始證據反駁。** 它之所以沒造成損害，是因為那個數字有 Fig. 1 軸頂這個外部錨點可以對。 |
| 2026-11-17 | 反思 r2 | `A6_簽核清單.md` 自己 §0 寫「六項／20 分鐘」、§2 寫「五項／15 分鐘」。 | 清單寫完後改過項目數，沒有同步標題。 | 已修：§2 標題改為「六項／20 分鐘」，與 §0 及實際的 2.1–2.6 六個小節一致。 | no |

## 交件與公開發布 — 2026-11-23（補寫的 loop plan）

> **補寫聲明**：本節的 loop plan 是在執行之後才補的。這是 `AGENTS.md` §6 要求「執行前寫入」的規定第三次被違反（A5、反思、本節），見下方第四列。

1. **Goal**: 助教以未登入身分打開一個連結，就能瀏覽簡報、wiki 與流程證據；繳交文件的每個數字與連結都可查證。
2. **Limits**: 不得公開付費期刊 PDF；不得公開本機 email；不得改 `raw/`；只改繳交文件、log、被審查指出的檔案。
3. **Done criteria**: 公開 URL 以讀者身分全部 200；公開 repo 0 個 PDF；繳交文件的計數可由文件內的指令或 `checks/` 的 artefact 重現；獨立審查的 A 類全部修正或附理由拒絕。
4. **Stop conditions**: 獨立審查最多 2 輪（§8a）。本節目前是第 1 輪審查後的修正。
5. **Trigger**: 人工指示「推到 GitHub 讓助教瀏覽」「上線後換連結」「檢查更正」。

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? (yes/no + why) |
|---|---|---|---|---|---|
| 2026-11-23 | 交件 | **兩個已發布的 artifact 權限都是 `read: "owner"`**——助教點開只會得到權限錯誤。簡報與 wiki 在本機、在發布結果裡都「完成」了，但對唯一的讀者不可達。 | 把「發布成功」當成「對方打得開」。發布工具回傳 200 與一個 URL，沒有回傳權限，而這個 MCP server 也改不了分享設定。 | 改用 GitHub Pages 重新發布，並以讀者身分（未登入、純 HTTP）逐一實測 6 條路徑皆 200。 | yes — **產出不是「做完」就算交付，要以讀者的身分、用讀者的權限打開一次。** 這個檢查必須在交件節點之前，而不是交件之後。 |
| 2026-11-23 | 交件 | 要把 repo 推公開時才發現 **`raw/` 的五篇 PDF 全在 git 歷史裡**，其中四篇是付費期刊論文——直接 push 等於公開散佈。 | `AGENTS.md` §1 只規定 `raw/` 唯讀，沒有規定 `raw/` 不得離開 repo。唯讀防的是「改壞來源」，防不了「把來源發出去」。 | 另建單一 commit 的公開快照 repo（不含 `raw/` PDF，附 `raw/papers/README.md` 說明原因），並寫 `HISTORY.md` 保存第六節引用的 8 個 commit hash 及其用途（`raw/papers/README.md` 只存在於公開快照，本機因 §8 限制 `raw/` 只能新增來源檔而不放）。以 GitHub API 查核公開 repo：tree 共 110 筆（含 17 個目錄），其中 93 個檔案、0 個 PDF。（初版寫成「110 個檔案」把目錄當成檔案，經獨立審查更正。） | yes — **§1 應補一條：`raw/` 不得出現在任何對外發布的產物裡，git 歷史也算。** 唯讀與不可外流是兩條不同的規則。 |
| 2026-11-23 | 交件 | `checks/section6_review_appendix.md` 引用的重推腳本 `ord3.py` 指向暫存目錄，**該目錄現已被清空，檔案不存在**——第六節最吃重的那個結論（三門檻排序）的可執行證據沒了。 | 審查者當時就在同一行警告過這個風險（「暫存目錄，隨時可能被清除」），但只留了警告，沒有把檔案搬進 repo。 | 把該行改成過去式並說明倖存的是報告裡的書面推導；同時指出 `scripts/a4_gammamax_confirm.py` 仍可獨立佐證 $\gamma_{\max}$ 那一半。 | yes — **凡是在產出裡被引用的 artefact，必須當場移入 repo；暫存路徑不算引用。** 自己標了風險卻不處理，等於把風險留給讀者。 |
| 2026-11-23 | 交件 | **`log.md` 的 §6 loop plan 缺失第三次發生**，而且是在補前兩次教訓的同一輪裡。上一輪反思 r2 曾寫下「§6 的五項應該變成寫入 `log.md` 時的必填欄位，而不是靠記得」。 | 靠記得，所以又忘了。那條「列為下一版要補」的改動沒有被做出來，只被寫下來。 | 補寫上方的 loop plan 並標明是補寫。**沒有**做結構性修正（例如寫入 log 的腳本強制檢查五欄）。 | no — 只補了這一次。**把改善「記下來」不等於改善「做了」**：第三次發生就是證據，結構性修正仍待辦。 |
| 2026-11-23 | 交件 | 上一輪我 commit 了一批更正（`84be944`），但**公開 repo 完全沒有收到**：助教打開的繳交文件七處計數仍是舊的、`log.md` 沒有 11/23 的列。獨立審查用 GitHub API 查出。 | 「commit 成功」被當成「讀者看到了」——和本節第一列的 artifact 權限是同一個錯誤的第二次發生，只是這次發生在 git 而不是 artifact。 | 在公開 repo 同步並 push，之後從 `raw.githubusercontent.com` 以讀者身分重抓驗證。 | yes — **每次更正的收尾動作是「在讀者的 URL 上看到它」，不是 commit。** 驗證的對象是公開樹，不是本機樹。 |
| 2026-11-23 | 交件 | **`README.md` 與 `docs/index.html` 只存在於公開 repo，不在本機版本控制下**，所以我之前所有「全 repo 重數、全 repo grep」都結構性地掃不到它們。實際藏在裡面的錯誤：`80 筆／43 筆` 舊計數、`17,700 字` 無 artefact、`六份報告`（實際 7 份，而繳交文件本身已明文決定不寫份數）、`本 repo 是單一 commit 快照`（實際已有多個 commit）。 | 公開版是用複製建出來的，landing page 與 README 在那一步才寫出來，之後沒有回灌到本機。兩個樹各自演化。 | 在公開樹直接修正；同時把本輪的所有檢查改成**同時掃兩個樹**。**沒有**把這兩個檔納入本機版控。 | yes — **凡是會被對外發布的檔案，必須在被檢查的那棵樹裡。** 否則檢查只對一半的東西說了真話。這次靠獨立審查才發現，我自己的檢查設計就有盲區。 |
| 2026-11-23 | 交件 | **姓氏寫錯：公開的 `README.md` 與 `docs/index.html` 都寫「陸明權」，繳交文件第六節開頭也是**（正確是「呂明權」）。同一輪我還對使用者說「入口頁沒有任何署名」，那句也是錯的——它已經署了名，只是署錯。 | 姓名是我憑印象寫的，不是從使用者提供的資料來的；而且錯字出現在使用者**剛要求我更新個人資料**的同一輪。 | 三處全改成「呂明權」；檢查改成 grep 兩個樹的身分字串。 | no — 但值得記：**更新個人資料時，只改使用者指給你的那一處，等於沒有更新個人資料。** 要把同一個事實在全部出現處掃一遍。 |
| 2026-11-23 | 交件 | 繳交文件兩個已被 §5 自己標為「應有 artefact」的宣稱仍沒有 artefact：`約 17,700 字`、`0 個 KaTeX 錯誤`（§2／§3 用「實測」斷言，§5 B10 列卻自承「當時是肉眼看的」——同一份文件前後矛盾）。 | 上一輪審查只修了 §5 那一處，沒有回頭改 §2／§3 的斷言。 | 沒有只把話放軟，而是**實際量測並存檔**：`checks/wiki_wordcount.txt`（原始詞數 17,836、散文詞數 14,007，兩個口徑都寫出來；原本的 17,700 接近原始詞數）、`checks/live_render_check.txt`（線上版 deck 103／wiki 644 個節點、0 個 `.katex-error`）。三處斷言都改為指向 artefact，並寫明它證明什麼、不證明什麼。 | no — 規則本來就有（不得寫沒量過的數字），只是沒被執行。但注意 17,700 這例子：**數字是對的，錯的是沒留證據**，所以讀者無法分辨它是量出來的還是編的。 |
| 2026-11-23 | 交件 | §6 問題一寫「表面上 A3 最多（18 筆）」。補了三列 log 重數後，**審查第六節反思的那兩輪有 20 筆，比 A3 的 18 筆多**，這句話不成立。 | 重數時只更新了「80→83」這類**數字**，沒有重新檢查**依賴這些數字的排序主張**。 | 改成「筆數最高的是審查第六節反思的那兩輪（20 筆），其次才是 A3（18 筆）」，並把論述對象改為「這些全是檢查節點」，結論不變。 | no — 但這是計數錯誤的一個新類型：**不只數字會過期，由數字推出的「最多／最少」也會。** 重數之後要把每個比較句再讀一次。 |
| 2026-11-23 | 交件 | **`log.md` 第 215 行的一格內含一個沒被處理的豎線字元（shell 管線 `grep` 前的那一條），整列被切成 7 欄**，繳交文件裡的計數指令把「改變了流程」欄位讀成別的格，**這一列一直沒被算進去：原本公布的「46 筆改變流程」少算 1**。前一輪獨立審查重跑同一個指令得到相同的數字，所以**重跑同一個指令抓不到這個錯**。 | 計數指令只擋「欄數小於 6」，不擋「欄數大於 6」；而我寫 log 時沒有想到表格格內不能放豎線字元。 | 把該格的豎線改成全形 ｜（用反斜線跳脫豎線在 Markdown 渲染上有效，但只認半形豎線切欄的計數指令不認，所以沒用）；計數指令多印一個「欄數不是 6 的列數」，必須為 0 才算數；全部計數重算。 | yes — **驗證指令本身也要有自我檢查。** 一個只印出「結果」的計數指令，在輸入格式壞掉時會安靜地給出錯的數字；要讓它在壞掉時大聲失敗（Rule 8）。 |
