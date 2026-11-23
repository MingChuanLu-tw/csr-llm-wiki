# What "CSR" is, formally: five papers, five different objects

**Sources so far**: all 5 — [[Kopel2021-CSR]] · [[Chen2021-OptimalCSR]] · [[HiroseMatsumura2022-CommonOwnershipECSR]] · [[BarcenaRuizSagasta2021-CrossOwnershipCSR]] · [[XingLee2023-EnvironmentalRD]]

> **[our reading].** A cross-source observation. No single paper makes it.

## The five formalisations

All five papers say they model "corporate social responsibility" in a duopoly.
They model five different things.

| Source | CSR is… | Enters through | Costed how | Chosen by |
|---|---|---|---|---|
| [[Kopel2021-CSR]] (p. 494) | an investment $s_i$ that raises willingness to pay | the **demand intercept** | explicit $s_i^2$ | the firm, sequentially |
| [[Chen2021-OptimalCSR]] (p. 178) | a level $\beta_i \in [0,1]$ | **both** demand ($\beta_i e$) and the objective ($+\beta_i CS$) | no separate cost | the firm, simultaneously |
| [[HiroseMatsumura2022-CommonOwnershipECSR]] (p. 2) | a binding **emissions cap** $E_i$ | the **cost** side, via abatement $x_i$ | $k x_i^2/2$ | the firm, before prices |
| [[BarcenaRuizSagasta2021-CrossOwnershipCSR]] (p. 371) | a weight $\theta_i \in [0,1]$ on consumer surplus | the **objective only** | no cost | the *shareholder* |
| [[XingLee2023-EnvironmentalRD]] (p. 2686) | a degree $h_i \ge 0$ of concern for damage | the **manager's objective** ($-h_i D$) | no direct cost | the *owner*, delegating |

## Why the difference matters

**It decides what the result can mean.** Where CSR enters determines what the
model can say:

- **Demand-side** (Kopel, Chen): CSR is a *differentiation* instrument. The
  question becomes whether the benefit is appropriable — which is exactly
  Kopel's $\theta$ and [[appropriability]].
- **Cost-side** (Hirose & Matsumura): CSR raises marginal cost, which raises
  *both* firms' prices. The question becomes how much softening of competition
  it buys. There is no appropriability problem at all — the commitment works
  through price, not through a benefit the rival could copy.
- **Objective-side** (Bárcena-Ruiz, Xing & Lee): CSR is a *delegation* device.
  The question becomes who sets the weight and why — and the answer in both is
  that it is chosen strategically, not out of social concern.

**A result in one category does not transfer to another.** Kopel's conclusion —
unilateral CSR leadership rarely pays — is a statement about *appropriable
demand shifts*. It does not follow that an emissions cap fails to pay, because
that mechanism does not depend on keeping a benefit away from the rival.

**[our reading]** This is the single most useful thing about having five sources
rather than one. With Kopel alone, "CSR" looks like one object with one logic.
It isn't.

## Where they do converge

Despite the differences, four of the five reach a version of the same negative
conclusion about unilateral CSR:

| Source | Unilateral CSR… |
|---|---|
| Kopel | rarely yields a first-mover advantage (Lemma 2, p. 500) |
| Chen | in Model CN drives the rival out; CSR level falls as the market gets more CSR-sensitive (Prop. 1, p. 179) |
| Bárcena-Ruiz | high cross-ownership *discourages* the controlling shareholder from CSR (p. 370) |
| Xing & Lee | **is not adopted at all** without cooperation: $h^{NN} = 0$ (Prop. 1, p. 2688) |

Hirose & Matsumura is the partial exception: there, moderate common ownership
*stimulates* abatement (Prop. 4, p. 4) — because the mechanism is cost-side and
mutual, not a race to differentiate.

**Why this is the right shape for the talk.** The convergence is not "CSR
doesn't pay". It is narrower and more defensible: **in these models, CSR pays
the firm that does it only when something stops the rival from getting the
benefit — and in most specifications nothing does.**

## Symbol clashes this creates

See [[glossary]]. The worst: $\theta$ is a *spillover rate* in Kopel (p. 494)
and a *CSR level* in Bárcena-Ruiz (p. 371); $\beta$ is a *CSR level* in Chen
(p. 178) and a *cross-ownership share* in Bárcena-Ruiz (p. 371). Any slide
drawing on more than one source must name the source with the symbol.

## Links

[[appropriability]] · [[csr-spillovers]] · [[strategic-commitment]] ·
[[rival-exclusion]] · [[glossary]]
