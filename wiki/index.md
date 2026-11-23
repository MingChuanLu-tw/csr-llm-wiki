# Index

Catalogue of every page in the wiki. A5 (lint) checks that this list matches the
files on disk and that no page is orphaned.

**Start here**: [[overview]]

## Source pages — `wiki/papers/`

| Page | Source | A1 | A3 | A4 | A6 |
|---|---|---|---|---|---|
| [[Kopel2021-CSR]] | Kopel (2021), *Decis. Econ. Finan.* 44:489–505 — **FULL depth** | ✅ | ✅¹ | ✅ | ✅ |
| [[Chen2021-OptimalCSR]] | Chen et al. (2021), *Manage. Decis. Econ.* 42:177–184 — light | ✅ | — | — | ✅ |
| [[HiroseMatsumura2022-CommonOwnershipECSR]] | Hirose & Matsumura (2022), *Energy Econ.* 114:106269 — light | ✅ | — | — | ✅ |
| [[BarcenaRuizSagasta2021-CrossOwnershipCSR]] | Bárcena-Ruiz & Sagasta (2021), *Manchester School* 89:367–384 — light | ✅ | — | — | ✅ |
| [[XingLee2023-EnvironmentalRD]] | Xing & Lee (2023), *Manage. Decis. Econ.* 44:2684–2696 — light | ✅ | — | — | ✅ |

**Light** = read and summarised; no symbolic verification, no independent review. See [[sources]].

¹ A3 round 1 returned FAIL (5 blockers, 14 should-fix, 9 minor); round 2, after the fixes, returned **PASS WITH FIXES** — no blockers remain and 26 of 29 findings are fully fixed. The round-2 residue was addressed in turn. Two rounds is the `AGENTS.md` §8a maximum. Report: `checks/a3_report.md`. A5 (lint) ran afterwards: the mechanical half passes 10/10 (`scripts/a5_lint.py`, `checks/a5_lint_run3.txt`) and the judgement half returned FAIL with one blocker, now fixed (`checks/a5_report.md`). **A6: signed off by MingLu 2026-11-17.** All Graph A nodes complete; Graph B started.

## Concept pages — `wiki/concepts/`

| Page | One line | Sources |
|---|---|---|
| [[first-mover-advantage]] | $\pi_1^*>\pi_2^*$; the region is far smaller than the paper's prose implies | 1 |
| [[csr-spillovers]] | $\theta$ transfers incentive from leader to follower; switches strategic substitutes to complements | 1 |
| [[appropriability]] | the economics behind $\theta$; comes from an asset the rival lacks | 1 |
| [[competition-intensity]] | $\gamma$; markup vs demand vs strategic effects; the U-shape and its reversal | 1 |
| [[strategic-commitment]] | why sequencing creates over-investment, and the three links that can break | 1 |
| [[rival-exclusion]] | three independent models drive a rival to zero output — the clearest cross-source pattern | 3 |
| [[csr-modelling-choices]] | "CSR" is five different formal objects across the five sources, and results do not transfer between them | 5 |

## Reference pages — `wiki/`

| Page | Role in the graph |
|---|---|
| [[overview]] | entry point and concept map |
| [[glossary]] | canonical symbols; keeps sources 2–5 consistent |
| [[equations]] | canonical LaTeX — **B8 checks slide equations against this** |
| [[numbers]] | every citable number with provenance — **B10 checks slide numbers against this** |
| [[sources]] | ingest register and candidates for sources 2–5 |
| [[open-questions]] | seminar discussion material |

## Synthesis pages — `wiki/syntheses/`

*(empty — saved query answers go here as they are produced)*

## Outside the wiki

| Path | Contents |
|---|---|
| `raw/papers/` | source PDFs, read-only |
| `checks/` | verification reports — `a4_report.md` and raw script output |
| `scripts/` | the sympy/mpmath verification scripts |
| `notes/` | speaker script and evidence cards (Graph B) |
| `slides_html/` | the deck (Graph B) |
| `log.md` | run log and reflection table |
| `AGENTS.md` | the schema all agents follow |
| `需求摘要.md` | confirmed requirements |

## Counts

- Sources ingested: **5** (1 full depth, 4 light) — assignment requirement met
- Concept pages: 7
- Reference pages: 6
- Syntheses: 0
- Open questions: 9 (0 closed)
