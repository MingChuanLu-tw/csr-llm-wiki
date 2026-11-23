# §6「反思」獨立事實查核報告

- **日期**：2026-11-17
- **審查者**：獨立 reviewer，fresh context。未撰寫 `繳交/繳交內容.md` 的任何部分，也未修改它。
- **受審範圍**：`繳交/繳交內容.md` 第 179–268 行（`## 六、反思` 至 `### 最後一點` 結尾）。
- **受審版本的重要前提**：受審文字是**工作區未提交版本**。`git status --short` 顯示
  ` M 繳交/繳交內容.md`，`git diff --stat 8d0f2fe` 顯示 74 insertions / 22 deletions。
  已提交版本（`8d0f2fe`）的 §6 內容與此不同。評分者若 clone repo 會看到舊版。
- **一手證據**：`log.md`、`AGENTS.md`（含 `git show de8d030:AGENTS.md` 的初版）、
  `checks/a3_report.md`、`checks/a4_report.md`、`checks/a5_report.md`、`checks/b7_report.md`、
  `checks/a5_lint_run1.txt`、`checks/b8_b11_run4.txt`、`wiki/open-questions.md`、
  `wiki/numbers.md`、`A6_簽核清單.md`、`git log`／`git log -S`、
  `raw/papers/Kopel2021-CSR.pdf`（`pdftotext -layout`，換行正規化後搜尋）。
- **本審查自己做的額外動作**：用 `git log -S` 逐一追查七個 blocker 的**文字首次進入 repo 的 commit**，
  而不採信 `log.md` 的 Cause 欄。這一步推翻了 §6 最核心的那張表（見 §2.1）。
- **檔案前情**：本路徑原已存在一份 605 行的未追蹤草稿（同一任務的前次嘗試）。本檔為本次審查的
  完整報告，已覆蓋該草稿。前稿未發現 §2.1 的歸屬錯誤。

> **勘誤（2026-11-17，由 round 2 追加；本文其餘內容未改動）**
> 本報告自身有兩處錯誤，詳見 `checks/section6_review_round2.md` §0：
> (1) §2.18 第一個補充點拿 `AGENTS.md:88`「two added nodes (B8 … B11)」當作否證第 1、2、4 項的論據——
> 該句在 `de8d030:AGENTS.md:61` 就已存在，不能用來區分「本輪新增」，且同段
> 「B8、B11 §6 一個字都沒提」有誤（B11 出現在（甲）表）。第 1、4 項純靠 `de8d030` 本身即可否證，
> 第 2 項另有 `需求摘要.md:77`（證據卡是老師示範節點）佐證，結論不變。
> (2) §2.16 只實際查了 F12，F19 於 round 2 補查（`a3_report.md:499–502`，確為非逐字），結論不變。

---

## 0. 判定總表

| # | §6 的主張（摘要） | 判定 |
|---|---|---|
| 1 | 整輪共 **7 個 blocker** | **VERIFIED**（但分母只來自三份會分級的報告） |
| 2 | blocker 歸屬 **A1→5、A2→1、B3→1** | **WRONG** — F2 與 F4 的文字是 **A4** 寫進 repo 的，不是 A1 |
| 3 | F5（§9／§10 自相矛盾）是 A1 缺陷 | **VERIFIED** |
| 4 | A5-01 是 A2 的、不是 A1 的 | **VERIFIED** |
| 5 | A3 第一輪 FAIL 發生在 Graph B 啟動之前 | **VERIFIED** |
| 6 | 5 個 blocker 因此沒進到 10 張卡片、30 張投影片 | **VERIFIED** |
| 7 | 「下游每一道檢查都會回報通過」 | **OVERSTATED** — 對 F1/F2/F4 成立，F3/F5 被 A3 自己當場抓到 |
| 8 | `"Spillovers must be very low" (p. 491)` 在論文中不存在 | **VERIFIED**（已查 PDF 全文） |
| 9 | 「修正」是第二大錯誤來源（四個實例） | 四個實例 **VERIFIED**；「第二名」**OVERSTATED**（換了度量） |
| 10 | 「修正是一次未受檢查的寫入，原設計假設只有生成節點會寫入」 | **OVERSTATED** — 初版 §8a 已有 fix → re-review |
| 11 | §3 含 "Do not use outside knowledge…" | **VERIFIED**（`AGENTS.md:54` 逐字相符） |
| 12 | B4「may read」欄只寫 "evidence cards only" | **VERIFIED**（`AGENTS.md:95`；欄名是 **May read**） |
| 13 | A6／B5 的 **Writes** 欄只寫 "decision" | **VERIFIED**（`AGENTS.md:82`、`96`；欄名確實是 Writes） |
| 14 | 「人是這個 graph 裡唯一沒有被規範輸入輸出的節點」 | **WRONG** — Reads 欄與失敗邊都有寫，且 `A6_簽核清單.md` 就是「人該看什麼」 |
| 15 | 57 筆裡 30 筆改變了流程 | **WRONG（可重算）** — 實際 **60 筆 / 32 筆 yes** |
| 16 | open-questions Q1 整輪都沒有被執行 | **VERIFIED**（Q1 內容描述略失準） |
| 17 | （甲）連結／孤兒檢查移到 A2 結尾 | **VERIFIED**（但未寫進 schema） |
| 18 | （甲）第一版逐字稿 24–28 分鐘 | **VERIFIED**（`log.md:179` 逐字相符） |
| 19 | （甲）時長檢查「移到 B6 寫稿前先定字數」 | **UNSUPPORTED** — 是結論，不是已執行的移動 |
| 20 | （甲）渲染檢查移到真正發布環境 | **VERIFIED** |
| 21 | （乙）三條 §3 規則 | **全部 VERIFIED**（逐字核對，含觸發來源註記） |
| 22 | 第三種前移：lint L4 修檢查而非修實例 | **VERIFIED** |
| 23 | A5 第一輪 8 問題：3 改頁面、5 放寬腳本（2 L5 + 3 L7） | **VERIFIED**（與 `a5_lint_run1.txt` 完全對帳） |
| 24 | 問題三「結構性修改四項」 | **3 項 WRONG、1 項 VERIFIED**（見 §2.11） |
| 25 | 三個門檻相差約 **105 倍** | **OVERSTATED** — 105× 只在 γ=0.3；全域是 6×–940× |
| 26 | FMA 死後領導者仍持續嚇阻、持續超額投資 | **VERIFIED** |
| 27 | 「新想法只被允許待在一個地方：open-questions」 | **WRONG** — 被本文件自己的最佳發現否證 |
| 28 | 報告 4 份／腳本 8 支／commit 15 次 | **VERIFIED**（本檔寫入前的狀態） |
| 29 | 舊值「6 份／7 支／12 次」 | **UNSUPPORTED** — 無任何 artefact 可查（非被否證） |

---

## 1. 最重要的一件事（先講結論）

**§6 問題一的那張 blocker 歸屬表，把 A4 寫出來的兩個 blocker 算在 A1 頭上。**

這不是詮釋差異。`log.md` 的 Cause 欄確實寫「A1」，但 Cause 欄是回憶寫的；
repo 本身留著證據。用 `git log -S` 查每個 blocker 的字串**首次進入 repo 的 commit**：

| blocker | 內容 | 首次出現的 commit | 該 commit 是哪個節點 | §6 歸給 | 實際產生者 |
|---|---|---|---|---|---|
| F1 | TS&L 立場寫反 | `5acf804`（paper page §8）、`19779f3`（sources.md） | A1、A2 | A1 | **A1** ✅ |
| F2 | `ds₂/ds₁` 符號反 | **`39bd252`**（`checks/a4_report.md:48`） | **A4** | A1 | **A4**（經 A2 轉載） |
| F3 | θᵢ 定義反 | `5acf804`、`19779f3` | A1、A2 | A1 | **A1** ✅ |
| F4 | 捏造引文 | **`39bd252`**（`wiki/papers/Kopel2021-CSR.md` 🔎 box） | **A4** | A1 | **A4** |
| F5 | §9／§10 自相矛盾 | `5acf804` | A1 | A1 | **A1** ✅ |
| A5-01 | FMA 錯誤因果 | `19779f3`（concepts 兩頁） | A2 | A2 | **A2** ✅ |
| B7 slide-4 | 卡片比 wiki 短 | B3 製卡 | B3 | B3 | **B3**（B6 共犯） |

兩個關鍵指令，任何評分者 20 秒可複製：

```
git log -S'Spillovers must be very low' --oneline --all   # → 39bd252 (A4), 不含 5acf804
git show 5acf804:wiki/papers/Kopel2021-CSR.md | grep -c 'must be very low'   # → 0
```

**F4（捏造引文）**：A1 的 commit `5acf804` 裡**完全沒有這句話**。它是 A4 在 `39bd252` 連同
「Lemma 2 FMA frontier」的 🔎 box 一起寫進 A1 頁面的——那個 box 的最後一句
「This is arguably the sharpest result in the paper and a candidate headline slide」
正對應 `log.md:45` A4 那一列的 Change made 欄。同一句引文同時出現在
`checks/a4_report.md` §3，而 **`a3_report.md` F4 的 Files 欄自己就寫了
「also `checks/a4_report.md` §3」**——A3 已經指出來了，§6 還是歸給 A1。

**F2（符號錯）**：首次出現在 `checks/a4_report.md:48`（A4 的 commit）。A2 的
`equations.md`（`19779f3`）轉載時還加了一句註腳：「The factored form is **A4's**;
the paper states only the threshold.」A1 的頁面只寫了**正確的**門檻
`ds₂/ds₁ < 0 ⟺ θ < γ/(2-γ²)`，沒有那條符號反掉的比例式。

### 更正後的歸屬

| 產生缺陷的節點 | blocker 數 | 內容 |
|---|---|---|
| **A1 讀論文** | **3** | F1 立場寫反、F3 θ 定義反、F5 同一頁自相矛盾 |
| **A4 符號驗證** | **2**（見下方保留） | F2 符號反（A4 產生、A2 轉載）、F4 捏造引文（A4 直接寫進 wiki 頁面） |
| A2 概念頁 | 1 | A5-01 錯誤因果（另轉載 F2 進 `equations.md` 未查） |
| B3 證據卡 | 1 | 卡片引文比 wiki 短 |

**關於 A4 那一欄的保留**：F4 完全是 A4 的——A4 把它直接寫進 `wiki/papers/` 頁面。
F2 比較複雜：**源頭**是 A4（`checks/a4_report.md:48` 首次出現），但 A3 擋下的那段
**wiki 文字**是 A2 在 `19779f3` 寫進 `equations.md` 的（還註明「The factored form is
A4's」）。所以 F2 記 A4、記 A2、或兩邊各半都可以辯護；**唯一不能辯護的是記給 A1**，
因為 A1 的頁面裡沒有那條式子。穩健的結論是 **A1 = 3**，F2 的歸屬由作者自己決定。

**好消息：§6 的答案（A1 最常出錯）仍然成立**——3 of 7 仍是單一節點最高。
**壞消息有三層**：

1. 那張表現在是**可被兩個 git 指令拆掉的**。在一份講「驗證」的作業裡，這比數字錯更貴。
2. §5 的節點表寫「**A4 符號驗證｜4 筆｜改變流程 0**」，§6 全篇把 A4 當成「結構上有盲點但沒出錯」
   的節點。實際上 A4 是**第二大 blocker 產生者**，而且它產出的兩個錯都**不是**驗證錯誤——
   一個是抄 sympy 符號、一個是捏造引文，都是「寫作」行為。
3. 這反而讓 §6 自己的論點**更強**：A4 結構上不可能抓到 F2，**因為 F2 就是 A4 自己寫的**。
   一個節點無法稽核自己的輸出，比「比對清單裡沒有」更尖銳。建議改寫而不是刪掉。

**附帶一個沒被當成問題記錄的 schema 擴權**：`AGENTS.md:80` 的 A4 列，Writes 欄只有
「pass/fail report」，失敗邊是「mismatch → A1, record the difference on the page」。
A4 在 `39bd252` 卻自己寫了一個帶引文的 🔎 box 進 `wiki/papers/` 頁面。
**這個寫入動作本身有記錄**——`log.md:36` 的 A4 loop plan 自己把範圍放寬成
「verified corrections to `wiki/papers/Kopel2021-CSR.md`」，`log.md:45` 也寫了
「Added to the wiki page as a candidate headline slide」。
**沒有被記錄的是它的後果**：這次放寬讓一個只該輸出 pass/fail 的腳本節點
變成了會寫新散文、新引文的生成節點，而那次寫入產生了七個 blocker 中的一個（F4）。
這是問題三最好、也完全沒被用到的答案材料。

---

## 2. 逐項查核

### 2.1 blocker 總數 7 — VERIFIED（附保留）

- A3 round 1：5（`a3_report.md:8`「FAIL — 5 blockers, 14 should-fix, 9 minor」，
  F1/F2/F3/F4/F5 各自標 `**Severity**: blocker`，於 `:39/78/109/147/167`）
- A3 round 2：0（`a3_report.md:743`「0 blockers remain … 8 problems in the new text (0 blockers…)」）
- A5：1（`a5_report.md:11`「FAIL — 1 blocker」＝ A5-01，`:45`）
- B7：1（`b7_report.md:22`「FAIL — 1 blocker」＝ slide 4，`:56`）
- A4：`checks/a4_report.md` 全文 **0 次**出現 "blocker"。B2/B8/B10/B11 皆 PASS。

合計 7，數字正確。**保留**：分母由「哪些節點會分嚴重度」決定。A4、B8、B10、B11
從不產生 blocker 分級，所以它們在這張表上結構性為零。§6 用 blocker 數排名時，
應說明這點，否則排名偏向「有審查報告的節點」的對手。（此保留在更正後更重要：
A4 的兩個 blocker 是**別的節點**判給它的。）

### 2.2 F5 真的是 A1 缺陷嗎 — VERIFIED

是。`a3_report.md:167–180`：F5 的 **File** 欄只有一個檔案：
`wiki/papers/Kopel2021-CSR.md` §9 item 4，與它矛盾的 §10 在**同一頁**。
該頁是 A1 的唯一寫入目標（`AGENTS.md:77`）。`git log -S'which are analytic'`
→ `5acf804`（A1 commit）。`log.md:77` Cause：「Two sections written at different
times; no internal consistency pass.」完全是 A1 內部的事。歸 A1 無誤。

### 2.3 A5-01 真的是 A2 的而非 A1 的嗎 — VERIFIED

是。`a5_report.md:47–62`：Location A = `wiki/concepts/strategic-commitment.md`、
Location B = `wiki/concepts/first-mover-advantage.md`——兩者都在 `wiki/concepts/`，
是 A2 的寫入範圍（`AGENTS.md:78` 的 Writes 欄、`:41` 的「A2 writes」段）。Location C 是「證據」而非缺陷
（`a5_report.md` 明寫 overview「is not itself a defect」）。
`git log -S'That effect is destroyed by'` → `19779f3`（A2 commit）。歸 A2 無誤。

### 2.4 B3 歸屬 — 可接受但不完整

`log.md:184` Cause 欄有**兩個**主體：「B3 carded a shorter span than the wiki page
held, **and B6 then drew on the wiki habit rather than the card**.」§6 只記 B3。
把源頭記在 B3 可以接受（卡片是閘門，窄掉的是卡片），但 B6 違反了
`AGENTS.md:97`「B6 … May read: outline + its cards」——它讀了 wiki。
建議表格內容改成「B3（窄化）＋B6（繞過卡片）」，否則漏掉一個真實的規則違反。

### 2.5 「A3 第一輪判 FAIL 發生在 Graph B 啟動之前」— VERIFIED

| 事件 | 時間 | 依據 |
|---|---|---|
| A3 r1 報告（FAIL） | 2026-11-16 **23:29** | commit `c4934b8` |
| 5 blocker 修完 | 11-16 23:37 / 11-17 00:07 | `6854f91`、`e2d664a` |
| A5 lint | 11-17 00:41 | `244a45d` |
| A6 簽核 | 11-17（`log.md:147–150`） | commit `42a4637`（與 B1–B4 同一 commit；簽核清單本身為 `f95ebc8` 07:53、`03ce2dc` 08:36） |
| Graph B B1–B4 | 11-17 **08:44** | `42a4637` |

時序明確，相差約 9 小時，且中間有 A6 人工簽核。
`log.md:158` Graph B 的 Trigger 欄寫「human instruction『簽核，開始 Graph B』(2026-11-17)」，
`AGENTS.md:163` 也禁止 A6 前啟動 Graph B。**VERIFIED**。

「沒有進到 10 張卡片和 30 張投影片」也 VERIFIED：`ls notes/cards/` = 10 個檔案；
`checks/b8_b11_run4.txt`「slides in deck: 30 (+7 backup)」。

### 2.6 「下游每一道檢查都會回報通過」— OVERSTATED

對 F1、F2、F4 成立（都是 A3 才抓到，且 A4 比對清單看不到）。
但 F3 與 F5 **都是同一頁內部的矛盾**，而 `log.md:77` 自己寫
「A5 lint should catch within-page contradictions」——也就是說作者自己認為
既有檢查**應該**抓得到。F3 的矛盾（§4.1 vs §4.2）同樣在一頁之內
（`a3_report.md:135`「flatly inconsistent with its §4.1 definition」）。
這兩個缺陷不是「下游全部回報通過」的例子，是「A5 還沒跑」的例子。
建議把這句限定到 F1/F2/F4，論點不會變弱。

另外「A1 寫的 wiki 頁是 A2 概念頁的**唯一**輸入」與 schema 不符：
`AGENTS.md:78` A2 的 Reads 欄是「A1 page **+ existing concept pages**」，
`:97` B3 是「one wiki section each」（不限概念頁）。本輪因為只有一篇來源、
沒有既有概念頁，事實上近似「唯一輸入」，但「唯一」是對 schema 的錯誤陳述。
改成「本輪實際上的唯一輸入」即可。

### 2.7 捏造引文 — VERIFIED（已查 PDF）

`pdftotext -layout` 全文、換行正規化後搜尋：

- `"Spillovers must be very low"` → **0 次**
- `"must be very low"` → **0 次**
- A3 指出的真句（p. 491）**存在且逐字相符**：
  「What is surprising, however, is that the level of CSR spillovers for which a
  first-mover advantage can be sustained is in fact very low.」

**一個值得加進 §6 的細節**：論文 p. 491 另有一句
「if there are no spillovers to the rival or **spillovers are very low**」。
所以那個捏造不是無中生有，而是把**鄰近真句的詞**壓縮進引號。
這讓 §6「在寫的人的視角裡，它看起來已經查證過了」這句話從修辭變成可證實的機制。
（但歸屬要改：寫下它的是 A4，見 §1。）

### 2.8 「修正」是第二名 — 實例全 VERIFIED，排名 OVERSTATED

四個實例逐一對帳：

| §6 的敘述 | 一手出處 | 判定 |
|---|---|---|
| 修 F9 時把說明段落插進 `numbers.md` 表格中間 | `log.md:93`；`a3_report.md:962` **N1，Severity: should-fix** | VERIFIED |
| 修 F14 時把舊頁碼帶到新句子 | `log.md:94`；`a3_report.md:975` **N2，should-fix** | VERIFIED |
| F9 的修正只到了四個頁面中的三個 | `log.md:95`；`a3_report.md:990` **N3，should-fix**（記為 F9 residue） | VERIFIED |
| 一回合後在 `equations.md` 犯完全相同的表格錯誤 | `log.md:125` **A5-03**，`a5_report.md` 類別 6（3 should-fix） | VERIFIED |

**但「第二名」換了度量。** §6 讓 A1 坐上第一名用的是 **blocker 數**。
用同一把尺，「修正」的 blocker 數是 **0**——上面四項全是 should-fix。
用「缺陷總數」當尺，A1 的 should-fix 也遠多於 4。所以「第二名」沒有任何一種
一致的度量支持它。這是一個**被包裝成排名的質性判斷**。

建議改寫成不帶名次的版本（證據完全支撐）：
「有一整類缺陷不屬於任何節點：**修正本身**。四個實例，全部由下一輪審查抓到，
其中一個是同一個缺陷在一回合內重犯。」

### 2.9 「修正是一次未受檢查的寫入，而原本的設計假設只有生成節點會寫入」— OVERSTATED

`git show de8d030:AGENTS.md`（**初始 commit**）的 §8a 已經寫了：
「The writer fixes only the items the report marks as fail. **The reviewer then
checks again.** Maximum 2 review rounds per artifact」。
所以「修正會被再審一次」從第一天就在規格裡，並不是本輪才發現的缺口——
而且本輪四個修正缺陷**全部**是被這條規則抓到的（A3 r2、A5）。
真正成立的說法是：規格有 re-review，但**沒有把修正當成一次需要跑 lint 的寫入**
（`log.md:93` 自己寫「A5 lint would have caught this; it has never run」）。
請把「原本的設計假設只有生成節點會寫入」改掉——這句話會被 `de8d030` 的 §8a 否證。

### 2.10 五個 schema 引文 — 全部 VERIFIED

| §6 的引用 | `AGENTS.md` 實際內容 | 判定 |
|---|---|---|
| §3「Do not use outside knowledge. Only `raw/` and approved `wiki/` pages may be cited.」 | **`:54` 逐字相符**（含兩個反引號與句點） | VERIFIED |
| B4「may read」欄只寫「evidence cards only」 | **`:95`** cell = `evidence cards only`，無其他字 | VERIFIED |
| A6／B5 的「Writes」欄只寫一個字 `decision` | **`:82`**（A6）、**`:96`**（B5），兩格都只有 `decision` | VERIFIED |
| 欄名是否真的叫「Writes」 | §4 表頭 `:75`、§5 表頭 `:90` 都是 `Writes`（§4 第三欄是 `Reads`，§5 第三欄是 `May read`） | **欄名正確** |

§6 寫「B4 大綱節點的『may read』欄」——`AGENTS.md:90` 的欄名首字大寫為
`May read`。大小寫差異，不影響判定。

### 2.11 「人是這個 graph 裡唯一沒有被規範輸入輸出的節點」— WRONG

這句話被 repo 裡**兩處**直接否證：

1. **輸入與失敗邊都有寫。**
   - `AGENTS.md:82`：A6 的 Reads = `lint report + summary`，失敗邊 = `reject → A2`
   - `AGENTS.md:96`：B5 的 Reads = `outline + discussion questions`，
     失敗邊 = `"revise outline" → B4; "missing evidence" → B1 (fetch more wiki)`

   所以「沒有被規範輸入輸出」不成立；沒被規範的是**輸出的內容**（Writes 只有 `decision`）。
2. **「人該看什麼、該抽查幾項、什麼情況該退回」已經寫了一整份檔案。**
   `A6_簽核清單.md`（183 行，commit `f95ebc8`／`03ce2dc`）第 0 節：
   「1. **抽查**第 2 節的六個項目（約 20 分鐘）… 3. 在第 5 節**簽核或退回**。退回會回到 A2。」
   第 2 節逐項列出要抽查什麼（`:34` 起），第 5 節是簽核欄（`:160`「**退回 A2** → …」）。
   這正是 §6 說「沒寫」的東西。

**真正站得住、而且更有力的版本**（全部可查證）：
A6 的人工程序寫在一份**一次性的 `A6_簽核清單.md`** 裡，不在 `AGENTS.md`（schema）內，
所以它不會被下一輪、下一篇來源自動繼承；而 **B5 根本沒有對應的清單**
（`ls` 顯示 repo 只有 `A6_簽核清單.md` 一份）。缺口是「人工節點的程序沒有進 schema、
且只做了兩個人工節點中的一個」，不是「完全沒有規範」。

### 2.12 「57 筆裡 30 筆改變了流程」— WRONG，可重算

用腳本重數 `log.md` 所有表格資料列（排除表頭與分隔列）：

```
total data rows: 60
yes: 32   no: 27   other: 1  (第 17 行 A1 first run，最後一欄是「—」)
```

節點分佈：A3 11、A3 r2 7、A5 10、A1 4、A1 light 2、A2 5、A4 4、B7 6、
B2/B3/B4/B6/B8/B9/B10/B11 各 1、**交件 3**。

**差額的來源完全可以定位**。交件段共 3 列，其中 2 列的 workflow 欄是 yes，
所以 `60 − 3 = 57`、`32 − 2 = 30`——兩個數字都剛好等於**排除最後那三列「交件」**的結果。
成因有兩種，本審查無法分辨：要麼是刻意的計數規則（「交件不是 graph 節點」），
要麼只是數完之後交件三列才被寫進 `log.md`（那三列屬於最後一個階段）。
無論哪一種，現在交出去的數字都是錯的。

這條規則本身可以辯護，但有兩個問題：

1. **§6 自己把其中一列當證據用。** 「最後一點」整段（`繳交內容.md:266`）引用的
   就是 `log.md:197`「Three of the counts in my own submission document were wrong」——
   一列被排除在分母外、同時被當成論據。
2. **§5 的節點表漏了 B3。** 表中列出「B2/B4/B6/B8/B9/B10/B11 各 1」，B3 不在裡面，
   但 B3 有一列（`log.md:162`）。該表加總 = 18+10+6+6+5+4+7 = **56**，不是 57。

兩個修法都可以，但必須二選一並說清楚：
- 改成「**60 筆，其中 32 筆改變了流程**」（全列），同時把 §5 表加上 B3 與交件 3 列；或
- 保留 57／30，但明說「不含 3 列交件階段紀錄」，並把 B3 補進 §5 表。

§5 其他數字對帳全部正確：A3 18（11+7）、A5 10、A1 6（4+2）、B7 6、A2 5、A4 4；
「改變流程」子欄 11／6／3／3／2／0／5 與重算**完全一致**。

### 2.13 open-questions Q1 — VERIFIED（描述略失準）

`wiki/open-questions.md:13–29`，Q1 標題是「**Is $\theta_1 = 0$ doing too much work?**」，
「What would settle it」欄寫：「Re-solve with $0 < \theta_1 < \theta_2$ and check whether
the first-mover-advantage frontier moves materially. **This is tractable with the verified
sympy model in `scripts/`.** Feasible to do before the talk if there is time.」

- 「用 A4 驗證過的 sympy 模型」→ **VERIFIED**（Q1 原文就這麼寫）
- 「去跑論文沒做的**比較靜態**」→ **略失準**。Q1 要的是**放寬假設重解模型**
  （θ₁ 從 0 放開），不是對既有解做比較靜態。建議改成
  「用 0 < θ₁ < θ₂ 重解模型，看 FMA 邊界會不會動」。
- 「整輪都沒有被執行」→ **VERIFIED**，三條獨立的負面證據：
  1. `grep -rn 'th1\|theta_1\|theta1' scripts/` → **0 命中**（8 支腳本都沒有 θ₁ 參數）
  2. `log.md` 全文沒有任何一列記錄執行 open question（只有 `:144` 提到**新增** Q9）
  3. Q1 只以「討論題」身分進了 `notes/cards/C9-limits.md:7`（C9.1 引用 `[[open-questions]] Q1`）
- 「沒有任何節點的職責包含『執行 open question』」→ **VERIFIED**。
  `AGENTS.md` §4／§5 共 17 列，無一列的 Writes 欄涵蓋執行開放問題；
  A2 只是**寫** `open-questions.md`（`:50`）。

### 2.14 「新想法只被允許待在一個地方：`open-questions.md`」— WRONG

被本文件自己的內容否證：

- `AGENTS.md:55–59` §3 明文允許在**任何**頁面標記自己的推論：
  「Use a 🔎 box for a substantive finding, or an inline **[our reading]** /
  **[own calculation]** tag.」
- 本輪**最好的發現**就住在別的地方：`wiki/numbers.md:46–50`
  「### Three thresholds」標著 **[own calculation]**，並自稱
  「This is the sharpest thing in the wiki and **it is not in the paper**」。
- 它還一路上了投影片：`log.md:164`「Moved the three-thresholds result to slides 22–23 of 30」。

所以創意不只被歸檔，它有一條**已經走通的出路**：標記 → 進登錄表 → 進卡片 → 進投影片。
§6 的「流程把創意歸檔了，但沒有給它一條出路」與自己的「最後一點」那段互相矛盾。

**可以守住的版本**：需要**新算一輪**（而非只是重新詮釋既有數字）的想法沒有出路——
Q1 要重解模型，而沒有節點的職責包含「跑一次新的推導」。這個限定版本與 §2.13 的
三條負面證據完全一致，而且不會被 `numbers.md` 否證。

### 2.15 （甲）三個「往前移」— 一個 UNSUPPORTED，兩個 VERIFIED

| §6 的列 | 一手出處 | 判定 |
|---|---|---|
| 連結／孤兒檢查 A5 → A2 結尾；觸發：`index.md` 寫成孤兒頁 | `log.md:58` 逐字支持，含「running it at the end of A2 catches breakage before it is committed, which is cheaper」 | **VERIFIED** |
| 逐字稿時長 B11 → B6 寫稿前先定字數；觸發：第一版只有 **24–28 分鐘** | `log.md:179`「The first script ran **24–28 minutes** — below the 30-minute floor.」數字**逐字相符** | 數字 **VERIFIED**；移動本身 **UNSUPPORTED** |
| 渲染檢查 `127.0.0.1` → 真正發布環境；artifact CSP 封鎖 cdnjs | `log.md:195` 完整支持（含 254 KB woff2 內嵌、402 KB、已重新發布） | **VERIFIED（但見下）** |

**第二列的移動沒有發生。** `log.md:179` 的 Change made 欄寫的是
「Expanded by ~900 words …」——也就是**事後補字**，不是把檢查移到 B6。
「Did it change the workflow?」欄寫的是一句結論：「write the script to the clock,
not to the slides」。而 schema 裡沒有任何對應修改：
- `AGENTS.md:97` B6 列完全沒有字數或時間預算
- `AGENTS.md:102` B11 仍然是唯一的時長關卡
- `AGENTS.md` 最後一次被修改是 `e2d664a`（A3 round 2），**早於整個 B6–B11 階段**

**第一列也要注意**：A2 結尾那次連結檢查是 inline 做掉的（`log.md:58`
「Caught by an inline link check before commit」），同樣沒寫進 `AGENTS.md:78` 的
A2 列（Check 欄仍是 `—`）。它確實發生過一次，但不會被下一輪繼承。

**第三列用同一把尺也不完整。** `log.md:195` 記的是**把問題修掉**（KaTeX 內嵌，
留下 `scripts/b9_inline_katex.py` 這個機制）＋一句教訓（「test in the environment
you ship to」）；而且問題是**發布結果自己的警告**抓到的，不是新檢查抓到的。
`log.md` 沒有任何一列記錄「在發布 origin 上重跑一次 B10」。
所以它是「改了做法、留下機制，但沒有把檢查真的移到那個環境」。

所以（甲）表三列，**沒有一列是把關卡搬到更早節點並寫進規格**：
第一列做過一次、未入規格；第二列只有結論；第三列留下修補腳本、但沒有重跑檢查。建議表格加一欄「已入規格／只做一次／僅結論」，
誠實度會提高，而且正好對應 §6 自己的主題。

### 2.16 （乙）三條 §3 規則 — 全部 VERIFIED

| §6 的列 | `AGENTS.md` 實際文字 | 判定 |
|---|---|---|
| 引號內必須逐字相符，含作者筆誤（用 *sic*）；觸發 F4、F12/F19 | `:63–66`「**Quotation marks mean verbatim.** … character for character, including the author's own typos (use *sic*). Elisions take an ellipsis. … **(Added after A3 F4, F12, F19** — a quotation with a page number that did not exist in the paper.)」 | **VERIFIED**（連觸發編號都逐字相符） |
| 標記推論，並定義標籤作用範圍：一個標籤只管它開頭的那一句或那一條；觸發 F16、A3 r2 | `:55–62`「Mark every inference that is not the author's claim … **Added after A3 F16.** — **Scope**: a tag governs the sentence or bullet it *opens*, and nothing else … **(A3 round 2.)**」 | **VERIFIED** |
| 論文自相矛盾時：先寫我方讀法，再註明矛盾與理由，絕不默默覆蓋原文；觸發 F8 | `:67–68`「**Where the paper contradicts itself**, state our reading, then note the contradiction and why we resolved it that way. Never silently overwrite the source **(A3 F8)**.」 | **VERIFIED** |

**這是 §6 全節最紮實的一段。** 而且 `git diff` 證明這三條是**本輪才加的**：
`6854f91`（F16 標記規則＋F8 矛盾規則）、`e2d664a`（標籤 Scope ＋逐字引文規則）。
這些才是「因此修改了 workflow」的真正證據——見 §2.18。

F12／F19 也查了：`a3_report.md:336`「F12 — The Burke & Logsdon blockquote is not
verbatim」，Severity should-fix，確實是非逐字 blockquote。§6 的描述正確。

### 2.17 第三種前移（修檢查而非修實例）＋「放寬」段 — 全部 VERIFIED

- **lint L4**：`log.md:125`「L4 extended to flag a lone pipe-line; **verified against
  the pre-fix file that the new rule catches it**」——§6 說「拿修正前的檔案實測確認會攔下來」，
  逐字相符。`a5_report.md` A5-03 同樣記載 L4「only examined runs of ≥2 pipe-lines」。**VERIFIED**
- **放寬段**：`log.md:122`「Of run 1's 8 problems, only 3 were fixed in the pages;
  **5 were fixed by relaxing the script** — 2 L5 hits … and 3 L7 hits」。
  與 `checks/a5_lint_run1.txt` 完全對帳：run 1 共 8 筆 = 1×L6 + 5×L7 + 2×L5。
  放寬的 5 筆 = 2×L5（`$[0,1)$` 半開區間誤判）+ 3×L7（`Kopel2021-CSR.md` 的三個
  verification-status 段落——`log.md:122` 自己寫明是這兩類）。
  **總數與分類 VERIFIED。** 但「改頁面的是哪 3 筆」`log.md` 沒列；
  由 run 1 的 8 筆扣除已知的 5 筆放寬項**推得**為 L6（`numbers.md:55` 的 `0.8107`）
  ＋2×L7（`first-mover-advantage.md:5`、`:86`）。這一步是本審查的推論，不是紀錄。
- 「一個為了通過而被放寬的檢查，不等於一個通過的檢查」——`log.md:122` 的
  workflow 欄幾乎是同一句話。**VERIFIED**
- 小修正：§6 寫「我只改了 **3 個頁面**」。`a5_lint_run1.txt` 顯示那 3 筆分佈在
  **2 個檔案**（`numbers.md`、`first-mover-advantage.md`）。原文應為「3 個問題」。

### 2.18 問題三「結構性修改四項」— 3 項 WRONG

這是 §2.1 之外第二個必須改的地方。判準很簡單：作業問的是「**你有沒有因此修改**
workflow／graph」。所以必須是**本輪發現之後**才加的東西。
`git show de8d030:AGENTS.md`（**init commit，A1 還沒跑**）已經包含：

| §6 稱「新增」 | 初始 commit `de8d030` 是否已有 | 判定 |
|---|---|---|
| 1. 新增「獨立 agent 審查」節點（§8a），寫的人不審自己、審查者拿不到起草對話 | **已有，整節逐字存在**（`de8d030:AGENTS.md:112–117`），含「The agent that wrote the text must not review its own text」與「the same input rule as B7」 | **WRONG**（內容描述正確，「新增」錯） |
| 2. 新增 B3 證據卡作為資訊閘門 | **已有**（`de8d030:AGENTS.md:67` B3 列完整存在） | **WRONG**，且 `log.md:162` 該列「Did it change the workflow?」欄自己寫 **no** |
| 3. 新增兩層保證水準（完整／輕量） | **沒有**。`log.md:141` 該列為 **yes**，確實是本輪新增 | **VERIFIED**（但見下） |
| 4. 把 wiki↔論文 與 wiki↔wiki 拆成兩種檢查（A3 與 A5） | **已有**。`de8d030:AGENTS.md:52` A3 列、`:54` A5 列，且 A5 的失敗邊從一開始就是「**contradiction** → A2」 | **WRONG** |

補充三點：

- **`AGENTS.md:88` 自己就否證了第 1、2、4 項**：「Order follows the instructor's
  demonstration graph, **with two added nodes (B8 equation check and B11 timing check)**」
  ——本輪相對於原始示範 graph 加的是 B8 與 B11，不是 §8a、B3、A3/A5。
  而 B8、B11 §6 一個字都沒提，它們卻各自抓到真缺陷（`log.md:178`、`:179`）。
- **第 3 項雖然成立，但沒進 schema**：`grep -c -i assurance AGENTS.md` → **0**。
  兩層保證水準只落在 `sources.md`、`index.md` 和各頁橫幅（`log.md:141`）。
  依 `AGENTS.md:13`「This file is the schema」，它不算改到 graph。
- **第 4 項真正成立的部分是「教訓」而非「修改」**：`log.md:124` workflow 欄
  「wiki↔source checking cannot find wiki↔wiki contradictions. The two checks are
  not substitutes.」——A5-01 **驗證**了這個既有設計，沒有創造它。這其實是更好的故事：
  「拆分不是我這輪加的，但這輪才證明它不是多餘的。」

**可以替換上去的四項真修改（`git diff de8d030 HEAD -- AGENTS.md` 全部可查）：**

| 真正的 schema 修改 | commit | 觸發它的事實 |
|---|---|---|
| §10 新增 model／effort policy（Opus 判斷、Haiku 機械） | `5acf804` | `log.md:29`：Haiku 版 A1 只抄了 eq. (1)–(2) |
| §2 新增四張登錄表 ＋「A2 writes」段，使 B8／B10 有可機器比對的對象 | `19779f3` | `log.md:60`：A4 的發現卡在 `checks/`，Graph B 讀不到 |
| §3 新增「標記推論」規則 ＋「論文自相矛盾」規則 | `6854f91` | A3 F16、F8 |
| §3 新增標籤 Scope 定義 ＋「引號即逐字（含 *sic*）」規則 | `e2d664a` | A3 r2、F4／F12／F19 |

這四項是真的、可用兩個 git 指令證明的，而且第一項（換模型）正好對應 §6 後面
「真正改變走向的三個決定全都是人做的」那段。目前它們被放在問題二的（乙）表裡，
問題三卻用了三個站不住的「新增」。**把材料換個位置就能從 WRONG 變成 VERIFIED。**

### 2.19 「相差約 105 倍」— OVERSTATED

`wiki/numbers.md:52–58` 的表（與 `a5_report.md:65–72` 同源）：

| γ | FMA 邊界 | s₁*=s₂* 邊界 | 嚇阻切換 γ/(2−γ²) | 切換 ÷ FMA |
|---|---|---|---|---|
| 0.1 | 0.0000534 | 0.00256 | 0.0503 | ≈ **940×** |
| 0.3 | 0.00150 | 0.0169 | 0.1571 | ≈ **105×** |
| 0.5 | 0.00867 | 0.0427 | 0.2857 | ≈ 33× |
| 0.7 | 0.0393 | 0.0951 | 0.4636 | ≈ 12× |
| 0.8 | 0.0960 | 0.1527 | 0.5882 | ≈ **6×** |

三個問題：

1. **105× 只是 γ = 0.3 這一格。** 全域範圍是 6×–940×。§6 寫「三個門檻…相差約 105 倍」
   沒有任何 γ 條件。
2. **它不是「三個門檻相差」的倍數**，而是**第一與第三個門檻**的比值（切換÷FMA）。
   中間那個門檻（s₁*=s₂*）不在這個比值裡。
3. **它直接違反來源自己寫下的禁令。** `wiki/numbers.md:66–68`：
   「The gap narrows sharply with competition, so 'two orders of magnitude' holds only
   up to about $\gamma = 0.3$ and **must not be stated generally**.」
   `a5_report.md:74–76` 同樣警告。而**同一份繳交文件的 §5** 寫的是正確版本
   「嚇阻門檻比 FMA 邊界高 **6 到 940 倍**」——§6 與 §5 互相衝突。

**改法**：「三個門檻嚴格排序，嚇阻門檻比 FMA 邊界高 6 到 940 倍（γ=0.3 時約 105 倍）」。

### 2.20 「FMA 消失之後領導者仍持續嚇阻、持續超額投資」— VERIFIED

`a5_report.md:76–81`：「at $\gamma=0.3$ the leader stops out-earning the follower at
$\theta\approx0.0015$, while $ds_2/ds_1$ stays negative until $\theta\approx0.157$.
So at the moment the FMA dies, the commitment is still working as described: CSR levels
are still strategic substitutes, the follower still retreats when the leader invests,
and the leader still invests more ($s_1^*>s_2^*$ survives until 0.0169). **Nothing about
deterrence has broken.**」
`wiki/numbers.md:60–64` 同樣結論：「**Deterrence has not broken — the leader is winning
the strategic game and losing on profit anyway.**」

嚴格排序 FMA < 投資 < 嚇阻 在表中五個 γ 全部成立。**VERIFIED**。
「不是靠更仔細讀論文得到的，而是 A5 跨頁一致性檢查的副產品」也 VERIFIED
（`log.md:124` workflow 欄：「this is now the sharpest point in the deck, and it came
out of a consistency check, not a content pass」）。

### 2.21 自報數字 4／8／15 — VERIFIED（本檔寫入前）

**本報告寫入前**的實際狀態：

| 項目 | §5／§6 寫 | 實數 | 依據 |
|---|---|---|---|
| 檢查報告 | 4 份 | **4** | `ls checks/*.md` = `a3_report.md`、`a4_report.md`、`a5_report.md`、`b7_report.md`（另有 9 個 `.txt` 原始輸出，未計入，與「另有原始腳本輸出」一致） |
| 可重跑腳本 | 8 支 | **8** | `ls scripts/` = a4_gammamax_confirm、a4_gammamax_hunt、a4_verify_kopel2021、a5_lint、b6_figures、b8_b11_checks、b9_inline_katex、build_wiki_site |
| git commit | 15 次 | **15** | `git log --oneline \| wc -l` |

**⚠️ 本報告會讓它過期。** 本檔 `checks/section6_review.md` 一旦存在，
`ls checks/*.md` 就是 **5 份**。受影響的兩處：

- §5「本次執行的成果」表：`| 檢查報告 | 4 份，約 26,000 字 |`
- 「附件清單」：列了 4 份 `checks/*` 報告

兩個都要處理。建議：§5 改成「**5 份**（含 §6 的獨立事實查核）」，
並在附件清單加一列 `checks/section6_review.md`。
把這份查核報告列進附件，對一份講「驗證」的作業反而是加分項。

另外 commit 數會因為「要不要 commit 這份報告」而再變一次。
建議在 §5 加一句「截至 commit `8d0f2fe`」把基準點釘住，避免下一次變動又失準。

### 2.22 舊值「6 份／7 支／12 次」— UNSUPPORTED

`log.md:197` 只記了「**Three of the counts** in my own submission document were wrong —
reports, scripts, commits」，**沒有記下錯誤的舊值**。
`繳交/繳交內容.md` 第一次進 git 是 `8d0f2fe`，當時已是修正後的 4／8／15
（`git show 8d0f2fe:繳交/繳交內容.md` 第 137–139 行）。
所以「6 份／7 支／12 次」在 repo 裡**沒有任何一手出處**——不是被否證，是無法查證。

這是 §6 全節唯一一處「憑記憶寫的數字」，而它出現的那一段主題正是
「憑印象寫的數字，不管主題是什麼，都會錯」。建議改成
「三個數字（報告／腳本／commit）都寫錯了，用腳本重數後是 4／8／15（舊值未留存）」。

（參考點：`A6_簽核清單.md:20–26` 留下了 A6 當時的計數——報告 4 份、腳本 **4** 支、
commit **8** 次。這證明計數是隨時間成長的，但仍無法還原「6／7／12」。）

---

## 3. 必須在繳交前修的（A 類）

按嚴重度排序。前四項都可以被評分者用一兩個指令拆掉。

1. **【最嚴重】問題一的 blocker 歸屬表：F2 與 F4 是 A4 寫的，不是 A1。**
   改成 A1→3、A4→2、A2→1、B3→1。答案（A1 最常出錯）不變，但表必須改。
   同時 §5 的「A4 符號驗證｜4 筆｜0」要加註 A4 產生了兩個 blocker。
   否證指令：`git log -S'Spillovers must be very low' --oneline --all`、
   `git show 5acf804:wiki/papers/Kopel2021-CSR.md | grep -c 'must be very low'`。
   （§2.1、§1）
2. **問題三的「結構性修改四項」有三項不是本輪的修改**（§8a、B3、A3/A5 拆分都在
   `de8d030` 初始 commit 裡；B3 那列的 log 自己寫 `no`）。
   否證指令：`git show de8d030:AGENTS.md`。
   建議換成 §2.18 末表列的四項真修改（§10 model policy、§2 登錄表、§3 兩次規則新增）。
3. **「57 筆／30 筆」→ 實際 60 筆／32 筆。** 二選一：改成 60／32（並把 §5 表補上 B3
   與交件 3 列），或保留 57／30 但明說排除交件三列。
   現狀的矛盾是：被排除的那三列之一，正是「最後一點」整段的證據。（§2.12）
4. **「相差約 105 倍」必須加 γ 條件或改成 6–940 倍。**
   它違反 `wiki/numbers.md:66–68` 自己寫的「must not be stated generally」，
   且與同文件 §5 的「6 到 940 倍」衝突。（§2.19）
5. **「人是這個 graph 裡唯一沒有被規範輸入輸出的節點」要改。**
   A6／B5 的 Reads 欄與失敗邊都有寫，而且 `A6_簽核清單.md` 就是「人該看什麼、
   抽查幾項、什麼情況退回」。改成「人工程序寫在一次性清單裡、沒進 schema，
   且 B5 連清單都沒有」。（§2.11）
6. **「新想法只被允許待在一個地方」要改。** 被 `wiki/numbers.md:46–50`
   （三門檻，`[own calculation]`，已上投影片 22–23）直接否證，也與
   §6 自己的「最後一點」衝突。改成「需要新算一輪的想法沒有出路」。（§2.14）
7. **「修正是…原本的設計假設只有生成節點會寫入」要改。**
   `de8d030:AGENTS.md` §8a 從第一天就有 fix → re-review。（§2.9）
8. **§5／附件清單的「檢查報告 4 份」會因為本檔變成 5 份。** 併同修正，
   並建議把本檔列入附件。（§2.21）

## 4. 不致命但不精確的（B 類）

9. 「第二名是『修正』」——四個實例都真，但名次沒有一致度量支撐
   （用 blocker 算是 0）。改成不帶名次的敘述。（§2.8）
10. 「下游每一道檢查都會回報通過」——對 F1/F2/F4 成立；F3、F5 是同頁矛盾，
    `log.md:77` 自己說 A5 lint 該抓到。請限定範圍。（§2.6）
11. 「A1 的 wiki 頁是 A2 的**唯一**輸入」——`AGENTS.md:78` 寫的是
    「A1 page + existing concept pages」。改成「本輪實際上的唯一輸入」。（§2.6）
12. （甲）表第二列「時長檢查移到 B6 寫稿前先定字數」是結論，不是已執行的移動
    （`AGENTS.md:97` B6 無字數預算，`:102` B11 仍是唯一時長關卡，
    且 `AGENTS.md` 最後修改於 `e2d664a`，早於 B6–B11）。第一列的 A2 連結檢查
    也只做過一次、未入規格。建議表格加「已入規格／只做一次／僅結論」一欄。（§2.15）
13. Q1 是「用 0 < θ₁ < θ₂ **重解模型**」，不是「比較靜態」。（§2.13）
14. 「我只改了 3 個頁面」→ 是 3 個**問題**，分佈在 2 個檔案。（§2.17）
15. 「6 份／7 支／12 次」無一手出處，建議標明舊值未留存。（§2.22）
16. B7 slide-4 的 Cause 欄有 B3 **和 B6** 兩個主體；只記 B3 會漏掉 B6 違反
    「May read: outline + its cards」的事實。（§2.4）
17. 「整輪 7 個 blocker」建議補一句：只有 A3／A5／B7 三個節點做嚴重度分級，
    A4／B8／B10／B11 結構上不產生 blocker。（§2.1）
18. 受審文字尚未 commit（`git status` 顯示 ` M`）。繳交前請確認交出的是這一版。

## 5. 做得好、不要動的部分

- **（乙）三條 §3 規則**：三條全部逐字可查，連「Added after A3 F4, F12, F19」
  這種觸發註記都對得上。這是全節最強的一段，也是真正的「把檢查移到寫入時」。
- **A3 r1 FAIL 在 Graph B 之前**：時序、commit、人工簽核三重可查。
- **捏造引文**：PDF 全文搜尋確認不存在，而且 p. 491 真有「spillovers are very low」
  這個鄰近詞組——建議補上這一點，它把「看起來已經查證過了」從修辭變成機制。
- **A5 放寬段**：8 = 3 改頁面 + 5 放寬（2 L5 + 3 L7）與 `a5_lint_run1.txt` 完全對帳。
  「一個為了通過而被放寬的檢查，不等於一個通過的檢查」是全節最誠實的一句。
- **三個門檻的實質發現**（排序、嚇阻未斷、副產品於一致性檢查）：全部 VERIFIED，
  只有倍數的陳述要加條件。
- **「最後一點」自承數字寫錯**：`log.md:197` 支持，而且它是全節唯一自我歸因的段落。
- **一個額外的、尚未被使用的好材料**：A4 的 loop plan（`log.md:36`）把自己的寫入範圍
  從 `AGENTS.md:80` 的「pass/fail report」放寬成「verified corrections to the wiki page」，
  然後在 `39bd252` 寫了一個帶引文的 🔎 box 進去——那個 box 裡就是 F4。
  擴權有記錄、後果沒有。用它來回答問題三，比三個站不住的「新增」有力得多。

---

## 判定

**FAIL**

理由：§6 的三個答案本身（A1 最常出錯、檢查往前移的三個方向、改了 workflow）
方向都站得住，支撐材料也大多真實可查——（乙）三條 §3 規則、A3 時序、捏造引文、
A5 放寬段、三門檻發現都通過了相當嚴格的查核。

但 **A 類 8 項裡有 4 項是會被兩三個 git／grep 指令當場拆掉的事實錯誤**，
而且集中在兩個答案的**主證據**上：

- 問題一的核心證據表把 **A4 寫出來的兩個 blocker 算給 A1**（F2、F4）；
- 問題三的四項「結構性修改」有**三項存在於 A1 還沒跑的初始 commit**，
  其中一項的 log 自己寫著 `no`。

在一份主題是「驗證、獨立審查、不要憑印象寫數字」的作業裡，這兩處的性質
和它自己批評的錯誤完全相同（憑 `log.md` 的 Cause 欄回憶歸因、憑印象說「新增」），
所以不能降級為 PASS WITH FIXES。

A 類 8 項改完即可達 **PASS**——**不需要改結論，只需要改歸屬、換證據、重數兩個數字**。
修改量估計：問題一一張表、問題三一張表、兩個數字、四句限定語。
論點不會變弱；§2.1 與 §2.18 提供的更正版本其實比原文更尖銳。

---

*本報告由獨立 reviewer 撰寫，未修改 `繳交/繳交內容.md`。
重數 `log.md` 的腳本與 PDF 文字檔在本次 session 的 scratchpad，未留在 repo。
本檔使 `checks/*.md` 由 4 份變為 5 份——見 §2.21。*
