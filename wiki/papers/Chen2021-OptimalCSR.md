# Chen, Sun, Liu & Huo (2021) — The optimal level of CSR based on the duopoly model

- **Source**: `raw/papers/Chen2021-OptimalCSR.pdf`
- **Citation**: Chen, J., Sun, C., Liu, J. & Huo, Y. (2021). The optimal level of corporate social responsibility based on the duopoly model. *Managerial and Decision Economics*, 42(1), 177–184. doi:10.1002/mde.3222
- **Ingest depth**: ⚠️ **LIGHT** — read and summarised; **no A4 symbolic verification, no independent A3 review.** Claims here are at a lower assurance level than [[Kopel2021-CSR]]. Do not put an unverified number from this page on a slide without checking it.
- **Links**: [[csr-modelling-choices]] · [[rival-exclusion]] · [[competition-intensity]] · [[first-mover-advantage]]

## Model (§2, pp. 178)

Cournot duopoly, two stages: CSR level first, output second (Assumptions 1–2, p. 178).

- Inverse demand with CSR: $p_i = a + \beta_i e - q_i - q_j$, where $\beta_i \in [0,1]$ is firm $i$'s **CSR level** and $e > 0$ is the **market's sensitivity to CSR**.
- Firm utility $U_i = \pi_i + \beta_i CS$ — CSR enters the *objective*, weighted by the same $\beta_i$ that shifts demand.
- Profits $\pi_i = p_i q_i - c q_i$, with $a > c > 0$.

Three scenarios compared: **NN** (neither does CSR), **CN** (only firm 1), **CC** (both).

## Results

| Scenario | Key finding | Where |
|---|---|---|
| NN | benchmark $q_i = (a-c)/3$ | eq. (1), p. 179 |
| **CN** | **firm 2 is driven out: $q_2^{CN} = 0$, $\pi_2^{CN} = 0$** — "a monopoly can lead to a higher CSR level" | Lemma 1, p. 179 |
| CN | $\partial\beta^{CN}/\partial e < 0$ — optimal CSR **falls** as the market gets more CSR-sensitive | Prop. 1, p. 179 |
| CC | $\partial\beta^{CC}/\partial e > 0$ — optimal CSR **rises** with sensitivity | Prop. 2, p. 180 |
| CC | profits *decline* as $e$ rises: both firms raise CSR and neither gains share | p. 180 |

Thresholds in the comparisons (Prop. 3, p. 180): $e = 1.142(a-c)$ for CSR levels; $e = 0.085(a-c)$ and $0.125(a-c)$ for profits; $e = 0.876(a-c)$ for welfare.

Extension (§4): cost advantage/disadvantage changes the optimal CSR level; a cost **disadvantage** raises it (Props. 4–6, pp. 181–182).

Conclusion (p. 182): CSR level should be decided on the competitor's behaviour and market demand; "excessive CSR should not be undertaken blindly".

## Relation to [[Kopel2021-CSR]]

**Agrees on the structure, disagrees on the mechanism.** Both are two-stage duopolies where CSR is chosen before the market stage. But:

| | Kopel (2021) | Chen et al. (2021) |
|---|---|---|
| Competition | Bertrand, differentiated | Cournot, homogeneous |
| What CSR is | a demand shift $s_i$ bought at cost $s_i^2$ | a weight $\beta_i$ on consumer surplus *and* a demand shifter |
| Asymmetry | sequential timing (leader/follower) | which firms adopt (CN vs CC) |
| Spillovers | central ($\theta$) | **absent** |
| Rival driven to zero | at $\gamma_{\max}$ | in Model CN, at the optimum |

**[our reading]** The most useful contrast is the role of a sensitivity parameter. In Kopel, competition intensity $\gamma$ has a U-shaped effect on the leader's CSR. In Chen, market sensitivity $e$ has **opposite-signed** effects depending on whether one firm or both do CSR. Both papers conclude the competition–CSR relation is not monotone and depends on the configuration, which is the point [[competition-intensity]] makes.

**Note the symbol clash**: Chen's $\beta_i$ is a CSR level. Kopel has no $\beta$. See [[glossary]].
