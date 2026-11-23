# CSR 領導、外溢與先行者優勢 — LLM Wiki ＋ 教學簡報

115-1 TAICA《生成式 AI：文字與圖像生成的原理與實務》**第十週作業** ／ 呂明權

### 👉 [線上瀏覽（GitHub Pages）](https://mingchuanlu-tw.github.io/csr-llm-wiki/)

| | |
|---|---|
| **教學簡報** | https://mingchuanlu-tw.github.io/csr-llm-wiki/slides/ — 30 張正片 ＋ 7 張備用，← → 翻頁 |
| **LLM Wiki** | https://mingchuanlu-tw.github.io/csr-llm-wiki/wiki.html — 19 頁、約 17,800 詞（`wc -w`，含公式與表格；散文約 14,000 詞，見 [`checks/wiki_wordcount.txt`](checks/wiki_wordcount.txt)）、644 條方程式 |
| **流程圖** | https://mingchuanlu-tw.github.io/csr-llm-wiki/workflow.svg |

---

## 這是什麼

把 Karpathy 的 LLM Wiki 方法套用到讀論文：五篇論文放進唯讀的 `raw/`，經過一條
**有驗證關卡的 graph**（不是單一 loop）累積成 wiki，再由第二條 graph **只根據通過驗證的
wiki** 產出 30–45 分鐘研討會用的簡報與逐字稿。

主來源 Kopel (2021), *Decisions in Economics and Finance* 44: 489–505（CC BY 4.0）
做完整深度：12 條方程式全部用 sympy 從 eq. (1) 重新推導、兩輪獨立審查。
另外四篇做輕量深度，每頁都標示保證水準。

設計原則一句話：**錯誤要在離源頭最近的地方被抓到。**
每道關卡都是一支腳本或一份有逐條判定的獨立審查報告——說「檢查一下」不算驗證。

## 作業要求對應

| 要求 | 在哪裡 |
|---|---|
| 至少 5 份來源、用「先討論後生成」 | [`wiki/sources.md`](wiki/sources.md)、[`wiki/`](wiki/) 共 19 頁 |
| LLM Wiki 連結 | [wiki.html](https://mingchuanlu-tw.github.io/csr-llm-wiki/wiki.html) |
| 教學 HTML 簡報連結 | [slides/](https://mingchuanlu-tw.github.io/csr-llm-wiki/slides/) |
| loop / graph 的流程設計說明 | [`繳交/繳交內容.md`](繳交/繳交內容.md) 第四節 ＋ [`workflow.svg`](docs/workflow.svg) ＋ [`AGENTS.md`](AGENTS.md) |
| 反思：哪個節點最常出錯、檢查往前移到哪、有沒有改流程 | [`繳交/繳交內容.md`](繳交/繳交內容.md) **第六節** |

## 流程證據

| 檔案 | 內容 |
|---|---|
| [`AGENTS.md`](AGENTS.md) | 規格書：每個節點可讀什麼、可寫什麼、不可做什麼、失敗退回哪裡 |
| [`log.md`](log.md) | **90 筆**執行紀錄，其中 **50 筆改變了流程**。反思完全由這份表寫出來 |
| [`checks/`](checks/) | 逐條判定的報告（份數見目錄）：A3 獨立審查（兩輪）、A4 符號驗證、A5 跨頁矛盾、B7 忠實度，以及對第六節反思本身的兩輪審查 |
| [`scripts/`](scripts/) | 8 支 Python ＋ 1 支瀏覽器端檢查腳本，全部可重跑 |
| [`notes/`](notes/) | 10 張證據卡、30 張投影片大綱、英文逐字稿（4,710 字 → 36.2 分鐘） |
| [`HISTORY.md`](HISTORY.md) | 完整 git 歷史（本 repo 是不含 PDF 的重建快照，歷史與本機不對應，原因見下） |

## 流程抓到的四個 blocker

| 節點 | 抓到什麼 |
|---|---|
| A3 獨立審查 | 一條帶頁碼的引文**在論文裡並不存在**；論文對 Tetrault Sirsly & Lamertz 的立場被寫反；θ 的定義方向寫反 |
| A3 獨立審查 | `ds₂/ds₁` 符號反——而 A4 符號驗證**結構上不可能抓到**，因為那條式子是 A4 自己寫的 |
| A5 跨頁矛盾 | 兩頁寫著「先行者優勢死於嚇阻失效」，而反證就在 wiki 自己登錄的數字裡：嚇阻門檻遠高於先行者優勢的邊界 |
| B7 忠實度 | 證據卡承載的引文比 wiki 短，讓投影片的宣稱失去依據 |

**最值得看的實質發現**：領導者的先行者優勢消失之後，它仍然在嚇阻、仍然在超額投資。
三個門檻嚴格排序，倍數隨競爭強度遞減（γ=0.8 約 6 倍、γ=0.3 約 105 倍、γ=0.1 約 940 倍）。
這不是靠更仔細讀論文得到的，是**跨頁一致性檢查的副產品**。

## 自行重跑驗證

```bash
pip3 install sympy mpmath
python3 scripts/a4_verify_kopel2021.py    # 12 條方程式符號重推，不需要 PDF
python3 scripts/a5_lint.py                # wiki 機械健檢
python3 scripts/b8_b11_checks.py          # 方程式登錄比對 ＋ 逐字稿時長
```

## 為什麼沒有論文 PDF，也沒有完整 git 歷史

`raw/` 依 `AGENTS.md` §1 是唯讀來源資料夾。五篇論文中只有 Kopel (2021) 是 CC BY 4.0
開放取用，其餘四篇為付費期刊論文（*Managerial and Decision Economics*、
*Energy Economics*、*The Manchester School* 等），公開散布全文會侵犯版權。

因為那些 PDF 存在於原始 repo 的 git 歷史裡，公開版本是**不含 `raw/` PDF 的重建快照**，它的 commit 歷史與原始歷史不對應。
完整歷史與第六節引用的 8 個 commit hash 的用途保存在 [`HISTORY.md`](HISTORY.md)。
完整引用與 DOI 見 [`wiki/sources.md`](wiki/sources.md)。

---

繁體中文為主；`wiki/`、`slides_html/`、`notes/` 內容為英文（聽眾多為國際學生）。
方程式以 LaTeX 撰寫，由 KaTeX 0.16.9 在瀏覽器端排版。
