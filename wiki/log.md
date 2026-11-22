# Wiki 操作紀錄

本檔按 Asia/Taipei（UTC+08:00）追加。舊紀錄保留當時狀態；目前來源完成情況以來源頁與 [ingest 登錄](../reports/ingest-register.json) 為準。前置下載／審閱的時間已保存在 [原始檢查紀錄](../reports/checks/source-review-2026-11-22.md)，不回填成當時已完成 Wiki ingest。

## [2026-11-22 15:22 +08:00] ingest | S01–S06 | 開始正式入庫

- 輸入：使用者「好那接下來幫我正式寫入 LLM Wiki」的授權、AGENTS.md、六份原始快照、閱讀登錄與已提出的 12 頁架構。
- 執行：確認當時尚無 Wiki；依既有審閱範圍整合規則、角色、技術、戰術、觀賽及版本差異，保留來源定位。
- 邊界：本次建立 Markdown Wiki；HTML 簡報與網站尚不列為完成。待來源頁、主題頁、索引、檢查與紀錄皆具備後，才標 `ingested`。
- 已知事項：S03 出版年未確認、賽事程序措辭差異與未讀範圍移入 [issues](issues.md)，不阻擋有明確依據的內容整合。

## [2026-11-22 15:25 +08:00] ingest | S01 | 基準版本連結複查

- 網頁讀取工具兩次逾時；改用 curl 成功取得官方規則目錄，HTTP 200。
- 原文 Current Edition English 連到 S01 的 2025–2028 v05 文件；保存 [目錄快照與查核結果](../raw/verification/fivb-rules-index-2026-11-22.json)。
- 結果：維持 S01 作基準，S06／V01／V02 分項標註。這不是對所有聯盟修訂的完整調查。

[返回索引](index.md)

## [2026-11-22 15:44 +08:00] workflow | 摘要前的章節與雙欄檢查

- 將 S02 雙欄原頁確認、分欄重抽與 S03 目錄／章首頁定位核對加入 AGENTS.md。
- S03 先前章節標記及未處理範圍文字已更正，保留檢查報告；首次示範確認節點依使用者授權標為已完成。
- 這是具體檢查方法的補強；版本檢查在初始設計就已前移，沒有假裝是這次才新增。

## [2026-11-22 15:44 +08:00] query | 後排舉球員移到網前的身分與權限

- 15:42 先讀 Wiki 索引，再搜尋並閱讀輪轉、角色、系統與攻擊頁的相關段落。
- 輸出：[可重用問答](queries/setter-front-row-status.md)，以 S01 7.4、13、14 及 S03 51–53 頁為根據。
- 結果：Wiki 已足以回答；保留後排身分、球高、攻擊完成及攔網限制。未新增無來源的事實，也未開始製作簡報。

## [2026-11-22 15:44 +08:00] lint | 初次結構檢查

- [實際輸出](../reports/checks/ingest-lint-initial.json)：23 個 Wiki 頁面、417 個相對連結；檢查未通過。
- 六個來源對應的訊息源自同一個正反斜線比較問題，並非原始檔缺失或未整合。修改檢查器以統一相對路徑。

## [2026-11-22 15:45 +08:00] lint | 路徑修正後複查

- [實際輸出](../reports/checks/ingest-lint-recheck.json)：通過；6 個來源、12 個主題、1 個 query、全部 Wiki 可從索引到達。
- 原始快照雜湊相符、來源 metadata 與實際引用／反向連結一致。程式不負責判定內容事實。

## [2026-11-22 15:47 +08:00] lint | 內容複查與條件精確化

- 核對輪轉、自由球員、後排攻擊、角色／系統、作者觀點與賽事範圍，見 [內容檢查表](../reports/checks/ingest-2026-11-22.md)。
- 修正兩處混合來源的引用標籤；攔網定義明確區分身體部分高度與觸球點高度，依 S01 14.1.1。
- 保留 4 項 metadata／賽事／範圍限制，沒有把未知事項寫成已驗證規則。

## [2026-11-22 15:47 +08:00] ingest | S01 | 完成正式入庫

- 輸入：[來源頁](sources/s01-fivb-rules-2025-2028.md)、[原始取得紀錄](../raw/S01/retrieval.json)。
- 處理範圍：版本、目錄；規則第 1–21 條
- 整合輸出：[ball-contacts-and-faults](topics/ball-contacts-and-faults.md)、[blocking-and-defense](topics/blocking-and-defense.md)、[court-and-scoring](topics/court-and-scoring.md)、[libero](topics/libero.md)、[player-roles](topics/player-roles.md)、[rotation-and-positions](topics/rotation-and-positions.md)、[rule-versions-and-tests](topics/rule-versions-and-tests.md)、[serve-and-reception](topics/serve-and-reception.md)、[setting-and-attack](topics/setting-and-attack.md)、[systems-and-transition](topics/systems-and-transition.md)、[volleyball-overview](topics/volleyball-overview.md)、[watching-a-rally](topics/watching-a-rally.md)。
- 檢查：來源與原始檔可追溯，重要主張有定位；內容核對與結構複查已完成，索引、術語、問題清單及本紀錄同步更新。
- 狀態：`ingested`，只限明列範圍。未讀內容及保留差異見來源頁與 [issues](issues.md)；不將整本下載當成全文精讀。

## [2026-11-22 15:47 +08:00] ingest | S02 | 完成正式入庫

- 輸入：[來源頁](sources/s02-fivb-coaches-level-i.md)、[原始取得紀錄](../raw/S02/retrieval.json)。
- 處理範圍：版本、目錄；第 VI、VIII、IX 章相關文字；第 XI 章部分規則比較。
- 整合輸出：[blocking-and-defense](topics/blocking-and-defense.md)、[player-roles](topics/player-roles.md)、[rule-versions-and-tests](topics/rule-versions-and-tests.md)、[serve-and-reception](topics/serve-and-reception.md)、[setting-and-attack](topics/setting-and-attack.md)、[systems-and-transition](topics/systems-and-transition.md)、[volleyball-overview](topics/volleyball-overview.md)、[watching-a-rally](topics/watching-a-rally.md)。
- 檢查：來源與原始檔可追溯，重要主張有定位；內容核對與結構複查已完成，索引、術語、問題清單及本紀錄同步更新。
- 狀態：`ingested`，只限明列範圍。未讀內容及保留差異見來源頁與 [issues](issues.md)；不將整本下載當成全文精讀。

## [2026-11-22 15:47 +08:00] ingest | S03 | 完成正式入庫

- 輸入：[來源頁](sources/s03-fivb-coaches-level-ii.md)、[原始取得紀錄](../raw/S03/retrieval.json)。
- 處理範圍：目錄；第 III 章第 10 節 Technical Skills（36–48 頁）及第 IV 章 Advanced Tactics 相關部分（49–57 頁）。
- 整合輸出：[blocking-and-defense](topics/blocking-and-defense.md)、[libero](topics/libero.md)、[player-roles](topics/player-roles.md)、[rotation-and-positions](topics/rotation-and-positions.md)、[rule-versions-and-tests](topics/rule-versions-and-tests.md)、[serve-and-reception](topics/serve-and-reception.md)、[setting-and-attack](topics/setting-and-attack.md)、[systems-and-transition](topics/systems-and-transition.md)。
- 檢查：來源與原始檔可追溯，重要主張有定位；內容核對與結構複查已完成，索引、術語、問題清單及本紀錄同步更新。
- 狀態：`ingested`，只限明列範圍。未讀內容及保留差異見來源頁與 [issues](issues.md)；不將整本下載當成全文精讀。

## [2026-11-22 15:47 +08:00] ingest | S04 | 完成正式入庫

- 輸入：[來源頁](sources/s04-recipe-for-a-setter.md)、[原始取得紀錄](../raw/S04/retrieval.json)。
- 處理範圍：L001-L033，完整文章正文
- 整合輸出：[player-roles](topics/player-roles.md)、[setting-and-attack](topics/setting-and-attack.md)、[systems-and-transition](topics/systems-and-transition.md)、[watching-a-rally](topics/watching-a-rally.md)。
- 檢查：來源與原始檔可追溯，重要主張有定位；內容核對與結構複查已完成，索引、術語、問題清單及本紀錄同步更新。
- 狀態：`ingested`，只限明列範圍。未讀內容及保留差異見來源頁與 [issues](issues.md)；不將整本下載當成全文精讀。

## [2026-11-22 15:47 +08:00] ingest | S05 | 完成正式入庫

- 輸入：[來源頁](sources/s05-defense-as-a-team.md)、[原始取得紀錄](../raw/S05/retrieval.json)。
- 處理範圍：L001-L022，完整文章正文
- 整合輸出：[blocking-and-defense](topics/blocking-and-defense.md)、[player-roles](topics/player-roles.md)、[serve-and-reception](topics/serve-and-reception.md)、[systems-and-transition](topics/systems-and-transition.md)、[watching-a-rally](topics/watching-a-rally.md)。
- 檢查：來源與原始檔可追溯，重要主張有定位；內容核對與結構複查已完成，索引、術語、問題清單及本紀錄同步更新。
- 狀態：`ingested`，只限明列範圍。未讀內容及保留差異見來源頁與 [issues](issues.md)；不將整本下載當成全文精讀。

## [2026-11-22 15:47 +08:00] ingest | S06 | 完成正式入庫

- 輸入：[來源頁](sources/s06-fivb-2026-rule-tests.md)、[原始取得紀錄](../raw/S06/retrieval.json)。
- 處理範圍：L001-L027，完整公告正文
- 整合輸出：[ball-contacts-and-faults](topics/ball-contacts-and-faults.md)、[court-and-scoring](topics/court-and-scoring.md)、[libero](topics/libero.md)、[rotation-and-positions](topics/rotation-and-positions.md)、[rule-versions-and-tests](topics/rule-versions-and-tests.md)、[setting-and-attack](topics/setting-and-attack.md)。
- 檢查：來源與原始檔可追溯，重要主張有定位；內容核對與結構複查已完成，索引、術語、問題清單及本紀錄同步更新。
- 狀態：`ingested`，只限明列範圍。未讀內容及保留差異見來源頁與 [issues](issues.md)；不將整本下載當成全文精讀。

## [2026-11-22 15:47 +08:00] lint | 最終完成狀態與一致性檢查

- 結果：passed；6 個來源頁、12 個主題頁、1 個 query，Wiki 合計 23 個 Markdown 頁面。
- 檢查 484 個本機相對連結，無死連結、無索引不可達頁；來源對應、完成紀錄、狀態與原始檔完整性通過。
- 實際輸出保存於 reports/checks/ingest-lint-final.json。此為內容複查及狀態同步後的正式檢查；不包含尚未製作的 HTML。

## [2026-11-22 16:14 +08:00] workflow | 採用已確認的簡報 graph v1.0

- 輸入：使用者確認 graph，要求先整理大綱並等確認後再寫逐頁內容；沿用兼顧講解與自讀、整份內容稿確認的偏好。
- 節點及輸出：保留原討論草案，另存 [簡報 graph](../reports/slides-graph.md)；同步 [AGENTS.md](../AGENTS.md)、[README](../README.md) 及 [整體流程](../reports/workflow.md)。
- 檢查：H1 大綱確認與 H2 整份內容確認順序一致；圖解／HTML 在 H2 後。graph 已確認，大綱仍未確認。
- 問題與修正：未新增退回路徑；此次是落實使用者決策，不宣稱為執行錯誤後的流程改進。未解事項：等待 H1。

## [2026-11-22 16:14 +08:00] query | 從 Wiki 整理 18 頁教學大綱

- 輸入：[索引](index.md)、12 個主題、6 個來源頁相關定位、[既有 query](queries/setter-front-row-status.md) 與 [issues](issues.md)。
- 執行 A–C：建立 [brief](../slides/brief.md)、[17 組證據](../slides/evidence.md)、[大綱 v0.1](../slides/outline.md) 與 [來源對照](../slides/source-map.md)。
- 結果：18 頁，主講預估 18 分 20 秒，精簡主頁與展開補充；未新增排球知識或 ingest 篇數。
- 檢查：每頁先有 Wiki 支持；版本與教練觀點分開；必要條件保留；未解暫停措辭及未知出版年不填造。未發現需補知識的缺口，無本輪內容錯誤修正。
- 尚未執行：逐頁完整文案、測驗答案、正式圖解、HTML、試講與讀者測試。

## [2026-11-22 16:14 +08:00] lint | 大綱 v0.1 與來源對照

- 輸入：大綱、brief、evidence、source-map、已確認 graph 與更新的專案入口。
- D 節點：閱讀檢查教學順序、目標覆蓋及條件；程式檢查頁數、欄位、ID、時間、對照、狀態與本機連結。
- 結果：65 個結構斷言通過；18 頁／1,100 秒；當次 268 個相對連結有效。詳見 [實際檢查紀錄](../reports/checks/outline-review-2026-11-22.md) 及 [JSON](../reports/checks/outline-review-2026-11-22.json)。
- 發現問題與修正：本輪檢查沒有失敗項，未新增錯誤 ID；第 06、08、11 頁密度列為下一階段的預防檢查，不算實際錯誤。
- 未解事項：停在 H1 等待使用者確認大綱；尚無 HTML 或圖解實測，不宣稱完整作業已完成。

## [2026-11-22 16:34 +08:00] workflow | H1 已通過，執行 E／F 並交 H2

- 輸入：使用者確認 18 頁大綱 v0.1，明確要求完成整份逐頁內容。
- 變更：記錄 [大綱](../slides/outline.md) 的 H1 確認；同步 [AGENTS.md](../AGENTS.md)、[brief](../slides/brief.md)、[graph](../reports/slides-graph.md)、README 與整體流程狀態。
- 檢查：頁數、標題、順序、固定 ID 與原時間預算未變；整份內容尚待 H2，正式素材與 HTML 未開始。
- 問題與修正：沿用既有 F→E／R 路徑，不新增流程順序；沒有把 H1 授權擴張為 H2。

## [2026-11-22 16:34 +08:00] query | 完成整份 18 頁內容稿與 54 組主張對照

- 輸入：Wiki 索引、12 個主題、既有 query、來源定位、issues，以及已核准大綱；[本輪輸入雜湊](../reports/checks/content-baseline-2026-11-22.json)。
- E 輸出：[content.md v0.1](../slides/content.md)，包含主頁、完整補充、講解提示、圖解規格／圖說、三題測驗及答案；[source-map v0.2](../slides/source-map.md) 細化為 54 組主張／必要條件。
- F 發現 CT01：第 03 頁場地細節和 Wiki 明示範圍未完全對齊。刪除非必要側向延伸；回查 S01 衍生文字 PDF 15 的 1.3.4／1.4.1，補明 [場地頁](topics/court-and-scoring.md) 的攻擊線後緣與場內前區界線，更新 [S01 定位](sources/s01-fivb-rules-2025-2028.md) 後同步 C03.1。
- 另複核 V01 PDF 18 的接發第一個動作與八次換人條文，既有適用範圍與定位可沿用。原始檔未改，沒有新增來源或 ingest 次數。
- 修正後閱讀核對：主頁、圖解規格、Wiki 與來源對照一致；未採用未解的挑戰後暫停措辭。詳細證據見 [內容檢查紀錄](../reports/checks/content-review-2026-11-22.md)。
- 未解事項：H2 尚待使用者確認；時間未試講，圖解尚未實繪。

## [2026-11-22 16:34 +08:00] lint | 內容 v0.1 與受影響 Wiki 的一致性檢查

- 輸入：已核准大綱、內容稿、source-map v0.2、專案入口與 Wiki。
- 執行：閱讀核對規則條件、版本、圖解語意、回合與答案；[check_slide_content.py](../scripts/check_slide_content.py) 檢查結構與跨檔一致性。
- 結果：18 頁／1,100 秒；54 組主張對照；123 個結構斷言通過，789 個本機相對連結有效。第 06、13 頁輪轉前後配置各六人且對應正確。詳見 [JSON](../reports/checks/content-review-2026-11-22.json)。
- 問題：本輪只有一個獨立範圍問題 CT01；已修正並閱讀複查，程式檢查無失敗項。測驗選項順序的例行調整不另算事實錯誤。
- 限制：未做正式素材、HTML／瀏覽器、試講或真實初學者測試；不能把內容檢查通過當作版面通過。下一步等待 H2。

## [2026-11-22 17:08 +08:00] workflow | H2 已確認與 J0 建置前檢查

- 輸入：使用者確認整份內容稿 v0.1，授權完成正式圖解、18 頁 HTML 及實際操作／版面檢查；H1／H2 均完成。
- 執行：G／V／J／K。產生 18 組、31 個 SVG 狀態檔，簡報及由 Markdown 產生的 Wiki 閱讀入口。沒有新增來源或 ingest 次數，原始快照未改。
- 流程修改：HTML01 在瀏覽器發現 CRLF 解析漏文後，先統一換行並加 J0（H2、18 頁、每頁必要區塊非空）；QA01 將初始與展開狀態分開量測。已同步 [AGENTS](../AGENTS.md) 與 [graph v1.1](../reports/slides-graph.md)，保留 v1.0 快照。
- 輸出：[正式簡報](../slides/index.html)、[Wiki 網頁](../site/index.html)、[素材紀錄](../assets/credits.md)、README、檢查與反思。核准教學文字、頁序與時間維持不變。

## [2026-11-22 17:08 +08:00] lint | HTML 圖解、內容、操作與三種視窗

- 輸入：已核准的內容稿、大綱、54 組主張對照、正式 SVG、HTML 與 Wiki。
- 已執行：Chrome 真實瀏覽器以本機 file URL 測試 1440×1000、1024×768、390×844，翻頁、鍵盤、全螢幕、圖解、測驗、展開、來源新分頁、原文路徑及離線閱讀。
- 結果：16:51:13 的 154 項檢查有 2 項失敗；修正後 16:58:19 的完整複查 182 項通過，沒有瀏覽器腳本錯誤。初次漏文曾導致檢查中斷，沒有冒稱完整通過。另保存 29 張複查截圖。
- 問題與處理：HTML01 換行解析、HTML02 小桌面角色頁高度、HTML03 粗體顯示；QA01 為檢查器狀態殘留，不當成 HTML 內容缺陷。詳見 [HTML 實測](../reports/checks/html-review-2026-11-22.md)。
- 本輪交付前的受影響範圍複查（測驗圖幅與更新後連結）獨立保存到 [delivery 結果](../reports/checks/html-2026-11-22/delivery/browser-results.json)；以該檔實際時間及結果為準。
- 限制：18:20 未真人試講，未測真實初學者理解、其他瀏覽器及實體手機，未部署公開網址。反思依已記錄的根因整理，見 [reflection](../reports/reflection.md)。

## [2026-11-22 17:12 +08:00] lint | 最後圖文對照 D01 與局部複查

- 輸入：[delivery 首輪結果](../reports/checks/html-2026-11-22/delivery/browser-results.json)，18 項程式檢查通過。
- 發現：閱讀第 06 頁第二狀態截圖時，C 的標記落在攻擊線後，與「移到網前」不符。這是 G 的圖文對齊問題，由 K 最後閱讀發現；沒有因程式通過而忽略。
- 修正：沿 K→G 調整落點到網前，保留原後排身分、六人與核准說法；另檢查與其他標記間距。同步報告與反思，D01 只計一次。
- 複查輸出：[delivery-recheck](../reports/checks/html-2026-11-22/delivery-recheck/browser-results.json)，以檔內實際結果為準；新增幾何條件並重新閱讀截圖。正式主頁文字、CSS、JS 沒有變更。

## [2026-11-22 17:14 +08:00] lint | 交付複查完成

- D01 修正後的 delivery-recheck：17:12:37 +08:00，19 項通過，無失敗與腳本錯誤；已重新閱讀輪轉截圖，C 的位置與「網前但仍後排」一致。
- [內容檢查](../reports/checks/content-html-delivery-2026-11-22.json)：17:13:01，124 個斷言及 821 個受檢連結通過；18 頁、54 組主張與 18:20 預估未改。
- [Wiki lint](../reports/checks/wiki-lint-html-delivery-2026-11-22.json)：17:13:03，23 頁、6 個來源、532 個連結通過，原始檔雜湊符合取得紀錄。
- 本次只再同步紀錄與生成的閱讀網頁，不重新計入 ingest、不將結構測試當成排球事實驗證。最終檔案與連結結果見 [交付完整性](../reports/checks/final-artifact-integrity-2026-11-22.json)。

## [2026-11-22 17:29 +08:00] workflow | 作業完成度審查後整理 GitHub 資料夾

- 輸入：使用者要求先核對作業，核心完成後整理成可全部上傳 GitHub 的資料夾，保留教授要求的成果與證據。
- 審查：6 份 ingest、23 頁 Wiki、18 頁 HTML、54 組來源對照、graph、執行紀錄與反思完整；整理前 Wiki／內容檢查通過，正式 HTML／CSS／JS／SVG 雜湊未變。見 [完成度審查](../reports/submission-audit.md)。公開網址與本人繳交標題仍待填寫，沒有把本機檔案當成公開連結。
- 清理：逐檔確認路徑留在 HW10、雜湊未變且沒有保留文件連到它，刪除 62 個過渡截圖、快取與一次性總覽工具，共約 6.49 MiB。原始資料、全部來源、核准內容、graph 前後版本、真實成功／失敗 JSON 與代表截圖保留；見 [清單](../reports/cleanup-manifest.json)。
- 輸出：SUBMISSION.md、GITHUB.md、更新 README、Git 設定及依賴版本；建置工具可使用一般 npm 安裝與指定瀏覽器，既有簡報主張與圖解不改。沒有建立遠端儲存庫、推送或部署。
- 後續檢查：重建閱讀網頁，核對原始雜湊、正式產物、檔案大小、連結與大小寫，並模擬專案子路徑下的瀏覽器操作。實際結果保存在 [整理後驗證](../reports/checks/repository-validation-2026-11-22.json)；不覆寫歷史結果或把刪除的重複截圖列成目前仍保留。

## [2026-11-22 17:33 +08:00] lint | GitHub 上傳資料夾驗證

- [repository validation](../reports/checks/repository-validation-2026-11-22.json)：17:31:38 +08:00，21 項通過，無失敗及瀏覽器錯誤。以大小寫敏感的本機 HTTP 伺服器模擬專案子路徑，檢查操作、來源及 PDF；不是遠端部署測試。
- RC01：原頁圖只有資料夾連結，已補靜態圖庫入口；原始 14 圖與來源快照未改。首次 HTTP 測試的環境限制與中止紀錄保留，換到允許本機連線的環境後完成複查。
- 保留：6 份有效 ingest、23 頁 Wiki、18 頁簡報、31 個 SVG、54 組來源對照、graph、反思及實測證據；原始資料雜湊與已交付 HTML／CSS／JS／SVG 一致。
- 整理紀錄見 [repository-cleanup](../reports/repository-cleanup.md)。公開網址、姓名等繳交標題及課程平台提交仍待後續處理；本次未執行發布。

## [2026-11-22 17:47 +08:00] workflow | GitHub 上傳與 Pages 公開驗證

- 輸入：使用者明確授權發布至 Eugene-xyz 已建立的 HW10 儲存庫；核心成果及整理檢查已完成。
- 執行：保留遠端 Initial commit，在 main 接續提交完整目錄；Pages 從根目錄發布，HTTPS 啟用。首次內容提交為 3aee131，部署工作 45008733642 成功。
- 實際結果：公開簡報與 Wiki 均可瀏覽；Chrome 抽查翻頁、鍵盤、補充、來源追溯、目錄、三題測驗及放大圖。另以不帶登入資訊的公開 HTTP 請求檢查 89 項，全數通過；83 檔內容雜湊一致，6 原始來源可取得。
- 輸出：正式網址回填 README、SUBMISSION、GITHUB；新增 [發布紀錄](../reports/deployment.md)、[HTTP 結果](../reports/checks/pages-2026-11-22/initial-http.json)、[瀏覽器觀察](../reports/checks/pages-2026-11-22/browser-observations.json) 與代表截圖。重新建置文件閱讀網頁；原始快照、核准教學內容及簡報互動未改。
- 問題：Git 的預設空白檢查將保留的 CRLF 與原始內容空白列為提示；沒有更動來源原文以消除提示，沿用保留位元組及雜湊比對。
- 限制：此次公開抽查不重複宣稱全套 182 項或所有手機版面已重新測過。尚需本人填寫繳交標題並於課程平台提交；沒有代填未知身分或代交作業。

## [2026-11-22 18:18 +08:00] query | 完整 graph 匯出 PNG 並更新 GitHub

- 輸入：使用者要求將對話中的完整流程圖轉為可放入作業的 PNG，存入 HW10 並同步 GitHub。
- 輸出：[PNG 流程圖](../assets/workflow/hw10-graph.png)、SVG、Mermaid 原始檔、匯出工具與 [檢查紀錄](../reports/graph-export.md)；README、SUBMISSION 及既有流程說明加入圖片入口。
- 已檢查：24 個節點、41 條連線完整；中文字與標籤未越出畫布，並逐段閱讀最終圖片。圖片為 2692 × 10186 像素、白底、約 0.9 MiB，H1/H2 與 J0 有標示。
- 修正：匯出檢查器曾因 Mermaid 節點前綴及空白 SVG 標籤誤判；已修正後複查。為了閱讀網頁能顯示相同圖片，建置器新增圖片 src 的相對路徑轉換。
- 範圍：只整理既有流程的圖像呈現與入口，未增加 ingest、變更核准教學內容或修改原始來源。公開檔案仍需在推送後以實際部署結果核對。
