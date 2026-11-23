# 完整 git 歷史（快照說明）

公開 repo 是**單一 commit 的快照**，原因是原始 repo 的歷史裡含有五篇論文的 PDF，
其中四篇是付費期刊論文，不能公開散布（見 `raw/papers/README.md`）。

代價是：`繳交/繳交內容.md` 第六節引用了 8 個 commit hash 來佐證「哪些修改是本輪才做的」，
那些 hash 在公開 repo 裡不會解析。這份檔案保存那段歷史，讓那些引用仍然可查。

第六節引用到的 commit：

| hash | 它在第六節裡被用來證明什麼 |
|---|---|
| `de8d030` | 初始 commit。§8a 獨立審查、B3 證據卡、A3/A5 拆分**在 A1 還沒跑之前就存在**——所以它們不是本輪的修改 |
| `5acf804` | A1 以 Opus 重跑，同時新增 `AGENTS.md` §10 的 model/effort 政策（本輪真正的 schema 修改之一） |
| `39bd252` | A4 符號驗證。**F2 符號錯與 F4 捏造引文的字串首次進 repo 都在這裡**，不在 A1 的 commit 裡 |
| `19779f3` | A2 建概念層，新增四張登錄表與「A2 writes」條款 |
| `6854f91` | 修完 A3 的 5 個 blocker，同時新增 §3 的「標記推論」與「論文自相矛盾」規則 |
| `e2d664a` | A3 第二輪，新增 §3 的標籤作用範圍定義與「引號即逐字」規則 |
| `8d0f2fe` | 交件包。**三個計數寫錯是在這裡被自己抓到的**，早於任何對第六節的審查 |
| `5c919b9` | 第六節改寫；commit 計數錨定在這個版本 |

兩個可自行驗證的指令（需要原始 repo）：

```bash
git log -S'Spillovers must be very low' --oneline --all   # → 39bd252，不含 5acf804
git show de8d030:AGENTS.md | grep 'must not review its own text'
```

---

## git log（完整，含每個 commit 動到的檔案）

### de8d030 — init: project skeleton and source PDF

*2026-11-16 19:56*

- `A` .gitignore
- `A` AGENTS.md
- `A` CLAUDE.md
- `A` checks/.gitkeep
- `A` notes/.gitkeep
- `A` raw/papers/Kopel2021-CSR.pdf
- `A` slides_html/.gitkeep
- `A` wiki/concepts/.gitkeep
- `A` wiki/entities/.gitkeep
- `A` wiki/papers/.gitkeep
- `A` wiki/syntheses/.gitkeep
- `A` "\351\234\200\346\261\202\346\221\230\350\246\201.md"

### 5acf804 — A1: rewrite Kopel2021-CSR wiki page on Opus 5

*2026-11-16 20:08*

- `M` AGENTS.md
- `A` log.md
- `A` wiki/papers/Kopel2021-CSR.md

### 39bd252 — A4: verify Kopel2021 symbolically and numerically

*2026-11-16 20:16*

- `A` checks/a4_gammamax.txt
- `A` checks/a4_gammamax_confirm.txt
- `A` checks/a4_report.md
- `A` checks/a4_run1.txt
- `M` log.md
- `A` scripts/a4_gammamax_confirm.py
- `A` scripts/a4_gammamax_hunt.py
- `A` scripts/a4_verify_kopel2021.py
- `M` wiki/papers/Kopel2021-CSR.md

### 19779f3 — A2: build concept layer, reference registers, overview and index

*2026-11-16 20:26*

- `M` AGENTS.md
- `M` log.md
- `A` wiki/concepts/appropriability.md
- `A` wiki/concepts/competition-intensity.md
- `A` wiki/concepts/csr-spillovers.md
- `A` wiki/concepts/first-mover-advantage.md
- `A` wiki/concepts/strategic-commitment.md
- `A` wiki/equations.md
- `A` wiki/glossary.md
- `A` wiki/index.md
- `A` wiki/numbers.md
- `A` wiki/open-questions.md
- `A` wiki/overview.md
- `A` wiki/sources.md

### c4934b8 — A3: independent review report (FAIL - 5 blockers, 14 should-fix, 9 minor)

*2026-11-16 23:29*

- `A` checks/a3_report.md

### 6854f91 — A3 fixes: all 5 blockers, 14 should-fix and minors

*2026-11-16 23:37*

- `M` AGENTS.md
- `M` checks/a4_report.md
- `M` log.md
- `M` scripts/a4_verify_kopel2021.py
- `M` wiki/concepts/appropriability.md
- `M` wiki/concepts/competition-intensity.md
- `M` wiki/concepts/csr-spillovers.md
- `M` wiki/concepts/first-mover-advantage.md
- `M` wiki/concepts/strategic-commitment.md
- `M` wiki/equations.md
- `M` wiki/glossary.md
- `M` wiki/index.md
- `M` wiki/numbers.md
- `M` wiki/open-questions.md
- `M` wiki/overview.md
- `M` wiki/papers/Kopel2021-CSR.md
- `M` wiki/sources.md

### e2d664a — A3 round 2: fix the residue, including two defects my own fixes introduced

*2026-11-17 00:07*

- `M` AGENTS.md
- `M` checks/a3_report.md
- `M` log.md
- `M` wiki/concepts/appropriability.md
- `M` wiki/concepts/csr-spillovers.md
- `M` wiki/concepts/strategic-commitment.md
- `M` wiki/equations.md
- `M` wiki/index.md
- `M` wiki/numbers.md
- `M` wiki/papers/Kopel2021-CSR.md

### 244a45d — A5 lint: mechanical 10/10, plus the cross-page contradiction it took to find a blocker

*2026-11-17 00:41*

- `A` checks/a5_lint_run1.txt
- `A` checks/a5_lint_run2.txt
- `A` checks/a5_lint_run3.txt
- `A` checks/a5_report.md
- `M` log.md
- `A` scripts/a5_lint.py
- `M` wiki/concepts/first-mover-advantage.md
- `M` wiki/concepts/strategic-commitment.md
- `M` wiki/equations.md
- `M` wiki/index.md
- `M` wiki/numbers.md
- `M` wiki/overview.md
- `M` wiki/papers/Kopel2021-CSR.md
- `M` wiki/sources.md

### f95ebc8 — A6: sign-off checklist for the human reviewer

*2026-11-17 07:53*

- `A` "A6_\347\260\275\346\240\270\346\270\205\345\226\256.md"

### 15e69de — Light ingest of sources 2-5: assignment requirement met, concept layer now cross-source

*2026-11-17 08:35*

- `A` checks/a5_lint_run4.txt
- `M` log.md
- `A` raw/papers/BarcenaRuizSagasta2021-CrossOwnershipCSR.pdf
- `A` raw/papers/Chen2021-OptimalCSR.pdf
- `A` raw/papers/HiroseMatsumura2022-CommonOwnershipECSR.pdf
- `A` raw/papers/XingLee2023-EnvironmentalRD.pdf
- `M` scripts/a5_lint.py
- `A` wiki/concepts/csr-modelling-choices.md
- `A` wiki/concepts/rival-exclusion.md
- `M` wiki/glossary.md
- `M` wiki/index.md
- `M` wiki/open-questions.md
- `M` wiki/overview.md
- `A` wiki/papers/BarcenaRuizSagasta2021-CrossOwnershipCSR.md
- `A` wiki/papers/Chen2021-OptimalCSR.md
- `A` wiki/papers/HiroseMatsumura2022-CommonOwnershipECSR.md
- `A` wiki/papers/XingLee2023-EnvironmentalRD.md
- `M` wiki/sources.md

### 03ce2dc — A6 checklist: fold in the completed source ingest

*2026-11-17 08:36*

- `M` "A6_\347\260\275\346\240\270\346\270\205\345\226\256.md"

### 42a4637 — A6 signed off; Graph B nodes B1-B4: cards and 30-slide outline

*2026-11-17 08:44*

- `M` log.md
- `A` notes/cards/C1-question.md
- `A` notes/cards/C10-discussion.md
- `A` notes/cards/C2-model.md
- `A` notes/cards/C3-timing.md
- `A` notes/cards/C4-benchmark.md
- `A` notes/cards/C5-spillovers.md
- `A` notes/cards/C6-thresholds.md
- `A` notes/cards/C7-shapes.md
- `A` notes/cards/C8-crosssource.md
- `A` notes/cards/C9-limits.md
- `A` notes/outline.md
- `M` wiki/index.md
- `M` wiki/sources.md

### 842b044 — B6-B11: 30-slide deck, speaker script, and the checks that caught three real defects

*2026-11-17 09:26*

- `A` checks/b8_b11_run1.txt
- `A` checks/b8_b11_run2.txt
- `A` checks/b8_b11_run3.txt
- `M` log.md
- `A` notes/script.md
- `A` scripts/b6_figures.py
- `A` scripts/b8_b11_checks.py
- `A` slides_html/fig/fig-benchmark.svg
- `A` slides_html/fig/fig-theta021.svg
- `A` slides_html/fig/fig-thresholds.svg
- `A` slides_html/index.html
- `M` wiki/equations.md

### 355a36e — B7 fixes: all 1 blocker, 17 should-fix, 17 minor, plus seven backup slides

*2026-11-17 09:47*

- `A` checks/b7_report.md
- `A` checks/b8_b11_run4.txt
- `M` log.md
- `M` notes/cards/C1-question.md
- `M` notes/cards/C10-discussion.md
- `M` notes/cards/C2-model.md
- `M` notes/cards/C3-timing.md
- `M` notes/cards/C5-spillovers.md
- `M` notes/cards/C6-thresholds.md
- `M` notes/cards/C8-crosssource.md
- `M` notes/script.md
- `M` scripts/b8_b11_checks.py
- `M` slides_html/index.html

### 8d0f2fe — Submission package: wiki and deck published, workflow diagram, submission document

*2026-11-17 10:29*

- `M` log.md
- `A` scripts/b9_inline_katex.py
- `A` scripts/build_wiki_site.py
- `A` slides_html/.katex-cache/KaTeX_AMS-Regular.woff2
- `A` slides_html/.katex-cache/KaTeX_Caligraphic-Bold.woff2
- `A` slides_html/.katex-cache/KaTeX_Caligraphic-Regular.woff2
- `A` slides_html/.katex-cache/KaTeX_Fraktur-Bold.woff2
- `A` slides_html/.katex-cache/KaTeX_Fraktur-Regular.woff2
- `A` slides_html/.katex-cache/KaTeX_Main-Bold.woff2
- `A` slides_html/.katex-cache/KaTeX_Main-BoldItalic.woff2
- `A` slides_html/.katex-cache/KaTeX_Main-Italic.woff2
- `A` slides_html/.katex-cache/KaTeX_Main-Regular.woff2
- `A` slides_html/.katex-cache/KaTeX_Math-BoldItalic.woff2
- `A` slides_html/.katex-cache/KaTeX_Math-Italic.woff2
- `A` slides_html/.katex-cache/KaTeX_SansSerif-Bold.woff2
- `A` slides_html/.katex-cache/KaTeX_SansSerif-Italic.woff2
- `A` slides_html/.katex-cache/KaTeX_SansSerif-Regular.woff2
- `A` slides_html/.katex-cache/KaTeX_Script-Regular.woff2
- `A` slides_html/.katex-cache/KaTeX_Size1-Regular.woff2
- `A` slides_html/.katex-cache/KaTeX_Size2-Regular.woff2
- `A` slides_html/.katex-cache/KaTeX_Size3-Regular.woff2
- `A` slides_html/.katex-cache/KaTeX_Size4-Regular.woff2
- `A` slides_html/.katex-cache/KaTeX_Typewriter-Regular.woff2
- `A` slides_html/.katex-cache/katex.min.css
- `M` slides_html/index.html
- `A` slides_html/wiki.html
- `A` "\347\271\263\344\272\244/wiki.html"
- `A` "\347\271\263\344\272\244/workflow.svg"
- `A` "\347\271\263\344\272\244/\347\271\263\344\272\244\345\205\247\345\256\271.md"
- `A` "\351\205\215\351\237\263\350\250\210\347\225\253.md"

### 5c919b9 — Section 6 reflection: answer the three assigned questions, then fix what review broke

*2026-11-17 15:53*

- `A` checks/b10_run5_37slides.txt
- `A` checks/section6_review.md
- `A` checks/section6_review_appendix.md
- `M` log.md
- `A` scripts/b10_overflow_check.js
- `A` "\347\271\263\344\272\244/\346\234\252\345\221\275\345\220\215.pages"
- `M` "\347\271\263\344\272\244/\347\271\263\344\272\244\345\205\247\345\256\271.md"

### 31c7cf7 — Anchor the commit count to a revision, since writing the document changes it

*2026-11-17 15:53*

- `M` "\347\271\263\344\272\244/\347\271\263\344\272\244\345\205\247\345\256\271.md"

### fc7bb16 — Section 6 round 2: nine fixes, including a claim with no artefact at all

*2026-11-17 16:36*

- `M` "A6_\347\260\275\346\240\270\346\270\205\345\226\256.md"
- `M` checks/section6_review.md
- `A` checks/section6_review_round2.md
- `M` log.md
- `M` "\347\271\263\344\272\244/\347\271\263\344\272\244\345\205\247\345\256\271.md"

### fe14a2f — Close the stale 待修 note: the A6 checklist six/five mismatch was already fixed

*2026-11-23 13:23*

- `M` log.md
