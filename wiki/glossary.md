# Symbol glossary

One canonical meaning per symbol across the whole wiki. When a new source uses a
different letter for the same object, record the mapping in the last column
rather than changing the canonical symbol.

| Symbol | Meaning | Range | First seen | Other sources' notation |
|---|---|---|---|---|
| $a$ | reservation price | $a > c$ | [[Kopel2021-CSR]] p. 493 | — |
| $c$ | constant unit production cost | $\ge 0$ | [[Kopel2021-CSR]] p. 493 | — |
| $\gamma$ | product substitutability = [[competition-intensity]] | $[0,1)$, analysis needs $<0.810736$ | [[Kopel2021-CSR]] p. 493 | — |
| $\gamma_{\max}$ | upper bound for an interior equilibrium | $0.810736$ (p. 495); $0.8107358771$ (A4 recomputation) | [[Kopel2021-CSR]] p. 495 | — |
| $\theta_i$ | share of the **rival's** CSR benefit captured by firm $i$ = [[csr-spillovers]] | $[0,1]$ | [[Kopel2021-CSR]] p. 493–494 | — |
| $\theta$ | shorthand for $\theta_2$, given $\theta_1 = 0$ | $[0,1]$ | [[Kopel2021-CSR]] eq. (1), p. 494 | — |
| $s_i$ | CSR investment level of firm $i$ | $\ge 0$ | [[Kopel2021-CSR]] p. 493 | — |
| $s_i^2$ | CSR investment cost | — | [[Kopel2021-CSR]] p. 493 | — |
| $x_i$ | quantity of firm $i$'s product | $\ge 0$ | [[Kopel2021-CSR]] p. 493 | — |
| $p_i$ | price of firm $i$'s product | — | [[Kopel2021-CSR]] p. 493 | — |
| $\pi_i$ | profit of firm $i$, net of CSR cost | — | [[Kopel2021-CSR]] p. 495 | — |
| $N$ | numerator polynomial in eq. (6) | — | [[Kopel2021-CSR]] p. 496 | — |
| $D$ | shared denominator of eq. (5) and (6) | — | A4 notation, not in the paper | — |

## ⚠️ Symbol clashes across sources

The canonical column above is **Kopel's** notation. Other sources reuse the same
letters for unrelated objects. A slide that draws on more than one source must
name the source with the symbol.

| Symbol | In [[Kopel2021-CSR]] | Elsewhere |
|---|---|---|
| $\theta$ | **spillover rate** | **CSR level** (weight on consumer surplus) in [[BarcenaRuizSagasta2021-CrossOwnershipCSR]] |
| $\beta$ | not used | **CSR level** in [[Chen2021-OptimalCSR]]; **cross-ownership share** in [[BarcenaRuizSagasta2021-CrossOwnershipCSR]]; demand slope in [[HiroseMatsumura2022-CommonOwnershipECSR]] (normalised to 1) |
| $\gamma$ | substitutability | $\delta$ in [[HiroseMatsumura2022-CommonOwnershipECSR]], same direction (larger = closer substitutes) |
| $s_i$ | CSR investment | $\beta_i$ (Chen), $E_i$ cap (Hirose & Matsumura), $\theta_i$ (Bárcena-Ruiz), $h_i$ (Xing & Lee) — but these are **not the same object**, see [[csr-modelling-choices]] |
| $c$ | unit cost | same in all five |

Symbols used only in one light-ingest source, listed so they are not mistaken
for canonical ones: $e$ (market sensitivity to CSR, Chen); $\lambda$ (common
ownership) and $\delta^*, \delta^{**}$ (Hirose & Matsumura); $h_i$ (ECSR degree),
$y_i$ (R&D effort), $d$ (marginal damage), $t$ (emissions tax) (Xing & Lee).

## Index conventions

- Firm **1** is always the CSR **leader** (moves first).
- Firm **2** is always the CSR **follower**.
- A star ($s_1^*$, $\pi_2^*$, …) denotes an equilibrium value of the full
  three-stage game.
- $D$ is our label for the common denominator; the paper writes it out in full
  each time. Introduced in `checks/a4_report.md` for readability.

## Terms

| Term | Meaning here |
|---|---|
| **FMA** | first-mover advantage, defined as $\pi_1^* > \pi_2^*$. See [[first-mover-advantage]] |
| **SMA** | second-mover advantage, $\pi_1^* < \pi_2^*$ |
| **Appropriability** | ability to capture one's own CSR benefit; inverse of $\theta$. See [[appropriability]] |
| **Divergent CSR** | CSR used to differentiate from rivals (Misani 2010) |
| **Convergent CSR** | CSR used to defend shared industry reputation (Misani 2010) |
| **Vertical differentiation** | quality-like shift in willingness to pay — how CSR enters |
| **Horizontal differentiation** | taste-based product distance — what $\gamma$ measures |
