# Bárcena-Ruiz & Sagasta (2021) — Cross-ownership and corporate social responsibility

- **Source**: `raw/papers/BarcenaRuizSagasta2021-CrossOwnershipCSR.pdf`
- **Citation**: Bárcena-Ruiz, J.C. & Sagasta, A. (2021). Cross-ownership and corporate social responsibility. *The Manchester School*, 89(4), 367–384. doi:10.1111/manc.12363
- **Ingest depth**: ⚠️ **LIGHT** — no A4 verification, no A3 review. Lower assurance than [[Kopel2021-CSR]].
- **Links**: [[rival-exclusion]] · [[csr-modelling-choices]] · [[strategic-commitment]] · [[appropriability]]

## Model (§2, pp. 370–371)

Cournot duopoly, homogeneous good, inverse demand $p = a - q_1 - q_2$, common marginal cost $c$.

**Ownership.** Shareholder $A$ fully owns firm 1 *and* holds a minority stake $\beta < 1/2$ in firm 2 (the **controlling shareholder**). Shareholder $B$ holds the remaining $(1-\beta)$ of firm 2. Incomes:

$$\pi_A = \pi_1 + \beta\pi_2, \qquad \pi_B = (1-\beta)\pi_2$$

**CSR.** Each shareholder publicly commits a weight $\theta_i \in [0,1]$ on consumer surplus:

$$V_A = \pi_1 + \beta\pi_2 + \theta_1 CS, \qquad V_B = (1-\beta)\pi_2 + \theta_2 CS$$

$\theta_i$ is **endogenous and strategic** — chosen to maximise the shareholder's income, not out of altruism.

**Three stages** (p. 372): (1) binary engage / not engage in CSR; (2) those who engage choose $\theta_i$; (3) firms choose outputs. Four subgames: NN, YY, NY, YN.

## Results

| # | Finding | Where |
|---|---|---|
| — | NN benchmark: $q_1^{NN} < q_2^{NN}$ — cross-ownership alone already makes the controlling shareholder's own firm less aggressive | eq. (6), p. 372 |
| Lemma 1 | with both doing CSR and $\beta < (3-\sqrt5)/2 \approx 0.3819$: $\theta_1^{YY} < \theta_2^{YY}$, and $\partial\theta_1^{YY}/\partial\beta < 0$ while $\partial\theta_2^{YY}/\partial\beta > 0$ | p. 374 |
| Lemma 2 | **for $\beta \ge (3-\sqrt5)/2$: $q_1^{YY} = 0$ and $\pi_1^{YY} = 0$ — firm 1 is driven out and firm 2 becomes a monopolist** | p. 375 |
| Prop. 1 | the strategic use of CSR depends critically on $\beta$; above the threshold the CSR level *decreases* in $\beta$ | p. 375 |
| — | welfare is lowest when neither firm does CSR and highest when both do; the government should encourage CSR | p. 370 |

A counterintuitive result the authors highlight (p. 370): with high cross-ownership the government may **prefer a monopoly to a duopoly**.

## Relation to [[Kopel2021-CSR]]

**A third independent route to the same exclusion phenomenon.** Kopel's
$\gamma_{\max}$ is where the follower's output and CSR hit zero; Chen's Model CN
crowds firm 2 out; here firm 1 is driven out at $\beta \ge 0.3819$. Three
different models, three different driving parameters, same corner. See
[[rival-exclusion]] — this is the clearest cross-source pattern the wiki has.

**CSR is strategic in both, but the lever differs.** Kopel's leader uses CSR to
deter; here shareholder $B$ uses firm 2's CSR level "to lead firm 1 not to
produce" (p. 375). In both, CSR is a commitment that shapes the rival's output,
not a preference.

> ⚠️ **Symbol clash — important.** Bárcena-Ruiz's $\theta_i$ is a **CSR level**
> (weight on consumer surplus). Kopel's $\theta$ is a **spillover rate**. Same
> letter, unrelated meaning. Chen's $\beta_i$ is also a CSR level while
> Bárcena-Ruiz's $\beta$ is a cross-ownership share. Any slide mixing sources
> must say which paper's notation it is using. Recorded in [[glossary]].
