# Hirose & Matsumura (2022) — Common ownership and environmental CSR

- **Source**: `raw/papers/HiroseMatsumura2022-CommonOwnershipECSR.pdf`
- **Citation**: Hirose, K. & Matsumura, T. (2022). Common ownership and environmental Corporate Social Responsibility. *Energy Economics*, 114, 106269. doi:10.1016/j.eneco.2022.106269
- **Ingest depth**: ⚠️ **LIGHT** — no A4 verification, no A3 review. Lower assurance than [[Kopel2021-CSR]].
- **Links**: [[strategic-commitment]] · [[competition-intensity]] · [[csr-modelling-choices]] · [[csr-spillovers]]

## Why this one matters here

**[our reading].** This is the closest structural match to [[Kopel2021-CSR]] of
the four light-ingest sources: price competition, differentiated products, and
CSR explicitly treated as "a commitment device to soften competition" (abstract,
p. 1). It is the paper against which Kopel's strategic-commitment story can be
stress-tested.

## Model (§2, p. 2)

All from §2, p. 2.

- Differentiated Bertrand duopoly from a quasi-linear quadratic utility (Dixit 1979) — the **same demand family as Kopel**.
- $\delta \in (0,1)$ is product substitutability; smaller $\delta$ = more differentiation. **Same direction as Kopel's $\gamma$.** Normalised $\alpha = \beta = 1$.
- Firm $i$ commits to an emissions cap $E_i$; output $q_i$ emits $h q_i$; abatement $x_i = \max\{0,\, h q_i - E_i\}$ at cost $k x_i^2/2$. **ECSR = a voluntary, binding cap.**
- $\lambda \in [0,1)$ is the **degree of common ownership**; firm $i$ maximises $\psi_i = \pi_i + \lambda \pi_j$.
- Two stages: caps $E_i$ simultaneously, then prices. Solved by backward induction.

## Results

| # | Finding | Where |
|---|---|---|
| Prop. 1 | $E^F(0,\delta) > E^F(1,\delta)$: emissions are lower with full common ownership; and $E^F$ is decreasing in $\lambda$ near $\lambda = 0$ and near $1$ | p. 3 |
| Prop. 2 | $E^F$ is **monotonically** decreasing in $\lambda$ iff $\delta < \delta^* \approx 0.862$ | p. 3 |
| Prop. 3 | equilibrium output $q^F$ is decreasing in $\lambda$ | p. 4 |
| Prop. 4 | abatement $x^F$ is **decreasing** in $\lambda$ when $\lambda$ is large; $(dx^F/d\lambda)\|_{\lambda=0} > 0$ iff $\delta > \delta^{**} \approx 0.531$ | p. 4 |

**The mechanism (p. 4)** is a commitment argument and reads like Kopel's: a
stricter cap raises the firm's marginal cost, which raises *both* firms' prices
through strategic interaction. When $\lambda$ is small, prices are far from the
joint-profit optimum, so the strategic value of committing is **large**. When
$\lambda$ is large, firms already reach near-cooperative prices without
committing, so they avoid costly commitments. Hence a **moderate** degree of
common ownership can stimulate abatement while a large degree dampens it.

Welfare (Fig. 4, p. 5) is inverted-U in $\lambda$ when damage is large.

## Relation to [[Kopel2021-CSR]]

**Supports the commitment mechanism, from a different direction.** Kopel's leader
over-invests because commitment deters the follower; here *both* firms
over-commit because commitment softens price competition. Both rest on the same
engine: an observable, binding, pre-market commitment that moves the rival's
price. See [[strategic-commitment]].

**Both find the structural parameter's effect is non-monotone.** Kopel: the
leader's CSR is U-shaped in $\gamma$. Hirose & Matsumura: abatement is
non-monotone in $\lambda$, and whether emissions fall monotonically depends on
$\delta$. Neither paper supports a linear story.

> 🔎 **Numerical curiosity, unexplained — [our reading].** Hirose & Matsumura's
> $\delta^{**} \approx 0.531$ (where the sign of $dx^F/d\lambda$ at $\lambda=0$
> flips) is strikingly close to Kopel's $\gamma \approx 0.531963$ (where the
> leader's CSR turns from falling to rising). Both are Bertrand duopolies on the
> Dixit demand family with a two-stage commitment, so a shared root is not
> impossible — **but we have not checked whether these are the same quantity, and
> the parameters are not the same object.** Do **not** present this as a result.
> Logged as a candidate question in [[open-questions]].
