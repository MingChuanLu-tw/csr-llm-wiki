# 這個資料夾在公開版本中刻意留空

`raw/` 依 `AGENTS.md` §1 是唯讀的來源資料夾，原本放五篇論文的 PDF。

公開版本不包含那些 PDF：五篇裡只有 Kopel (2021) 是 CC BY 4.0 開放取用，
另外四篇是付費期刊論文（*Managerial and Decision Economics*、*Energy Economics*、
*The Manchester School* 等），公開散布全文會侵犯版權。

五篇的完整引用與 DOI 在 [`wiki/sources.md`](../../wiki/sources.md)。
Kopel (2021) 可由 doi:10.1007/s10203-021-00328-9 免費取得。

要重跑驗證腳本（`scripts/a4_*.py`）不需要 PDF——它們從論文的 eq. (1)
以符號方式重新推導模型，不讀 PDF。需要 PDF 的只有人工比對頁面影像那一步（A3）。
