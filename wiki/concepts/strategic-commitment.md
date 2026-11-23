# Strategic commitment and over-investment

**Sources so far**: [[Kopel2021-CSR]] (1 of 5 planned)

## The idea

In Kopel (2021) the leader chooses $s_1$ in stage 1, "this level is observed by
the CSR follower", the follower chooses $s_2$ in stage 2, and prices are set
simultaneously in stage 3 (p. 495). Because $s_1$ is fixed before the follower
decides, the leader can use it to shape the follower's behaviour — the paper
calls it "a sort of commitment device" (p. 497).

**[our reading]** Describing the commitment as *observed and irreversible* is
standard game-theoretic vocabulary, not the paper's wording; the paper gets
observability from the stage structure and never discusses reversibility.

Remove the sequencing and the mechanism disappears: with simultaneous investment
the leader has no way to influence $s_2$. This is exactly what separates Kopel
from Arya & Mittendorf (2013), where all investments are simultaneous (p. 493).

## Over-investment

The leader invests **more than it would** if it only cared about the direct
return. Kopel's phrasing (p. 499): there is an incentive for the leader to
"overinvest" in CSR activities, which leads to $s_1 > s_2$.

Decomposition of the leader's incentive:

$$
\underbrace{\frac{\partial\pi_1}{\partial s_1}}_{\text{direct}}
\;+\;
\underbrace{\frac{\partial\pi_1}{\partial s_2}\cdot\frac{\partial s_2}{\partial s_1}}_{\text{strategic effect}}
$$

Footnote 14 (p. 499) states only that the product is positive:
$\frac{\partial\pi_1}{\partial s_2}\frac{\partial s_2}{\partial s_1} > 0$.

**[our reading]** The reason is that both factors are negative: more follower CSR
hurts the leader ($\partial\pi_1/\partial s_2 < 0$), and more leader CSR makes
the follower retreat ($\partial s_2/\partial s_1 < 0$, fn. 13). Two negatives
multiply to a positive push toward higher $s_1$. The paper gives the product's
sign without decomposing it.

## The strategic effect is conditional

$\partial s_2/\partial s_1 < 0$ holds only while

$$
\theta < \frac{\gamma}{2-\gamma^2}
$$

(footnote 13, p. 499; verified in `checks/a4_report.md` §1). Above that threshold
CSR levels become strategic **complements** and the sign of the strategic effect
flips — the commitment stops working as a deterrent. See [[csr-spillovers]].

**[our reading]** So the leader's advantage rests on a chain with three links,
each of which can break:

1. The commitment must be **observable** — built into the stage structure (p. 495).
2. The commitment must hold once made — the model gives the leader no chance to
   revise $s_1$, but does not discuss this.
3. The benefit must be **appropriable** enough that CSR levels stay strategic
   substitutes, i.e. $\theta < \gamma/(2-\gamma^2)$ — otherwise the follower
   answers the leader's investment by raising its own instead of retreating.
   See [[appropriability]].

> **Terminology.** "Free-riding" in this wiki means the *low*-$\theta$ behaviour
> the paper describes: the follower benefits from the leader's CSR and therefore
> invests less itself (p. 496). It does **not** name the high-$\theta$ regime,
> where the follower *increases* its CSR "to counterbalance" the leader's
> withdrawal (p. 496). Those are opposite responses and should not share a word.

**But the first-mover advantage dies long before link 3 breaks.** Putting the
wiki's own registered numbers side by side (see [[numbers]], "Three thresholds"):
at $\gamma = 0.3$ the leader stops out-earning the follower at
$\theta \approx 0.0015$, stops out-investing it at $\theta \approx 0.0169$, and
the substitutes→complements switch does not arrive until
$\theta \approx 0.157$ — about **100× later**. At the moment the FMA dies the
commitment is still working exactly as described above: CSR levels are still
strategic substitutes and the follower still retreats.

So link 3 is a **later, separate regime change**, not the cause of the FMA's
failure. The leader keeps deterring, keeps out-investing, and still loses on
profit. For what does kill the FMA at those minute $\theta$ values, see
[[csr-spillovers]], "Why spillovers destroy the first-mover advantage".

The three-link framing is ours; the paper argues only the third.

## Interaction with competition

The strategic effect strengthens as products become closer substitutes (p. 499):
"a higher degree of competition makes the strategic effect even more pronounced,
leading to an increase in the difference between the CSR engagements". This is why
the leader's profit advantage *widens* with $\gamma$ at $\theta = 0$ — but see the
caveat about $\gamma_{\max}$ in [[competition-intensity]].

## What is assumed away

- **The order of moves is exogenous.** Kopel states it: "in my paper the
  leader–follower structure is exogenously given" (p. 502). **[our reading]**
  Nobody chooses to be the leader, so the model cannot price the option of moving
  first.
- **No cost advantage from moving first.** Both firms face the same cost $s_i^2$
  (p. 493). **[our reading]** The leader's only edge is strategic, never a
  learning or scale effect.
- **One shot — but not "static".** The game is multi-stage; footnote 2 (p. 492)
  explicitly calls it a "dynamic (multi-stage) setting like the present paper".
  What it lacks is repeated interaction across periods: Kopel notes that "most
  existing work is done in static environments" and lists dynamic CSR as an
  extension (p. 502). **[our reading]** So the right caveat is no repeated play,
  no learning and no consumer memory — not that the model is static.

Endogenous timing is listed by Kopel as an extension (Kopel & Löffler 2012,
p. 502). See [[open-questions]] Q2.

## Links

[[first-mover-advantage]] · [[csr-spillovers]] · [[appropriability]] ·
[[competition-intensity]] · [[Kopel2021-CSR]]
