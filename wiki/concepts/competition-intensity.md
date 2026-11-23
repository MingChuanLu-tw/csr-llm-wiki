# Competition intensity ($\gamma$)

**Sources so far**: [[Kopel2021-CSR]] (1 of 5 planned)

## Definition

$\gamma$ is the degree of product substitutability in the demand system
(eq. (1), p. 494). $\gamma = 0$: independent products. $\gamma \to 1$: perfect
substitutes. **Higher $\gamma$ = more intense competition** (p. 493).

This is *horizontal* differentiation. CSR, by contrast, enters as a *vertical*
shift in willingness to pay (p. 494) — the two are separate dimensions.

## The admissible range is bounded

The analysis requires $\gamma < \gamma_{\max} = 0.810736$ (p. 495). The paper says
only that this "guarantees that the equilibrium of the game is in the interior and
all second-order conditions are satisfied", without naming the binding condition.

> 🔎 **Identified in A4, not stated in the paper.** The binding condition is the
> follower's **interiority at $\theta = 0$**: at that point the leader's strategic
> over-investment drives $s_2^*$ and $x_2^*$ to zero simultaneously. Formally
> $\gamma_{\max}$ is the unique root in $(0,1)$ of the eq. (6) numerator at
> $\theta = 0$, equal to $0.8107358771$. Every second-order condition fails only at
> larger $\gamma$ (leader's at $0.830176$, follower's at $0.932526$).
> See `checks/a4_report.md` §2a.

**Consequence for interpretation — [our reading], following A4.** $\gamma_{\max}$ is not a technical nuisance —
it marks where the duopoly would collapse into a monopoly. The paper's claim that
the leader's advantage "can not only be sustained, but made even larger" as
products become homogeneous (p. 499) is therefore evaluated right against the edge
where the follower is squeezed out of the market.

## Three effects of competition on the incentive to invest

Kopel decomposes the incentive (pp. 498–499). This decomposition is the
explanatory core of the paper and should survive into the talk.

| Effect | Direction as $\gamma$ rises | Applies to |
|---|---|---|
| **Markup effect** | negative — prices fall toward marginal cost, so each unit of extra demand is worth less | both firms |
| **Demand effect** | positive — CSR shifts more demand when products are closer substitutes. The paper states this **for the no-spillover case**: $\partial(\partial x_i/\partial s_i)/\partial\gamma>0$ (p. 498) | both firms |
| **Strategic effect** | positive — committing to high CSR induces the rival to cut its CSR | **leader only** |

For the leader, the markup effect dominates at low $\gamma$ and the demand effect
at high $\gamma$, producing a **U-shape** (fn. 11, p. 498). For the follower the
paper gives $\partial(\partial\pi_2/\partial s_2)/\partial\gamma<0$ throughout
(fn. 12, p. 498), so investment falls monotonically when spillovers are low.
**[our reading]** Attributing that to the *absence* of a strategic effect is our
inference; the paper reports the sign without explaining it this way.

## The shape reverses with spillovers

Verified numerically in `checks/a4_report.md` §3:

| $\theta$ | $s_1^*$ (leader) | $s_2^*$ (follower) |
|---|---|---|
| 0 | U-shaped | decreasing |
| 0.15 | U-shaped | decreasing |
| **0.21** | **U-shaped** | **U-shaped** |
| 0.25 | decreasing | U-shaped |
| 0.5 | decreasing | U-shaped |
| 0.9 | decreasing | U-shaped |

The thresholds are $\theta = 0.202167$ (follower) and $\theta = 0.229499$
(leader) — see [[csr-spillovers]]. The narrow band between them is where both
curves are U-shaped; Fig. 3 plots that case.

> 🔎 **A3 caveat.** Footnote 15's criterion is the sign of the derivative
> *evaluated at $\gamma_{\max}$*, so it cannot detect an interior hump. A3 found
> the follower's curve already becomes non-monotone (down–up–down) between
> $\theta = 0.190$ and $0.1925$, below the stated 0.202167. The six rows above
> are each correct; "monotone throughout" below 0.202167 is not. See
> `checks/a3_report.md` F9.

At $\theta = 0$ the leader's turning point is $\gamma = 0.531963$ (verified:
$0.5319633163$).

## Why this matters

The relation between competition and CSR is **ambiguous and asymmetric**
(p. 492). This is Kopel's answer to a **theoretical** literature with conflicting
conclusions: Bagnoli & Watts (2003) find more competition lowers CSR; Fisman
et al. (2006) "use a signaling model" and conclude the opposite (p. 492). Both
are models, not empirical studies.

**[our reading]** If the true relation is U-shaped and differs by firm role, a
linear empirical specification would recover whichever sign the sample happens to
span. That inference is ours, not Kopel's. Good discussion material — see
[[open-questions]] Q4.

## Links

[[csr-spillovers]] · [[first-mover-advantage]] · [[strategic-commitment]] ·
[[Kopel2021-CSR]]
