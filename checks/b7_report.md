# B7 — Faithfulness check (cards → deck/script)

**Node**: B7. **Date**: 2026-11-17. **Reviewer**: independent session, no access to
the B6 drafting conversation.

**Artifacts reviewed**: `slides_html/index.html` (30 slides), `notes/script.md`
(30 sections + 7 backup entries), `slides_html/fig/*.svg` (3 figures, read via
`scripts/b6_figures.py`).
**Permitted source**: `notes/cards/C1`–`C10`. **Consulted only to adjudicate what a
card says**: `wiki/`, `checks/a3_report.md`, `checks/a5_report.md`.
The source PDFs were **not** opened.

**Not verified by B7** (state it when relaying this report): nothing against the
paper itself — if a card is wrong, B7 cannot see it; the rendered appearance of
any slide or figure (B10); whether the shipped SVGs match the current
`b6_figures.py`; LaTeX compilation (B8); timing (B11). Prior-report statuses
cited below are **as of the A5 report**, with the three that matter spot-checked
against today's wiki (see the A3/B3 section).

---

## Verdict: **FAIL** — 1 blocker, 17 should-fix, 17 minor

One blocker: slide 4 displays a three-sentence block quotation attributed to
*The Economist* of which **only the final clause is traceable anywhere in the
permitted chain** — not on card C1, not in `wiki/`, not in the A3 or A5 reports.
Everything else is fixable in place.

Per the A5 convention (any blocker = FAIL), B6 should redo **slides 4, 12, 18,
23, 25, 28, 29, 30** and script sections **§4, §10, §12, §16, §20, §21, §22,
§23, §25, §26, §28, §29, §30**. The remaining 22 slides carry no blocker and no
should-fix; they are listed in "Checked and faithful".

Each finding is counted **once**, under its primary check; the finding heading
names every check it touches.

| Check | Result | Blocker | Should-fix | Minor |
|---|---|---|---|---|
| F1 Claim support | FAIL | 0 | 1 | 6 |
| F2 Drift | FAIL | 0 | 2 | 1 |
| F3 Attribution | FAIL | 0 | 3 | 3 |
| F4 Light-source leakage | FAIL | 0 | 2 | 0 |
| F5 Numbers | PASS WITH FIXES | 0 | 2 | 0 |
| F6 Quotations | FAIL | 1 | 2 | 3 |
| F7 "Do not say" list | PASS WITH FIXES | 0 | 1 | 2 |
| F8 Script–slide agreement | FAIL | 0 | 3 | 1 |
| F9 Presenter embarrassment | FAIL | 0 | 1 | 1 |
| **Total** | **FAIL** | **1** | **17** | **17** |

---

# Blocker

## B7-01 — Slide 4: most of *The Economist* quotation is not traceable in the permitted chain (F6/F1)

**Severity**: blocker. **Slide 4**; **script §4**.

**What the card says** — C1.7, in full:

> Industry practice: one consultancy advises big clients to be "number two or
> three on corporate responsibility rather than number one". | The Economist
> (2008), quoted Kopel p. 490

The quoted span on the card is exactly `number two or three on corporate
responsibility rather than number one`. `wiki/papers/Kopel2021-CSR.md` line 28
and `wiki/concepts/first-mover-advantage.md` line 69 carry the same single
fragment and nothing more.

**What the deck says** — slide 4, as a display block quote:

> "First-mover advantage soon passes. After a while, for example, everybody
> turns green, and the winners are the companies with the best execution. One
> large consultancy advises its big clients to be number two or three on
> corporate responsibility rather than number one."
> — The Economist (2008), quoted in Kopel p. 490

Two sentences and a sentence-opening clause are inside quotation marks with a
page citation, and **no part of them appears in any card, any wiki page, or
either prior report**. Greps for `turns green` and `best execution` across
`wiki/`, `notes/cards/`, `checks/a3_report.md` and `checks/a5_report.md` return
nothing. The wording of the traceable clause has also changed: the chain says
*"a consultancy advises big clients"*, the slide says *"One large consultancy
advises its big clients"*.

I am **not** asserting the passage is invented — it may well be in the paper. I
am asserting it is **not traceable in the permitted chain**, which under
AGENTS.md §3 ("Quotation marks mean verbatim … Checked at A3") and B7's own
input rule is the same defect either way: the deck is displaying unverified
verbatim text to an advisor.

**Why it matters.** It is the only full-screen quotation in Act I, it is
attributed to a named publication, and it is the slide the script leans on to
motivate the whole paper ("that's an empirical claim about an equilibrium").

**Fix.** Cut back to the clause the chain carries, in the chain's wording:

> one consultancy advises big clients to be "number two or three on corporate
> responsibility rather than number one"

and do the framing in the deck's own voice. If the longer passage is wanted,
it has to go back through A3 against p. 490 first and be added to C1.

---

# Should-fix

## B7-02 — Slide 25 / script §25: the second-order-condition values are on no card (F1/F5)

**Card**: C3.8 says only that γmax is "the point where the **follower's** CSR and
output hit zero at θ=0 — root of the eq. (6) numerator, 0.8107358771. **Not
stated in the paper.**" It says nothing about where the second-order conditions
fail.

**Deck, slide 25**: "Every second-order condition fails only at larger $\gamma$."
**Script §25**: "It isn't the second-order conditions — those fail at 0.83 and
0.93."

Both are supported upstream (`wiki/numbers.md` lines 77–82: leader's stage-1 SOC
0.830176, follower's stage-2 SOC 0.932526; `wiki/concepts/competition-intensity.md`
lines 24–25), so this is a **card gap, not an invention** — but F1 is a
slide-to-card check, and a presenter saying two specific numbers out loud should
have them on a card. The claim is also load-bearing: it is the step that makes
"γmax is not housekeeping" an argument rather than an assertion.

**And the script's version has lost a qualifier.** `wiki/numbers.md` §"Boundary
conditions, by binding order" lists **four** conditions, not two: follower
interiority 0.8107359 (at θ = 0), leader's stage-1 SOC 0.830176 (**at θ = 0**),
the bracket root 0.865759, follower's stage-2 SOC 0.932526 (any θ). "Those fail
at 0.83 and 0.93" drops the θ = 0 condition on the first number and silently
omits the bracket condition that binds between them.

**Fix.** Add the full binding-order table to C3.8, and in script §25 say "at
θ = 0 the leader's second-order condition doesn't bind until 0.83, and the other
conditions later still".

## B7-03 — Slide 12: "strategic substitutes / complements" is our terminology, shown under a Kopel footer (F3)

**Card**: C3.4 — "strategic substitutes below, complements above", untagged.
**But** A5-09 (should-fix; spot-checked today — no "labels ours" clause has been added to `numbers.md` or `strategic-commitment.md`, so still open) records that three wiki pages tag this wording
`[our reading]`, with the note "The labels 'substitutes / complements' are
standard terminology and are ours; **the paper states only the threshold**."

**Deck, slide 12**: two cards headed "Strategic **substitutes**" / "Strategic
**complements**", footer "Kopel p. 496", no own-marking anywhere on the slide.
**Script §12**: "Below that threshold, CSR levels are strategic **substitutes**."

So the deck presents our vocabulary as the paper's. The only part of slide 12
that is Kopel's is the inequality and the "counterbalance this effect" quote.

**Fix.** One clause on the slide — "labels ours; the paper states only the
threshold" — and the card gets the same tag. (Card-level cause logged in §A3/B3
below; A5-09 is open as of the A5 report and still open on today's wiki.)

## B7-04 — Slide 29 / script §29: our frontier number sits under a Kopel-only footer, and the script drops its qualifier (F3/F2)

**Card**: C10.3 — "The FMA needs $\theta<0.0015$ **at $\gamma=0.3$**". The 0.0015
is `[own calculation]` (C5.4, C6.2); the "quite hard to measure accurately"
concession is Kopel's (p. 491).

**Deck, slide 29**: "The FMA needs $\theta < 0.0015$ at $\gamma = 0.3$, and the
paper concedes the answer 'depends on factors which are quite hard to measure
accurately.'" Footer: **"Kopel pp. 491, 502"**. No `own calculation` tag on the
slide. A slide whose only attribution line names Kopel, carrying our number, is
exactly the F3 case.

**Script §29** is worse, because it also loses the conditioning: "The
first-mover advantage needs theta below **0.0015**, and Kopel concedes…" — the
γ=0.3 qualifier is gone and our number is spoken immediately before "Kopel
concedes", so the room hears one attribution for both.

**Fix.** Add the `own calculation` tag to the 0.0015 on slide 29 and restore
"at γ = 0.3" in the script; change the footer to "own calculation · Kopel
pp. 491, 502".

## B7-05 — Slide 23 / script §23: the transfer-of-incentive framing loses its tag, and gains a phrasing C5.5 forbids (F3/F7)

**Cards**: C6.5 is ours (A5-01). C5.1 is Kopel's (p. 499 §5.2). C5.5: "Phrase it
as a **bound on the spillover rate**, not as 'the leader retains 99.85%' — θ adds
to the rival, **it does not subtract from the leader**."

Slide 17 handles this correctly: the transfer framing carries `our reading`.

**Deck, slide 23**, in the red key box, untagged: "Because $\theta$ transfers
incentive continuously from $\theta=0$: the follower **captures part of the
leader's demand shift** without paying for it." Footer: "own calculation ·
mechanism from Kopel p. 499 §5.2" — which reads as if the mechanism sentence is
Kopel's, when slide 17 marked the same idea as ours.

**Script §23**: "The follower is capturing part of the leader's demand shift
without paying for it."

"Captures part of the leader's demand shift" implies the leader's shift is
reduced. It is not: slide 10's own note says θ "adds to the *follower's* demand.
It does not subtract from the leader's", script §10 spells out that "the
leader's demand shift is *s-one* whatever theta is", and script §20 repeats it
as the reason "retains 99.85%" is wrong. The deck thus disclaims the subtraction reading on two slides and
re-imports it on a third — on the climax slide.

**Fix.** "the follower receives $\theta s_1$ of demand shift it did not pay for,
while the leader's own shift is unchanged", and tag the sentence `our reading`
as slide 17 does.

## B7-06 — Slide 18: Lemma 2 is labelled "verbatim" but two sentences are missing, and the missing ones matter (F6/F9)

**Card**: C5.2 gives only the gist ("verbatim available"), so the card cannot
adjudicate. `wiki/papers/Kopel2021-CSR.md` line 307 carries the full lemma, which
has **four** sentences. The deck prints the first two and closes the quote.

Omitted:

> Moreover, the CSR leader selects a higher activity level of CSR than the CSR
> follower if the outcomes of the CSR efforts are highly specific to the firm,
> i.e., if CSR spillovers are quite small (independent of the degree of
> competition). Otherwise, the CSR follower has a higher level of CSR activity,
> $s_1^* < s_2^*$.

Two problems. (a) AGENTS.md §3: "Elisions take an ellipsis" — the footer says
"Kopel p. 500, verbatim" and it is not. (b) **Presenter risk**: the omitted
clause is Kopel separating the *profit* comparison from the *CSR-level*
comparison himself. Slide 22's script opens "It's natural to assume these are
roughly the same event. They are not" — an advisor who knows Lemma 2 will point
out that Kopel already distinguishes them, and the deck has just shown a
truncated Lemma 2 that hides it. Our contribution survives (Kopel says "quite
small" for *both* comparisons; the magnitudes — 0.0015 vs 0.0169 vs 0.157 — are
ours), but it must be framed as *quantifying a distinction Kopel states
qualitatively*, not as noticing one he missed.

**Fix.** Print the full lemma, or mark the elision with "…". Add one script line
at §22: "Kopel separates these two comparisons in Lemma 2; what he does not do is
put numbers on how far apart they are."

## B7-07 — Slide 25: the γmax justification is misquoted and half of it is dropped (F6)

**Chain** (`wiki/papers/Kopel2021-CSR.md` line 120): γmax "guarantees that the
equilibrium of the game **is** in the interior **and all second-order conditions
are satisfied**" (p. 495).

**Deck, slide 25**: "which the paper justifies **only** as keeping 'the
equilibrium of the game in the interior.'"

Two defects: the word `is` is dropped from inside the quotation marks, and the
"only" is false — the paper's sentence also claims the second-order conditions.
The script gets it right ("it keeps 'the equilibrium of the game in the
interior' and satisfies the second-order conditions"), so the slide also
contradicts its own script.

**Fix.** Quote the whole clause and drop "only"; the point ("he doesn't say which
condition binds") is unaffected and is separately supported by the chain.

## B7-08 — Script §20: "γ = 0.8, the most competitive case the model allows" (F2/F8)

**Cards**: C3.7/C9.4 — the model requires $\gamma < \gamma_{\max} = 0.810736$.
C5.4's table simply stops at 0.8.

**Script §20**: "At gamma of 0.8, **the most competitive case the model allows**,
it's still under ten percent."

0.8 is the last row of our table, not the model's limit. Five slides later the
deck tells the room γmax = 0.810736 and makes an argument out of what happens
there. Self-contradicting, in front of the one audience that will notice.

**Fix.** "At gamma of 0.8, the top of my table and close to the model's limit of
0.81…"

## B7-09 — Script §25: "the axis is labelled 0.66, which is exactly the leader's CSR level at γmax" (F2/F5)

**Card**: C3.9 — "axis top 0.66 **matches** computed $s_1^*(\gamma_{\max}) =
0.6562$."

**Script §25**: "The axis is even labelled 0.66 at the top, which is **exactly**
the leader's CSR level at gamma-max on my recomputation."

0.66 ≠ 0.6562. The card's claim is that a printed axis top is *consistent with*
our computed value — corroboration, not coincidence. "Exactly" invites the
obvious question and loses the argument on a point we did not need to make.

**Fix.** "The axis tops out at 0.66, just above my computed 0.6562 at gamma-max —
consistent with the leader's curve reaching the top-right corner."

## B7-10 — Script §23: "stated in the text twenty pages earlier" (F5)

The substitutes threshold is p. 496 (C3.4); the profit frontier derives from the
Lemma 2 region, p. 500 (C5.2). Four pages, in a paper that runs 489–505 and so
cannot contain a twenty-page gap. **Fix**: "a few pages earlier".

## B7-11 — Script §16 says the follower's curve hits zero *inside* the range; slide 25 says *at the edge* (F8)

**Card**: C3.8/C3.9 — follower's CSR and output reach zero **at** γmax, the
boundary of the analysed range; the dashed curve "hits zero exactly at the
right-hand edge".

**Script §16**: "It goes to zero, and it does that *inside* the range the paper
analyses."
**Deck, slide 25** and **script §25**: "hits zero exactly at the right-hand
edge."

The script states the stronger, wrong version first and the correct version nine
slides later. **Fix**: §16 → "It goes to zero right at the edge of the range the
paper analyses — hold that, we come back to it."

## B7-12 — The backup slides the script promises do not exist in the deck (F8/F1)

**Script §10**: "I've put the full equilibrium expressions on a backup slide if
anyone wants to see them." **Script, closing section**: seven backup slides
B1–B7 are specified.

`slides_html/index.html` contains exactly 30 `<section class="slide">` elements,
numbered 1/30 to 30/30. There are no backup slides, and `slides_html/fig/` holds
only the three main figures. The outline (B4) lists B1–B7 as deliverables.

If the advisor asks for equations (5)–(7) — likely, after slide 14 says we
re-derived them — there is nothing to show.

**Fix.** Either build B1–B7 or remove the promise from script §10 and relabel the
list as "answers to have ready", not slides.

## B7-13 — Script §26: the Hirose & Matsumura mechanism is off-card, and reverses what the card says (F4/F2)

**Card** C8.5, a light-depth source: "Hirose & Matsumura treat ECSR explicitly as
'a commitment device to soften competition' — **same engine as Kopel's, applied
mutually rather than sequentially**."

**Script §26**: "Their firms commit to an emissions cap, which raises marginal
cost, which raises *both* firms' prices through the strategic interaction.
There's no appropriability problem in that story at all… Same word, **completely
different machine**."

The marginal-cost-to-prices mechanism is on no card. And "completely different
machine" is the opposite of the card's "same engine": the card's distinction is
*mutual vs sequential*, not *different mechanism*. This is delivered in the
confident register, about a source C8 explicitly marks as unverified.

**Fix.** "They treat an emissions cap as a commitment device to soften
competition — the same engine as Kopel's, applied mutually rather than
sequentially, so the appropriability problem does not arise in the same way. I
have not verified that paper."

## B7-14 — Slide 30 / script §30 repeat a light-source claim without the C8 caveat (F4)

**Card** C8 header: "⚠️ All facts below come from **light-depth** sources: read
and summarised, no symbolic verification, no independent review."

Slide 26 carries this properly (`lower assurance` warn tag) — good. But slide 30,
the **closing** slide, restates C8.1 ("Three independent models — Kopel, Chen
et al., Bárcena-Ruiz & Sagasta — each contain a corner where one firm's output
goes to zero") with no caveat, no light-source tag, footer blank ("Thank you —
questions"). Script §30 likewise. Four slides separate the warning from its
last use, and the last use is the one the discussion starts from.

**Fix.** One `lower assurance` tag on slide 30, or a half-sentence in §30: "on my
unverified reading of the other two".

## B7-15 — Slide 28 / script §28: Kopel's conditional "if" is dropped from "copies and improves" (F2)

**Card** C10.1: 'A follower who "copies **and improves**" (p. 494) **would**
create a reverse spillover the model excludes.' The chain
(`wiki/open-questions.md` line 22) is explicit that p. 494 reads *"**if** the CSR
follower copies and improves the green…"* — a conditional clause in Kopel's
setup, not an assertion about followers.

**Deck, slide 28**: "Kopel's own text **says** the follower 'copies and improves'
the leader's green attributes (p. 494) — which would create a reverse spillover."
**Script §28**: "Kopel's own text **undercuts** it: on page 494 **he says** the
follower 'copies and improves'…"

A conditional has become a statement, and the script escalates it to Kopel
contradicting himself. The card's hedged version makes the same discussion point
without the overreach.

**Fix.** "Kopel's own setup contemplates a follower who copies *and improves* the
leader's green attributes (p. 494) — a case that would create a reverse spillover
the model excludes by construction."

## B7-16 — Script §21 states Lemma 3's monotonicity without the C7.6 caveat (F7)

**Card** C7.6: "fn. 15's criterion is the derivative **at the endpoint** γmax, so
it cannot see an interior hump. The follower's curve is already down–up–down from
about θ = 0.190. **'Monotone throughout' is too strong.**"

**Script §21**: "Below the first, the follower's CSR **declines in competition**
while the leader's is U-shaped." No caveat. The caveat exists only as backup B4
("only if asked") — and per B7-12 the backup slides do not exist.

Restating Kopel's lemma is legitimate; what C7.6 forbids is leaving the room with
"monotone" unqualified when we have found otherwise. The deck's slide 21 body is
clean (it describes the two thresholds, not monotonicity), so this is a script
fix only.

**Fix.** Add: "— though that is the paper's endpoint criterion; on my own plots
the follower's curve is already non-monotone from about theta 0.19."

## B7-17 — Slide 30's closing line says the leader "keeps out-investing", unscoped, nine slides after we showed it does not (F9)

**Card** C6.5 carries the same unscoped phrasing (see §A3/B3 below), and it is
correct *at the FMA frontier* — C6.4's "when the FMA dies … the leader still
invests more" is conditioned on θ at the profit frontier.

**Deck, slide 30** (final key box) and **script §30** (last line before thanks):
"The leader keeps deterring. It keeps out-investing. And it still loses."

Slide 21 has already shown the follower investing more at θ = 0.21, and slide 22
gives the crossover at θ = 0.0169 for γ = 0.3. Unscoped, the takeaway line is
false over most of the θ range, and it is the sentence the room will repeat back.

**Fix.** "In the region where the advantage dies, the leader is still deterring
and still out-investing — and still loses." Slide 23's version is correctly
scoped ("At the moment the first-mover advantage disappears"); slide 30 should
match it.

## B7-18 — Slide 25 / script §25 tell the room to look at a figure the deck does not show (F8/F3)

**Card** C3.9 is about **Kopel's printed Fig. 1**: "the dashed curve hits zero
exactly at the right-hand edge, axis top 0.66 matches computed
$s_1^*(\gamma_{\max}) = 0.6562$." That is a statement about the paper's figure,
offered as independent corroboration of C3.8.

**Deck, slide 25**: "Look back at **slide 16**: the dashed curve hits zero
exactly at the right-hand edge. The paper's own Figure 1 has been showing this
all along."
**Script §25**: "go back to the first figure. The dashed line hits zero exactly
at the right-hand edge. Kopel's own Figure 1 has been showing this the whole
time. **The axis is even labelled 0.66 at the top**…"

Slide 16 is **our replot**, tagged `own calculation`, and by outline decision 5
the deck never reproduces Kopel's Fig. 1. Per `scripts/b6_figures.py`, our
figure sets `ax.set_ylim(0, 0.70)` and `ax.set_xlim(0, float(GMAX) * 1.02)`, so
on screen there is **no 0.66 axis label** and the dashed curve reaches zero
slightly short of the right-hand edge, beside an annotation reading "follower's
CSR and output reach zero here".

So the presenter points at a replot while describing features of a figure that
is not in the room, and credits the corroboration to "the paper's own Figure 1"
in the same breath. Either the room sees nothing matching the words, or it
concludes slide 16 is Kopel's figure — the F3 failure the `own calculation` tag
exists to prevent.

**Fix.** Separate the two: "Our replot (slide 16) shows the follower's curve
reaching zero at gamma-max. Kopel's own Figure 1, which I haven't reproduced
here, independently agrees — its dashed curve ends at the right-hand edge and
its axis tops out at 0.66, just above my computed 0.6562." Combine with B7-09,
which fixes "exactly" in the same sentence.

---

# Minor

The **F** column gives each minor's primary check, matching the summary table.

| # | F | Where | What | Fix |
|---|---|---|---|---|
| m1 | F6 | Slide 5 | p. 502 quote closes at "sustain a first-mover advantage." The chain reads "…advantage **based on investments in CSR**." Unmarked elision in a quotation. | Add the clause or an ellipsis. |
| m2 | F6 | Script §8 | Burke & Logsdon quote truncated at "shared by others." (chain: "…by others in the industry, community or society at large"), no ellipsis. The deck gets it right. | Read the full clause or mark the elision. |
| m3 | F6 | Slide 9 | The θ₁ ≤ θ₂ quotation is on no card. It matches `wiki/concepts/csr-spillovers.md` and A3 F3, **but A5-11 records a conflict** (two pages still quote "sensible" — confirmed present today in `open-questions.md` and `Kopel2021-CSR.md`) marked "not resolvable without the PDF". | Add to C2 with the A5-11 status noted; close A5-11 upstream before presenting. |
| m4 | F1 | Slide 8 | "defended a premium segment" is not on C2.10 (in chain: fn. 7, "defending its advantage in a premium-segment of the market"). | Add to C2.10. |
| m5 | F1 | Slide 29 | "Kopel lists endogenous timing as an extension" is on no card (C10.2 says only that the model cannot represent it). In chain at `Kopel2021-CSR.md` line 339. | Add to C10.2. |
| m6 | F1 | Script §3 | "Vogel in *The Market for Virtue*" — title is in `wiki/sources.md` line 52, not on C1.6. | Add to C1.6. |
| m7 | F1 | Script §10 | "a seventh-degree polynomial", "which is unusual and is one reason this specification was chosen" — neither is on a card; the second is a claim about the author's motivation. | Cut the motivation claim; keep the derivation walk-through. |
| m8 | F3 | Script §12 | "At gamma of 0.1 it's about 0.05; at gamma of 0.8 it's about 0.59" — arithmetic on C3.4's formula is right (0.0503, 0.5882) but these are our numbers, spoken untagged. | "On my arithmetic…" |
| m9 | F3 | Slide 25 | "γmax marks where the duopoly would collapse into a monopoly" is our inference, outside the `we checked` box and untagged. | Move inside the box or tag it. |
| m10 | F8 | Slides 5 / 19 | "What it adds is a magnitude" (slide 5, script §5) vs "He never puts a number on it" (slide 19). A listener may hear the slide-20 frontier as Kopel's. | "What he adds is that the condition is *restrictive* — and I'll put a number on how restrictive." |
| m11 | F3 | Slide 21 | The figcaption's `own calculation` tag spans a caption whose thresholds (0.202167, 0.229499) are **Kopel's** (C7.1), reproduced by us (C7.3). Tag over-reaches in the harmless direction, but AGENTS.md §3 scope rule says a tag governs the sentence it opens. | Tag the figure, not the band. |
| m12 | F1 | Slide 12 | "the follower retreats and free-rides" at low θ — inherited A5-02 (should-fix; `log.md` line 127 records a terminology box added to `strategic-commitment.md`, so partly addressed — the wording on this slide still follows the old usage): free-riding is capturing θs₁ at any θ > 0, not a low-θ behaviour. | Follow A5-02's fix: low θ "retreats", high θ "counterbalances". |
| m13 | F7 | Script §20 | The script voices "the leader must retain 99.85 percent" in order to refute it. C5.5 forbids the phrasing; the script obeys in substance but plants the number. | Judgement call. Safer: "It's tempting to turn this into a retention percentage. That's wrong, because…" — no number. |
| m14 | F7 | Script, backup block | The δ** ≈ 0.531 / γ ≈ 0.532 coincidence appears **only** inside the "Do not raise" instruction, which is correct per C10 — but the number is written into a file that may be handed out. | Keep, or replace the numbers with "the Hirose & Matsumura / Kopel numerical coincidence". |
| m15 | F1 | Slide 1 | "44: 489–505", "Open access, CC BY 4.0" are on no card (in `wiki/sources.md` line 8). Bibliographic, low risk. | Add a bibliographic line to C1. |
| m16 | F2 | Slide 12 | "The leader's own incentive **collapses**" vs C3.5's "the leader's incentive **falls so much that**…". Mild intensification. | "falls far enough that". |
| m17 | F9 | Deck, throughout | C4.8 ("at γ = 0 the two curves coincide at 1/3 — 'the leader always invests more' holds only for γ > 0") appears nowhere. Slide 13 quotes Lemma 1 verbatim so is not wrong, but slide 16's figure starts at γ = 0. | One clause in script §16, or leave as a prepared answer. |

---

# Checked and faithful

Traced in full and found sound — no finding against any of these:

**Numbers (F5).** Every figure in the deck and script was checked against the
card that carries it, and the derived ratios recomputed:

| Figure | Deck / script | Card | Result |
|---|---|---|---|
| FMA frontier, all five rows | 0.0000534 / 0.00150 / 0.00867 / 0.0393 / 0.0960 | C5.4 | exact match |
| "0.15%" headline, slide 20 | 0.15 % at γ = 0.3, qualifier shown | C5.4, C6.2 | exact; qualifier present on the slide |
| Three thresholds, slide 22 | 0.0015 / 0.0169 / 0.157 | C6.2 | exact match |
| 105× | slide 22, script §22, figure annotation | C6.3 | 0.157/0.0015 = 104.7 ✓ |
| 940× and 6× | slide 24, script §24 | C6.3 | 0.0503/0.0000534 = 941; 0.5882/0.0960 = 6.1 ✓ |
| γmax | 0.810736 (slide 25), 0.8107358771 (box) | C3.7, C3.8 | exact |
| U-shape turning point | 0.531963 / 0.5319633 | C4.4 (0.5319633163) | correct truncation |
| Lemma 3 thresholds | 0.202167, 0.229499; "0.202 and 0.229" | C7.1, C7.3 | exact |
| Fig. 3 / θ = 0.21 band | 0.21 inside 0.202167–0.229499 | C7.4 | exact |
| Backup B5 | 0.504 → 0.208 at γ = 0.8 | C7.7 (0.5039, 0.2082) | correct rounding |
| 39 grid points | slide 14, script §14 | C4.3 | exact |
| "five in a hundred thousand" | script §20 | C5.4 (0.0000534) | fair rendering |
| γ/(2−γ²) at 0.3 | 0.157 | C6.2 | 0.15707 ✓ |

**Figures.** The three SVGs are matplotlib path-rendered, so their on-screen text
is not machine-readable; what I checked is the **generator source**,
`scripts/b6_figures.py`, not pixels. In the source: curves are computed from the
verified equilibrium expressions (not copied from the PDF); the plotted
thresholds are computed live by root-finding on the same expressions rather than
hard-coded, so they agree with C5.4/C6.2/C3.4 by construction; the θ = 0.21 title
matches C7.4; the literal annotation strings `0.0015`, `0.0169`, `0.157` and
"≈ 105× apart" match C6.2/C6.3. **Not verified**: that the rendered SVGs were
produced by this version of the script, and how any of it looks on screen (B10's
job). B7-18 is the one place where the source shows the slide cannot support what
the script says about it.
Script §22's walk-through of the three curves (dash-dotted top = deterrence,
dashed middle = out-investing, solid red bottom = FMA, shaded region beneath)
matches the plotting code line for line. All three carry an `own calculation`
tag in the figcaption.

**Quotations that check out** against the chain, character for character: Lemma 1
(slide 13, full and verbatim); the "simple comparison is therefore omitted" *sic*
(slide 14); Burke & Logsdon on specificity (slide 8, deck version); the StarKist
"imitated this policy almost immediately" (slide 8); "to counterbalance this
effect" (slide 12); "can not only be sustained, but made even larger" (slide 16);
"in fact very low" (slide 19); "quite hard to measure accurately" (slide 29);
"in my paper the leader–follower structure is exogenously given" (slide 11);
Tetrault Sirsly & Lamertz's three conditions (slide 3); the θ₁ ≤ θ₂ sentence
(slide 9, subject to m3).

**F7, the "do not say" list.**
- δ** / γ coincidence: **obeyed**. Absent from all 30 slides and from the spoken
  script; appears only in the script's own "Do not raise" instruction (m14).
- "Leader retains 99.85%": **obeyed in substance**. Slide 20's box states the
  bound-on-the-rate framing verbatim from C5.5, and script §20 names the wrong
  phrasing only to reject it, with C5.5's reason (m13). Partially undercut by
  B7-05, which re-imports the subtraction reading on slide 23.
- "Monotone throughout": obeyed on the slides; script §21 needs B7-16.

**F1/F3 passes worth naming.** The 22 slides carrying **no blocker and no
should-fix** — 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21,
22, 24, 26, 27 — trace to their outline cards; six of them carry a minor
(m1/m3/m4/m8/m10/m11/m15/m16/m17), listed above. Attribution
handled correctly and visibly on slide 8 (`our reading`), slide 14 (`what we
did`), slide 16 (`own calculation`), slide 17 (`our reading`), slide 20 (`own
calculation`, twice), slides 21/22 (`own calculation`), slide 25 (`we checked`),
slide 26 (`lower assurance`), slide 27 (`one thing we can strengthen`). Script
§15's self-correction — "the paper gives only the sign of the product; splitting
it into the two factors is my reading, not his" — is a model of what F3 wants,
as is §14's "strong evidence. **It is not a proof.**"

**C1.8 honoured.** Slide 5 and script §5 state explicitly that the conclusion
groups Tetrault Sirsly & Lamertz *with* Reinhardt and Burke & Logsdon, and that
the paper formalises rather than refutes them. Slide 3's two-camps framing is
corrected two slides later, in the deck's own voice. No slide presents TS&L as
the losing side.

**C9 honesty slides present and faithful.** Slide 14 (unproved lemmas), slide 24
(C6.7's "rules out the wrong mechanism, does not prove the right one" — stated
almost verbatim), slide 27 (C9.5, C9.6, C9.7 all three, including the WLOG
argument with its homogeneity degrees correct).

**F4, light sources.** No number from C8 reaches any slide — in particular
Bárcena-Ruiz's β ≥ (3−√5)/2 ≈ 0.3819, Chen's Lemma 1 and Xing & Lee's page
reference are all absent. Slide 26 carries the warning prominently. The two
defects are B7-13 (mechanism detail beyond the card) and B7-14 (slide 30 without
the caveat).

---

# Not B7's business — defects in the cards themselves (for A3 / B3)

Reported separately, as instructed, and **not** counted in the verdict. Each is a
case where the deck is faithful to its card but the card is thinner or looser
than the wiki it draws on.

1. **C5.2 omits two of Lemma 2's four sentences** — including the clause where
   Kopel himself separates the profit and CSR-level comparisons. This is the
   direct cause of B7-06 and it affects how slide 22's contribution should be
   claimed. Highest priority of the six.
2. **C3.8 omits the second-order-condition values** (0.830176, 0.932526) that the
   deck and script both use. Cause of B7-02.
3. **C6.5 states "the leader keeps deterring, keeps out-investing" unscoped**;
   C6.4 has the scope ("when the FMA dies"). The deck inherited the unscoped
   version onto its closing slide. Cause of B7-17.
4. **C10.3 prints 0.0015 without an `[own calculation]` tag**, although C5.4 and
   C6.2 both tag it. Contributing cause of B7-04.
5. **C3.4 carries "strategic substitutes / complements" with no `[our reading]`
   mark**, while three wiki pages carry one — A5-09, confirmed still open on today's wiki. Cause of B7-03.
6. **C1.7, C2.9, C2.10, C4.3 each quote a shorter span than the wiki page they
   draw on**, so B7 could not adjudicate slides 4, 8 and 14 from the cards alone
   and had to fall back on `wiki/`. For C1.7 this is how the blocker went
   unnoticed at B3: the card was not wrong, it was simply silent about a passage
   the deck then printed.
