# HW10 繳交總覽

繳交標題格式：**〈學校〉 〈學號〉 〈系級〉 〈姓名〉 看懂排球：從基本規則到場上戰術**。尖括號內容需由本人填寫。

已部署 GitHub Pages，公開 Wiki 與簡報已實際開啟並測試。以下連結可直接貼到作業繳交欄位；[GitHub 完整成果](https://github.com/Eugene-xyz/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10) 保留原始資料、知識庫、graph 與檢查紀錄。[發布驗證](reports/deployment.md)。

## 1. LLM Wiki 主題與簡短介紹

主題為「看懂排球：從基本規則到場上戰術」，對象是室內六人排球的初學者，目標是看懂比分、輪轉、角色與攻防配合。Wiki 採原始來源、持久化知識頁與工作規範三層，保留 ingest、query、lint 操作；AI 整理內容，使用者確認主題取捨、大綱及整份內容稿。

## 2. LLM Wiki 成果

[Wiki 網頁](site/index.html)／[Markdown 索引](wiki/index.md)。已完成 S01–S06 **6 份有效 ingest**，形成 12 個主題、6 個來源頁及維護／問答頁，共 23 頁。六份來源包括 FIVB 正式規則、兩本教練手冊、USA Volleyball 兩篇教學文章及 FIVB 2026 測試公告。

長手冊只宣稱完成明列範圍，沒有將章節、鏡像或補充規程重複計算。證據見 [ingest 登錄](reports/ingest-register.json) 與 [來源閱讀範圍](reports/reading-register.json)。

公開 Wiki 網址：[閱讀排球 LLM Wiki](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/site/index.html)。

## 3. 教學 HTML 簡報

[18 頁 HTML 簡報](slides/index.html)，預估主講 18 分 20 秒，含 18 組自製圖解、可逐步切換的回合、三題測驗、展開補充與講解提示。54 組主張／條件可沿 [來源對照](site/slide-sources.html) 回到 Wiki 與原文。

公開簡報網址：[開啟 18 頁教學 HTML 簡報](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/slides/index.html)。

## 4. loop／graph 設計

取得來源 → 可讀性／版本／範圍檢查 → 擷取重點與證據 → 討論確認 → 整合 Wiki → lint → 依教學問題查詢 Wiki → 大綱與檢查 → H1 確認大綱 → 全文與檢查 → H2 確認全文 → 圖解 → J0 解析預檢 → HTML → 瀏覽器檢查 → 紀錄與反思。

- 每份來源重複取得、閱讀、整合及 lint；查詢不足時回補 Wiki，不直接用未查證內容寫簡報。
- 版本、條件或證據不足，回原文／Wiki；內容問題回全文；圖文不一致回圖解；版面與操作問題回 HTML。
- H1／H2 分別確認教學結構及內容，避免切版後才大幅改方向。檢查通過才前進；只重查受影響範圍。

完整流程圖、輸入輸出及退出條件：[Wiki workflow](reports/workflow.md)／[簡報 graph v1.1](reports/slides-graph.md)。

## 5. 一次實際執行與檢查

2026-11-22 完成從六份來源到 Wiki、核准大綱與內容、正式 HTML 的實際路徑。使用 Chrome 檢查 1440×1000、1024×768、390×844，包含翻頁、鍵盤、全螢幕、展開、測驗、圖解、來源及離線閱讀。182 項完整檢查與最後 19 項局部複查通過；同時保留失敗結果與代表截圖。

實際紀錄：[Wiki log](wiki/log.md)、[ingest 檢查](reports/checks/ingest-2026-11-22.md)、[內容檢查](reports/checks/content-review-2026-11-22.md)、[HTML 實測與修正](reports/checks/html-review-2026-11-22.md)。上線後另完成 89 個公開 HTTP 檔案檢查及 Chrome 操作抽查，見 [發布驗證](reports/deployment.md)。這些數字是程式斷言或請求數，不是獨立教學實驗次數。

## 6. 反思與調整

這次簡報部分，J「內容轉成 HTML」出現 3 個獨立問題：換行解析漏文、小桌面遮擋、粗體顯示。K 的最後圖文閱讀另發現輪轉圖落點與「網前」文字不符；也發現檢查器保留展開狀態的誤報。相同根因的多次檢查只算一次。

HTML01 原本在瀏覽器才被看見，後來將「統一換行、確認 18 頁與每頁必要區塊非空」移到 J0，再產生 HTML。保留瀏覽器與圖文閱讀檢查，因為非空或邊界通過不能保證內容正確。改動已反映於 graph v1.1，重新建置與複查亦已實際執行。

詳細統計、前後流程及限制見 [實作反思](reports/reflection.md)。18:20 尚未真人試講，也未測真實初學者理解；此處不把規劃當成實驗結果。
