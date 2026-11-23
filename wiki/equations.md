# Equation register

Canonical LaTeX for every equation the deck may cite. Node **B8** checks slide
equations against this file: a slide equation must either appear here verbatim or
be derivable from entries here. Status column records A4 verification.

Symbols: see [[glossary]]. Source: [[Kopel2021-CSR]] unless stated.

| ID | Source ref | Status |
|---|---|---|
| K-gen | p. 493, unnumbered | A3 ✅ (page image) ² |
| K-1 | eq. (1), p. 494 | A3 ✅ (page image) ² |
| K-2 | eq. (2), p. 495 | A4 ✅ |
| K-profit | p. 495, unnumbered | A3 ✅ (page image) ² |
| K-theta | p. 499, §5.2 | A3 ✅ |
| K-fma | definition, pp. 490, 499–500 | A3 ✅ |
| K-3 | eq. (3), p. 495 | A4 ✅ |
| K-4 | eq. (4), p. 496 | A4 ✅ |
| K-5 | eq. (5), p. 496 | A4 ✅ |
| K-6 | eq. (6), p. 496 | A4 ✅ |
| K-7 | eq. (7), pp. 496–497 | A4 ✅ |
| K-pi | p. 497, unnumbered | A4 ✅ |
| K-gap | p. 497, unnumbered | A4 ✅ |
| K-sub | p. 496 / footnote 13 | A3 ✅ (corrected) ¹ |

¹ K-sub is a *derived* quantity, not one of the paper's printed equations, so it was never in A4's twelve-equation comparison set. A4 passed it while it carried a sign error; A3 caught and corrected it. **Derived entries need their own check.**

² K-gen, K-1 and K-profit are A4's **premises** — A4 re-derived everything *from* them, so it could not confirm them; a premise is not verified by what follows from it. A3 round 2 rendered pp. 493–495 as images and checked all three against the printed page. Same defect class as the K-sub footnote: a check cannot validate its own starting point.

---

### K-gen — general inverse demand (both spillovers)

$$
p_1 = a + (s_1 + \theta_1 s_2) - x_1 - \gamma x_2, \qquad
p_2 = a + (s_2 + \theta_2 s_1) - x_2 - \gamma x_1
$$

### K-1 — inverse demand used in the paper ($\theta_1 = 0$, $\theta_2 = \theta$)

$$
p_1 = a + s_1 - x_1 - \gamma x_2, \qquad
p_2 = a + (s_2 + \theta s_1) - x_2 - \gamma x_1
$$

### K-2 — direct demand

$$
x_1 = \frac{a(1-\gamma) + (1-\gamma\theta)s_1 - \gamma s_2}{1-\gamma^2}
      - \frac{1}{1-\gamma^2}p_1 + \frac{\gamma}{1-\gamma^2}p_2
$$

$$
x_2 = \frac{a(1-\gamma) + s_2 - (\gamma-\theta)s_1}{1-\gamma^2}
      - \frac{1}{1-\gamma^2}p_2 + \frac{\gamma}{1-\gamma^2}p_1
$$

### K-profit — profits net of CSR cost

$$
\pi_1 = (p_1-c)\,x_1 - s_1^2, \qquad \pi_2 = (p_2-c)\,x_2 - s_2^2
$$

Generic form, for use on a slide where the index does not need spelling out:

$$
\pi_i = (p_i - c)\,x_i - s_i^2
$$

### K-theta — spillovers move the two incentives in opposite directions

$$
\frac{\partial}{\partial\theta}\left(\frac{\partial\pi_1}{\partial s_1}\right) < 0
$$

$$
\frac{\partial}{\partial\theta}\left(\frac{\partial\pi_2}{\partial s_2}\right) > 0
$$

Stated in the text at p. 499, §5.2. This pair is the mechanism that actually
kills the first-mover advantage — see [[numbers]] "Three thresholds" for why it
is not the substitutes/complements switch.

### K-fma — the definition of a first-mover advantage

$$
\pi_1^* > \pi_2^*
$$

Not an equation of the paper's but the definition it works with throughout
(pp. 490, 499–500). Registered so a slide may state it. See
[[first-mover-advantage]] for why this is **not** the same as $s_1^* > s_2^*$.

### K-3 — stage-3 equilibrium prices given $(s_1,s_2)$

$$
p_1(s_1,s_2) = \frac{a(2+\gamma)(1-\gamma) + (2+\gamma)c + (2-\gamma^2-\gamma\theta)s_1 - \gamma s_2}{4-\gamma^2}
$$

$$
p_2(s_1,s_2) = \frac{a(2+\gamma)(1-\gamma) + (2+\gamma)c + (2-\gamma^2)s_2 + ((2-\gamma^2)\theta-\gamma)s_1}{4-\gamma^2}
$$

### K-4 — follower's stage-2 reaction function

$$
s_2(s_1) = \frac{(2-\gamma^2)\big((a-c)(2+\gamma)(1-\gamma) + s_1((2-\gamma^2)\theta-\gamma)\big)}{12-20\gamma^2+8\gamma^4-\gamma^6}
$$

### K-sub — strategic substitutes / complements switch

$$
\frac{ds_2}{ds_1} = \frac{(2-\gamma^2)\big((2-\gamma^2)\theta-\gamma\big)}{12-20\gamma^2+8\gamma^4-\gamma^6}
\qquad\Longrightarrow\qquad
\frac{ds_2}{ds_1} < 0 \iff \theta < \frac{\gamma}{2-\gamma^2}
$$

The denominator is positive for $\gamma<\gamma_{\max}$ (7.48 at $\gamma=0.5$), so the sign is carried by $(2-\gamma^2)\theta-\gamma$. Equivalently $\frac{ds_2}{ds_1}\propto(\gamma^2-2)(\gamma^2\theta+\gamma-2\theta)$.

The explicit derivative is ours; the paper states only the threshold. **Corrected after A3 F2** — an earlier version wrote this proportionality with the opposite sign, which inverted the implication.

### Shared denominator $D$ (A4 notation)

$$
D = \big(12-20\gamma^2+8\gamma^4-\gamma^6\big)^2 - \big(1-\gamma^2\big)\big(6-\gamma(4\theta+\gamma(5-\gamma\theta-\gamma^2))\big)^2
$$

### K-5 — leader's equilibrium CSR

$$
s_1^* = \frac{(a-c)(1-\gamma^2)\big[6-\gamma(4+\gamma(5-\gamma-\gamma^2))\big]\big[6-\gamma(4\theta+\gamma(5-\gamma\theta-\gamma^2))\big]}{D}
$$

### K-6 — follower's equilibrium CSR

$$
s_2^* = \frac{(a-c)(1-\gamma)(2-\gamma^2)\,N}{D}
$$

$$
N = 6(3+\theta) + 2\gamma(3+5\theta-2\theta^2) - \gamma^2(35+\theta+4\theta^2) - \gamma^3(15+6\theta-\theta^2) + \gamma^4(15+\theta^2) + \gamma^5(7+\theta) - 2\gamma^6 - \gamma^7
$$

### K-7 — equilibrium prices

$$
p_1^* = c + \frac{12-20\gamma^2+8\gamma^4-\gamma^6}{6-\gamma(4\theta+\gamma(5-\gamma\theta-\gamma^2))}\,s_1^*, \qquad
p_2^* = c + \frac{(4-\gamma^2)(1-\gamma^2)}{2-\gamma^2}\,s_2^*
$$

### K-pi — equilibrium profits

$$
\pi_1^* = \frac{(a-c)\big(6-\gamma(4+\gamma(5-\gamma-\gamma^2))\big)}{6-\gamma(4\theta+\gamma(5-\gamma\theta-\gamma^2))}\,s_1^*, \qquad
\pi_2^* = \frac{(4-\gamma^2)(2-\gamma^2)^2-4}{(2-\gamma^2)^2}\,(s_2^*)^2
$$

The asymmetry (linear in $s_1^*$, quadratic in $s_2^*$) is genuine — A4 confirmed
it follows from substituting out one factor using the leader's stage-1 FOC.

### K-gap — investment gap in the benchmark ($\theta = 0$)

$$
s_1^* - s_2^* = \frac{\gamma^2(2+\gamma)}{(1+\gamma)(3-\gamma^2)\big(6-\gamma(4+\gamma(5-\gamma-\gamma^2))\big)}\,s_1^* > 0
\quad\text{for } 0<\gamma\le\gamma_{\max}
$$

### Second-order conditions (A4, not in the paper)

$$
\frac{\partial^2\pi_i}{\partial p_i^2} = \frac{2}{\gamma^2-1} < 0, \qquad
\det H_{\text{price}} = \frac{4-\gamma^2}{(1-\gamma^2)^2} > 0
$$
