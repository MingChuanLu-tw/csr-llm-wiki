# A4 verification report — Kopel (2021)

- **Date**: 2026-11-16
- **Target**: `wiki/papers/Kopel2021-CSR.md`
- **Scripts**: `scripts/a4_verify_kopel2021.py`, `scripts/a4_gammamax_hunt.py`, `scripts/a4_gammamax_confirm.py`
- **Raw output**: `checks/a4_run1.txt`, `checks/a4_gammamax.txt`, `checks/a4_gammamax_confirm.txt`
- **Environment**: Python 3.9, sympy 1.14.0, mpmath (30 dp)
- **Verdict**: **PASS.** 12/12 symbolic checks, 3/3 numerical thresholds, 3/3 lemmas.

## Method

The script does **not** plug numbers into the paper's stated formulas. It re-derives
the whole three-stage game from the inverse demand system eq. (1) with sympy —
invert demand, solve the stage-3 price FOCs, solve the stage-2 follower FOC,
substitute the reaction function into the leader's profit, solve the stage-1 FOC —
and only then compares each derived expression with the one transcribed into the
wiki page. A pass therefore confirms **both** the paper's algebra and the
transcription at the same time.

## 1. Symbolic checks — 12/12 PASS

| Equation | Result |
|---|---|
| eq. (2) direct demand $x_1$ | PASS |
| eq. (2) direct demand $x_2$ | PASS |
| eq. (3) stage-3 price $p_1(s_1,s_2)$ | PASS |
| eq. (3) stage-3 price $p_2(s_1,s_2)$ | PASS |
| eq. (4) follower reaction $s_2(s_1)$ | PASS |
| eq. (5) leader equilibrium $s_1^*$ | PASS |
| eq. (6) follower equilibrium $s_2^*$ (incl. $N$) | PASS |
| eq. (7) equilibrium price $p_1^*$ | PASS |
| eq. (7) equilibrium price $p_2^*$ | PASS |
| profit $\pi_1^*$ (p. 497) | PASS |
| profit $\pi_2^*$ (p. 497) | PASS |
| $s_1^*-s_2^*$ closed form at $\theta=0$ (p. 497) | PASS |

Every equation transcribed into the wiki page is exact, including the long
numerator $N$ in eq. (6). **The §5.4 concern about the $\pi_1^*$/$\pi_2^*$
asymmetry is resolved: the asymmetry is genuine, not a transcription error.**
$\pi_1^*$ really is linear in $s_1^*$ while $\pi_2^*$ is quadratic in $s_2^*$,
because the leader's first-order condition lets one factor of $s_1^*$ be
substituted out and the follower's does not.

Supporting facts recovered:

- Price-stage second-order condition: $\partial^2\pi_i/\partial p_i^2 = 2/(\gamma^2-1) < 0$ for $\gamma<1$. Hessian determinant $=(4-\gamma^2)/(1-\gamma^2)^2 > 0$. The price stage is well behaved throughout.
- The sign of the follower's reaction slope factors cleanly:
  $\dfrac{ds_2}{ds_1} = \dfrac{(2-\gamma^2)((2-\gamma^2)\theta-\gamma)}{12-20\gamma^2+8\gamma^4-\gamma^6}
  \propto (\gamma^2-2)(\gamma^2\theta + \gamma - 2\theta)$,
  which changes sign exactly at $\theta = \gamma/(2-\gamma^2)$, as the paper states on p. 496.
  **Corrected after A3 F2** — this line originally carried a leading minus sign, having
  dropped the sign of sympy's denominator, which inverted the implication.

## 2. Numerical thresholds — 3/3 reproduced

| Quantity | Paper | Recomputed | Difference |
|---|---|---|---|
| turning point of $s_1^*$ at $\theta=0$ | 0.531963 | 0.5319633163 | 3.2e-7 |
| $\theta^*$ above which $s_1^*$ is monotone decreasing | 0.229499 | 0.2294985504 | 4.5e-7 |
| $\theta^*$ below which $s_2^*$ is monotone decreasing | 0.202167 | 0.2021670222 | 2.2e-8 |

All three agree with the paper to the precision the paper reports. The two
$\theta$ thresholds were reproduced using the paper's own stated method
(footnote 15, p. 501): evaluate $\partial s_i^*/\partial\gamma$ at
$\gamma=\gamma_{\max}$ and find where the sign changes.

### 2a. $\gamma_{\max} = 0.810736$ — initially unexplained, now resolved

This one took three runs. The paper says only that $\gamma<\gamma_{\max}=0.810736$
"guarantees that the equilibrium of the game is in the interior and all
second-order conditions are satisfied" (p. 495), without saying which condition
binds. The first run showed it is **not**:

| Candidate | Binds at | Not 0.810736 |
|---|---|---|
| denominator $D = 0$ (at $\theta=0$) | 0.830176 | ✗ |
| leader's stage-1 SOC (at $\theta=0$) | 0.830176 | ✗ |
| follower's stage-2 SOC | 0.932526 | ✗ |
| $12-20\gamma^2+8\gamma^4-\gamma^6 = 0$ | 0.932526 | ✗ |
| bracket $6-\gamma(4+\gamma(5-\gamma-\gamma^2))=0$ | 0.865759 | ✗ |

The second run swept every equilibrium object for a boundary crossing. The match
is **interiority of the follower at $\theta = 0$**: both $s_2^*$ and $x_2^*$ reach
zero at $\gamma = 0.810735877$. The third run confirms this is the root of the
eq. (6) numerator evaluated at $\theta=0$,

$$
N(\gamma,0) = 18 + 6\gamma - 35\gamma^2 - 15\gamma^3 + 15\gamma^4 + 7\gamma^5 - 2\gamma^6 - \gamma^7 = 0
$$

whose only root in $(0,1)$ is $\gamma = 0.8107358771227719$, i.e. **0.810736 to
six decimal places**. Exact match.

It is also the *binding* constraint: the root rises monotonically in $\theta$
(0.8107 at $\theta=0$, 0.8592 at $\theta=0.2$, 0.9325 at $\theta=1$ — A3 F22
corrected a typo here, 0.8599, against the script output 0.8591995836), so the
no-spillover benchmark is the worst case, and every second-order condition fails
only at larger $\gamma$.

**Economic reading, and a discussion point.** $\gamma_{\max}$ is the point at
which the leader's strategic over-investment drives the follower's CSR — and its
output — to zero. The bound is not a technical nuisance; it marks where the
duopoly would collapse to a monopoly. The paper's claim that the leader's profit
advantage "can not only be sustained, but made even larger" as products become
more homogeneous (p. 499) is therefore evaluated right up against the edge where
the follower is squeezed out of the market entirely. Worth raising in the talk.

## 3. Lemmas — 3/3 confirmed

**Lemma 1** ($\theta=0$): verified on 39 grid points across $(0,\gamma_{\max})$.
$s_1^*>s_2^*$ holds everywhere; $\pi_1^*>\pi_2^*$ holds everywhere. The closed-form
gap expression on p. 497 is exact.

**Lemma 2** (FMA needs small $\theta$): the frontier $\pi_1^*=\pi_2^*$ was computed
directly. The paper's qualitative wording is "in fact very low" (p. 491); the
"rather small" phrase on p. 500 refers to the $s_1^*>s_2^*$ region, not the FMA
region (A3 F15). Either way it is far smaller than the prose suggests:

| $\gamma$ | FMA holds only for |
|---|---|
| 0.1 | $\theta < 0.0000534$ |
| 0.3 | $\theta < 0.00150$ |
| 0.5 | $\theta < 0.00867$ |
| 0.7 | $\theta < 0.0393$ |
| 0.8 | $\theta < 0.0960$ |

**This is the sharpest result in the paper and the author never states it
numerically.** At moderate competition ($\gamma=0.3$) the spillover rate must
stay below **0.15%**. (A3 F10: do not phrase this as "the leader retains
99.85% of its benefit" — $\theta$ adds a benefit to the rival rather than
subtracting one from the leader.) The paper's qualitative wording understates it
by orders of magnitude at low $\gamma$. Recommended as a headline slide.

**Lemma 3** (shape by $\theta$ band): classified numerically on 120 grid points.

| $\theta$ | $s_1^*$ | $s_2^*$ |
|---|---|---|
| 0 | U-shaped | decreasing |
| 0.15 | U-shaped | decreasing |
| **0.21** | **U-shaped** | **U-shaped** |
| 0.25 | decreasing | U-shaped |
| 0.5 | decreasing | U-shaped |
| 0.9 | decreasing | U-shaped |

Exactly matches the paper's two thresholds, and confirms the A1 reading that the
band $0.202167<\theta<0.229499$ is where both firms are U-shaped — which is
precisely the case Fig. 3 plots at $\theta=0.21$.

## 4. Figure claims

**Fig. 3 ($\theta=0.21$): the follower is above the leader.** Confirmed at every
sampled $\gamma$ — the A1 page is correct:

| $\gamma$ | $s_1^*$ | $s_2^*$ |
|---|---|---|
| 0.05 | 0.3192 | 0.3452 |
| 0.2 | 0.2846 | 0.3182 |
| 0.4 | 0.2499 | 0.2937 |
| 0.6 | 0.2221 | 0.2785 |
| 0.8 | 0.2082 | 0.2781 |

**Fig. 1 vs Fig. 3 levels.** The claim A1 removed as unsupported can now be
settled, and it was removed correctly — the removed claim was backwards:

| $\gamma$ | $s_1^*$ at $\theta=0$ | $s_1^*$ at $\theta=0.21$ |
|---|---|---|
| 0.05 | 0.3229 | 0.3192 |
| 0.4 | 0.2789 | 0.2499 |
| 0.8 | 0.5039 | 0.2082 |

The leader's CSR is **lower** with spillovers, not higher, and dramatically so at
high competition. Good that it was not asserted from reading the plots.

## 5. Items still open

1. **Figures not regenerated.** A4 verified the underlying functions but did not
   redraw Figs. 1–3. If the deck reproduces the figures, they should be plotted
   from these verified expressions rather than copied from the PDF (the paper is
   CC BY 4.0, so copying is permitted with attribution — but plotting is safer
   and lets us annotate).
2. **Lemma 1 and Lemma 2 checked numerically, not proved symbolically.** The
   paper omits both proofs ("follows from a simple comparison"). A grid check is
   strong evidence, not a proof. Acceptable for a seminar; worth stating honestly
   on the slide.
3. **$a>c$ assumption** in Lemma 3 was not stress-tested; all runs used $a-c=1$
   per footnote 9.

## 6. Actions taken

- `wiki/papers/Kopel2021-CSR.md` §10 updated: verification queue closed, results folded in.
- $\gamma_{\max}$ explanation added to the wiki page §4.3 — it is **new information
  not in the paper** and is marked as such.
- Lemma 2 frontier table added to the wiki page §7.2.
