# First-mover advantage (FMA)

**Sources so far**: [[Kopel2021-CSR]] (1 of 5 planned)

## Definition used in this wiki

Kopel asks whether "the firm which invests in CSR before the rival, always
achieves a **first-mover advantage**" (p. 490) and settles it by comparing
equilibrium profits (Lemma 1, p. 499; Lemma 2, p. 500). So in this wiki an FMA
exists when the firm that commits first earns higher equilibrium profit than the
firm that follows:

$$
\pi_1^* > \pi_2^*
$$

This is a statement about **profit**, not about investment level. Keep the two
apart — they are different conditions and they do not coincide.

## Two distinct comparisons

Kopel (2021) tracks both, and Fig. 2 (p. 500) draws them as two separate curves
in the $(\gamma,\theta)$ plane:

| Comparison | Meaning | Curve in Fig. 2 |
|---|---|---|
| $\pi_1^* \gtrless \pi_2^*$ | who earns more — **this is the FMA** | bold |
| $s_1^* \gtrless s_2^*$ | who invests more in CSR | dashed |

**[our reading]** The dashed curve lies above the bold one, so there is a band
where the leader invests more but still earns less. **Investing more is not the
same as winning.** This is our reading of Fig. 2, not a sentence in the paper,
but it is verified: the $s_1^*=s_2^*$ frontier sits above the $\pi_1^*=\pi_2^*$
frontier at every $\gamma$ tested (0.0169 vs 0.0015 at $\gamma=0.3$;
`checks/a3_report.md` C8).

Caution for the talk: the sentence on p. 500 describes the dashed-curve regions
the other way round. It contradicts the figure's own labels and Lemma 2, and we
follow the figure. See [[Kopel2021-CSR]] §7.2.

## How large is the FMA region?

**[own calculation]** Not a table in the paper. Computed in `checks/a4_report.md`
§3 and reproduced independently by A3:

| $\gamma$ | FMA holds only for |
|---|---|
| 0.1 | $\theta < 0.0000534$ |
| 0.3 | $\theta < 0.00150$ |
| 0.5 | $\theta < 0.00867$ |
| 0.7 | $\theta < 0.0393$ |
| 0.8 | $\theta < 0.0960$ |

At $\gamma = 0.3$ the spillover rate must stay below **0.15%**. The region widens
as competition intensifies, but never becomes large within the admissible range
$\gamma < \gamma_{\max} = 0.810736$.

The paper's own wording is qualitative: the level of spillovers that sustains an
FMA is "in fact very low" (p. 491).

## The prior debate

The framing on p. 490 sets two positions against each other:

| Position | Authors | Claim |
|---|---|---|
| FMA is sustainable | Tetrault Sirsly & Lamertz (2008) | if the CSR initiative is "central to the firm mission, visible to stakeholders and with firm-specific benefits beyond those of public goods" (p. 490) |
| FMA erodes | Reinhardt (1998), Vogel (2005) | CSR is hard to keep specific to a firm's strategy and to profit from in the long run (p. 490) |
| Industry practice | The Economist (2008), quoted p. 490 | one consultancy advises clients to be "number two or three on corporate responsibility rather than number one" |

**But the conclusion does not pick a winner the way the framing suggests.** On
p. 502 Kopel groups Tetrault Sirsly & Lamertz **with** Burke & Logsdon (1996) and
Reinhardt (1998) as all arguing that an FMA is difficult to sustain, and on
p. 491 he writes that "in line with Tetrault Sirsly and Lamertz (2008) I find
that a first-mover advantage exists" when CSR is firm-specific. The paper
**formalises TS&L's condition** — it does not refute them. It separately "gives
substance to the critical assessment of Vogel (2005)" (p. 502).

**[our reading]** What the model adds is a magnitude: the condition TS&L state
qualitatively turns out to be met only in a very narrow region.

## Where the result comes from (pp. 498–499)

The leader's advantage rests on a [[strategic-commitment]] effect: by committing
to high CSR it induces the follower to cut its own CSR (pp. 498–499).

**[our reading]** What spillovers do *not* do is break that deterrence — at least
not anywhere near the frontier. The substitutes→complements switch sits at
$\theta = \gamma/(2-\gamma^2)$, which is 6× to 940× higher than the FMA frontier
depending on $\gamma$ (see [[numbers]], "Three thresholds"). At $\gamma = 0.3$
the FMA is already gone at $\theta \approx 0.0015$ while deterrence holds until
$\theta \approx 0.157$.

What kills the FMA instead is that $\theta$ is a **transfer of incentive**, not a
neutral leak: it lowers the leader's marginal return to CSR and raises the
follower's, continuously from $\theta = 0$ upward (p. 499, §5.2). The follower
captures part of the leader's demand shift without paying for it. So the leader
keeps deterring the follower, keeps out-investing it — and still loses on profit.
See [[csr-spillovers]].

## Open issues

- The leader–follower order is **exogenous**: "in my paper the leader–follower
  structure is exogenously given" (p. 502). **[our reading]** Nobody chooses to
  move first, so the model cannot say whether moving first is worth it ex ante.
  See [[open-questions]] Q2.
- Lemmas 1 and 2 are confirmed numerically, not proved symbolically; the paper
  omits both proofs (pp. 499, 500).

## Links

[[csr-spillovers]] · [[appropriability]] · [[strategic-commitment]] ·
[[competition-intensity]] · [[Kopel2021-CSR]]
