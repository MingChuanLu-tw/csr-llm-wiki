# Xing & Lee (2023) — Non-cooperative and cooperative environmental R&D under ECSR

- **Source**: `raw/papers/XingLee2023-EnvironmentalRD.pdf`
- **Citation**: Xing, M. & Lee, S.-H. (2023). Non-cooperative and cooperative environmental R&D under environmental corporate social responsibility with green managerial coordination. *Managerial and Decision Economics*, 44(5), 2684–2696. doi:10.1002/mde.3842
- **Ingest depth**: ⚠️ **LIGHT** — no A4 verification, no A3 review. Lower assurance than [[Kopel2021-CSR]].
- **Links**: [[csr-spillovers]] · [[csr-modelling-choices]] · [[strategic-commitment]]

## Model (§2, p. 2686)

Polluting Cournot duopoly, homogeneous good, $p = a - q_1 - q_2$, marginal cost $c$, $m \equiv a - c$ (eqs. (1)–(4), p. 2686).

- Output pollutes one unit each; ER&D effort $y_i$ cuts it, so emissions are $e_i = q_i - y_i$ (end-of-pipe). ER&D cost $y_i^2/2$. Damage $D = d(e_1+e_2)$, emissions tax $t$ per unit.
- **Green managerial delegation**: owners pick the **ECSR degree** $h_i \ge 0$; managers then maximise $V_i = \pi_i - h_i D$.
- **Three stages**: (1) owners choose $h_i$, cooperatively or not; (2) managers choose $y_i$, cooperatively or not; (3) managers choose outputs non-cooperatively.

Four regimes by who cooperates: **NN, NY, YN, YY** (first letter = ECSR, second = ER&D).

## Results

| # | Finding | Where |
|---|---|---|
| Prop. 1 | $h^{YN} > h^{YY} > h^{NY} = h^{NN} = 0$ — **owners adopt zero ECSR unless they can cooperate on it**, with or without a tax | p. 2688 |
| Prop. 2 | $y_i^{YN} > y_i^{YY} > y_i^{NY} = y_i^{NN}$ — ER&D is higher under cooperative ECSR | p. 2689 |
| Prop. 3 | $q_i^{NN} = q_i^{NY} > q_i^{YY} > q_i^{YN}$ — cooperative ECSR works "as a collusive device to decrease the output and increase prices and profit" | p. 2689 |
| Prop. 4 | $\pi_i^{YN} > \pi_i^{YY} > \pi_i^{NY} = \pi_i^{NN}$ — owners prefer **non**-cooperative ER&D between their managers | p. 2689 |
| Prop. 5 | whether managers want to cooperate on ER&D depends on $t$ and $d$ — a genuine owner/manager conflict of interest | p. 2689 |

Welfare: cooperative ECSR is **not** beneficial to society when damage is low; strict oversight of collusive behaviour matters (p. 2685).

## Relation to [[Kopel2021-CSR]]

**The sharpest contrast in the set, and the most uncomfortable one.**

Kopel asks *who gains* when one firm leads on CSR, and finds the first mover
rarely does. Xing & Lee ask whether firms adopt CSR **at all** in a competitive
delegation setting, and find **$h^{NN} = 0$: without cooperation, nobody adopts
it.** CSR appears only as a *collusive* device that lowers output and raises
prices.

**[our reading]** Put beside Kopel this produces a genuinely awkward pair of
conclusions worth raising in the seminar. Kopel's leader invests heavily and
loses; Xing & Lee's firms will not invest unilaterally at all. Both are
strategic-CSR models with sequential structure, and both conclude that
unilateral CSR does not pay the firm that does it. The difference is what fills
the gap: Kopel's follower free-rides, Xing & Lee's firms coordinate. Neither
mechanism is the "CSR as competitive advantage" story.

**On spillovers.** There is no spillover parameter here — the channel is explicit
cooperation rather than involuntary leakage. That makes it a useful boundary case
for [[csr-spillovers]]: Kopel's $\theta$ is imposed by imitability, Xing & Lee's
coordination is chosen. The outcomes rhyme (the leader cannot keep the benefit)
but the causes do not.

> **Symbol note.** $h_i$ is the ECSR degree; $d$ is marginal damage; $t$ is the
> emissions tax; $y_i$ is R&D effort. None of these collide with Kopel's
> notation, but $d$ and $t$ are used nowhere else in this wiki. See [[glossary]].
