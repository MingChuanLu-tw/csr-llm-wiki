# Number register

Every number the deck may show. Node **B10** checks that each figure on a slide
appears here. A number not in this register may not go on a slide.

Verification source: `checks/a4_report.md`, scripts in `scripts/`.

## From the paper, verified

| Value | Meaning | Paper | Recomputed | Diff | Status |
|---|---|---|---|---|---|
| $\gamma_{\max}$ | upper bound for interior equilibrium | 0.810736 | 0.8107358771 | 1.2e-7 | ✅ |
| $\gamma^\dagger$ | turning point of $s_1^*$ at $\theta=0$ | 0.531963 | 0.5319633163 | 3.2e-7 | ✅ |
| $\theta^{(2)}$ | below it, $\partial s_2^*/\partial\gamma<0$ **at $\gamma_{\max}$** | 0.202167 | 0.2021670 | <1e-6 | ✅ |
| $\theta^{(1)}$ | above it, $\partial s_1^*/\partial\gamma<0$ **at $\gamma_{\max}$** | 0.229499 | 0.2294985 | <1e-6 | ✅ |
| $\theta = 0.21$ | the value plotted in Fig. 3 | 0.21 | — | — | ✅ in the band $(\theta^{(2)},\theta^{(1)})$ |
| $a - c = 1$ | normalisation in all figures (footnote 9) | 1 | — | — | ✅ used in all A4 runs |

Both thresholds are defined by footnote 15's criterion — the sign of the
derivative *evaluated at the endpoint* $\gamma_{\max}$ — not by monotonicity over
the whole interval. A3 reproduced them to 6–7 dp but got 0.2294985134 against
A4's 0.2294985504, so quote at most 7 significant digits. A3 also found the
follower's curve already develops an interior hump between $\theta=0.190$ and
$0.1925$; from there up to $\theta^{(2)}$ the curve is down–up–down, so "monotone
throughout" is too strong. See `checks/a3_report.md` F9.

## Computed in A4, not stated in the paper

Mark these clearly on any slide as **own calculation**, not the author's.

### First-mover-advantage frontier, $\pi_1^* = \pi_2^*$

| $\gamma$ | FMA holds only for | max spillover rate |
|---|---|---|
| 0.1 | $\theta < 0.0000534$ | 0.005% |
| 0.3 | $\theta < 0.00150$ | 0.15% |
| 0.5 | $\theta < 0.00867$ | 0.87% |
| 0.7 | $\theta < 0.0393$ | 3.9% |
| 0.8 | $\theta < 0.0960$ | 9.6% |

Do **not** phrase this as "the leader must retain $1-\theta$ of its benefit". In
eq. (1) the leader's own demand shift is $s_1$ regardless of $\theta$; $\theta$
adds a benefit to the rival rather than subtracting one from the leader. The
defensible statement is a bound on the spillover rate. (A3 F10.)

### Three thresholds — they are not the same event

**[own calculation]** Arithmetic on numbers already registered above, plus
$\theta = \gamma/(2-\gamma^2)$ from [[equations]] K-sub. This is the sharpest
thing in the wiki and it is not in the paper.

| $\gamma$ | FMA dies ($\pi_1^*=\pi_2^*$) | leader stops out-investing ($s_1^*=s_2^*$) | deterrence switches ($\gamma/(2-\gamma^2)$) | switch ÷ FMA |
|---|---|---|---|---|
| 0.1 | 0.0000534 | 0.00256 | 0.0503 | ≈ 940× |
| 0.3 | 0.00150 | 0.0169 | 0.1571 | ≈ 105× |
| 0.5 | 0.00867 | 0.0427 | 0.2857 | ≈ 33× |
| 0.7 | 0.0393 | 0.0951 | 0.4636 | ≈ 12× |
| 0.8 | 0.0960 | 0.1527 | 0.5882 | ≈ 6× |

The ordering is strict at every $\gamma$: **FMA frontier < investment frontier <
deterrence switch.** So at the moment the first-mover advantage dies, CSR levels
are still strategic substitutes, the follower still retreats when the leader
invests, and the leader still invests more. **Deterrence has not broken — the
leader is winning the strategic game and losing on profit anyway.**

Two cautions for the slide. The gap narrows sharply with competition, so "two
orders of magnitude" holds only up to about $\gamma = 0.3$ and must not be
stated generally. And these numbers rule out the *wrong* mechanism; they do not
by themselves prove the right one — for that, see the derivative signs on
p. 499, §5.2 ([[csr-spillovers]]).

### Boundary conditions, by binding order

| Condition | Binds at $\gamma$ | $\theta$ |
|---|---|---|
| **follower interiority** ($s_2^*, x_2^* \to 0$) — **binding** | **0.8107359** | 0 |
| leader's stage-1 SOC | 0.830176 | 0 |
| bracket $6-\gamma(4+\gamma(5-\gamma-\gamma^2))=0$ | 0.865759 | — |
| follower's stage-2 SOC | 0.932526 | any |

The follower-interiority root rises in $\theta$: 0.810736 at $\theta=0$, 0.859200
at $\theta=0.2$, 0.932526 at $\theta=1$ — so $\theta=0$ is the worst case and
sets $\gamma_{\max}$.

### Fig. 3 values ($\theta = 0.21$) — follower above leader

| $\gamma$ | $s_1^*$ | $s_2^*$ |
|---|---|---|
| 0.05 | 0.3192 | 0.3452 |
| 0.2 | 0.2846 | 0.3182 |
| 0.4 | 0.2499 | 0.2937 |
| 0.6 | 0.2221 | 0.2785 |
| 0.8 | 0.2082 | 0.2781 |

### Leader's CSR: no spillovers vs $\theta = 0.21$

| $\gamma$ | $s_1^*$ at $\theta=0$ | $s_1^*$ at $\theta=0.21$ |
|---|---|---|
| 0.05 | 0.3229 | 0.3192 |
| 0.4 | 0.2789 | 0.2499 |
| 0.8 | 0.5039 | 0.2082 |

Spillovers **lower** the leader's CSR, sharply so at high competition.

## Conditions, not constants

| Expression | Meaning |
|---|---|
| $\theta < \dfrac{\gamma}{2-\gamma^2}$ | CSR levels are strategic substitutes; also the condition under which the leader's CSR *lowers* the follower's price |
| $\theta > \dfrac{\gamma}{2-\gamma^2}$ | strategic complements |
| $a > c$ | required for Lemma 3 (p. 501) |

## Evidence standard

- Lemma 1 ($\theta=0$: $s_1^*>s_2^*$ and $\pi_1^*>\pi_2^*$) — confirmed on **39
  grid points**, not proved symbolically. The paper omits the proof too.
- Lemma 3 shape classification — **120 grid points** per $\theta$ value.
- State this honestly on any slide that asserts a lemma.
