# Overview — CSR leadership and first-mover advantage

**Scope**: when does committing to CSR *before* a competitor pay off?

**Status**: 5 sources ingested — [[Kopel2021-CSR]] at full depth (verified and
twice reviewed) and four others at **light** depth (read and summarised only, no
verification; see [[sources]]). The talk is about Kopel; the other four exist so
the concept layer has something to compare against.

---

## The question in one paragraph

A firm that invests in socially responsible activities before its rival may raise
consumers' willingness to pay for its product and so earn more (pp. 489–490).
But if the rival can copy or benefit from that investment, the leader has paid
for an advantage it cannot keep (p. 494). Whether CSR leadership pays therefore
turns on **appropriability**: how much of the benefit stays with the firm that
paid for it.

## The answer so far

From [[Kopel2021-CSR]], verified in `checks/a4_report.md` and reviewed in
`checks/a3_report.md`:

1. With **no spillovers**, the leader invests more and earns more — a genuine
   [[first-mover-advantage]] (Lemma 1, p. 499).
2. That region is **tiny** (Lemma 2, p. 500). The paper calls the sustaining
   level of spillovers "in fact very low" (p. 491); **[own calculation]** at
   $\gamma = 0.3$ the frontier is $\theta < 0.0015$, a spillover rate under
   0.15%. Otherwise the follower gets a second-mover advantage.
3. The effect of **competition** on CSR is non-monotone and *asymmetric between
   the two roles* (Lemma 3, pp. 500–501), against a **theoretical** literature
   with conflicting conclusions (p. 492).
4. Industry pressure toward **convergent CSR** — leaders themselves "pressure and
   support" rivals to imitate (p. 491) — makes it "impossible for the CSR leader
   to profit from its leadership" (p. 502).

## The causal chain

```
appropriability (low θ)
        │
        ▼
leader's commitment deters the follower   ← breaks last:  θ > γ/(2−γ²)   (0.157 at γ=0.3)
        │
        ▼
leader over-invests  (s₁* > s₂*)          ← breaks next:  θ > 0.0169     (at γ=0.3)
        │
        ▼
leader earns more  (π₁* > π₂*)  = FMA     ← breaks FIRST: θ > 0.0015     (at γ=0.3)
```

Read the break points from the bottom up. The FMA fails **first**, about 100×
earlier than deterrence at $\gamma = 0.3$. See [[numbers]], "Three thresholds".

**[our reading]** The chain is our synthesis of pp. 494–500, not a figure in the
paper. Each arrow is a separate condition, and they do **not** coincide: there is
a band where the leader invests more but still earns less. See
[[first-mover-advantage]] for the two curves in Fig. 2.

## Concept map

| Page | What it covers |
|---|---|
| [[first-mover-advantage]] | the definition ($\pi_1^*>\pi_2^*$), how small the region is, the prior debate |
| [[csr-spillovers]] | the parameter $\theta$, its asymmetric effect, the substitutes/complements switch |
| [[appropriability]] | the economics behind $\theta$ — Patagonia vs StarKist, what makes CSR defensible |
| [[competition-intensity]] | the parameter $\gamma$, the three effects, the U-shape, the $\gamma_{\max}$ bound |
| [[strategic-commitment]] | why sequencing matters, over-investment, what the commitment rests on |
| [[rival-exclusion]] | **cross-source**: three models independently drive a rival to zero output |
| [[csr-modelling-choices]] | **cross-source**: "CSR" is five different formal objects, and results do not transfer |

## Reference layer

| Page | Use |
|---|---|
| [[index]] | catalogue of every page, with node status |
| [[glossary]] | one canonical meaning per symbol |
| [[equations]] | canonical LaTeX; B8 checks slides against it |
| [[numbers]] | every citable figure with verification status; B10 checks slides against it |
| [[sources]] | what has been ingested, and candidates for sources 2–5 |
| [[open-questions]] | discussion material for the seminar |

## Source pages

| Page | Depth |
|---|---|
| [[Kopel2021-CSR]] — Kopel (2021), *Decis. Econ. Finan.* 44:489–505 | **full** |
| [[Chen2021-OptimalCSR]] — Chen et al. (2021) | light |
| [[HiroseMatsumura2022-CommonOwnershipECSR]] — Hirose & Matsumura (2022) | light |
| [[BarcenaRuizSagasta2021-CrossOwnershipCSR]] — Bárcena-Ruiz & Sagasta (2021) | light |
| [[XingLee2023-EnvironmentalRD]] — Xing & Lee (2023) | light |

## What the four extra sources changed

They were not a box-ticking exercise. Two things became visible that one paper
could not show:

1. **[[rival-exclusion]]** — three independent models reach a corner where one
   firm's output goes to zero. In Kopel that corner is presented as a technical
   bound; in the others it is a result or a deliberate strategy.
2. **[[csr-modelling-choices]]** — the five papers formalise "CSR" five
   different ways (demand shift, objective weight, emissions cap, delegation
   parameter). **A result in one category does not transfer to another**, which
   bounds how far Kopel's conclusion can be generalised in the talk.

## What is still **not** known

- whether the empirical literature supports the U-shape (no empirical source ingested);
- whether endogenous timing changes the answer (needs Kopel & Löffler 2012);
- whether the three exclusion results survive non-linear demand or free entry.

Tracked in [[sources]] and [[open-questions]]. A slide claim beyond the wiki is
not permitted by `AGENTS.md` §3.
