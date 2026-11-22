# GitHub 資料夾整理紀錄

日期：2026-11-22（Asia/Taipei）。使用者要求先確認作業完成度，通過後保留必要成果與繳交證據，再整理成可放上 GitHub 的資料夾。

## 先檢查，再整理

[完成度審查](submission-audit.md) 及 [audit JSON](checks/submission-audit-2026-11-22.json) 判定核心實作完成：6 份 ingest、23 頁 Wiki、18 頁簡報、54 組來源對照、graph、實際執行與反思均具備。整理前重新跑過 Wiki／內容檢查，且交付 HTML／CSS／JS／SVG 與已測版本雜湊一致，才執行刪除。

公開網址、本人繳交標題及課程平台提交仍待完成；這次整理沒有將本機成果冒稱已公開上線。

## 刪除範圍

共刪除 **62 個檔案，6.49 MiB**。逐檔路徑、大小、原雜湊及理由在 [cleanup-manifest.json](cleanup-manifest.json)。

- 32 個中途 recheck 畫面／總覽 HTML：保留能證明 HTML03 粗體問題的 gallery-3.png。
- 5 個首次 delivery 截圖：新版已取代；保留 D01 輪轉落點錯誤的 06-movement.png。
- 23 個 final 的非必要逐頁截圖：保留 6 張代表桌面、小桌面、窄視窗、補充、完整回合與測驗的畫面。
- 1 個 Python bytecode 快取、1 個一次性總覽產生工具。

刪除前先確認仍保留的 Markdown／HTML 沒有連到候選檔，再逐檔驗證解析後的絕對路徑位於 HW10、目標是檔案、雜湊與規劃一致，最後以 PowerShell LiteralPath 刪除。沒有遞迴刪除資料夾或碰觸 HW10 以外的檔案。

## 保留什麼，以及原因

| 保留內容 | 原因 |
| --- | --- |
| raw 的全部 34 份檔案 | 原始快照、正文、取得時間與雜湊支撐 6 份 ingest；V01／V02 是 S06 的範圍核對依據 |
| 23 頁 Wiki 及全部正式教學檔 | 作業核心成果與近端引用路徑 |
| graph 草案、v1.0、v1.1、核准大綱與全文 | 證明先討論後生成、流程修改前後，以及人工確認節點 |
| 真實檢查 JSON、log、反思 | 保留當時時間、結果、錯誤與修正；失敗結果沒有刪掉 |
| 14 張來源原頁圖、15 張代表瀏覽器畫面 | 足以回查來源圖解、前後修正及主要裝置／操作證據 |
| 42 頁既有閱讀網頁及新增總覽頁 | Markdown 為主檔，HTML 供瀏覽器直接閱讀；兩者用途不同 |
| 主要建置、來源抽取及檢查工具 | 可重建、核對與延續 Wiki；不是只留不可追溯的成品 |

歷史 JSON 中的 `screenshots` 清單保留當時產出紀錄；部分已被本次清單明確刪除。不能把「曾產生 29 張」改寫成「當時只測了保留的 6 張」，也不能假裝所有舊圖現在都還存在。

## 為 GitHub 補齊的內容

- [SUBMISSION.md](../SUBMISSION.md)：依教授六項要求整理的繳交總覽。
- [GITHUB.md](../GITHUB.md)：根目錄上傳、Pages 設定、公開網址與部署後檢查。
- `.nojekyll`：直接發布已生成靜態檔；`.gitignore` 排除套件、快取及本機設定。
- `.gitattributes`：保留原始位元組，避免 Git 換行轉換造成既有原始檔雜湊失效。
- package.json／requirements.txt：固定維護時使用的套件版本；runtime.cjs 支援一般 npm 安裝、已安裝的瀏覽器及指定路徑。
- 新的瀏覽器測試預設使用時間戳名稱，避免不小心覆寫歷史 initial／delivery 結果。

沒有重新編寫核准的排球內容或修改圖解，沒有變更 ingest 次數，也沒有發布到遠端。

## 整理後驗證

整理後重新建置閱讀網頁，確認正式簡報與圖解位元組維持一致；再檢查本機連結、原始資料雜湊、檔案大小與路徑大小寫，以及模擬 GitHub 專案子路徑的 HTTP 操作。結果保存於 [repository-validation.json](checks/repository-validation-2026-11-22.json)，以該檔實際執行時間與通過狀態為準。


**實際結果（17:31:38 +08:00）：21 項通過，0 失敗、0 瀏覽器錯誤。** 檢查了 49 個正式／閱讀／圖庫 HTML 的本機引用與大小寫；模擬 `/hw10-check/` 子路徑，可開簡報、補充、測驗、來源主張、Wiki、繳交總覽及 S01 PDF。正式 HTML／CSS／JS 與全部 SVG 和原交付雜湊一致；原始來源也符合取得紀錄。代表畫面見 [繳交總覽 HTTP 截圖](checks/repository-2026-11-22/submission-http.png)。這是本機 HTTP 模擬，沒有宣稱已在 GitHub 公開上線。

### 本次檢查實際發現的事項

- **RC01：資料夾連結不適合直接發布。** 原始審閱報告連到 figures 資料夾，本機可以列目錄，但靜態發布需要入口。新增 14 張原頁圖的 [靜態圖庫](checks/figures/index.html)，更新該連結；原圖片不改，沒有刪除來源證據。修正後連結檢查通過。
- 首次 HTTP 瀏覽因執行環境限制本機網路而中止，未計為通過；在允許 Chrome 存取 127.0.0.1 的執行環境重跑，21 項通過。原失敗輸出保留於 [initial JSON](checks/repository-validation-initial-2026-11-22.json)。這是工具執行環境問題，未更改正式簡報功能。
- 來源語意、原始簡報逐頁內容與圖解沒有修改；不為資料夾整理再次宣稱完成一輪新 ingest 或新的 182 項全量瀏覽器測試。

紀錄同步後的結構複查另存為 [Wiki](checks/post-cleanup-wiki-2026-11-22.json)、[內容](checks/post-cleanup-content-2026-11-22.json) 與 [完整性](checks/post-cleanup-integrity-2026-11-22.json)。這些檔案保留實際時間及通過／失敗狀態，不覆寫整理前或原始實測結果。
