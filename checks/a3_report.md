# A3 independent review — Kopel (2021) wiki

- **Date**: 2026-11-16
- **Reviewer**: A3, fresh context. Did not write any of the reviewed material.
- **Inputs used**: `raw/papers/Kopel2021-CSR.pdf` (text layer via `pdftotext -layout`, plus journal pages 495–497 rendered at 125 dpi and page 500 at 110 dpi with `pdftoppm` and read as images), `checks/a4_report.md`, and my own sympy/mpmath re-derivation (`/usr/bin/python3`, sympy 1.14.0, mpmath 30 dp).
- **Scope**: the 12 pages listed in the review brief. No wiki file was modified.

## Verdict: **FAIL** — 5 blockers, 14 should-fix, 9 minor (+1 advisory)

"FAIL" here has a specific meaning, not a global judgement: the wiki is in good shape
and the great majority of it survived aggressive checking (see §"Checked and correct").
But five defects would propagate into the deck as false statements about what the author
says or as a wrong equation, and three of them are the kind an advisor catches in the
room. **Graph B must not start until the blockers are fixed and re-reviewed.** The fixes
are localised — roughly fifteen lines across six files.

| Item | Result | Problems found |
|---|---|---|
| C1 Citation accuracy | FAIL | 6 (4 should-fix, 2 minor) |
| C2 Verbatim quotations | FAIL | 4 (1 blocker, 1 should-fix, 2 minor) |
| C3 Author's claims vs ours | FAIL | 5 (2 blockers, 2 should-fix, 1 minor) |
| C4 No outside knowledge | FAIL | 5 (3 should-fix, 2 minor) |
| C5 θ threshold logic | PASS with 1 caveat | 1 should-fix (overclaim, not a reversal) |
| C6 Equation register | FAIL | 1 blocker |
| C7 Number register | PASS with 3 problems | 3 (2 should-fix, 1 minor) |
| C8 Internal consistency | PASS with 1 minor | 1 minor |
| C9 Overclaiming | FAIL | 2 (1 blocker, 1 should-fix) |
| C10 Anything else | — | 1 advisory |

Each finding is counted once, under its primary category; several touch more than one and
say so in their heading. Total: 28 defects (5 / 14 / 9) plus one advisory note, F28.

---

# Blockers

## F1 — The paper is said to argue *against* Tetrault Sirsly & Lamertz. It argues *with* them.

**Severity**: blocker. **Categories**: C3, C4, C10.
**Files**: `wiki/papers/Kopel2021-CSR.md` §8; `wiki/concepts/first-mover-advantage.md`
"The prior debate this settles"; `wiki/sources.md` candidates table.

The wiki §8 says:

> This supports the skeptical readings of Vogel (2005), Reinhardt (1998) and Burke &
> Logsdon (1996) **over** Tetrault Sirsly & Lamertz (2008).

`sources.md` repeats it: Tetrault Sirsly & Lamertz is listed as "the paper Kopel is
directly arguing against on FMA sustainability". `first-mover-advantage.md` builds a
three-row "prior debate" table with TS&L as the losing side, then adds the unmarked
inference "the optimists are right about the *mechanism* … but wrong about how often the
condition is met."

**Evidence (p. 502, §6, first paragraph):**

> "My study provides support for the claims in conceptual papers like Tetrault Sirsly and
> Lamertz (2008), Burke and Logsdon (1996), and Reinhardt (1998) who argue that it seems
> rather difficult to sustain a first-mover advantage based on investments in CSR."

And p. 491:

> "If CSR activities are specific to the CSR leader … then **in line with Tetrault Sirsly
> and Lamertz (2008)** I find that a first-mover advantage exists."

Kopel puts TS&L on the *same* side as Burke & Logsdon and Reinhardt in his conclusion.
(On p. 490 he does set TS&L "in contrast to" Reinhardt and Vogel in the framing of the
debate — the wiki §1 handles that correctly. The error is in the conclusion.)

**Fix**: §8 should read that the study supports the claims in Tetrault Sirsly & Lamertz
(2008), Burke & Logsdon (1996) and Reinhardt (1998) (p. 502), and separately gives
substance to Vogel's critical assessment (p. 502). Delete "over Tetrault Sirsly &
Lamertz". Rewrite the `sources.md` row ("the conceptual paper whose condition Kopel
formalises"). On `first-mover-advantage.md`, either drop the two-sides table or mark the
"optimists wrong about how often" sentence as our reading, and reconcile it with p. 502.

## F2 — `equations.md` K-sub has the wrong sign; the stated implication does not follow

**Severity**: blocker. **Category**: C6.
**Files**: `wiki/equations.md` K-sub; `wiki/concepts/csr-spillovers.md`
"The strategic-substitutes / complements switch". (`checks/a4_report.md` §1 has it too.)

Both write:

$$\frac{ds_2}{ds_1} \propto -(\gamma^2-2)(\gamma^2\theta+\gamma-2\theta)
\;\Longrightarrow\; \frac{ds_2}{ds_1}<0 \iff \theta<\frac{\gamma}{2-\gamma^2}$$

The proportionality is off by a factor of −1, so the "⟹" is false as written. From eq. (4)
(p. 496, confirmed on the rendered page):

$$\frac{ds_2}{ds_1}=\frac{(2-\gamma^2)\big((2-\gamma^2)\theta-\gamma\big)}{12-20\gamma^2+8\gamma^4-\gamma^6}$$

sympy gives `simplify(ds2/ds1 * den) = (g**2-2)*(g**2*th+g-2*th)` — i.e. **+**, not −.
Numerically at γ = 0.5, θ = 0: true slope = **−0.1169**, the wiki expression = **+0.875**.
The denominator is positive throughout the admissible range (7.48 at γ = 0.5, 0.52 at
γ = 0.9), so the sign of the wiki's expression is the sign of −ds₂/ds₁ everywhere.

This matters because `equations.md` is the register B8 validates slides against. A slide
reproducing K-sub would assert that the leader's CSR *raises* the follower's CSR when
spillovers are zero — the opposite of the paper's p. 496 text and of the whole free-riding
story.

**Fix**: write $\frac{ds_2}{ds_1}\propto(\gamma^2-2)(\gamma^2\theta+\gamma-2\theta)$, or more
transparently $\frac{ds_2}{ds_1}\propto(2-\gamma^2)\big((2-\gamma^2)\theta-\gamma\big)$ with a
note that $12-20\gamma^2+8\gamma^4-\gamma^6>0$ for $\gamma<\gamma_{\max}$. The threshold
conclusion itself is correct and needs no change. A4 §1 should be corrected in the same pass.

## F3 — The definition of $\theta_i$ is inverted relative to the paper's own demand system

**Severity**: blocker. **Categories**: C3, C8.
**Files**: `wiki/papers/Kopel2021-CSR.md` §4.1 third bullet; `wiki/concepts/csr-spillovers.md`
"Definition"; `wiki/glossary.md` row $\theta_i$.

All three define $\theta_i$ as "the share of firm *i*'s CSR benefit that accrues to the
rival". In the paper's general system (p. 493) $\theta_1$ multiplies $s_2$ inside $p_1$:

> $p_1 = a + (s_1 + \theta_1 s_2) - x_1 - \gamma x_2$
> $p_2 = a + (s_2 + \theta_2 s_1) - x_2 - \gamma x_1$

So $\theta_i$ is the share of the **rival's** CSR that firm *i* captures — the spillover
*into* firm *i*, not out of it.

One sentence in the paper can be read the wiki's way and will probably be cited back
(p. 494): "The parameters $\theta_1$ and $\theta_2$ **capture the firms' abilities to
protect their CSR investments** against appropriation or imitation by competitors." That
prose is loose — read strictly it would make $\theta_i$ firm *i*'s leakage — but the
equation governs, and the equation puts $\theta_1$ on $s_2$ inside $p_1$. The paper's next
sentence settles it in the same direction as the equation: $\theta_1 \le \theta_2$ is
plausible "because the CSR follower can free ride on the CSR efforts of the leader",
i.e. firm 2 *receives* more than firm 1 does.

The wiki's own §4.2 then reads it the correct way
("$\theta_1 = 0$ … means the leader gets *nothing* from the follower's later CSR"), which
is flatly inconsistent with its §4.1 definition. The paper's justification only makes
sense on the correct reading: p. 494, "it seems plausible to assume that $\theta_1 \le
\theta_2$, because the CSR follower can free ride on the CSR efforts of the leader" —
i.e. firm 2 *receives* more than firm 1 does.

Nothing downstream is wrong, because only $\theta_2=\theta$ survives; but a slide showing
the general system with the wiki's definition would be wrong on its face.

**Fix**: "$\theta_i \in [0,1]$ — the share of the *rival's* CSR benefit captured by firm
$i$ (p. 494)." Keep the one-firm shorthand "$\theta$ = the share of the leader's CSR that
spills to the follower", which is right.

## F4 — A quotation attributed to p. 491 is not in the paper

**Severity**: blocker. **Category**: C2.
**Files**: `wiki/papers/Kopel2021-CSR.md` §7.2 🔎 box; also `checks/a4_report.md` §3.

The box reads: `"Spillovers must be very low" (p. 491) understates this by orders of
magnitude at low $\gamma$.` No such sentence exists anywhere in the paper. What p. 491 says is:

> "What is surprising, however, is that the level of CSR spillovers for which a
> first-mover advantage can be sustained is in fact very low."

This is the sentence most likely to end up on the headline slide, in quotation marks,
with a page number. **Fix**: quote the real sentence, or drop the quotation marks and
paraphrase ("the paper's qualitative 'very low' understates …").

Related, same category, should-fix severity: §2 of the same page quotes
*"what is surprising … is that the level of CSR spillovers for which a first-mover
advantage can be sustained is very low."* — the words **"in fact"** are deleted from
inside the quotation without an ellipsis, and the capital "W" is silently lowercased.

## F5 — "Lemmas 1 and 2 … are analytic" states as proved what the paper does not prove

**Severity**: blocker. **Categories**: C9, C8.
**File**: `wiki/papers/Kopel2021-CSR.md` §9 item 4.

> "The qualitative claims are illustrated, not proved, for general parameters — **except
> Lemmas 1 and 2, which are analytic.**"

The paper proves neither. p. 499: "The proof of the lemma follows from a simple
comparison is therefore omitted." p. 500: "The proof follows again immediately from the
arguments above and a simple comparison of profits and CSR investments." Both are
assertions with the proof omitted. §10 of the very same page says the opposite of item 4
("Lemmas 1 and 2 are confirmed numerically, not proved symbolically; the paper omits both
proofs"), as does `first-mover-advantage.md` and A4 §5.2. One of the two statements will
end up on a slide.

**Fix**: delete "— except Lemmas 1 and 2, which are analytic", and see F6, which removes
the rest of that item's premise.

# Should-fix

## F6 — The $a-c=1$ caveat is not a real limitation; the model is homogeneous in $a-c$

**Severity**: should-fix (an over-cautious caveat does not put a false claim on a slide,
but it invites exactly the question it is trying to pre-empt). **Categories**: C9, C10.
**Files**: `wiki/papers/Kopel2021-CSR.md` §9 item 4 and §10 "Remaining gaps" 3;
`checks/a4_report.md` §5.3.

The wiki flags as an open risk that "all runs used $a-c=1$" and that general-parameter
claims are "illustrated, not proved". But eq. (5) and (6) (p. 496) carry $(a-c)$ as a bare
multiplicative factor, and $c$ appears nowhere else in $s_1^*, s_2^*$; $\pi_1^*\propto(a-c)s_1^*$
and $\pi_2^*\propto (s_2^*)^2$ (p. 497). Hence $s_i^*$ is homogeneous of degree 1 and
$\pi_i^*$ of degree 2 in $(a-c)$, with $c$ entering prices only as a level shift. Every
ordering ($s_1^*\gtrless s_2^*$, $\pi_1^*\gtrless\pi_2^*$) and every sign of
$\partial s_i^*/\partial\gamma$ is therefore **independent of $a-c$ for any $a>c$**. The
normalisation is without loss of generality, which is presumably why Kopel states Lemma 3
"holds for $a>c$" (p. 501) rather than for a specific value.

**Fix**: replace the caveat with the homogeneity argument — it is a stronger statement and
removes "remaining gap 3" entirely. This is also a good 20-second slide point.

---

## F7 — p. 500 cited for a result that is on p. 499

**Severity**: should-fix. **Category**: C1.
**Files**: `wiki/papers/Kopel2021-CSR.md` §7.1 ("Spillovers dampen the leader's incentive
and strengthen the follower's (p. 500)"); `wiki/concepts/csr-spillovers.md` "Why spillovers
destroy the first-mover advantage" ("(p. 500)").

Section 5.2 of the paper begins on p. 499, and the sentence

> "We have $\partial(\partial\pi_1/\partial s_1)/\partial\theta < 0$ for the leader, but
> $\partial(\partial\pi_2/\partial s_2)/\partial\theta > 0$ for the follower."

sits in §5.2 in the lower half of p. 499 (confirmed by extracting PDF page 11 on its own).
p. 500 opens with Fig. 2.

**Fix**: p. 499 in both places. (§7's heading "pp. 499–501" is fine; the Lemma 2 and Fig. 2
cites to p. 500 are correct.)

## F8 — The wiki silently reverses a sentence on p. 500 instead of flagging a contradiction in the paper

**Severity**: should-fix. **Categories**: C3, C10.
**File**: `wiki/papers/Kopel2021-CSR.md` §7.2, second bullet.

The wiki says: "**Dashed curve** = locus where $s_1^*=s_2^*$. Above it $s_1^*<s_2^*$;
below it $s_1^*>s_2^*$." The paper's text says the opposite:

> "Figure 2 also depicts the region where the leader's CSR investments are higher than the
> follower's ($s_1^* > s_2^*$ in the region **above** the dashed curve and $s_1^* < s_2^*$
> below)." (p. 500)

**The wiki is substantively right and the paper's sentence is wrong.** Fig. 2's own region
labels (rendered page: "$\pi_1^*<\pi_2^*$ / $s_1^*<s_2^*$" in the upper area, "$s_1^*>s_2^*$ /
$\pi_1^*>\pi_2^*$" at bottom right) agree with the wiki, as does my computation: at
γ = 0.3 the $s_1^*=s_2^*$ frontier is θ = 0.01693, and at γ = 0.3, θ = 0.05 (above it)
$s_1^*=0.2820 < s_2^*=0.2889$. Lemma 2 itself ("the CSR leader selects a higher activity
level … if CSR spillovers are quite small") also agrees with the wiki.

But a wiki whose rule is "cite the paper" must not quietly overwrite the paper. If an
advisor reads p. 500 and the slide says the reverse, the presenter needs the answer ready.

**Fix**: state the wiki's (correct) reading, then add one line: "Note: the sentence on
p. 500 states this the other way round; it contradicts Fig. 2's own labels and Lemma 2,
and our computation confirms the figure. Treated here as a slip in the paper." Same
treatment is worth adding where `first-mover-advantage.md` says "the dashed curve lies
above the bold one" (that claim is correct — verified at all five γ values; see
"Checked and correct").

## F9 — The follower threshold 0.202167 is an endpoint criterion, not whole-interval monotonicity; "A4 matches exactly" overclaims

**Severity**: should-fix. **Categories**: C5, C9.
**Files**: `wiki/papers/Kopel2021-CSR.md` §7.3 table and §10; `wiki/concepts/competition-intensity.md`
shape table; `wiki/numbers.md` evidence standard. (Originates in `checks/a4_report.md` §3.)

The **direction of both thresholds is stated correctly everywhere** (see C5 under "Checked
and correct") — this is not a repeat of the earlier backwards draft. The problem is the
strength of the claim. The wiki's §7.3 table asserts "$\theta<0.202167$ ⇒
$\partial s_2^*/\partial\gamma<0$ **throughout**", and §10 records "Lemma 3 shape bands —
match exactly".

That is the paper's own wording (footnote 15, p. 501), but it is not exactly true, and a
numerical grid is what would miss it. Taking the maximum of $\partial s_2^*/\partial\gamma$
over 2000 points in $(0,\gamma_{\max})$:

| θ | max $\partial s_2^*/\partial\gamma$ | at γ |
|---|---|---|
| 0.18 | −2.81e−2 | 0.744 |
| 0.19 | −5.86e−3 | 0.765 |
| **0.1925** | **+1.04e−3** | **0.769** |
| 0.195 | +8.60e−3 | 0.774 |
| 0.202167 | +3.49e−2 | 0.788 |

So the interior hump appears somewhere between θ = 0.190 and θ = 0.1925, well before the
paper's 0.202167. In that range the follower's curve is **down–up–down**: it rises on an interior
interval around γ ≈ 0.77–0.79 and falls again before $\gamma_{\max}$. The paper's method
(footnote 15: evaluate the derivative *at* $\gamma_{\max}$) cannot see this, which is why
0.202167 is where the slope at the endpoint flips, not where monotonicity first fails.
The leader's threshold 0.229499 does not have this problem (max $\partial s_1^*/\partial\gamma$
is already −1.2e−3 at θ = 0.22950).

**Fix**: keep the thresholds and Lemma 3 as quoted, but state in §7.3 what footnote 15's
criterion actually is ("the sign of the derivative evaluated at $\gamma_{\max}$"), and
replace "match exactly" in §10 with the honest version: the thresholds reproduce to 6 dp,
and A3 additionally found a narrow band just below 0.202167 where the follower's curve is
non-monotone in the interior although its endpoint slope is still negative. Good
discussion material, and safer than being corrected from the floor.

## F10 — "The leader must retain 99.85% of its CSR benefit" is not a quantity in the model

**Severity**: should-fix. **Categories**: C3, C10.
**Files**: `wiki/numbers.md` FMA frontier table (column "leader must retain");
`wiki/papers/Kopel2021-CSR.md` §7.2 box; `wiki/concepts/first-mover-advantage.md`;
`wiki/overview.md` item 2 (where it is stated unmarked under "From [[Kopel2021-CSR]]");
`checks/a4_report.md` §3.

In eq. (1) the leader's own demand shift is $s_1$ whatever θ is. θ adds a benefit to the
*rival*; it does not subtract one from the leader. So "retaining $1-\theta$ of the
benefit" is a metaphor, and at θ = 0.0015 the arithmetic "99.85%" reads as a model output.
The defensible statement is: **the spillover rate must stay below 0.15% at γ = 0.3.**

`overview.md` is the worse case: item 2 presents the figure directly under "From
[[Kopel2021-CSR]]" with no own-calculation marking, so a reader takes 99.85% for Kopel's
number. The underlying frontier is correct — I reproduced all five rows (see below).

**Fix**: drop the "retain" column or rename it "max spillover rate"; mark the frontier as
own calculation wherever it appears outside the 🔎 boxes, `overview.md` included.

## F11 — Bagnoli & Watts and Fisman et al. are theory papers; the wiki calls the literature empirical

**Severity**: should-fix. **Category**: C4.
**Files**: `wiki/overview.md` item 3 ("may reconcile a conflicting empirical literature");
`wiki/concepts/competition-intensity.md` "Why this matters empirically";
`wiki/open-questions.md` Q4.

p. 492 describes both as models:

> "Bagnoli and Watts (2003) find an inverse relationship between the intensity of
> competition and provision of CSR … Fisman et al. (2006) **use a signaling model** and
> conclude that strategic CSR is more likely to be observed when the intensity of
> competition in the product market is higher."

The paper's only "empirical studies show no or a rather weak link" remark (p. 491) is
about corporate social vs. financial performance — a different literature. The argument
"a linear empirical specification will recover whichever sign the sample spans" is also
ours, not Kopel's, and is unmarked in all three places.

**Fix**: "a theoretical literature with conflicting conclusions (p. 492)"; mark the
specification argument as our inference (it is a good discussion point, just not his).

## F12 — The Burke & Logsdon blockquote is not verbatim

**Severity**: should-fix. **Category**: C2.
**File**: `wiki/concepts/appropriability.md`, the blockquote.

Wiki: "specificity **is** the firm's ability to capture or internalize the benefits …".
Footnote 6, p. 494: "**Specificity refers to** the firm's ability to capture or internalize
the benefits of a CSR programme, rather than simply creating collective goods which can be
shared by others in the industry, community or society at large." (Burke and Logsdon 1996,
p. 497).

Only the opening clause was altered, but it is presented as a blockquote of a
double-nested quotation, which is exactly where a reader will not check.

**Fix**: restore "Specificity refers to", and keep the "(Burke and Logsdon 1996, p. 497),
quoted in Kopel 2021 fn. 6, p. 494" attribution chain. (The version on the paper page §4.2
quotes only the second half and is accurate.)

## F13 — The lake example is given a benefit the footnote does not give it

**Severity**: should-fix. **Categories**: C4, C3.
**File**: `wiki/concepts/appropriability.md`, paragraph after the Patagonia/StarKist table.

Wiki: the firm "both serves the environment and gains a **cost/comfort advantage
competitors cannot copy without the same lake**."

Footnote 6, p. 494: "think of a firm which—instead of air conditioning—uses water from a
nearby lake to keep its offices cool and comfortable. This not only serves the
environment, but also the firm **which can strategically communicate these activities to
stakeholders**; see Tetrault Sirsly and Lamertz (2008)."

Kopel's stated benefit is strategic communication to stakeholders. The "competitors cannot
copy without the same lake" reading is ours — plausible, and it even supports the next
sentence ("appropriability comes from an asset the rival does not have", also unmarked),
but it is not the footnote's content.

**Fix**: quote the footnote's benefit, then add our gloss marked as ours.

## F14 — Convergence: the wiki makes leaders the object of pressure; the paper makes them the agent

**Severity**: should-fix. **Categories**: C1, C3.
**Files**: `wiki/papers/Kopel2021-CSR.md` §8; `wiki/concepts/csr-spillovers.md`
"Convergence as an endogenous force"; `wiki/concepts/appropriability.md` last table row.

Wiki: "Industry leaders **are pressured** to help competitors adopt their CSR practices
(Misani 2010; Vogel 2005)" / "leaders **pressured** to help rivals adopt their practices".

p. 491: "Being aware of reputation spillovers, **industry leaders oftentimes pressure and
support** less socially responsible competitors to imitate their CSR practices (Misani
2010; Vogel 2005)." p. 502 adds the motive: "due to the fear of negative reputation
spillovers—the CSR leader **might find it appropriate to support** the CSR follower".

The leader is the actor, out of self-interest. That is the interesting version of the
story — the wiki's passive phrasing makes it weaker. Two citation details: the
Misani/Vogel parenthetical belongs to p. 491 (the wiki cites p. 502 for it); and
"Convergent CSR raises θ endogenously" is our inference, not in the paper, and is unmarked.

**Fix**: use the paper's active phrasing with p. 491; keep p. 502 for the fear-of-
reputation-spillover motive and fn. 16; mark "raises θ endogenously" as our reading.

## F15 — "Rather small" (p. 500) refers to the $s_1^*>s_2^*$ region, not the FMA region

**Severity**: should-fix. **Category**: C1.
**File**: `wiki/papers/Kopel2021-CSR.md` §2, finding 2: "The FMA survives **only for very
low θ**. The region is 'rather small' (p. 500)."

p. 500: "Figure 2 also depicts the region where the leader's CSR investments are higher
than the follower's … Again, it can be noted that **this region** is rather small, meaning
that the existence of CSR spillovers drastically reduces the incentives for the CSR leader
to engage heavily in CSR." The antecedent is the investment region, not the profit region.
Both regions are in fact small (frontiers at γ = 0.3: 0.0015 vs 0.0169), so the claim is
not false — but the quote is hung on the wrong referent, and `checks/a4_report.md` §3
reuses it the same way ("The paper calls the region 'rather small'") as the phrase its
FMA frontier table "understates".

**Fix**: cite "rather small" for the $s_1^*>s_2^*$ region and use the p. 491 "in fact very
low" sentence for the FMA region.

## F16 — Unmarked own-inference on the concept pages (C3 sweep beyond §9 and the 🔎 boxes)

**Severity**: should-fix (collectively). **Category**: C3.

§9 and the 🔎 boxes are correctly marked — §9 says "A1 observation — not the author's
words" and "These are mine"; both 🔎 boxes say "not in the paper" / "Identified in A4, not
stated in the paper"; `numbers.md` separates "From the paper" from "Computed in A4". The
concept pages have no equivalent convention, and several analytic passages there read as
the paper's:

| File / section | Passage presented as the paper's |
|---|---|
| `competition-intensity.md`, "Consequence for interpretation" | the $\gamma_{\max}$-as-monopoly-boundary reading is A4's; the 🔎 box above it is marked, this paragraph is not |
| `competition-intensity.md`, after the three-effects table | "For the follower there is no strategic effect, so the markup effect dominates throughout" — the paper states $\partial(\partial\pi_2/\partial s_2)/\partial\gamma<0$ (fn. 12, p. 498) but does not attribute it to the absence of a strategic effect |
| `first-mover-advantage.md`, "Two distinct comparisons" | "there is a band where the leader invests more but still earns less" — true (verified), but it is our reading of Fig. 2, not a statement in the paper |
| `strategic-commitment.md`, "The idea" and "What is assumed away" | "observed and irreversible", "CSR is a sunk investment", "no reputation accumulation" — none of these words appear in the paper |
| `strategic-commitment.md`, strategic-effect paragraph | "$\partial\pi_1/\partial s_2<0$" is ours; fn. 14 (p. 499) gives only the product "$\frac{\partial\pi_1}{\partial s_2}\frac{\partial s_2}{\partial s_1}>0$". Same issue on the paper page §6.2 ("both factors negative") |
| `appropriability.md`, "The pattern:" and the raises/lowers table | "industry-wide certification or standards" and "CSR central to brand identity" are not in the paper (only "protected by legal means", p. 494) |
| `open-questions.md` Q3, "What the paper does" | "Shows the FMA requires θ below roughly 0.0015" — the paper shows no such number; the heading attributes our computation to the paper, even though the source is cited in the next clause |

None of these is false. The risk is uniform: B3/B6 will lift them into evidence cards and
slides as Kopel's claims.

**Fix**: one convention on the concept pages, e.g. a bracketed "[our reading]" tag, or the
same 🔎 box used on the paper page. Q3's heading should say "What the paper does … / what
we computed".

## F17 — `appropriability.md` uses the 0.0015 frontier with no provenance

**Severity**: should-fix. **Category**: C7.
**File**: `wiki/concepts/appropriability.md`, "Measurement problem".

"Given that the first-mover advantage requires $\theta$ below roughly $0.0015$ at moderate
competition …" — no citation to `checks/` and no own-calculation marking, on a page that
otherwise cites carefully. `numbers.md` explicitly requires: "Mark these clearly on any
slide as **own calculation**, not the author's."

**Fix**: add "(own calculation, `checks/a4_report.md` §3; γ = 0.3)".

## F18 — `sources.md`: Wang et al. (2018) described as having "no sequencing"

**Severity**: should-fix (it is a characterisation of a cited work beyond what Kopel says —
C4's explicit test). **File**: `wiki/sources.md`, candidates table.

p. 493: "A similar analysis is provided by Wang et al. (2018). The difference here is that
the CSR firm does not make demand-enhancing investments with (negative) spillovers, but
that the CSR firm maximizes an extended objective function which includes profit and
consumer surplus." "A similar analysis" refers back to Chen et al. (2016), whose setting is
"Cournot–Stackelberg market competition". Kopel never says Wang et al. lacks sequencing;
the difference he names is the objective function.

**Fix**: "closest formal model — duopoly CSR with an extended objective function including
consumer surplus (p. 493)".

## F29 — Several concept-page sections carry no page citation at all

**Severity**: should-fix. **Category**: C1 (the "does every claim carry a citation?" half).
**Files**: `wiki/overview.md`; `wiki/concepts/first-mover-advantage.md`;
`wiki/concepts/appropriability.md`.

The paper page is densely cited and `equations.md`, `numbers.md` and `glossary.md` all
carry source columns. The gap is on the narrative sections of three concept pages:

- `overview.md` "The answer so far", items 1–4: four substantive claims about the paper's
  results with no page numbers (only a blanket "From [[Kopel2021-CSR]], verified in
  `checks/a4_report.md`" above them). Item 2 also carries the unmarked 99.85% (F10).
- `overview.md` "The question in one paragraph" and "The causal chain": no citations.
- `first-mover-advantage.md` "Where the result comes from" and "Kopel's model sides with
  the skeptics conditionally …": no citations; the second is also our inference (F1).
- `appropriability.md` "Why it is the pivot of the whole paper" and "What it means": no
  citations until the footnote-6 quote.

AGENTS.md §3 requires "every factual claim carries (Kopel 2021, p. X)", and the wiki's own
A3 checklist (paper page §10) lists "Every claim on this page carries a page citation".
Each claim above is traceable — I did not find an uncitable one — so this is a
completeness defect, not an accuracy one. But B3's evidence cards are rejected if a card
has no page citation, so these sections will fail at B3 rather than here.

**Fix**: add the page numbers (overview items 1–4 map to pp. 499, 500, 500–501 and 491–502
respectively).

---

# Minor

**F19 (C2).** `wiki/papers/Kopel2021-CSR.md` §6.3: `Proof: "follows from a simple comparison
and is therefore omitted" (p. 499)`. The paper reads "The proof of the lemma follows from a
simple comparison is therefore omitted." — the wiki inserts "and", tidying the author's
typo inside quotation marks. Use `[sic]` or paraphrase.

**F20 (C2).** The Lemma 1 and Lemma 2 blockquotes drop the comma after each "i.e.,"
(three occurrences). That is the only deviation: everything else in all three lemma
blockquotes is character-for-character correct, Lemma 3 in full included, and Lemma 1's
"that is the leader obtains" matches the paper exactly (the paper has no comma there
either). Worth fixing only because the page presents them as verbatim.

**F21 (C1).** `wiki/open-questions.md` Q1: "footnote 7 mentions the follower 'copies **and
improves**'". That phrase is in the **main text** of p. 494 ("If the CSR follower copies and
improves the green attributes of the CSR leading firm, it can raise the demand for its
product without having to bear the full development costs."), immediately before the
footnote-7 marker. Footnote 7 itself is the Patagonia/StarKist note.

**F22 (C8).** `checks/a4_report.md` §2a says the follower-interiority root is "0.8599 at
θ = 0.2"; `wiki/numbers.md` and the wiki page say 0.8592. My computation: **0.8591995836**.
The wiki is right and A4 has the typo — but the two documents disagree in print, and A5
(contradiction lint) should catch it.

**F23 (C7/C1).** `wiki/glossary.md` gives $\gamma_{\max}$'s value as $0.8107358771$ in a row
sourced to "[[Kopel2021-CSR]] p. 495", where the paper prints 0.810736. The extra four
digits are A4's. Same row convention puts $a$, $x_i$, $p_i$ at "p. 494"; all three are
introduced on p. 493 (eq. (1) is on p. 494, but the symbols are defined in the preceding
paragraph).

**F24 (C1).** `wiki/papers/Kopel2021-CSR.md` §1: "The paper is a revised version of a 2009
working paper". The unnumbered footnote on p. 489 says the working paper "has been
circulated and frequently cited **since** 2009" — it does not date the paper to 2009.

**F25 (C3).** `wiki/papers/Kopel2021-CSR.md` §5.2: "the follower raises its CSR **to exploit
the gap**". p. 496: "the follower has to increase its own CSR activities **to counterbalance
this effect**." Different mechanism in English; the paper's is defensive, the wiki's is
opportunistic.

**F26 (C4).** `wiki/concepts/competition-intensity.md` demand-effect row omits the condition
the paper attaches: p. 498 says "**in the case of no CSR spillovers**, we have
$\partial(\partial x_i/\partial s_i)/\partial\gamma>0$". The paper page §6.2 includes the
qualifier; the concept page does not.

**F27 (C4).** Vocabulary not in the paper, used without flagging: "strategic
substitutes/complements" (`csr-spillovers.md`, `equations.md`, paper page §5.2),
"irreversible"/"sunk" (`strategic-commitment.md`), "war of attrition"
(`open-questions.md` Q2), "taste-based" (`glossary.md`). Grepping the PDF text returns
zero hits for all four. These are standard terms and the usages are correct; they are
listed only because AGENTS.md §3 bars outside material and B7 will be checking slide
wording against the wiki, not against the paper.

**F28 (C10, advisory — not a wiki defect).** The presenter should know that p. 499 contains
a slip of its own: "a first-mover advantage only occurs if the level of **appropriability**
is very low" — it should read "spillovers". The wiki consistently uses the economically
correct direction (appropriability must be *high*), which is right, but anyone reading
p. 499 during the talk will see the opposite sentence. One pre-emptive line in the
speaker notes, as with F8.

---

# Checked and correct

Method is stated per item: **[text]** = PDF text layer, **[page]** = rendered PDF page read
as an image, **[sympy]** / **[mp]** = my own re-derivation or numerics.

**C1 — citations that check out.** Every page number below was verified against the page
on which the material actually sits **[text, page]**: the unnumbered working-paper
footnote and the research questions (pp. 489–490); the Economist and Tetrault Sirsly
quotes (p. 490); the three literature streams (pp. 492–493); model primitives, timing and
the general demand system (p. 493); eq. (1), $\theta_1,\theta_2\in[0,1]$, fn. 4, fn. 6,
fn. 7, the legal-protection remark, vertical-vs-horizontal (p. 494); eq. (2), the profit
definitions, $\gamma_{\max}$ with the Garella & Petrakis attribution, eq. (3), the
$\theta>\gamma/(2-\gamma^2)$ price condition (p. 495); the equal-CSR higher-price remark,
eq. (4), eq. (5), eq. (6), $N$, fn. 8 (p. 496); eq. (7) $p_1^*$ spanning to $p_2^*$, both
profits, the $s_1^*-s_2^*$ gap, 0.531963, fn. 9 (p. 497); Fig. 1, the three-effects
decomposition, fns. 10–12 (p. 498); fns. 13–14, "overinvest", "can not only be sustained,
but made even larger", "a higher degree of competition makes the strategic effect even
more pronounced", Lemma 1 (p. 499); Fig. 2, Lemma 2, both thresholds in the main text
(p. 500); Fig. 3 at θ = 0.21, Lemma 3, fn. 15, "holds for $a>c$" (p. 501); conclusions,
managerial implication, the six extensions, fn. 16 (p. 502). The pagination mapping (PDF
page n = journal page 488 + n) holds on every page I rendered. Five wrong-page citations
were found (F7, F14, F15, F21, F24) plus one completeness gap (F29); every other citation
I traced, listed above, points at the page that actually carries the material.

**C2 — quotations that are verbatim [text, page].** Lemma 1, Lemma 2 and Lemma 3
blockquotes are character-for-character correct apart from the dropped commas in F20 —
in particular both thresholds inside Lemma 3 and the clause "(independent of the degree of
competition)" in Lemma 2. The Economist "number two or three on corporate responsibility
rather than number one"; the Tetrault Sirsly & Lamertz "central to the firm mission,
visible to stakeholders and with firm-specific benefits beyond those of public goods"; the
$\gamma_{\max}$ sentence "guarantees that the equilibrium of the game is in the interior
and all second-order conditions are satisfied"; "can not only be sustained, but made even
larger"; "a higher degree of competition makes the strategic effect even more pronounced,
leading to an increase in the difference between the CSR engagements"; "depends on factors
which are quite hard to measure accurately"; "no or a rather weak link"; "might be
ambiguous for firms"; the second half of the Burke & Logsdon definition as quoted on the
paper page §4.2; and StarKist's "its main competitors imitated this policy almost
immediately" — all exact.

**C5 — the θ threshold logic is correct in all four required locations.** Lemma 3 (p. 501)
and fn. 15 assign **0.202167 to the follower** ($\partial s_2^*/\partial\gamma<0$ below it)
and **0.229499 to the leader** ($\partial s_1^*/\partial\gamma<0$ above it) **[text, page]**.
The paper page §7.3 table, `csr-spillovers.md` "Threshold values", `competition-intensity.md`
(both the prose and the six-row shape table) and `numbers.md` ($\theta^{(2)}$, $\theta^{(1)}$
labels) all state it this way. No reversal anywhere. I reproduced both thresholds by the
paper's own method **[mp]**: derivative at $\gamma_{\max}$ changes sign at
$\theta = 0.2021669652$ (follower) and $0.2294985134$ (leader) — both agree with the paper
to the 6 dp it prints. (Note for `numbers.md`: my 10-digit values differ from A4's in the
8th decimal, 0.2294985134 vs 0.2294985504, so the 10-digit "recomputed" column is robust to
6–7 dp, not to 10.)

The **both-U-shaped band** claim holds, and **Fig. 3's θ = 0.21 sits in it** — but the
band edges are the endpoint sign changes above, not the output of a shape classifier.
Verbatim output of my classifier (sign changes of successive differences; 200 γ-points for
the first run, 400 for the second) **[mp]**:

| θ | leader $s_1^*$ | follower $s_2^*$ |
|---|---|---|
| 0, 0.15 | U-shaped | decreasing |
| 0.195 | U-shaped | **other (2 sign changes)** |
| 0.201, 0.203, 0.21, 0.228 | U-shaped | U-shaped |
| 0.231, 0.24, 0.25, 0.5, 0.9 | decreasing | U-shaped |

Two things to read correctly here. θ = 0.201 classifies as U-shaped although it is below
0.2021670 — that is the interior hump of F9, not a contradiction of the threshold, which
is defined by the endpoint slope. And θ = 0.195 returns "other", not "decreasing", for the
same reason. So `competition-intensity.md`'s six-row shape table is right at every θ it
lists (0, 0.15, 0.21, 0.25, 0.5, 0.9), and the band claim is right; F9 concerns the
strength of the "monotone throughout" wording just below 0.202167, not the direction of
either threshold or the existence of the band.

**C6 — every equation in the register matches the printed page.** I compared each entry
against the rendered pages 495, 496 and 497 **[page]**, not only the text layer: K-gen,
K-1, K-2 (both lines, including the asymmetric numerators $(1-\gamma\theta)s_1-\gamma s_2$
and $s_2-(\gamma-\theta)s_1$), K-profit, K-3 (both lines, including
$(2-\gamma^2-\gamma\theta)s_1$ in $p_1$ and $((2-\gamma^2)\theta-\gamma)s_1$ in $p_2$),
K-4, K-5, K-6 with the full seven-term $N$, K-7 (both prices), K-pi (both profits,
including the unusual numerator $(4-\gamma^2)(2-\gamma^2)^2-4$), and K-gap with its range
"$0<\gamma\le\gamma_{\max}$". **Zero transcription errors.** Independently of A4 I
re-derived the whole game from eq. (1) in sympy — invert demand, stage-3 FOCs, stage-2 FOC,
substitute, stage-1 FOC — and all twelve comparisons returned True **[sympy]**, including
the $\pi_1^*$-linear / $\pi_2^*$-quadratic asymmetry the wiki flags as "genuine, not a
transcription error". That asymmetry is genuine. The only register defect is K-sub's sign
(F2), which is not one of the paper's own equations.

**C7 — the number register.** Reproduced independently **[mp]**: $\gamma_{\max}$ as the
root of $N(\gamma,0)$ = **0.8107358771** (matches 0.810736 to 6 dp); turning point
**0.5319633163**; both θ thresholds (above); the follower-interiority reading of
$\gamma_{\max}$ — $x_2^*$ at θ = 0 falls to 2.5e−7 at γ = 0.81073587 and 0.00125 at
γ = 0.8107, so $s_2^*$ and $x_2^*$ really do vanish together there, confirming the 🔎 box
and Q5; the root's rise in θ (0.8107 → **0.8591996** at θ = 0.2 → 0.9325259 at θ = 1); all
five FMA-frontier rows (**5.343e−5, 0.0015022, 0.0086694, 0.039281, 0.096008** — matching
0.0000534 / 0.00150 / 0.00867 / 0.0393 / 0.0960 exactly); all ten Fig. 3 values at θ = 0.21
to 4 dp; all six leader-CSR values in the θ = 0 vs θ = 0.21 table; and Lemma 1 on an
80-point grid at θ = 0 (no violations). The paper-vs-recomputed "Diff" column is
arithmetically right in all four rows. The separation of "From the paper, verified" from
"Computed in A4, not stated in the paper" is the right structure and is honestly applied
inside `numbers.md` itself; the leakage is on other pages (F10, F17).

**C8 — consistency that holds.** $\gamma_{\max} = 0.810736$ is stated identically on the
paper page, `glossary.md`, `numbers.md`, `competition-intensity.md` and `open-questions.md`
Q5 (with the F23 precision nit). Both θ thresholds are identical across the four pages that
carry them. The FMA frontier table is identical in `numbers.md`, the paper page §7.2 and
`first-mover-advantage.md`. The Fig. 3 ordering — **follower above leader** — is stated the
same way on the paper page §7.3, in `numbers.md` and in A4, and I confirmed it at five γ
values **[mp]** and against the Fig. 3 caption **[text]** ("the CSR follower's investments
(dashed curve) are higher than the CSR leader's investment (bold curve)"). The related
Fig. 2 claim that the **dashed curve lies above the bold one** (`first-mover-advantage.md`)
is also correct: the $s_1^*=s_2^*$ frontier sits above the $\pi_1^*=\pi_2^*$ frontier at
every γ I tested (0.00256 vs 5.3e−5 at γ = 0.1; 0.0169 vs 0.0015 at 0.3; 0.0427 vs 0.0087 at
0.5; 0.0951 vs 0.0393 at 0.7; 0.1527 vs 0.0960 at 0.8) **[mp]**, so the "invests more but
earns less" band is real.

**C9 — honest statements that are already right.** The paper page §10 and `numbers.md`
both say Lemma 1 is "confirmed on 39 grid points, not proved symbolically. The paper omits
the proof too", and A4 §5.2 says the same; `first-mover-advantage.md` repeats it. The
🔎 boxes label their content "not in the paper" / "the paper never states this
numerically". `glossary.md` marks $D$ as "A4 notation, not in the paper". These are the
right instincts; F5, F9 and F16 are the places where they were not applied.

**C10 — other things I checked and found sound.** The three-stage timing table matches
p. 495. The strategic-substitutes/complements economics is the paper's, only the labels are
ours. The "$\gamma_{\max}$ is where the duopoly collapses to monopoly" reading survives
numerical scrutiny and is the strongest original contribution of the wiki. The open
questions are genuinely open and none of them misstates what the paper does, apart from
Q3's heading (F16) and Q1's footnote attribution (F21); Q7's speculation that negative
spillovers would strengthen the advantage is clearly framed as a question, though it is
untested and outside the model's $\theta\in[0,1]$ range — worth a one-word hedge. A4's raw
outputs (`a4_run1.txt`, `a4_gammamax.txt`, `a4_gammamax_confirm.txt`) exist as cited; note
that the `python3 -I` invocation in the script header does not work on this machine
(sympy is in the user site-packages that `-I` suppresses), so anyone re-running A4 should
drop `-I`.

---

# Not verified — the limits of this review

So that the coverage above is not read as wider than it is:

1. **Only pp. 495, 496, 497 and 500 were rendered and read as images.** Everything else
   rests on the `pdftotext -layout` text layer. That layer is reliable for prose and page
   boundaries but mangles fractions, so any equation *not* on those four pages has not had
   the independent visual check. In practice this covers all of them — every equation in
   the register is on pp. 493–497 — except K-gen and K-1 (p. 493/494), which I checked in
   the text layer only.
2. **Figures 1 and 3 were not inspected visually.** Claims about them (Fig. 1's U-shape and
   widening gap, Fig. 3's follower-above-leader) were checked against the printed captions
   **[text]** and against my own computation of the underlying functions **[mp]**, which
   agree — but I did not look at the plotted curves. A4 did not redraw them either, so
   nobody in this pipeline has yet compared a curve to a curve.
3. **Third-party quotations were checked only as Kopel reproduces them.** The Burke &
   Logsdon "specificity" definition, the Economist line and the Tetrault Sirsly & Lamertz
   phrase were verified against the Kopel PDF. The original sources are not in `raw/`, so I
   cannot confirm Kopel quoted them correctly — and under the project's own rules nobody
   should try until those PDFs are ingested.
4. **No lint-type checks were run**: `[[link]]` resolution, LaTeX compilation, index/disk
   agreement and `log.md` coverage are A5's job, not A3's, and I did not do them.
5. **`需求摘要.md`, `log.md` and the scripts were not reviewed** beyond reading the A4
   script header; I re-derived the model independently rather than auditing A4's code.

---

## What to fix first

1. **F1 (Tetrault Sirsly & Lamertz)** — the author's conclusion is misstated in three
   files, and it is the kind of thing an advisor who knows the literature will raise.
2. **F3 (the $\theta_i$ definition)** — wrong on the first model slide.
3. **F2 (the K-sub sign)** — a wrong expression in the register B8 trusts, though the
   threshold it concludes with is still correct.
4. **F4, F5** — a fabricated quotation with a page number, and a false "analytic".

Then the should-fix list, then re-review. F6, F8, F9 and F28 are not just corrections —
each is a point the presenter can use.

---

# Round 2 — verification of fixes (2026-11-16)

- **Reviewer**: A3, same reviewer, re-reviewing commit `6854f91` against round 1.
- **Round-1 findings are above, unedited.** They remain the record of what was wrong.
- **New evidence this round**: journal pages 493 and 494 rendered at 130 dpi, and the
  Fig. 1 (p. 498) and Fig. 3 (p. 501) pages at 150 dpi, read as images; a fresh sympy
  homogeneity proof; and mpmath recomputation of both figures' curves. This closes both
  items I had carried forward as "Not verified".

## Verdict: **PASS WITH FIXES** — 0 blockers remain, 26 of 29 findings fully fixed, 8 problems in the new text (0 blockers, 2 should-fix, 6 minor) plus 5 presentational items

**A3 no longer blocks.** None of the five blockers survives, and the two mathematical
claims the writer added — the corrected K-sub quotient and the homogeneity argument — are
both correct under independent check. This does not by itself start Graph B: AGENTS.md §9
requires A6 sign-off first, and A5 (lint) has not run — N1 is exactly the kind of defect
lint exists to catch, so A5 should run before A6. Under §8a this was the second review
round, so the remaining residue goes to the human rather than to a third round.

| Pass | Result |
|---|---|
| Pass 1 — round-1 findings | 26 FIXED · 2 PARTIALLY FIXED (F9, F27) · 1 NOT FIXED (F28, advisory only) · **2 fixes introduced a new problem** (F14→N2, F9→N1) |
| Pass 2 — new text | 8 problems: 2 should-fix (N1, N2), 6 minor (N4, N5, N6, N8, N9, N10); plus 3 tag placements, 1 undefined tag scope in AGENTS.md §3 and 1 log/schema mismatch, in their own sections |

**Counting note.** N3 is not a separate new problem — it is F9's unfixed residue, counted
once under F9. N7 is not new text either: it is old text I missed in round 1, so it is my
omission, not a regression. Both are written up below so the writer has the location, but
neither is counted in the "new text" total.

---

## Pass 1 — finding by finding

### Blockers — all five fixed, and fixed correctly

**F1 (TS&L) — FIXED**, in all four places: paper page §1 (new ⚠️ box), §8 (rewritten with
the p. 502 sentence quoted in full), `first-mover-advantage.md` ("The prior debate", which
now keeps the p. 490 framing table but adds "the conclusion does not pick a winner the way
the framing suggests"), and `sources.md` ("the conceptual paper whose condition for a
sustainable FMA Kopel formalises"). **§1 and §8 do not contradict each other**: both say
the same thing — p. 490 contrasts, p. 502 groups — and §1's box points forward to §8.
Burke & Logsdon was correctly *removed* from the p. 490 "FMA erodes" row in
`first-mover-advantage.md`, since Kopel groups them with the skeptics only on p. 502; that
row now carries Reinhardt and Vogel with a p. 490 citation, which matches the page.

**F2 (K-sub sign) — FIXED, and the new expression is right.** `equations.md`,
`csr-spillovers.md` and `checks/a4_report.md` now all give

$$\frac{ds_2}{ds_1}=\frac{(2-\gamma^2)\big((2-\gamma^2)\theta-\gamma\big)}{12-20\gamma^2+8\gamma^4-\gamma^6}$$

which is exactly what differentiating eq. (4) gives, and the restated proportionality
$(\gamma^2-2)(\gamma^2\theta+\gamma-2\theta)$ now carries the sign sympy actually returns
(`simplify(ds2/ds1 * den) = (g**2-2)*(g**2*th+g-2*th)`). The added note that the
denominator is positive below $\gamma_{\max}$ is correct (7.48 at $\gamma=0.5$, 0.52 at
$\gamma=0.9$). The implication $\frac{ds_2}{ds_1}<0\iff\theta<\gamma/(2-\gamma^2)$ now
follows from what is written.

**F3 ($\theta_i$ direction) — FIXED, and now visually confirmed.** I rendered p. 493,
which I had only read in the text layer in round 1. The printed general system is
$p_1 = a + (s_1+\theta_1 s_2) - x_1 - \gamma x_2$, $p_2 = a + (s_2+\theta_2 s_1) - x_2 -
\gamma x_1$ — $\theta_1$ multiplies $s_2$ inside $p_1$, so the corrected reading is right.
The three locations agree with each other and with §4.2: paper page §4.1 ("the share of
the **rival's** CSR benefit captured by firm $i$"), `csr-spillovers.md` Definition (same
wording, plus the $\theta_1=0,\theta_2=\theta$ specialisation), `glossary.md` (same).
§4.1's handling of the conflicting prose is exactly what AGENTS.md's new rule asks for: it
quotes the p. 494 sentence that reads the other way, says the equation governs, and gives
Kopel's free-riding justification as the tie-breaker. I also rendered p. 494 and confirm
eq. (1) prints as $p_2 = a + (s_2+\theta s_1) - x_2 - \gamma x_1$.

**F4 (fabricated quotation) — FIXED.** The §7.2 box now reads 'The paper's qualitative "in
fact very low" (p. 491)', and the §2 quotation is restored to "What is surprising, however,
is that the level of CSR spillovers for which a first-mover advantage can be sustained is
in fact very low." I re-checked it character-for-character against the text layer: exact.

**F5 ("Lemmas 1 and 2 are analytic") — FIXED.** The clause is gone; §9 item 4 is struck
through and replaced; §10 and `first-mover-advantage.md` still say the lemmas are confirmed
numerically, and nothing on the page now contradicts that.

### Should-fix

**F6 ($a-c$ homogeneity) — FIXED, and the replacement argument is mathematically correct.**
I re-derived the equilibrium from eq. (1) and tested the substitution $a \mapsto c+k(a-c)$:

| object | claim | result |
|---|---|---|
| $s_1^*$ | homogeneous of degree 1 in $(a-c)$ | **True** |
| $s_2^*$ | homogeneous of degree 1 | **True** |
| $\pi_1^*$ | homogeneous of degree 2 | **True** |
| $\pi_2^*$ | homogeneous of degree 2 | **True** |

I also confirmed the two supporting statements separately: $c$ enters $s_1^*$ and $s_2^*$
only through $(a-c)$ (`diff(s_i*,c) + diff(s_i*,a) = 0`), and the ratio $\pi_2^*/(s_2^*)^2$
is free of $a$ and $c$ — so the $\pi_2^*\propto(s_2^*)^2$ step the writer relies on does
hold for the follower, which was the part most at risk. Every ordering and every
$\partial/\partial\gamma$ sign therefore scales by a positive constant and is unchanged for
any $a>c$. The claim is sound, is tagged **[our reading]**, and the now-redundant
"remaining gap 3" was removed.

**F7 (p. 500 → p. 499) — FIXED** in both places; both now read "(p. 499, §5.2)".

**F8 (Fig. 2 contradiction) — FIXED**, and well. Paper page §7.2 carries a ⚠️ box stating
our reading, the contradicting sentence, the three reasons we override it and the numerical
evidence; `first-mover-advantage.md` cross-references it. AGENTS.md §3 gained the general
rule. This is now a talking point rather than a liability.

**F9 (endpoint criterion) — PARTIALLY FIXED, and the fix broke a table.** Three of the
four places that carry the thresholds were updated: paper page §7.3 (criterion stated in the lead sentence, table
rows reworded to "at the endpoint", plus a 🔎 A3 box), `competition-intensity.md` (🔎 A3
caveat box, and it correctly notes "the six rows above are each correct"), and
`numbers.md` (threshold meanings now say "**at $\gamma_{\max}$**", with the hump recorded).
**`csr-spillovers.md` "Threshold values" was missed** — see N3, which is this finding's
residue rather than a new problem. Separately, the paragraph added to `numbers.md` was
dropped into the middle of a markdown table and broke it: **FIXED BUT INTRODUCED A NEW
PROBLEM** (N1).

**F10 (99.85% retention) — FIXED everywhere**: `numbers.md` column renamed "max spillover
rate" with an explicit "do not phrase this as…" note, paper page §7.2 box, overview item 2
("a spillover rate under 0.15%", tagged **[own calculation]**), `first-mover-advantage.md`,
and `a4_report.md` §3.

**F11 (theory vs empirical) — FIXED** in all three places, each now quoting "use a
signaling model" (p. 492) and saying the conflict is between models.

**F12 (Burke & Logsdon blockquote) — FIXED.** Now "Specificity refers to the firm's
ability to capture or internalize…". Verified against the rendered p. 494 footnote:
character-for-character exact, attribution chain intact.

**F13 (lake example) — FIXED.** The footnote's own words are quoted (verified verbatim
against rendered p. 494), and the defensibility gloss is separated and tagged.

**F14 (convergence agency) — FIXED BUT INTRODUCED A NEW PROBLEM.** The agency and the
quotes are right in all three places — paper page §8, `csr-spillovers.md` and
`appropriability.md` now use "industry leaders oftentimes pressure and support" with
p. 491, plus the p. 502 fear-motive quote. But the rewritten paragraph in
`csr-spillovers.md` attached a new wrong page number to the empirical-link claim (N2).

**F15 ("rather small") — FIXED.** Paper page §2 adds the separating sentence, §7.2 attaches
the phrase to the $s_1^*>s_2^*$ region, and `a4_report.md` §3 was corrected too.

**F16 (unmarked inference) — FIXED** at the scale that matters. Every passage I listed now
carries a tag or a quote: `competition-intensity.md` (two), `first-mover-advantage.md`,
`strategic-commitment.md` (four, including a rewritten "What is assumed away"),
`appropriability.md` (three), `overview.md` (two), open-questions Q3, Q4 and Q7. The
convention is stated at the top of the paper page and written into AGENTS.md §3.

Two qualifications. In "What is assumed away", two of the three bullets are anchored to a
p. 502 quote but the cost bullet is not — it cites p. 493 with no quotation, and its
second clause ("The leader's only edge is strategic, never a learning or scale effect") is
our inference sitting under a blanket **[our reading]** label rather than its own. And see
N7 (old text I missed in round 1) and the tag-placement paragraph after the new problems.

**F17, F18 — FIXED.** The 0.0015 figure now carries "own calculation, `checks/a4_report.md`
§3 — not a number in the paper"; the Wang et al. row now describes the extended objective
function with a p. 493 cite, matching what Kopel says.

**F29 (missing citations) — FIXED.** Overview's "The question in one paragraph" and items
1–4 now carry page numbers (Lemma 1 p. 499, Lemma 2 p. 500, Lemma 3 pp. 500–501, p. 491,
p. 492, p. 502 — all correct), the causal chain is tagged as our synthesis of pp. 494–500,
`first-mover-advantage.md`'s section heading gained "(pp. 498–499)", and
`appropriability.md` "Why it is the pivot" now cites Lemma 2, p. 500.

### Minor

**F19 FIXED** (the Lemma 1 proof sentence is now quoted as printed, with *sic*).
**F20 FIXED** (all three "i.e.," commas restored). Method, since "re-checked" means
nothing on its own: I split each lemma blockquote on its LaTeX segments and matched every
remaining prose fragment against a whitespace- and hyphenation-normalised copy of the
PDF text layer. Nine fragments across the three lemmas, **nine found verbatim, zero
misses**. I ran the same normalised match over all 22 quotations in the revised wiki —
every one of the new quotations the fixes introduced is verbatim, including "provides
support for the claims in conceptual papers like Tetrault Sirsly and Lamertz (2008)…",
"in line with Tetrault Sirsly and Lamertz (2008) I find that a first-mover advantage
exists", "pressure and support", "might find it appropriate to support the CSR follower",
"makes it impossible for the CSR leader to profit from its leadership", "a sort of
commitment device", "has to aim for a good match…", "copies and improves…", the restored
Burke & Logsdon definition and the lake example. The only two apparent misses were
artefacts of my own normalisation (a hyphenated line break at "dif-ficult", and an ASCII
"theta" in my test string); both were confirmed by eye on the rendered pages.
**F21 FIXED** (Q1 now quotes p. 494's main-text sentence in full — verified verbatim).
**F22 FIXED** (`a4_report.md` now reads 0.8592 with a note naming the typo; matches my
0.8591995836).
**F23 FIXED** (glossary shows "0.810736 (p. 495); 0.8107358771 (A4 recomputation)", and
$a$, $x_i$, $p_i$ moved to p. 493 — correct, I confirmed those symbols are defined on the
rendered p. 493).
**F24 FIXED** ("a working paper … which 'has been circulated and frequently cited since
2009'" — verbatim).
**F25 FIXED** (§5.2 now quotes "to counterbalance this effect" and adds "the paper's
mechanism is defensive, not opportunistic").
**F26 FIXED** (the demand-effect row now carries the no-spillover condition and p. 498).
**F27 — PARTIALLY FIXED.** "Irreversible/sunk" is properly handled: `strategic-commitment.md`
now carries a tagged note that the phrase is standard game-theoretic vocabulary, not the
paper's, and that the paper never discusses reversibility. "Strategic
substitutes/complements" is tagged in two places (paper page §5.2, `csr-spillovers.md`)
but still appears untagged in the `equations.md` K-sub heading, the `numbers.md`
"Conditions, not constants" table and `strategic-commitment.md`'s "The strategic effect
is conditional". "War of attrition" in open-questions Q2 is untouched — no diff hunk
reaches it — and "taste-based" survives in the glossary. Both of those last two are
defensible (Q2 is explicitly a question we are posing; the glossary column is headed
"Meaning here"), so this is a presentational residue, not a factual one.
**F28 — NOT FIXED** (advisory). Nothing in the wiki yet warns that p. 499 itself says "a
first-mover advantage only occurs if the level of **appropriability** is very low", where
the paper means spillovers. The wiki uses the correct direction throughout, so there is no
error to fix — but now that §7.2 has a ⚠️ box for the Fig. 2 slip, the same one-line
treatment here would protect the presenter. Recommend adding it; not a defect.

### Regressions

**Two fixes introduced a new problem: F14 → N2 (a new wrong page number) and F9 → N1 (a
broken table).** Both are small and both are in prose added by the fix, not in the
corrected content itself.

**No regression in the mathematics.** Method, so this is checkable rather than asserted:
`git diff 19779f3 6854f91 -- wiki/equations.md` shows exactly one changed entry, K-sub,
and it changed to the expression I verified above; K-gen, K-1, K-2, K-profit, K-3, K-4,
K-5, K-6, K-7, K-pi, K-gap and the SOC block are byte-identical to the versions I checked
against the rendered pages in round 1. Grepping the paper-page diff for math lines returns
only prose changes — no displayed equation on that page was touched. In `numbers.md` every
numeric cell is unchanged except the new "max spillover rate" column, whose arithmetic I
checked: 0.0000534 → 0.005%, 0.00150 → 0.15%, 0.00867 → 0.87%, 0.0393 → 3.9%, 0.0960 →
9.6%, all correct to the precision shown.

---

## Pass 2 — problems in the new text

N1, N2, N4, N5, N6, N8, N9 and N10 are defects in prose the fixes added. N3 is F9's residue and
N7 is old text I missed in round 1; both are described here for the writer's convenience
but are not counted as new.

### N1 — `numbers.md`: prose is inserted inside a markdown table, breaking it

**Severity**: should-fix. **Category**: C10 (and C7, because B10 parses this register).
**File**: `wiki/numbers.md` lines 14–25.

The F9 explanation paragraph ("Both thresholds are defined by footnote 15's criterion …")
was placed *between* the $\theta^{(1)}$ row and the two rows that follow it. A markdown
table ends at the first blank line, so the $\theta = 0.21$ and $a-c = 1$ rows now render
as literal pipe-separated text, not as table rows. The content is right; the structure is
broken, in the one file whose whole purpose is to be machine-checkable at B10.

**Fix**: move the paragraph below the complete table.

### N2 — `csr-spillovers.md`: the weak-empirical-link argument is cited to p. 502; it is on p. 491

**Severity**: should-fix. **Category**: C1.
**File**: `wiki/concepts/csr-spillovers.md`, "Convergence as an endogenous force", last line.

"Kopel offers this as a candidate explanation for the weak empirical CSR–financial
performance link (p. 502)." p. 502 says convergence "makes it impossible for the CSR leader
to profit from its leadership" and stops there. The empirical-link step is on p. 491:
"Consequently, since all firms converge on their CSR practices, empirical studies show no
or a rather weak link between corporate social and corporate financial performance." The
paper page §2 (row 5) cites this correctly as p. 491; this page does not.

**Fix**: cite p. 491 for the empirical-link claim, keeping p. 502 for the rest. Note this
is a *new* wrong-page citation introduced by the F14 rewrite, in the same paragraph.

### N3 — F9's caveat did not reach `csr-spillovers.md` *(F9 residue, not a new problem)*

**Severity**: should-fix. **Categories**: C5, C8, C9.
**File**: `wiki/concepts/csr-spillovers.md`, "Threshold values".

The table still says "$\theta = 0.202167$ — below it, the follower's CSR **falls
monotonically** in $\gamma$", and the line under it still asserts the band flatly. That is
precisely the wording F9 showed is too strong, and the three sibling pages now qualify it.
The result is an inconsistency *between* wiki pages, which is worse than the original
uniform overstatement: a B3 card drawn from this page will carry the unqualified claim
while one drawn from `competition-intensity.md` carries the caveat.

**Fix**: add one sentence — "both thresholds are endpoint criteria (fn. 15); see the A3
caveat in [[competition-intensity]]" — or repeat the 🔎 box.

### N4 — `equations.md` still marks K-sub "A4 ✅"

**Severity**: minor. **Category**: C8.
The status table row for K-sub reads "A4 ✅" while the entry below it says "Corrected after
A3 F2". A4 passed this expression when it was wrong — it was never in A4's twelve-equation
comparison set, as the log itself now records. The status cell should read "A3 ✅
(corrected)" or similar, otherwise the register tells a reader that the one entry A4 got
wrong was checked by A4.

### N5 — Paper page §7.3 states footnote 15's method twice

**Severity**: minor. **Category**: C10.
The new lead sentence ("Footnote 15 states the criterion: check the sign of
$\partial s_i^*/\partial\gamma$ **evaluated at $\gamma = \gamma_{\max}$** …") duplicates the
pre-existing closing sentence of the same section ("Footnote 15 states the method: check
the sign of … evaluated at $\gamma = \gamma_{\max}$, then find where the derivative changes
sign."). Harmless, but it reads as an unfinished edit. Delete the second.

### N6 — "All are now fixed" is a self-assessment stated as fact, in two files

**Severity**: minor. **Category**: C9.
Paper page §10, A3 subsection: "Verdict: 5 blockers, 14 should-fix, 9 minor. All are now
fixed." The same claim is in `index.md`'s new footnote 1: "all reported defects are fixed
and a re-review is pending." At the time of writing the re-review had not happened — and
as it turns out, F9 was only partly fixed, F27 partly, and F28 not at all. The paper
page's status line and "Remaining gaps 4" do say re-review is pending, so neither file is
misleading overall, and `sources.md` gets it exactly right with "⚠️ fixed, re-review
pending". Reword both to "all reported defects were addressed; see `checks/a3_report.md`
round 2 for what the re-review found."

### N7 — `appropriability.md`: the Patagonia row still carries an unmarked gloss *(old text, missed in round 1)*

**Severity**: minor. **Category**: C3. This sentence predates the fixes — my round-1 F16
sweep listed the raises/lowers table but not the examples table above it, so this is my
omission rather than a regression.
The "What raises or lowers it" table is now correctly prefaced ("Only the first row is the
paper's; the rest is **[our reading]**"), but the *examples* table above it is not, and its
Patagonia cell says "CSR attributes are **bound to the brand** and defended in a premium
segment". Footnote 7 says Patagonia "is quite successful in differentiating its products
and defending its advantage in a premium-segment of the market" — the brand-binding is our
gloss. One tag or a trim fixes it.

### N8 — `csr-spillovers.md` cites "(p. 499, §5.2)" twice in four lines

**Severity**: minor. **Category**: C10. Cosmetic leftover from the F7 edit: the citation
appears both in the lead-in sentence and again immediately after the display equation.

### N9 — "The model is static" sits badly with footnote 2, where Kopel calls his own model multi-stage

**Severity**: minor (but it is the kind of thing an advisor asks about).
**Categories**: C1, C4. **File**: `wiki/concepts/strategic-commitment.md`, "What is
assumed away", third bullet.

> "**One shot.** The model is static; Kopel notes that 'most existing work is done in
> static environments' and lists dynamic CSR as an extension (p. 502)."

The quotation is verbatim, but it is about *existing work*, not about this model, and it
is doing double duty as evidence that Kopel calls his own model static. Footnote 2 on
p. 492 says the opposite in so many words: "Starting from **dynamic (multi-stage) settings
like the present paper**, the analysis of R&D under spillovers has been extended to fully
dynamic models…". Kopel's three-stage game is multi-stage; what it lacks is repeated
interaction across periods. The paper page's §9 item 7 gets this right — "Static *within
each stage*; no repeated interaction, learning, or consumer memory" — so the two pages now
differ.

**Fix**: match §9's wording ("one-shot: multi-stage within the game, but no repeated
interaction"), and either cite fn. 2 p. 492 or drop the "static" label.

### N10 — The hump sentence in the paper page §7.3 box can be read as the band's width

**Severity**: minor. **Category**: C10. **File**: paper page §7.3, 🔎 A3 box.

"…the hump appears between $\theta = 0.190$ and $\theta = 0.1925$ — below the paper's
0.202167. **In that narrow band** the follower's curve is down–up–down." The antecedent of
"that narrow band" reads as 0.190–0.1925, which is the bracket for the *onset*. The band
in which the curve is actually down–up–down runs from the onset up to 0.202167 (at which
point the endpoint slope itself turns positive). `competition-intensity.md`'s version of
the box avoids this. **Fix**: "from there up to 0.202167 the follower's curve is
down–up–down."

---

## Tag placement — asked for specifically, so checked line by line

The **[our reading]** / **[own calculation]** tags are on the right sentences in the large
majority of cases: `first-mover-advantage.md` "Two distinct comparisons" and the frontier
table, `competition-intensity.md` "Consequence for interpretation" and the linear-
specification argument, `appropriability.md` "Why it is the pivot", the lake gloss and the
raises/lowers table, `overview.md` item 2 and the causal chain, open-questions Q3, Q4, Q7,
and the paper page §9 item 4. In each of those the tag opens the passage it governs and
the paper's own material is outside it. Three placements are weaker:

1. **Paper page §6.2.** The tag is appended *after* two sentences that are the paper's
   (fn. 14's product sign, fn. 13's condition) and before the sentence that explains what
   is ours. A reader scanning for tags could attach it to the footnote claims. Move it to
   the start of the explanatory sentence.
2. **`csr-spillovers.md` lines 52–54.** "**[our reading]** So $\theta$ is not a neutral
   leak — it is a transfer of incentive." The tag is correctly placed, but it immediately
   follows a duplicated "(p. 499, §5.2.)" citation (N8), so the tag and the citation
   collide and it is momentarily unclear which clause is the paper's.
3. **`strategic-commitment.md` "What is assumed away".** A single blanket label — "The
   first point is the paper's; the rest is **[our reading]**" — covers three bullets, two
   of which now contain direct quotations from p. 502. A blanket label over quoted
   material is the wrong way round: it marks as ours sentences that are the author's. Per-
   bullet marking would be clearer, and would have surfaced N9.

A tag in the wrong place implies the untagged neighbours were verified as the author's, so
these are worth a few minutes even though none of them is factually wrong.

## AGENTS.md — verdict on the two new rules

**Rule on marking inference (§3): adequate, with one gap.** It names both tag forms, says
where they apply (concept pages and the overview as much as source pages) and gives the
reason (B3 will otherwise lift the sentence onto a slide as the author's). What it does
not define is **scope** — how much text a tag governs. The three weak placements above are
all scope questions, and `strategic-commitment.md`'s blanket label is the predictable
result. Add one clause: a tag governs the sentence or bullet it opens; a passage longer
than that needs a 🔎 box or a tag per bullet.

**Rule on self-contradicting sources (§3): adequate as written.** "State our reading, then
note the contradiction and why we resolved it that way. Never silently overwrite the
source." That is exactly what §7.2 and §4.1 now do, and it generalises beyond this paper.

**One inconsistency between the log and the schema.** `log.md`'s F4 row records the
workflow change as "quotation marks now require a verbatim match, checked at A3, not a
plausible gist" — but no such rule was added to AGENTS.md §3, which still says only that
claims need citations. Of the five workflow changes the log claims, that is the one with
no corresponding schema text. Either add the rule to §3 or stop claiming it in the log;
the reflection table for the course assignment is written from that log.

---

## The two carried-forward gaps — both now closed

### Figures 1 and 3, curve-to-curve

This was the last unverified claim about the paper's figures, and it now checks out. I
rendered p. 498 and p. 501 at 150 dpi and compared the plotted curves against the verified
expressions evaluated with mpmath ($a-c=1$):

**Fig. 1 ($\theta=0$).** Computed: $s_1^*$ starts at exactly $1/3$ at $\gamma=0$, falls to a
minimum of 0.2740 at $\gamma=0.5320$, then rises steeply to **0.6562** at $\gamma_{\max}$;
$s_2^*$ falls monotonically from $1/3$ to **0** at $\gamma_{\max}$. The printed figure has
its y-axis labelled **0.66** at the top, the bold curve reaching the top-right corner, and
the dashed curve plunging to the axis at the right-hand edge — matching both endpoints to
the precision the axis allows. Three things follow. The wiki's "minimum near
$\gamma\approx0.532$", "the follower's falls throughout" and "the gap widens" are all
confirmed against the plot, not just the caption. The paper's own remark that "the maximum
equilibrium level of the leader's CSR investment is reached for $\gamma=\gamma_{\max}$"
(p. 498) is consistent. And **Fig. 1 independently corroborates the A4 $\gamma_{\max}$
finding**: the follower's curve visibly hits zero exactly at the right edge, which is the
interiority bound the 🔎 box identifies. The figure has been showing it all along.

One nuance the wiki may want: at $\gamma=0$ the two curves *coincide* at $1/3$ — the gap
formula is stated for $0<\gamma\le\gamma_{\max}$, so this is consistent, but "the leader
always invests more" (§6.1 heading) is true only for $\gamma>0$.

**Fig. 3 ($\theta=0.21$).** Computed: $s_1^*$ from 0.3333 down to 0.2072 at
$\gamma\approx0.772$ then up to 0.2100; $s_2^*$ from 0.3567 down to 0.2751 at
$\gamma\approx0.716$ then up to 0.2789. The printed figure shows exactly this: a 0.4 axis
top, both curves shallow-U with a visible upturn near $\gamma_{\max}$, the dashed curve
above the solid one throughout and starting slightly higher. **Follower above leader,
both U-shaped — confirmed curve-to-curve**, which is what `numbers.md` and paper page §7.3
assert.

(Fig. 2 was checked in round 1 against its printed region labels, and its two curves match
the computed frontiers qualitatively — both hug the bottom of the plot, both rise only
near the right-hand edge, dashed above bold throughout. I did not measure values off the
Fig. 2 curves, so that comparison stays qualitative; the frontier *values* are verified
against the equations, not against the plot.)

### eq. (1) and the general demand system, visually

Closed — see F3 above. Pages 493 and 494 are now rendered and read; the indexing is as the
corrected wiki states. Every equation in the register has now had a visual check against
the printed page.

### Still not verified after round 2

1. **Third-party quotations** (Burke & Logsdon, the Economist, Tetrault Sirsly & Lamertz)
   remain checked only as Kopel reproduces them; the originals are not in `raw/`. The paper
   page's "Remaining gaps" now records this, which is the right disposition.
2. **A5 lint checks** — links, LaTeX compilation, index/disk agreement — are still not my
   scope and have not been run. N1 is the kind of thing a lint pass should have caught, and
   is an argument for running A5 before A6.
3. **`log.md`, `需求摘要.md` and the verification scripts** were not audited; I read the
   log only to check whether F28 had been recorded.

## Round-2 bottom line

The writer fixed the substance, not just the wording: the two mathematical claims added in
response to this review (the K-sub quotient and the homogeneity argument) are both correct
under independent check, the marking convention is now a schema rule rather than a habit,
and the two self-contradictions in the paper are now handled openly instead of silently.

What is left, in priority order: **N3** (F9's caveat missing from `csr-spillovers.md` —
the only residue that could still put an overstated claim on a slide), **N1** (the broken
`numbers.md` table, which B10 parses), **N2** (a new wrong page number), then N4–N10, the
three tag placements, the AGENTS.md scope clause and the log/schema mismatch, all
cosmetic or procedural. F28 remains an optional speaker-note suggestion.

**A3 is done.** Two rounds is the §8a maximum; the residue above is for the human at A6,
together with an A5 lint pass, which should run before sign-off and would have caught N1.
