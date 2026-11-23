# Kopel (2021) — CSR leadership, spillovers, and first-mover advantage

- **Source**: `raw/papers/Kopel2021-CSR.pdf`
- **Full citation**: Kopel, M. (2021). CSR leadership, spillovers, and first-mover advantage. *Decisions in Economics and Finance*, 44, 489–505. https://doi.org/10.1007/s10203-021-00328-9
- **License**: CC BY 4.0 (open access). Figures may be reproduced with attribution.
- **Pagination**: all page references below are journal pages 489–505 (PDF page *n* = journal page 488 + *n*).
- **Status**: A1 complete; **A4 verified** (equations re-derived symbolically, thresholds reproduced — `checks/a4_report.md`); **A3 reviewed 2026-11-16** and the reported defects fixed — `checks/a3_report.md`. Awaiting A3 re-review and A6 (human sign-off).
- **Marking convention**: a 🔎 box or a **[our reading]** tag marks an inference that is *not* the author's claim. Everything else is attributed to the paper with a page number.
- **Links**: [[first-mover-advantage]] · [[csr-spillovers]] · [[competition-intensity]] · [[appropriability]] · [[strategic-commitment]]

---

## 1. The question (pp. 489–490)

A **CSR leader** is a firm that commits to socially responsible investment *before* its competitor. Kopel asks when this timing earns the leader a **first-mover advantage (FMA)**, defined throughout as $\pi_1^* > \pi_2^*$.

Four research questions, stated verbatim in substance on p. 490:

1. Does the CSR leader always obtain a first-mover advantage, or can the follower earn more?
2. Who has the higher *incentive* to invest in CSR, and who ends up with the higher *absolute level* of CSR?
3. How do **CSR spillovers** change these answers?
4. How does the **intensity of competition** change them?

The paper is a revised version of a working paper, "Strategic CSR, Spillovers, and First-Mover Advantage", which "has been circulated and frequently cited since 2009" (unnumbered footnote, p. 489).

**Why the question is open.** The strategy literature on first- versus second-mover advantage is large, but p. 490 notes that very few CSR papers address it. The two sides of the existing debate:

- *Skeptical*: Reinhardt (1998) and Vogel (2005) argue CSR activities are hard to keep firm-specific, so any advantage erodes. The Economist (2008) is quoted: a consultancy advises big clients to be "number two or three on corporate responsibility rather than number one" (p. 490).
- *Optimistic*: Tetrault Sirsly & Lamertz (2008) argue a CSR leader can sustain an FMA if the initiative is "central to the firm mission, visible to stakeholders and with firm-specific benefits beyond those of public goods" (quoted p. 490).

Kopel's contribution is to settle this with a formal model rather than argument.

> ⚠️ **Read the framing and the conclusion together.** On p. 490 Kopel sets Tetrault Sirsly & Lamertz "in contrast" to Reinhardt and Vogel, as above. But in the conclusion (p. 502) he groups all three on the *same* side: his study "provides support for the claims in conceptual papers like Tetrault Sirsly and Lamertz (2008), Burke and Logsdon (1996), and Reinhardt (1998) who argue that it seems rather difficult to sustain a first-mover advantage based on investments in CSR." See §8.

## 2. Headline findings (pp. 491, 499–502)

| # | Finding | Where |
|---|---|---|
| 1 | With no spillovers ($\theta = 0$) the leader invests more and earns more — an FMA exists. | Lemma 1, p. 499 |
| 2 | The FMA survives **only for very low $\theta$** — the level of spillovers that sustains it is "in fact very low" (p. 491). Otherwise the follower gets a second-mover advantage. | Lemma 2, p. 500 |
| 3 | The leader's CSR is **U-shaped** in competition intensity; the follower's is monotonically decreasing — when $\theta$ is low. | Fig. 1 p. 498, Lemma 3 p. 501 |
| 4 | The pattern **reverses** for high $\theta$: the leader's CSR decreases monotonically and the *follower's* becomes U-shaped. | Lemma 3, p. 501 |
| 5 | Because CSR practices converge through imitation, the leader gives up its differentiation — which may explain why empirical studies find "no or a rather weak link" between corporate social and financial performance. | p. 491, p. 502 |

The author's own emphasis (p. 491): *"What is surprising, however, is that the level of CSR spillovers for which a first-mover advantage can be sustained is in fact very low."* Even the smallest opportunity to free-ride hands the follower a competitive advantage.

Separately, p. 500 calls the region where the leader *invests* more ($s_1^*>s_2^*$) "rather small" — a different region from the FMA region, though both are small. See §7.2.

## 3. Where the paper sits in the literature (pp. 490–493)

Three streams, per §2 of the paper:

1. **CSR as strategic differentiation.** CSR raises consumers' willingness to pay in imperfectly competitive markets (Fernández-Kranz & Santalo 2010; Kitzmueller & Shimshack 2012; McWilliams & Siegel 2001). Bagnoli & Watts (2003) link private provision of a public good to price competition and find too little public good is provided. Kopel differs by adding **sequential CSR timing and spillovers** (p. 492).
2. **Competition and CSR, with conflicting conclusions.** Bagnoli & Watts (2003) find more competition lowers CSR; Fisman et al. (2006) "use a signaling model" and conclude the opposite (p. 492). Both are theoretical. Kopel's resolution: the relation is **ambiguous and asymmetric** between leader and follower (p. 492).
3. **CSR/environmental leadership**, previously mostly conceptual or empirical (Tetrault Sirsly & Lamertz 2008; Bansal & Hunter 2003; Nehrt 1996). The closest formal models are Chen et al. (2016) — Cournot, one investor, *negative* spillovers — and Wang et al. (2018) — the CSR firm maximises profit plus consumer surplus. Arya & Mittendorf (2013) have simultaneous rather than sequential investment (pp. 492–493).

**What is new here**: price competition + horizontal differentiation + *sequential* CSR + *positive asymmetric* spillovers, solved in closed form.

## 4. Model (pp. 493–495)

### 4.1 Primitives

Two firms produce horizontally differentiated products at constant unit cost $c$. Firm 1 is the **CSR leader**, firm 2 the **CSR follower**. Firm $i$ chooses CSR level $s_i$ at cost $s_i^2$ (quadratic, following Garella & Petrakis 2008).

Parameters:

- $a$ — reservation price (p. 493).
- $\gamma \in [0,1)$ — product substitutability. $\gamma = 0$: independent products; $\gamma \to 1$: perfect substitutes. **Higher $\gamma$ = more intense competition** (p. 493).
- $\theta_1, \theta_2 \in [0,1]$ — spillover parameters: $\theta_i$ is the share of the **rival's** CSR benefit captured by firm $i$ (p. 494). Read the index off the demand system in §4.2: $\theta_1$ multiplies $s_2$ inside $p_1$, so it is the spillover *into* firm 1, not out of it. The paper's prose on p. 494 ("the firms' abilities to protect their CSR investments") reads the other way, but the equation governs, and Kopel's own justification — $\theta_1 \le \theta_2$ "because the CSR follower can free ride on the CSR efforts of the leader" — only makes sense if firm 2 is the one *receiving*.

### 4.2 The spillover asymmetry — an assumption, not a result

The general inverse demand (unnumbered, p. 493):

$$
p_1 = a + (s_1 + \theta_1 s_2) - x_1 - \gamma x_2, \qquad
p_2 = a + (s_2 + \theta_2 s_1) - x_2 - \gamma x_1
$$

Kopel then argues (p. 494) that in a leader–follower setting it is "sensible to assume that spillovers are asymmetric", specifically $\theta_1 \le \theta_2$, "because the CSR follower can free ride on the CSR efforts of the leader." To keep the model tractable he sets $\theta_1 = 0$ and writes $\theta_2 = \theta \in [0,1]$, giving **eq. (1)**:

$$
p_1 = a + s_1 - x_1 - \gamma x_2, \qquad
p_2 = a + (s_2 + \theta s_1) - x_2 - \gamma x_1
\tag{1}
$$

> ⚠️ **Flag for discussion.** $\theta_1 = 0$ is a modelling choice, not a derived property. It means the leader gets *nothing* from the follower's later CSR, while the follower gets $\theta$ of the leader's. Since the whole paper is about who benefits from whom, this assumption does part of the work of the result. See [[open-questions]] Q1.

Interpretation of $\theta$: it measures **appropriability** — how well CSR benefits can be protected from imitation. Footnote 6 (p. 494) quotes Burke & Logsdon (1996, p. 497) on "specificity": the firm's ability to capture benefits "rather than simply creating collective goods which can be shared by others in the industry, community or society at large." Footnote 7 contrasts Patagonia (successfully differentiated) with StarKist's dolphin-safe policy (imitated almost immediately).

CSR enters as a **vertical** demand shift (quality-like), while $\gamma$ captures **horizontal** differentiation (p. 494).

### 4.3 Direct demand and profits

Inverting (1) gives **eq. (2)** (p. 495):

$$
x_1(p_1,p_2,s_1,s_2) = \frac{a(1-\gamma) + (1-\gamma\theta)s_1 - \gamma s_2}{1-\gamma^2} - \frac{1}{1-\gamma^2}p_1 + \frac{\gamma}{1-\gamma^2}p_2
$$

$$
x_2(p_1,p_2,s_1,s_2) = \frac{a(1-\gamma) + s_2 - (\gamma-\theta)s_1}{1-\gamma^2} - \frac{1}{1-\gamma^2}p_2 + \frac{\gamma}{1-\gamma^2}p_1
\tag{2}
$$

Profits net of CSR cost (p. 495):

$$
\pi_1 = (p_1 - c)\,x_1(p_1,p_2,s_1,s_2) - s_1^2, \qquad
\pi_2 = (p_2 - c)\,x_2(p_1,p_2,s_1,s_2) - s_2^2
$$

**Technical restriction** (p. 495): the demand system is discontinuous at $\gamma = 1$, so the analysis requires

$$
\gamma < \gamma_{\max} = 0.810736
$$

This "guarantees that the equilibrium of the game is in the interior and all second-order conditions are satisfied" (p. 495, citing Garella & Petrakis 2008). The paper does not say *which* condition binds.

> 🔎 **A4 finding — not in the paper.** The binding condition is **interiority of the follower at $\theta = 0$**. At that point the leader's strategic over-investment drives $s_2^*$ and $x_2^*$ to zero simultaneously. Formally, $\gamma_{\max}$ is the unique root in $(0,1)$ of the eq. (6) numerator at $\theta=0$,
> $$N(\gamma,0) = 18 + 6\gamma - 35\gamma^2 - 15\gamma^3 + 15\gamma^4 + 7\gamma^5 - 2\gamma^6 - \gamma^7 = 0,$$
> giving $\gamma = 0.8107358771$, which is $0.810736$ to six decimal places. It is the *binding* constraint: all second-order conditions fail only at larger $\gamma$ (leader's SOC at $0.830176$, follower's at $0.932526$), and the root rises monotonically in $\theta$, so the no-spillover benchmark is the worst case. See `checks/a4_report.md` §2a.
>
> **Why this matters for the talk.** $\gamma_{\max}$ is not a technical nuisance — it marks where the duopoly would collapse into a monopoly. So the paper's claim that the leader's advantage "can not only be sustained, but made even larger" as products become homogeneous (p. 499) is evaluated right up against the edge where the follower is squeezed out entirely.

### 4.4 Timing

Three stages, solved by backward induction (p. 495):

| Stage | Who | Chooses | Observed by |
|---|---|---|---|
| 1 | Leader (firm 1) | $s_1$ to maximise $\pi_1$ | follower |
| 2 | Follower (firm 2) | $s_2$ to maximise $\pi_2$ | — |
| 3 | Both, simultaneously | $p_1, p_2$ | — |

The leader–follower order is **exogenous** (acknowledged as a limitation, p. 502).

## 5. Equilibrium (pp. 495–497)

### 5.1 Stage 3 — prices

Solving $\partial\pi_1/\partial p_1 = 0$ and $\partial\pi_2/\partial p_2 = 0$ gives **eq. (3)** (p. 495):

$$
p_1(s_1,s_2) = \frac{a(2+\gamma)(1-\gamma) + (2+\gamma)c + (2-\gamma^2-\gamma\theta)s_1 - \gamma s_2}{4-\gamma^2}
$$

$$
p_2(s_1,s_2) = \frac{a(2+\gamma)(1-\gamma) + (2+\gamma)c + (2-\gamma^2)s_2 + ((2-\gamma^2)\theta-\gamma)s_1}{4-\gamma^2}
\tag{3}
$$

Two observations (p. 495):

- A firm's own CSR raises its own price, but **the marginal effect is smaller for the leader** when spillovers are positive (the $-\gamma\theta$ term in $p_1$).
- The leader's CSR **raises the follower's price** if $\theta > \dfrac{\gamma}{2-\gamma^2}$.
- If both choose the same CSR level $s_1 = s_2 > 0$, the **follower** sets the higher price when spillovers are positive (p. 496).

### 5.2 Stage 2 — the follower's reaction function

**Eq. (4)** (p. 496):

$$
s_2(s_1) = \frac{(2-\gamma^2)\big((a-c)(2+\gamma)(1-\gamma) + s_1((2-\gamma^2)\theta-\gamma)\big)}{12-20\gamma^2+8\gamma^4-\gamma^6}
\tag{4}
$$

**The sign of $ds_2/ds_1$ is the hinge of the whole paper:**

$$
\frac{ds_2}{ds_1} < 0 \iff \theta < \frac{\gamma}{2-\gamma^2}
$$

- **Low $\theta$** → strategic *substitutes*: more leader CSR makes the follower cut its own CSR and free-ride.
- **High $\theta$** → strategic *complements*: "then the leader's incentive to invest in CSR decreases and, therefore, the follower has to increase its own CSR activities to counterbalance this effect" (p. 496). Note the paper's mechanism is defensive, not opportunistic.

The labels "strategic substitutes / complements" are standard terminology and are ours; the paper states only the threshold. **[our reading]**

### 5.3 Stage 1 — the leader's equilibrium CSR

**Eq. (5)** (p. 496):

$$
s_1^* = \frac{(a-c)(1-\gamma^2)\big[6-\gamma(4+\gamma(5-\gamma-\gamma^2))\big]\big[6-\gamma(4\theta+\gamma(5-\gamma\theta-\gamma^2))\big]}{\big(12-20\gamma^2+8\gamma^4-\gamma^6\big)^2-\big(1-\gamma^2\big)\big(6-\gamma(4\theta+\gamma(5-\gamma\theta-\gamma^2))\big)^2}
\tag{5}
$$

**Eq. (6)** — the follower (p. 496):

$$
s_2^* = \frac{(a-c)(1-\gamma)(2-\gamma^2)\,N}{\big(12-20\gamma^2+8\gamma^4-\gamma^6\big)^2-\big(1-\gamma^2\big)\big(6-\gamma(4\theta+\gamma(5-\gamma\theta-\gamma^2))\big)^2}
\tag{6}
$$

with

$$
N = 6(3+\theta) + 2\gamma(3+5\theta-2\theta^2) - \gamma^2(35+\theta+4\theta^2) - \gamma^3(15+6\theta-\theta^2) + \gamma^4(15+\theta^2) + \gamma^5(7+\theta) - 2\gamma^6 - \gamma^7
$$

Footnote 8 (p. 496): the denominator of (5) embodies the second-order condition, which holds for $\gamma < \gamma_{\max}$ at all spillover levels; the equilibrium CSR level is positive.

### 5.4 Equilibrium prices and profits

**Eq. (7)** (pp. 496–497):

$$
p_1^* = c + \frac{12-20\gamma^2+8\gamma^4-\gamma^6}{6-\gamma(4\theta+\gamma(5-\gamma\theta-\gamma^2))}\,s_1^*, \qquad
p_2^* = c + \frac{(4-\gamma^2)(1-\gamma^2)}{(2-\gamma^2)}\,s_2^*
\tag{7}
$$

Profits (p. 497, unnumbered):

$$
\pi_1^* = \frac{(a-c)\big(6-\gamma(4+\gamma(5-\gamma-\gamma^2))\big)}{6-\gamma(4\theta+\gamma(5-\gamma\theta-\gamma^2))}\,s_1^*, \qquad
\pi_2^* = \frac{(4-\gamma^2)(2-\gamma^2)^2-4}{(2-\gamma^2)^2}\,(s_2^*)^2
$$

Note the asymmetric form: $\pi_1^*$ is linear in $s_1^*$ while $\pi_2^*$ is quadratic in $s_2^*$. **A4 verified this asymmetry is genuine, not a transcription error** — the leader's stage-1 first-order condition allows one factor of $s_1^*$ to be substituted out, and the follower's does not.

## 6. Benchmark: no spillovers, $\theta = 0$ (pp. 497–499)

### 6.1 The leader always invests more

From (5) and (6) with $\theta = 0$ (p. 497):

$$
s_1^* - s_2^* = \frac{\gamma^2(2+\gamma)}{(1+\gamma)(3-\gamma^2)\big(6-\gamma(4+\gamma(5-\gamma-\gamma^2))\big)}\,s_1^* > 0
\quad\text{for } 0 < \gamma \le \gamma_{\max}
$$

Comparative statics (p. 497):

$$
\frac{\partial s_1^*}{\partial\gamma} < 0 \text{ for } \gamma < 0.531963, \qquad
\frac{\partial s_1^*}{\partial\gamma} > 0 \text{ for } 0.531963 < \gamma < \gamma_{\max}
$$

$$
\frac{\partial s_2^*}{\partial\gamma} < 0 \text{ for } 0 < \gamma < \gamma_{\max}
$$

**Fig. 1** (p. 498) plots this, with $a = 1$, $c = 0$ (footnote 9: "In all the figures in this section, $a - c = 1$"). The leader's curve (bold) is U-shaped with minimum near $\gamma \approx 0.532$; the follower's (dashed) falls throughout. The gap widens as competition intensifies.

### 6.2 Why U-shaped? Three effects

Kopel decomposes the incentive to invest (pp. 498–499):

| Effect | Direction as $\gamma$ rises | Acts on |
|---|---|---|
| **Markup effect** | negative — prices fall toward marginal cost, so each unit of demand is worth less | both firms |
| **Demand effect** | positive — with $\theta = 0$, $\partial(\partial x_i/\partial s_i)/\partial\gamma > 0$, so CSR shifts more demand | both firms |
| **Strategic effect** | positive, **leader only** — committing to high CSR induces the follower to cut its CSR | leader |

For the leader, $\partial\pi_1/\partial s_1 > 0$ always; at low $\gamma$ the markup effect dominates ($\partial(\partial\pi_1/\partial s_1)/\partial\gamma < 0$), at high $\gamma$ the demand effect dominates — hence the U shape (footnote 11). For the follower, $\partial(\partial\pi_2/\partial s_2)/\partial\gamma < 0$ throughout (footnote 12), so no U shape.

The strategic effect is the reason the leader **over-invests**: $s_1 > s_2$. Footnote 14 states it is determined by $\dfrac{\partial\pi_1}{\partial s_2}\cdot\dfrac{\partial s_2}{\partial s_1} > 0$, and footnote 13 notes $ds_2^*/ds_1 < 0$ holds as long as $\theta < \gamma/(2-\gamma^2)$.

**[our reading]** That both factors are individually negative — more follower CSR hurts the leader, more leader CSR makes the follower retreat — is our inference, and it is what makes the product positive. The paper gives only the product's sign.

### 6.3 Lemma 1 (p. 499)

> **Lemma 1.** In an industry where the outcomes of the CSR investments are highly specific to the leader, i.e., there are no CSR spillovers ($\theta = 0$), a CSR leader invests more than a CSR follower, $s_1^* > s_2^*$. Furthermore, the CSR leader has a first-mover advantage, that is the leader obtains a higher profit than the CSR follower, $\pi_1^* > \pi_2^*$.

The paper gives no proof: "The proof of the lemma follows from a simple comparison is therefore omitted" (p. 499, *sic*).

Notably, the leader's profit advantage **grows** with competition intensity: as products become more homogeneous, the advantage "can not only be sustained, but made even larger" (p. 499).

## 7. Positive spillovers (pp. 499–501)

### 7.1 Asymmetric effect of $\theta$

$$
\frac{\partial}{\partial\theta}\!\left(\frac{\partial\pi_1}{\partial s_1}\right) < 0 \quad\text{(leader)}, \qquad
\frac{\partial}{\partial\theta}\!\left(\frac{\partial\pi_2}{\partial s_2}\right) > 0 \quad\text{(follower)}
$$

Spillovers dampen the leader's incentive and strengthen the follower's (p. 499, §5.2).

### 7.2 Lemma 2 and Fig. 2 (p. 500)

**Fig. 2** maps the $(\gamma, \theta)$ plane with $a = 1$, $c = 0$:

- **Bold curve** = locus where $\pi_1^* = \pi_2^*$. **Below it the leader has an FMA.**
- **Dashed curve** = locus where $s_1^* = s_2^*$. Above it $s_1^* < s_2^*$; below it $s_1^* > s_2^*$.
- Both curves lie **low** in the figure — the FMA region is visibly small, and widest at high $\gamma$. The paper calls the $s_1^*>s_2^*$ region "rather small" (p. 500).

> ⚠️ **Be ready for this one in the room.** The sentence on p. 500 states the dashed-curve regions the other way round: "$s_1^* > s_2^*$ in the region **above** the dashed curve and $s_1^* < s_2^*$ below". That contradicts Fig. 2's own region labels, contradicts Lemma 2 ("the CSR leader selects a higher activity level of CSR … if CSR spillovers are quite small"), and contradicts computation: at $\gamma=0.3$ the $s_1^*=s_2^*$ frontier is at $\theta=0.0169$, and at $\theta=0.05$ (above it) $s_1^*=0.2820 < s_2^*=0.2889$. We follow the figure and the lemma, and treat the sentence as a slip. Verified in `checks/a3_report.md` F8.

> 🔎 **A4 finding — the paper never states this numerically.** The frontier $\pi_1^*=\pi_2^*$ was computed directly:
>
> | $\gamma$ | FMA holds only for |
> |---|---|
> | 0.1 | $\theta < 0.0000534$ |
> | 0.3 | $\theta < 0.00150$ |
> | 0.5 | $\theta < 0.00867$ |
> | 0.7 | $\theta < 0.0393$ |
> | 0.8 | $\theta < 0.0960$ |
>
> At moderate competition ($\gamma = 0.3$) the spillover rate must stay below **0.15%** for the leader to out-earn the follower. The paper's qualitative "in fact very low" (p. 491) understates this by orders of magnitude at low $\gamma$. This is arguably the sharpest result in the paper and a candidate headline slide.
>
> Note the frontier is a bound on $\theta$ itself. Saying the leader "retains $1-\theta$ of the benefit" is a metaphor: in eq. (1) the leader's own demand shift is $s_1$ whatever $\theta$ is — $\theta$ adds a benefit to the rival rather than subtracting one from the leader.

> **Lemma 2.** A CSR leader achieves a FMA only if the outcomes of the CSR efforts are highly specific to the leader, that is the level of CSR spillovers $\theta$ is quite small. Otherwise, the CSR follower has a second-mover advantage, $\pi_1^* < \pi_2^*$. Moreover, the CSR leader selects a higher activity level of CSR than the CSR follower if the outcomes of the CSR efforts are highly specific to the firm, i.e., if CSR spillovers are quite small (independent of the degree of competition). Otherwise, the CSR follower has a higher level of CSR activity, $s_1^* < s_2^*$.

### 7.3 Lemma 3 — the pattern reverses (pp. 500–501)

Two numerical thresholds, both from **numerical analysis** (footnote 15, p. 501), not closed form. Footnote 15 states the criterion: check the sign of $\partial s_i^*/\partial\gamma$ **evaluated at $\gamma = \gamma_{\max}$** and find where it changes.

| Condition | Consequence |
|---|---|
| $\theta < 0.202167$ | $\partial s_2^*/\partial\gamma < 0$ at the endpoint — **follower decreasing** |
| $\theta > 0.202167$ | **follower U-shaped** — falls, then rises at high competition |
| $\theta > 0.229499$ | $\partial s_1^*/\partial\gamma < 0$ at the endpoint — **leader monotonically decreasing** |
| $\theta < 0.229499$ | leader U-shaped |

> 🔎 **A3 finding — the follower's threshold is an endpoint criterion, not whole-interval monotonicity.** Because footnote 15 evaluates the derivative only *at* $\gamma_{\max}$, it cannot see an interior hump. Maximising $\partial s_2^*/\partial\gamma$ over 2000 points shows the hump appears between $\theta = 0.190$ and $\theta = 0.1925$ — below the paper's 0.202167 — and from there up to 0.202167 the follower's curve is down–up–down. The leader's threshold does not have this problem. So 0.202167 is where the *endpoint slope* flips, not where monotonicity first fails. See `checks/a3_report.md` F9. Good discussion material, and safer than being corrected from the floor.

> **Lemma 3.** For sufficiently low levels of CSR spillovers ($\theta < 0.202167$), the CSR follower's investment in equilibrium decreases for increasing intensity of competition, whereas the CSR leaders' investment first decreases, but then increases again. If spillovers are sufficiently large ($\theta > 0.229499$), then CSR leader's investment is monotonically decreasing and the CSR follower's investment is U-shaped.

The lemma holds for $a > c$ (p. 501).

**The overlap band $0.202167 < \theta < 0.229499$** is where *both* firms' investments are U-shaped — the roles look qualitatively identical. **Fig. 3** (p. 501) illustrates exactly this case with $\theta = 0.21$: both curves U-shaped, with the **follower's (dashed) above the leader's (bold)**, i.e. the roles have swapped relative to Fig. 1.


## 8. Discussion and conclusions (p. 502)

**What the author concludes.** Only in the rare case where CSR outcomes are highly firm-specific does an FMA exist. In Kopel's own words the study "provides support for the claims in conceptual papers like Tetrault Sirsly and Lamertz (2008), Burke and Logsdon (1996), and Reinhardt (1998) who argue that it seems rather difficult to sustain a first-mover advantage based on investments in CSR" (p. 502). It separately "gives substance to the critical assessment of Vogel (2005)" (p. 502).

> ⚠️ Note that p. 502 groups Tetrault Sirsly & Lamertz **with** Burke & Logsdon and Reinhardt, whereas the framing on p. 490 set them in contrast. Kopel also writes on p. 491 that "in line with Tetrault Sirsly and Lamertz (2008) I find that a first-mover advantage exists" when CSR is firm-specific. The paper formalises TS&L's condition rather than refuting it. Do not present TS&L as the losing side.

A further mechanism: **reputation spillovers push toward convergence.** "Being aware of reputation spillovers, industry leaders oftentimes pressure and support less socially responsible competitors to imitate their CSR practices (Misani 2010; Vogel 2005)" (p. 491). The leader is the actor here, out of self-interest: p. 502 adds that "due to the fear of negative reputation spillovers — the CSR leader might find it appropriate to support the CSR follower". Even if strategically motivated, this surrenders the differentiation the FMA rested on. Footnote 16 (p. 502) introduces Misani's (2010) terms: *divergent CSR* (differentiate) vs *convergent CSR* (avoid shared risk, defend industry reputation).

**Managerial implication** (p. 502): the relation between competition intensity, CSR investment and profit "might be ambiguous for firms". Management must match CSR investment to industry structure (substitutability) and firm position (leader/follower, appropriability) — there is no general rule.

**Extensions the author lists** (p. 502): multiple leaders and followers; endogenous timing (Kopel & Löffler 2012); managerial rather than entrepreneurial firms (Baron 2001; Fisman et al. 2005/2006); mixed oligopoly where only some firms do CSR; CSR that changes the demand *slope* rather than the intercept; dynamic/multi-period CSR (Bischi et al. 2010, 2015; Kopel et al. 2014; Kopel & Lamantia 2018).

## 9. Limitations visible in the setup (A1 observation — not the author's words)

These are mine, extracted from the model, and are candidate discussion points:

1. **$\theta_1 = 0$ is assumed, not derived** (p. 494). The leader never benefits from the follower's CSR.
2. **The leader–follower order is exogenous** (acknowledged, p. 502). Nobody chooses to be the leader.
3. **$\gamma < 0.810736$**, so the "high competition" region of the figures stops well short of perfect substitutes. Claims about "increasingly homogeneous products" (p. 499) are bounded by this.
4. ~~**All figures use $a-c=1$**, so general-parameter claims are only illustrated.~~ **Withdrawn — this was an over-cautious caveat.** In eq. (5) and (6) $(a-c)$ is a bare multiplicative factor and $c$ appears nowhere else in $s_1^*, s_2^*$; $\pi_1^*\propto(a-c)s_1^*$ and $\pi_2^*\propto(s_2^*)^2$. So $s_i^*$ is homogeneous of degree 1 and $\pi_i^*$ of degree 2 in $(a-c)$, and **every ordering and every derivative sign is independent of $a-c$ for any $a>c$**. The normalisation is without loss of generality — presumably why Lemma 3 is stated for "$a>c$" rather than for a value. **[our reading]** (`checks/a3_report.md` F6.)
5. **Only positive spillovers** are studied; footnote 4 notes negative spillovers exist (Klein & Dawar 2004) but are excluded.
6. **CSR cost is $s_i^2$ for both firms** — the leader has no cost advantage from acting first, only a strategic one.
7. **Static** within each stage; no repeated interaction, learning, or consumer memory.

## 10. Verification status

### A4 — PASSED 2026-11-16 (`checks/a4_report.md`)

Method: the whole three-stage game was re-derived from eq. (1) with sympy, independently of the paper's stated results, then compared against the equations on this page. A pass confirms both the paper's algebra and this transcription.

- [x] Equations (1)–(7), $N$, both profit expressions, and the $s_1^*-s_2^*$ gap — **12/12 exact**.
- [x] $\gamma_{\max} = 0.810736$ — identified as the $\theta=0$ interiority bound, root at $0.8107358771$. See §4.3.
- [x] $\gamma \approx 0.531963$ — recomputed $0.5319633163$ (diff 3.2e-7).
- [x] $\theta = 0.202167$ — recomputed $0.2021670222$ (diff 2.2e-8).
- [x] $\theta = 0.229499$ — recomputed $0.2294985504$ (diff 4.5e-7).
- [x] Lemma 1 — holds on all 39 grid points in $(0,\gamma_{\max})$.
- [x] Lemma 3 shape bands — thresholds reproduce to 6 dp; see the A3 caveat in §7.3 about what the follower's threshold actually measures.
- [x] Fig. 3 has the follower above the leader — confirmed at every sampled $\gamma$.
- [x] $\pi_1^*/\pi_2^*$ asymmetry — genuine, see §5.4.

### A3 — reviewed 2026-11-16, FAIL, defects fixed (`checks/a3_report.md`)

An independent reviewer with fresh context re-derived the model from eq. (1) and checked the wiki against the PDF page images. Round 1: 5 blockers, 14 should-fix, 9 minor. Round 2 (same reviewer, verifying the fixes): **PASS WITH FIXES** — 26 of 29 fully fixed, no blockers remain, and the two mathematical claims added in response (the K-sub quotient and the homogeneity argument) were confirmed correct under independent check. The round-2 residue is listed under "Remaining gaps". What the review confirmed as sound:

- [x] Every equation in `equations.md` matches the printed page — **zero transcription errors**, independently re-derived.
- [x] The $\theta$ threshold logic is correct in all four locations — no reversal.
- [x] All three lemma blockquotes verbatim apart from three dropped commas (fixed).
- [x] Every FMA-frontier and Fig. 3 value reproduced independently.
- [x] The $\gamma_{\max}$-as-monopoly-boundary reading survives scrutiny — called "the strongest original contribution of the wiki".

What it found wrong on this page, now corrected: the conclusion's position on Tetrault Sirsly & Lamertz (§1, §8); the $\theta_i$ index direction (§4.1); a fabricated quotation (§7.2); a false "analytic" claim (§9); five wrong page numbers; several unmarked own-inferences.

### Remaining gaps

1. ~~Figures not regenerated.~~ **Closed in A3 round 2.** Figs. 1 and 3 were compared curve-to-curve against the verified expressions. Fig. 1's axis top of 0.66 matches the computed $s_1^*(\gamma_{\max}) = 0.6562$, and its dashed curve hits zero exactly at the right-hand edge — **the printed figure independently corroborates the $\gamma_{\max}$-interiority finding in §4.3.** Fig. 3 matches too. Fig. 2 remains checked qualitatively only.
2. **Lemmas 1 and 2 are confirmed numerically, not proved symbolically.** The paper omits both proofs. A grid check is strong evidence, not a proof — state this honestly on the slide.
3. **Third-party quotations verified only as Kopel reproduces them.** Burke & Logsdon, the Economist and Tetrault Sirsly & Lamertz are not in `raw/`, so we cannot confirm Kopel quoted them correctly.
4. ~~A5 (lint) has never run.~~ **Ran 2026-11-17.** Mechanical half: 10/10 pass (`scripts/a5_lint.py`). Judgement half: FAIL, one blocker — two pages said the first-mover advantage dies *because* the leader's deterrence breaks, but the deterrence switch sits 6×–940× higher than the FMA frontier, so deterrence is intact when the FMA dies. Fixed; see `checks/a5_report.md` and [[numbers]] "Three thresholds". **A6 human sign-off is now the only node outstanding.**
5. **At $\gamma = 0$ the two CSR curves coincide** at $1/3$ (A3 round 2, from Fig. 1). The gap formula in §6.1 is stated for $0<\gamma\le\gamma_{\max}$, so this is consistent — but "the leader always invests more" holds only for $\gamma>0$.
