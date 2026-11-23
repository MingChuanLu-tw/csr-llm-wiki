# AGENTS.md — CSR Leadership LLM Wiki (schema)

Status: DRAFT for review. Source of requirements: `需求摘要.md` (confirmed 2026-11-16).

## 0. Project in one paragraph

Build an English LLM Wiki from academic papers (Karpathy's LLM Wiki pattern), then use only that wiki to produce a ~30-slide English HTML teaching deck and an English speaker script for a 30–45 minute talk. Audience: graduate students and the advisor; the goal is discussion. The first source is Kopel (2021). The full paper content must be covered. Equations are written in LaTeX.

## 1. Three Karpathy principles (non-negotiable)

1. **`raw/` is read-only.** Sources go in `raw/papers/`. Never edit, rename, or summarize inside `raw/`.
2. **The wiki accumulates.** Each ingest updates existing pages (concepts, overview, index), not only creates a new page.
3. **This file is the schema.** Every agent action follows these rules. If a rule conflicts with a request, stop and ask.

Operations: **ingest** (add a source), **query** (answer from wiki and save useful answers to `wiki/syntheses/`), **lint** (health check).

## 2. Folder layout

```
raw/papers/            source PDFs (read-only)
wiki/papers/           one summary page per source, e.g. Kopel2021-CSR.md
wiki/concepts/         concept pages (first-mover advantage, spillover θ, competition γ, ...)
wiki/entities/         authors, journals, cited works when needed
wiki/syntheses/        saved query answers and comparisons
wiki/overview.md       the map of the whole wiki — entry point
wiki/index.md          catalogue of every wiki page, with node status
wiki/glossary.md       one canonical meaning per symbol, across sources
wiki/equations.md      canonical LaTeX register — B8 checks slides against it
wiki/numbers.md        every citable number with provenance — B10 checks slides against it
wiki/sources.md        ingest register; candidates for the remaining sources
wiki/open-questions.md discussion material for the seminar
checks/                verification reports and raw script output
scripts/               verification scripts (sympy / mpmath)
slides_html/           final HTML deck (English)
notes/                 speaker script (English) and evidence cards
log.md                 run log and reflection records (see §7)
```

`assets/` is NOT used in this round.

**A2 writes**: `wiki/concepts/*`, `wiki/overview.md`, `wiki/index.md`, and the four
reference registers (`glossary`, `equations`, `numbers`, `sources`) plus
`open-questions.md`. The registers exist so that B8 and B10 have something
machine-checkable to compare slides against; keeping them current is part of
every ingest, not a one-off.

## 3. Writing rules

- Language: English for everything in `wiki/`, `slides_html/`, `notes/`. Chinese only in this file and in `需求摘要.md`.
- Equations: LaTeX only, e.g. `$p_1 = a + s_1 - x_1 - \gamma x_2$`. In HTML use KaTeX or MathJax. Every equation in the wiki must carry its equation number from the paper.
- Citations: every factual claim carries `(Kopel 2021, p. X, eq. Y)` or `(Kopel 2021, p. X)`.
- Numbers: quote the paper's number, then state whether it is analytic or numerical. Numerical thresholds must say "numerical analysis, footnote 15" or the equivalent location.
- File names: `Author YEAR - keyword` in ASCII form, e.g. `Kopel2021-CSR.md`.
- Do not use outside knowledge. Only `raw/` and approved `wiki/` pages may be cited.
- **Mark every inference that is not the author's claim.** Use a 🔎 box for a substantive
  finding, or an inline **[our reading]** / **[own calculation]** tag. This applies to
  concept pages and the overview as much as to source pages: anything unmarked will be
  lifted into an evidence card at B3 and onto a slide as the author's claim. Added after
  A3 F16.
  - **Scope**: a tag governs the sentence or bullet it *opens*, and nothing else. A passage
    longer than that needs a 🔎 box, or one tag per bullet. Never put a blanket tag over a
    list that contains quotations — that marks the author's words as ours. (A3 round 2.)
- **Quotation marks mean verbatim.** Anything inside quotation marks must match the source
  character for character, including the author's own typos (use *sic*). Elisions take an
  ellipsis. A paraphrase goes outside the quotation marks. Checked at A3. (Added after
  A3 F4, F12, F19 — a quotation with a page number that did not exist in the paper.)
- **Where the paper contradicts itself**, state our reading, then note the contradiction
  and why we resolved it that way. Never silently overwrite the source (A3 F8).
- When two sources disagree, write both claims on the concept page, mark the conflict, and do not overwrite either.

## 4. Graph A — Wiki ingest

Each node has a fixed role. An AI node may only do what its row says.

| Node | Type | Reads | Writes | Must NOT | Check → on failure |
|---|---|---|---|---|---|
| A1 Read source | AI | one PDF in `raw/papers/` | `wiki/papers/<file>.md` | edit other pages; add outside claims | — |
| A2 Update concepts | AI | A1 page + existing concept pages | `wiki/concepts/*`, `wiki/overview.md`, `wiki/index.md` | rewrite an existing claim without marking it | — |
| A3 Citation check | script | A1/A2 pages | pass/fail report | edit pages | any uncited claim → A1 for that page only |
| A4 Equation and number check | script (Python) | A1 page and the PDF | pass/fail report | edit the paper | mismatch → A1, record the difference on the page |
| A5 Lint | script + AI | all wiki pages | lint report | silently fix | orphan page, broken link, contradiction → A2 |
| A6 Human review | you + advisor | lint report + summary | decision | — | reject → A2 |

Lint checks: orphan pages, broken `[[links]]`, missing index entries, contradictory numbers, LaTeX that does not compile, pages not listed in `log.md`.

## 5. Graph B — Deck and script

Order follows the instructor's demonstration graph, with two added nodes (B8 equation check and B11 timing check).

| Node | Type | May read | Writes | Must NOT | Check → on failure |
|---|---|---|---|---|---|
| B1 Retrieve wiki | AI | `wiki/` pages that passed Graph A | selected page list | use pages that did not pass A | — |
| B2 Coverage gate | script | outline items vs. selected pages | coverage report | — | any outline item without a verified card → STOP and return to Graph A (add source/concept) |
| B3 Evidence cards | AI, one per paper section (parallel) | one wiki section each | `notes/cards/*.md` | write slides | card without page citation → redo that card |
| B4 Outline | AI | evidence cards only | `notes/outline.md` (~30 slides) | add content not on cards | — |
| B5 Human review | you + advisor | outline + discussion questions | decision | — | "revise outline" → B4; "missing evidence" → B1 (fetch more wiki) |
| B6 Slide + script drafts | AI | outline + its cards | `slides_html/` section + `notes/` section per slide | use outside knowledge | — |
| B7 Faithfulness check | AI, NEW session | only the slide, its script, and the cited wiki pages | pass/fail per slide | see the drafting conversation | fail → B6 for that slide only, max 2 rounds |
| B8 Equation check | script | LaTeX source of each slide | pass/fail | edit the equations | does not compile or symbol differs from wiki → B6 |
| B9 Render HTML | script | slides | `slides_html/index.html` | — | — |
| B10 Render check | script + screenshot | rendered HTML | pass/fail | edit | overflow, broken image path, number not found on cards → B6 for that slide |
| B11 Timing check | script | `notes/` word counts | estimate of minutes | — | outside 30–45 min → B6 (adjust script length) |
| Deliver | — | — | — | — | — |

Pages that appear in `slides_html/` must be listed in the run log with the node that approved them.

## 6. Loop rules (apply to every AI loop)

Each loop must state these five things before it runs. Write them in `log.md` at the start of the run.

1. **Goal**: what finished output looks like.
2. **Limits**: what may and may not change.
3. **Done criteria**: the checks that must pass.
4. **Stop conditions**: max 3 rounds per node. Stop early if no progress.
5. **Trigger**: what starts the loop (a failed check, or a human decision).

Other rules:
- A check phrase like "looks good" or "checked" is not validation. Validation means a script or a new-session review with a written result.
- A big loop (going back from B10 to B1, or from Graph B to Graph A) is a signal. Record it in `log.md`, and move the check earlier next time.
- If a node fails twice, stop and ask the human. Do not retry a third time without a changed input.

## 7. Run log (`log.md`) and reflection

Every failure or back-edge gets one row:

| Date | Node | Symptom | Cause | Change made | Did it change the workflow? (yes/no + why) |
|---|---|---|---|---|---|

The final reflection for the course assignment is written from this table: which node fails most, where the check was moved forward to, and whether the graph was changed.

## 8. Git (auto + human acceptance)

- Repository initialized in the project root. Initial commit: `init: project skeleton and source PDF`.
- **Automatic commits**: when an automatic check passes (A3, A4, A5, B2, B8, B10, B11), commit the changed files. Message: `auto: <node> <source or slide id> pass`. Every failed attempt is committed too, so the history keeps the attempts used for the reflection.
- **Accepted commits**: when the human approves A6, B5, or Deliver, commit with the message `accepted: <node> <what was approved>`. Only accepted commits count as the version handed in.
- Never rewrite history (no `--amend`, no `reset --hard`) during a run. Failed attempts stay in the log.
- Never commit `raw/` changes other than adding new source files.

## 8a. Independent review (required)

- Any judgment about quality or faithfulness is done by a **separate reviewer agent** with fresh context. The agent that wrote the text must not review its own text.
- The reviewer receives only the artifact and the cited sources (the same input rule as B7). It returns a written report in `checks/` with each item marked pass or fail and the reason.
- The writer fixes only the items the report marks as fail. The reviewer then checks again. Maximum 2 review rounds per artifact; after that, stop and ask the human.
- Nodes that use this: A3 (claim-citation check), A5 (contradiction check), B3 (evidence cards), B7 (faithfulness check), B10 (render check against cards). A4 and B8 are scripts and do not need a reviewer.

## 10. Model and effort policy

| Work | Model | Effort | Who sets it |
|---|---|---|---|
| Main session (A1, A2, B3–B6, judgement and writing) | Opus 5.5 | medium | human, with `/model` or `claude --model claude-opus-5-5` |
| Independent review (A3, A5, B3 evidence cards, B7 faithfulness, B10 content check) | Opus 5.5 | medium | agent call with `model: opus`, `effort: medium` |
| Mechanical steps (create files, git add/commit, render HTML, timing count, script runs) | Haiku 5.5 | medium | agent call with `model: haiku`, `effort: medium` |

Rules:
- The reviewer must never be the same agent instance as the writer, and should use a different model from the writer where possible (Opus reviews text drafted in the main session).
- Mechanical sub-agents do no judgement. If a mechanical step fails, it stops and reports; it does not fix content.
- Effort is medium for all nodes. Raise it only when the human asks.

## 9. Scope limits

- Only one source for now (Kopel 2021). Additional sources are added later, one at a time.
- Do not download PDFs. The human supplies them into `raw/papers/`.
- Do not start Graph B until Graph A has passed A6 for the first source and the wiki has overview and index pages.
