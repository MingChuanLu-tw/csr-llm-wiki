# CSR spillovers ($\theta$)

**Sources so far**: [[Kopel2021-CSR]] (1 of 5 planned)

## Definition

$\theta_i \in [0,1]$ is the share of the **rival's** CSR benefit captured by firm
$i$ — the spillover *into* firm $i$, not out of it. Read the index off the
general demand system (p. 493): $\theta_1$ multiplies $s_2$ inside $p_1$.

In the specification Kopel actually uses, $\theta_1 = 0$ and $\theta_2 = \theta$,
so $\theta$ is the share of the **leader's** CSR that spills to the **follower**
(eq. (1), p. 494):

$$
p_2 = a + (s_2 + \theta s_1) - x_2 - \gamma x_1
$$

$\theta = 0$: CSR is fully proprietary. $\theta = 1$: the rival captures the
leader's CSR benefit in full.

Economically $\theta$ is the inverse of [[appropriability]].

## The asymmetry is assumed, not derived

Kopel sets $\theta_1 = 0$ and $\theta_2 = \theta$ (p. 494). The argument given is
that in a leader–follower setting "it seems plausible to assume that
$\theta_1 \le \theta_2$, because the CSR follower can free ride on the CSR efforts
of the leader."

> ⚠️ This is a modelling choice. It means the leader receives **nothing** from the
> follower's later CSR, while the follower receives $\theta$ of the leader's. Since
> the paper's question is precisely *who benefits from whom*, the assumption does
> part of the work of the answer. See [[open-questions]] Q1.

Note also that only **positive** spillovers are studied. Footnote 4 (p. 494)
acknowledges negative spillovers exist — an oil spill harms a whole industry; a
perceived CSR failure can damage a competitor (Klein & Dawar 2004) — but excludes
them.

## Why spillovers destroy the first-mover advantage

Spillovers act in opposite directions on the two firms (p. 499, §5.2):

$$
\frac{\partial}{\partial\theta}\!\left(\frac{\partial\pi_1}{\partial s_1}\right) < 0
\quad\text{(leader's incentive falls)}, \qquad
\frac{\partial}{\partial\theta}\!\left(\frac{\partial\pi_2}{\partial s_2}\right) > 0
\quad\text{(follower's incentive rises)}
$$

**[our reading]** So $\theta$ is not a neutral leak — it is a transfer of
incentive, and that is why the [[first-mover-advantage]] region collapses so fast
in $\theta$. The two derivative signs above are the paper's; the "transfer"
framing is ours.

## The strategic-substitutes / complements switch

The hinge of the whole model. From the follower's reaction function eq. (4),
verified symbolically in `checks/a4_report.md` §1:

$$
\frac{ds_2}{ds_1} = \frac{(2-\gamma^2)\big((2-\gamma^2)\theta-\gamma\big)}{12-20\gamma^2+8\gamma^4-\gamma^6}
\qquad\Longrightarrow\qquad
\frac{ds_2}{ds_1} < 0 \iff \theta < \frac{\gamma}{2-\gamma^2}
$$

The denominator is positive throughout the admissible range, so the sign is
carried by $(2-\gamma^2)\theta-\gamma$. (Sign corrected after A3 F2.)

| Regime | Condition | Behaviour |
|---|---|---|
| Strategic **substitutes** | $\theta < \dfrac{\gamma}{2-\gamma^2}$ | the leader invests more → the follower retreats and free-rides |
| Strategic **complements** | $\theta > \dfrac{\gamma}{2-\gamma^2}$ | the leader's incentive "decreases and, therefore, the follower has to increase its own CSR activities to counterbalance this effect" (p. 496) |

The labels "substitutes / complements" are standard terminology and are ours; the
paper states only the threshold. **[our reading]**

A related condition at the price stage: the leader's CSR **raises the follower's
price** when $\theta > \gamma/(2-\gamma^2)$ (p. 495) — the same threshold.

## Threshold values

Two numerical thresholds govern the shape of investment in competition
(Lemma 3, p. 501; all reproduced in `checks/a4_report.md` §2):

| Threshold | Governs |
|---|---|
| $\theta = 0.202167$ | below it, $\partial s_2^*/\partial\gamma < 0$ **at the endpoint** $\gamma_{\max}$ |
| $\theta = 0.229499$ | above it, $\partial s_1^*/\partial\gamma < 0$ **at the endpoint** $\gamma_{\max}$ |

Both are **endpoint criteria** (fn. 15, p. 501), not statements of monotonicity
over the whole interval. The follower's curve already develops an interior hump
from about $\theta = 0.190$. See the 🔎 A3 caveat in [[competition-intensity]].

Between them, **both firms' investments are U-shaped** — the roles look
qualitatively identical. Fig. 3 ($\theta = 0.21$) plots exactly this band.

## Convergence as an endogenous force

Kopel adds a mechanism outside the model, and the direction matters: the leader
is the **actor**, not the object. "Being aware of reputation spillovers, industry
leaders oftentimes pressure and support less socially responsible competitors to
imitate their CSR practices (Misani 2010; Vogel 2005)" (p. 491). The motive is on
p. 502: "due to the fear of negative reputation spillovers — the CSR leader might
find it appropriate to support the CSR follower".

Misani's terms (fn. 16, p. 502):

- **Divergent CSR** — differentiate from rivals.
- **Convergent CSR** — avoid shared risk, defend the industry's reputation.

**[our reading]** Convergent CSR raises $\theta$ endogenously, destroying the
leader's own advantage. The paper describes the behaviour and says it "makes it
impossible for the CSR leader to profit from its leadership" (p. 502) but does
not put it in terms of $\theta$. Kopel offers this as a candidate explanation for
the weak empirical link: "since all firms converge on their CSR practices,
empirical studies show no or a rather weak link between corporate social and
corporate financial performance" (p. 491).

## Links

[[appropriability]] · [[first-mover-advantage]] · [[competition-intensity]] ·
[[strategic-commitment]] · [[Kopel2021-CSR]]
