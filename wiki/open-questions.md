# Open questions

Discussion material for the seminar. The audience is graduate students and the
advisor, and the stated purpose of the talk is **discussion, not transmission** —
so these are the points designed to be argued about, not settled.

Each question states what the paper does, why it is questionable, and what a
good answer would look like. Questions marked ★ are the strongest candidates for
the discussion slide.

---

## ★ Q1. Is $\theta_1 = 0$ doing too much work?

**What the paper does.** Sets the leader's spillover to zero and the follower's
to $\theta$, arguing that $\theta_1 \le \theta_2$ is "sensible" because the
follower can free-ride (p. 494). See [[csr-spillovers]].

**Why it is questionable.** The paper's question is *who benefits from whom*. An
assumption that the leader benefits from the follower by exactly zero is not
neutral with respect to that question. A follower who improves on the leader's
CSR — p. 494 says "if the CSR follower copies **and improves** the green
attributes of the CSR leading firm, it can raise the demand for its product
without having to bear the full development costs" — would create a reverse
spillover the model rules out by construction.

**What would settle it.** Re-solve with $0 < \theta_1 < \theta_2$ and check
whether the first-mover-advantage frontier moves materially. This is tractable
with the verified sympy model in `scripts/`. **Feasible to do before the talk if
there is time.**

## ★ Q2. Would anyone choose to be the leader?

**What the paper does.** Takes the leader–follower order as exogenous (p. 502).

**Why it is questionable.** The paper's own conclusion is that leading is usually
worse than following. In a game where timing is chosen, both firms would then
want to wait — a war of attrition rather than a Stackelberg game. The model
cannot represent the thing its conclusion implies.

**What would settle it.** Kopel & Löffler (2012) endogenise timing; the paper
cites it as an extension. Worth asking the room what the equilibrium of the
timing game would look like given the frontier in
[[first-mover-advantage]].

## ★ Q3. Is a result about an unmeasurable parameter actionable?

**What the paper does, and what we computed.** The paper shows an FMA requires
spillovers to be "in fact very low" (p. 491) and concedes the answer "depends on
factors which are quite hard to measure accurately" (p. 491). It gives no
number; **[own calculation]** the frontier is $\theta < 0.0015$ at $\gamma = 0.3$
(`checks/a4_report.md` §3).

**Why it is questionable.** If $\theta$ cannot be observed and the admissible
region is that narrow, the model's practical content reduces to a prior: *assume
no first-mover advantage*. That may be the right prior, but it is a different
kind of claim from a comparative-static result.

**What would settle it.** Is there an observable proxy for $\theta$ — patent
protection, brand concentration, speed of imitation in the industry? See
[[appropriability]].

## Q4. Does the U-shape explain the mixed empirical literature?

**What the paper does.** Finds the competition–CSR relation is ambiguous and
asymmetric between leader and follower (p. 492), against a literature where
Bagnoli & Watts (2003) and Fisman et al. (2006) find opposite signs.

Note both are **theoretical** papers — Fisman et al. "use a signaling model"
(p. 492). The conflict is between models, not between datasets.

**Why it is interesting. [our reading]** If the true relation is U-shaped *and*
differs by firm role, a linear empirical specification recovers whichever sign
the sample spans. That would reconcile the conflicting findings without either
being wrong. This inference is ours, not Kopel's.

**What would settle it.** Has anyone tested for a U-shape in CSR intensity against
competition, splitting by first-mover status? Sacco & Schmutzler (2011) test a
U-shape for investment generally — cited on p. 498 but not for CSR.

## Q5. How much of the result survives the $\gamma < 0.810736$ bound?

**What the paper does.** Restricts attention to $\gamma < \gamma_{\max} = 0.810736$
for interiority (p. 495), and claims the leader's advantage grows as products
become "increasingly homogeneous" (p. 499).

**Why it is questionable.** A4 identified $\gamma_{\max}$ as the point where the
**follower's output and CSR hit zero** at $\theta = 0$ — the duopoly collapses to
a monopoly. So the strongest version of the leader-advantage claim is evaluated
right at the boundary where the follower exits. See [[competition-intensity]].

**What would settle it.** Is the comparative static economically meaningful near
the bound, or is it an artefact of pushing a duopoly model to the edge of its
own validity?

## Q6. Linear demand, quadratic cost — how much depends on it?

**What the paper does.** Uses a linear demand system derived from a
quality-enhanced quadratic utility function (footnote 3, p. 493) and quadratic
CSR cost $s_i^2$ (Garella & Petrakis 2008).

**Why it is questionable.** The U-shape comes from the balance of a markup effect
and a demand effect. Both are functional-form dependent. The paper notes as an
extension (p. 502) the case where CSR changes the demand *slope* rather than the
intercept — which would change the demand effect directly.

**What would settle it.** Numerical robustness check with a different cost
exponent. Cheap to run with the verified model.

## Q7. Only positive spillovers

Footnote 4 (p. 494) notes negative spillovers exist — an industry-wide scandal, a
perceived CSR failure damaging a rival (Klein & Dawar 2004; Bertels & Peloza
2008) — but excludes them. **[our reading, untested]** With $\theta < 0$ the
leader's CSR would *hurt* the follower, which might strengthen rather than
destroy the advantage — but $\theta<0$ is outside the model's stated range
$\theta\in[0,1]$, so the equilibrium expressions are not validated there and this
is speculation until someone re-solves it.

## Q8. Is rival exclusion a prediction or an artefact? *(cross-source)*

**What three papers do.** [[Kopel2021-CSR]], [[Chen2021-OptimalCSR]] and
[[BarcenaRuizSagasta2021-CrossOwnershipCSR]] each contain a corner where one
firm's output falls to zero — treated respectively as a technical bound, a
result, and a deliberate strategy. See [[rival-exclusion]].

**Why it is questionable.** All three use linear demand, no fixed costs and no
entry. Exclusion may be what the functional form does at the edge rather than
what CSR competition does.

**What would settle it.** Does the corner survive non-linear demand or free
entry? None of the three tests it.

## Q9. Is $\delta^{**} \approx 0.531$ the same object as Kopel's $\gamma \approx 0.532$? *(cross-source, low priority)*

[[HiroseMatsumura2022-CommonOwnershipECSR]]'s sign-change threshold sits at
$\delta^{**} \approx 0.531$; Kopel's turning point for $s_1^*$ at $\theta = 0$
is $\gamma \approx 0.531963$. Both models are differentiated Bertrand duopolies
on the Dixit demand family with a two-stage commitment, so a shared root is
conceivable — but the two parameters are **not the same object** and nobody has
checked. **Do not mention this in the talk unless it is actually derived.**
Listed only so the coincidence is on the record rather than rediscovered as a
"finding".

---

## Answered / closed

*(none yet — entries move here with the answer and its source once resolved)*

## Links

[[Kopel2021-CSR]] · [[first-mover-advantage]] · [[csr-spillovers]] ·
[[appropriability]] · [[competition-intensity]] · [[strategic-commitment]]
