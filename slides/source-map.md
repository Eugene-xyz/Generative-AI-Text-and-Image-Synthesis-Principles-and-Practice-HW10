---
title: 簡報頁面與 Wiki 來源對照
version: 0.2
status: implemented-and-reviewed
updated: 2026-11-22
---

# 簡報頁面與 Wiki 來源對照

本版配合已確認的 [18 頁大綱 v0.1](outline.md) 與 [整份內容稿 v0.1](content.md)。前半保留逐頁導覽，後半以 Cxx.x 細化主頁、補充、圖解規格與測驗答案的證據。內容稿 H2 已通過；正式 SVG 與 HTML 已完成並實際檢查，見 [實測紀錄](../reports/checks/html-review-2026-11-22.md)。原有 54 組主張與證據內容未改。

閱讀順序：**投影片 → Wiki 頁面及段落 → 來源頁 → 原始快照／網址與定位**。E01–E17 是 [證據表](evidence.md) 的選材 ID，不是新增來源。

定位慣例：以下「印刷／PDF」分別指文件標示頁碼與從 1 起算的 PDF 頁序；S03 的兩種頁碼相同。網頁 Lxxx 是本機正文的段落標記，須連同小節名稱讀取，並非網站自帶行號。

## 逐頁導覽（沿用大綱的固定 ID）

| 頁碼／固定 ID | 內容範圍或圖解 | Wiki 頁面及段落主題 | 原始來源及定位 | 必須保留的範圍 |
| --- | --- | --- | --- | --- |
| 01 `slide-intro` | 室內六人排球；觀賽學習目標（E01、E17） | [排球全貌](../wiki/topics/volleyball-overview.md)：一句話及回合；[索引](../wiki/index.md) | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 6.1–6.3、7.3.1，印刷 22–24／PDF 24–26 | 學習目標是本專案教學設計；規則基準明標 2025–2028 |
| 02 `slide-rally-overview` | 發球開始、典型接舉攻防與回合結果（E01、E04） | [排球全貌](../wiki/topics/volleyball-overview.md)：回合流程；[觸球與犯規](../wiki/topics/ball-contacts-and-faults.md)：三擊及界內外 | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 6.1、8.1–8.4、9.1–9.3、12.1，印刷 22、27–29、32／PDF 24、29–31、34；[S02](../wiki/sources/s02-fivb-coaches-level-i.md) VI 技術範圍，印刷 76–118／PDF 80–122 | 常見配合順序是教學示意，不是必須用滿三擊 |
| 03 `slide-court` | 尺寸、中線、攻擊線與球壓線（E02） | [場地與計分](../wiki/topics/court-and-scoring.md)：場地 | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 1.1、1.3.3–1.3.4，印刷 12–13／PDF 14–15；8.3，印刷 27／PDF 29；圖 2／PDF 66。網高延伸：2.1.1，印刷 14／PDF 16 | 球碰界線與球員踩線的規則不能混用；區域不是輪轉身分 |
| 04 `slide-scoring` | 得分、贏局、贏比賽及發球權（E03） | [場地與計分](../wiki/topics/court-and-scoring.md)：計分與決勝局 | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 6.1–6.3，印刷 22–23／PDF 24–25；18.2.2，印刷 41／PDF 43（交換場地延伸） | S01 基準局制；兩分差不可省略；比分圖為自製示例 |
| 05 `slide-contacts` | 最多三擊、攔網另計、可用身體部位與持球（E04） | [觸球與犯規](../wiki/topics/ball-contacts-and-faults.md)：擊球次數與合法觸球 | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 9.1–9.3，印刷 28–29／PDF 30–31；14.4，印刷 35／PDF 37 | 不把攔網畫成一般第一擊；連續觸球須考慮例外 |
| 06 `slide-rotation` | 輪轉觸發、順序、身分與移動（E05） | [位置與輪轉](../wiki/topics/rotation-and-positions.md)：六位置、輪轉及站位時點 | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 7.3–7.7，印刷 24–26／PDF 26–28；圖 4／PDF 68；[S03](../wiki/sources/s03-fivb-coaches-level-ii.md) IV Switching，53 頁 | 接發方取得發球權才輪轉；發球方與接發方要求不同；2026 比較移至第 15 頁 |
| 07 `slide-roles` | 五類常見角色的工作（E06） | [球員角色](../wiki/topics/player-roles.md)：角色表；[術語表](../wiki/glossary.md) | [S03](../wiki/sources/s03-fivb-coaches-level-ii.md) III §10，45、47 頁；IV Team Formation，49–53 頁；[S02](../wiki/sources/s02-fivb-coaches-level-i.md) IX，印刷 130–132／PDF 134–136；[S04](../wiki/sources/s04-recipe-for-a-setter.md) Communication and Leadership，L009–L011 | 常見角色不是法定五個名額，也不是固定輪轉格；S04 是作者觀點 |
| 08 `slide-libero` | 不同球衣、後排替換與動作限制（E07） | [自由球員](../wiki/topics/libero.md)：辨識、替換、攻擊與傳球限制 | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 19.1–19.3，印刷 42–43／PDF 44–45；13.1.3，印刷 33／PDF 35 | FIVB 基準；攻擊限制保留整顆球高於網頂及完成攻擊條件；前區高手傳球規定若出現，必須完整呈現 |
| 09 `slide-serve-receive` | 發球控制、一傳品質與攻擊選項（E08） | [發球與接發](../wiki/topics/serve-and-reception.md)：發球目的、接發及觀察線索；[舉球與攻擊](../wiki/topics/setting-and-attack.md) | [S02](../wiki/sources/s02-fivb-coaches-level-i.md) VI Serving，印刷 85–89／PDF 89–93；Reception，印刷 107–110／PDF 111–114；[S05](../wiki/sources/s05-defense-as-a-team.md) Choosing a Defense，L009–L013。發球動作延伸：[S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 12.4，印刷 32／PDF 34 | 接發品質提供可能性線索；不能保證下一球的攻擊種類 |
| 10 `slide-setting-attack` | 舉球高度、方向、時間與攻擊節奏（E09） | [舉球與攻擊](../wiki/topics/setting-and-attack.md)：舉球、攻擊及節奏；[球員角色](../wiki/topics/player-roles.md) | [S02](../wiki/sources/s02-fivb-coaches-level-i.md) Coaching Hints for Setting，印刷 82／PDF 86；Spiking，印刷 90–97／PDF 94–101；IX，印刷 131–132／PDF 135–136；[S04](../wiki/sources/s04-recipe-for-a-setter.md) Athletic Ability and Touch，L006–L008；Game Understanding，L014–L016 | 配合與選擇是技戰術，不是只有舉球員能碰第二球；圖中分支代表選項 |
| 11 `slide-back-row-attack` | 一般後排球員跳起攻擊的合法條件（E10） | [舉球與攻擊](../wiki/topics/setting-and-attack.md)：後排攻擊；[觸球與犯規](../wiki/topics/ball-contacts-and-faults.md)：攻擊條件 | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 13.1–13.3，特別是 13.2.2–13.2.3、13.3.3，印刷 33–34／PDF 35–36；圖 8／PDF 72 | 核對身分、起跳腳、觸球時球高、完成攻擊；落地位置不可誤當起跳位置；自由球員另論 |
| 12 `slide-block-defense` | 攔防空間配合、縫隙、攔網後計次（E04、E11） | [攔網與防守](../wiki/topics/blocking-and-defense.md)：定義與攔防；[觸球與犯規](../wiki/topics/ball-contacts-and-faults.md) | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 14.1–14.6，印刷 34–35／PDF 36–37；[S02](../wiki/sources/s02-fivb-coaches-level-i.md) VI，印刷 98–106、111–118／PDF 102–110、115–122；[S05](../wiki/sources/s05-defense-as-a-team.md) In the Back，L017–L019 | 示意配置不是唯一站法；攔網的身體高度條件不等同觸球點必須高於網頂 |
| 13 `slide-five-one` | 5–1 與舉球員前後排輪次（E05、E06、E12） | [攻擊系統與轉換](../wiki/topics/systems-and-transition.md)：5–1；[位置與輪轉](../wiki/topics/rotation-and-positions.md)；[球員角色](../wiki/topics/player-roles.md) | [S03](../wiki/sources/s03-fivb-coaches-level-ii.md) IV，51–53 頁；[S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 7.3–7.4，印刷 24–25／PDF 26–27。其他系統延伸：[S02](../wiki/sources/s02-fivb-coaches-level-i.md) VIII，印刷 125–127／PDF 129–131 | 一位主要舉球員跨輪次組織；不能由數字推論五人同時在前排攻擊 |
| 14 `slide-transition` | 救球後重組、進攻及掩護（E13） | [攻擊系統與轉換](../wiki/topics/systems-and-transition.md)：防守轉攻與掩護；[攔網與防守](../wiki/topics/blocking-and-defense.md) | [S02](../wiki/sources/s02-fivb-coaches-level-i.md) IX，印刷 132–135／PDF 136–139；[S05](../wiki/sources/s05-defense-as-a-team.md) In the Back，L020–L022 | 不把給年輕球隊的保守救球建議當全隊通則；三狀態圖是教學示例 |
| 15 `slide-rule-context` | 接發站位與可移動時點的版本比較（E05、E14） | [版本差異](../wiki/topics/rule-versions-and-tests.md)：S01、S06 及後續規程；[位置與輪轉](../wiki/topics/rotation-and-positions.md)：基準與測試 | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 7.4，印刷 24–25／PDF 26–27；[S06](../wiki/sources/s06-fivb-2026-rule-tests.md) Out of rotation error，L006–L007；同來源頁的 V01：VNL 2026 §6.3(b)，印刷 16–17／PDF 17–18 | 圖上各自明標 S01／VNL 2026；公告、測試、後續採用不能合稱全球新規則 |
| 16 `slide-rally-walkthrough` | 既有自製回合：計次、角色、比分與發球權（E03、E04、E05、E15） | [觀賽回合](../wiki/topics/watching-a-rally.md)：自製完整回合；[場地與計分](../wiki/topics/court-and-scoring.md)；[位置與輪轉](../wiki/topics/rotation-and-positions.md) | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 6.1、7.6、9.1、14.4，印刷 22、26、28、35／PDF 24、28、30、37；角色及配合沿用第 07、09–14 頁的證據 | 案例本身由 Wiki 自製，不標成官方判例或真實賽事；逐事件核對已完成，見 C16.1–C16.2 |
| 17 `slide-quiz-recap` | 輪轉、身分、攔網後計次三題與解答（E03、E04、E05、E16） | [觀賽回合](../wiki/topics/watching-a-rally.md)；[舉球員身分問答](../wiki/queries/setter-front-row-status.md)；[位置與輪轉](../wiki/topics/rotation-and-positions.md) | [S01](../wiki/sources/s01-fivb-rules-2025-2028.md) 6.1、7.3–7.6、9.1、14.4，印刷 22、24–26、28、35／PDF 24、26–28、30、37；[S03](../wiki/sources/s03-fivb-coaches-level-ii.md) IV，51–53 頁 | 題幹、選項與答案已寫入內容稿；見 C17.1–C17.3 的條件與理由 |
| 18 `slide-sources` | 來源用途分類與追溯入口（E17） | [索引](../wiki/index.md)；[術語表](../wiki/glossary.md)；[問題清單](../wiki/issues.md) | 下方六個來源頁的「來源與版本」「處理範圍」「重點與證據定位」 | 這頁是導覽設計，不能取代前面逐頁引用；未知出版年不填造 |

## 六份來源的實際用途

| 來源 | Wiki 來源頁 | 本大綱的主要使用頁 |
| --- | --- | --- |
| S01 正式基準規則 | [Official Volleyball Rules 2025–2028](../wiki/sources/s01-fivb-rules-2025-2028.md) | 02–06、08、11–13、15–17 |
| S02 基礎技術與團隊配合 | [Coaches Manual Level I](../wiki/sources/s02-fivb-coaches-level-i.md) | 02、07、09–10、12、14；13 的系統延伸 |
| S03 角色與攻擊系統 | [Coaches Manual Level II](../wiki/sources/s03-fivb-coaches-level-ii.md) | 06–07、13、17 |
| S04 舉球員的教練觀點 | [Recipe for a Setter](../wiki/sources/s04-recipe-for-a-setter.md) | 07、10 |
| S05 防守判讀與攔防觀點 | [Defense is More Than Just Another Team System](../wiki/sources/s05-defense-as-a-team.md) | 09、12、14 |
| S06 指定賽事測試與適用範圍 | [2026 rule tests](../wiki/sources/s06-fivb-2026-rule-tests.md) | 15；V01 作後續規程核對，不另計來源篇數 |

## 逐項內容對照（內容稿 v0.1）

下表每列是一項主張或不可拆開判斷的條件組。來源 ID 連到上方六份來源頁；原文快照、完整網址與讀取範圍在來源頁。文字已對照 Wiki；講者提示和圖說若重述同一概念，沿用相同 ID。學習提問、呈現順序、互動選項與圖的配置是教學設計，不偽裝成來源中的實驗結果。

| 查核 ID | 所在／主張 | Wiki 頁面與段落 | 原始證據定位及必要界線 |
| --- | --- | --- | --- |
| C01.1 | 主頁／補充／圖：六人、隔網及規則基準 | [排球全貌](../wiki/topics/volleyball-overview.md)：一句話；[版本頁](../wiki/topics/rule-versions-and-tests.md)：基準 | S01 6.1、7.3.1，印刷 22、24／PDF 24、26；S01 版本資訊。三個學習提問是本課程設計 |
| C02.1 | 主頁／補充／圖：回合、典型接舉攻防；接不等於接住 | [排球全貌](../wiki/topics/volleyball-overview.md)：先看懂一個回合；[術語表](../wiki/glossary.md) | S01 6.1.3、9.2.2，印刷 22、28／PDF 24、30；S02 VI，印刷 76–97、107–110／PDF 80–101、111–114。流程非強制 |
| C02.2 | 主頁／補充：回合結束、最多三擊與攔網另計 | [觸球與犯規](../wiki/topics/ball-contacts-and-faults.md)：三次擊球、判斷表 | S01 6.1、8.3–8.4、9.1、14.4，印刷 22、27–28、35／PDF 24、29–30、37；一次兩次也可回球 |
| C03.1 | 主頁／補充／圖：尺寸、中線、攻擊線與區域／身分區別 | [場地與計分](../wiki/topics/court-and-scoring.md)：球場上要認得的線；[位置與輪轉](../wiki/topics/rotation-and-positions.md)：三種位置 | S01 1.1、1.3.3–1.3.4、1.4.1，印刷 12–13／PDF 14–15；7.4，印刷 25／PDF 27；圖 2／PDF 66。圖上 3 公尺量到攻擊線後緣 |
| C03.2 | 主頁／補充／圖：球壓線；不能和球員踩線混用 | [場地與計分](../wiki/topics/court-and-scoring.md)：邊界；[發球與接發](../wiki/topics/serve-and-reception.md)：規則底線 | S01 8.3，印刷 27／PDF 29；12.4、13.2.2，印刷 32、34／PDF 34、36；球的落地接觸部分須碰線 |
| C03.3 | 補充：標準網高及地方賽邊界 | [場地與計分](../wiki/topics/court-and-scoring.md)：球網及賽事提醒；[issues](../wiki/issues.md)：I03 | S01 2.1.1，印刷 14／PDF 16；未取得地方規程，不推定一律相同 |
| C04.1 | 主頁／補充：每球得分、25／15、兩分差、三局勝、發球權 | [場地與計分](../wiki/topics/court-and-scoring.md)：一分一局一場 | S01 6.1–6.3，印刷 22–23／PDF 24–25；7.6.2，印刷 26／PDF 28；完成回合與接發方取得發球權條件保留 |
| C04.2 | 主頁／圖／補充：24 平與第五局 14 平演算 | [場地與計分](../wiki/topics/court-and-scoring.md)：自製例子 | S01 6.2–6.3，印刷 23／PDF 25；依同一兩分差規則演算，並非真實比賽 |
| C04.3 | 補充：第五局 8 分交換場地 | [場地與計分](../wiki/topics/court-and-scoring.md)：決勝局 | S01 18.2.2，印刷 41／PDF 43；原站位順序不變，不是 8 分勝局 |
| C04.4 | 補充：暫停與一般換人；八次測試 | [場地與計分](../wiki/topics/court-and-scoring.md)：暫停或換人 | S01 15.1、15.4.1、15.6、19.3.2.1，印刷 36–37、43／PDF 38–39、45；S06 Substitutions L008–L009、V01 §6.3(c)／PDF 18。核准規程另論 |
| C05.1 | 主頁／補充／圖：三擊、攔網另計與攔網者第一擊 | [觸球與犯規](../wiki/topics/ball-contacts-and-faults.md)：三次擊球 | S01 9.1、14.4，印刷 28、35／PDF 30、37；不把攔網點亮第 1 格 |
| C05.2 | 主頁／補充／圖：任何部位可碰球，但不可接住／拋擲 | [觸球與犯規](../wiki/topics/ball-contacts-and-faults.md)：合法觸球 | S01 9.2.1–9.2.2，印刷 28／PDF 30；靜態手貼球不單獨證明持球 |
| C05.3 | 補充：連續觸球例外與第二擊解釋 | [觸球與犯規](../wiki/topics/ball-contacts-and-faults.md)：三次擊球及第二擊補充 | S01 9.1、9.2.3、14.2，印刷 28–29、35／PDF 30–31、37；S06 Double contact interpretation L004–L005；V01 §6.3(a)／PDF 17。第二擊舉球須留同側，不能推出持球合法 |
| C05.4 | 補充：球碰網、人觸網及球推網碰人 | [觸球與犯規](../wiki/topics/ball-contacts-and-faults.md)：常見判斷表 | S01 10.2–10.3、11.3.1、11.3.3、11.4.4，印刷 30–31／PDF 32–33；保留擊球動作、竿間球網與干擾條件 |
| C06.1 | 主頁／補充／圖：輪轉觸發、位置次序與繼續發球 | [位置與輪轉](../wiki/topics/rotation-and-positions.md)：六位置、何時輪轉 | S01 6.1.3、7.4.1、7.6.2，印刷 22、25–26／PDF 24、27–28；只有接發得分取得發球權才輪轉 |
| C06.2 | 主頁／補充／圖：角色、輪轉身分、戰術移動 | [位置與輪轉](../wiki/topics/rotation-and-positions.md)：三種位置、移動不改身分 | S01 7.3–7.4、13.2–13.3、14.1.1，印刷 24–25、33–34／PDF 26–27、35–36；S03 IV Switching，53 頁 |
| C06.3 | 補充／圖條件：接發方、發球方、腳的位置與版本 | [位置與輪轉](../wiki/topics/rotation-and-positions.md)：站位檢查時點 | S01 7.4、7.7，印刷 25–26／PDF 27–28；圖 4／PDF 68；S06 L006–L007、V01 §6.3(b)／PDF 17–18；發球方自由站位不取消場內與發球次序要求 |
| C07.1 | 主頁／補充／圖：角色與輪轉不同、五類不是五人、別稱 | [球員角色](../wiki/topics/player-roles.md)：一句話、角色及換位；[術語表](../wiki/glossary.md) | S03 IV 49–53 頁；S01 7.3–7.4、19，印刷 24–25、42–43／PDF 26–27、44–45；中文別稱依本 Wiki 用語，不作法定名額 |
| C07.2 | 主頁／補充：舉球組織、溝通、作者觀點及非資格 | [球員角色](../wiki/topics/player-roles.md)：舉球員及第二球 | S04 Athletic Ability and Touch、Communication and Leadership、Game Understanding、Physical Attributes，L006–L025；S01 9.1–9.3，印刷 28–29／PDF 30–31；保留 Peggy Kane-Hopton 歸屬 |
| C07.3 | 主頁／圖：主攻、攔中、接應主要任務及對角 | [球員角色](../wiki/topics/player-roles.md)：五類角色表 | S02 IX，印刷 130–133／PDF 134–137；S03 IV 51–52 頁；S05 Choosing a Defense L011–L014；常見分工，並非各隊唯一配置 |
| C07.4 | 主頁／補充：自由球員的專門後排角色 | [自由球員](../wiki/topics/libero.md)：一句話、辨認 | S01 19.1–19.3，印刷 42–43／PDF 44–45；S03 III §10，47 頁；詳細動作限制在第 08 頁 |
| C08.1 | 主頁／補充／圖：球衣、替換、人數、次數與完成回合 | [自由球員](../wiki/topics/libero.md)：辨認與替換 | S01 7.3.1、19.1.3、19.2、19.3.1.1、19.3.2.1–19.3.2.4，印刷 24、42–43／PDF 26、44–45；同時一位 L、全隊六人，替換不限次非隨時可進出 |
| C08.2 | 主頁／補充／圖：發球、攔網、任何位置高球完成攻擊限制 | [自由球員](../wiki/topics/libero.md)：四限制與誤解；[觸球與犯規](../wiki/topics/ball-contacts-and-faults.md)：攻擊定義 | S01 19.3.1.2–19.3.1.3，印刷 42／PDF 44；13.1、13.3.5，印刷 33–34／PDF 35–36；整顆球高於網頂及完成攻擊不可刪 |
| C08.3 | 補充：自由球員前區高手手指傳球與隊友後續攻擊 | [自由球員](../wiki/topics/libero.md)：自製情境 | S01 19.3.1.4、13.3.6，印刷 43、34／PDF 45、36；條件是前區高手手指傳球＋隊友整球高於網頂完成攻擊，不是傳球動作本身即犯規 |
| C08.4 | 補充：自由球員可任隊長 | [自由球員](../wiki/topics/libero.md)：隊長、名單與版本 | S01 第 5 條，印刷 19／PDF 21；S02 舊敘述見印刷 145／PDF 149，不能覆蓋 S01 |
| C09.1 | 主頁／補充／圖：發球控制、接發方向高度及合法手法 | [發球與接發](../wiki/topics/serve-and-reception.md)：技術戰術、接發；[舉球與攻擊](../wiki/topics/setting-and-attack.md)：一傳連鎖 | S02 VI，印刷 85–89、107–110／PDF 89–93、111–114；IX，印刷 130–132／PDF 134–136；S01 9.2，印刷 28–29／PDF 30–31；低手非唯一合法接法 |
| C09.2 | 主頁／補充／圖：一傳品質提供選項線索，非確定預測 | [發球與接發](../wiki/topics/serve-and-reception.md)：自製觀賽練習 | S05 Choosing a Defense，L009–L014；S04 Game Understanding／better the ball，L014–L019；保留教練觀點，不標未有根據的成功率 |
| C09.3 | 補充：發球手法、八秒、端線與落地 | [發球與接發](../wiki/topics/serve-and-reception.md)：規則底線 | S01 12.4.1–12.4.4，印刷 32／PDF 34；擊球或跳發起跳時不得踩場內含端線／發球區外地面，擊球後可落場內 |
| C09.4 | 補充：接發責任區、縫隙及配置 | [發球與接發](../wiki/topics/serve-and-reception.md)：接發配置 | S03 IV Serve reception patterns，53 頁；人數與站位不是唯一強制陣形 |
| C10.1 | 主頁／補充／圖：舉球的高度方向時間、助跑及快高球節奏 | [舉球與攻擊](../wiki/topics/setting-and-attack.md)：舉球、三層觀察 | S02 Coaching Hints for Setting，印刷 82／PDF 86；Spiking，印刷 90–97／PDF 94–101；S03 Attack，54–57 頁；不設各攻擊共通的固定秒數 |
| C10.2 | 主頁／補充／圖：中間與側翼多點威脅 | [舉球與攻擊](../wiki/topics/setting-and-attack.md)：配合與觀賽提示；[系統頁](../wiki/topics/systems-and-transition.md)：戰術 | S02 IX，印刷 131–132／PDF 135–136；S03 Combination plays，56–57 頁；只是目的與可能性，不保證突破攔網 |
| C10.3 | 補充／圖：先到位、改善來球、溝通與不得持球 | [舉球與攻擊](../wiki/topics/setting-and-attack.md)：教練觀點、觸球規則 | S04 L006–L011、L014–L019；S01 9.2.2，印刷 28／PDF 30；作者建議不保證每球完美 |
| C11.1 | 主頁／補充／圖：後排高球跳起攻擊比較及完成攻擊 | [舉球與攻擊](../wiki/topics/setting-and-attack.md)：後排攻擊；[觸球頁](../wiki/topics/ball-contacts-and-faults.md)：攻擊定義 | S01 13.1.3、13.2.2–13.2.3、13.3.3，印刷 33–34／PDF 35–36；圖 8／PDF 72；身分、起跳腳、整球高於網頂、完成動作全部保留；合法起跳可落前區 |
| C11.2 | 補充：後排在前區處理較低的球，舉球員身分不變 | [舉球與攻擊](../wiki/topics/setting-and-attack.md)：後排攻擊；[既有 query](../wiki/queries/setter-front-row-status.md) | S01 7.4.4、13.2.3、13.3.3，印刷 25、34／PDF 27、36；不是一般觸球規則全部豁免 |
| C11.3 | 主頁／補充／圖：一般攻擊不必跳起；自由球員另論 | [觸球頁](../wiki/topics/ball-contacts-and-faults.md)：攻擊定義；[自由球員](../wiki/topics/libero.md)：限制 | S01 13.1、19.3.1.2，印刷 33、42／PDF 35、44；不能把線後起跳許可套到 L |
| C12.1 | 主頁／補充／圖：攔網與後排空間、縫隙配合 | [攔網與防守](../wiki/topics/blocking-and-defense.md)：攔網與後排接合 | S02 IX Defensive Game System，印刷 132–134／PDF 136–138；S05 In the Back，L017–L022；示意責任區非唯一陣形 |
| C12.2 | 主頁／補充／圖：攔網定義、身分限制與計次 | [攔網與防守](../wiki/topics/blocking-and-defense.md)：攔網規則 | S01 14.1.1、14.4–14.6、19.3.1.3，印刷 34–35、42／PDF 36–37、44；身體部分過網頂與觸點高度分開；不能攔發球 |
| C12.3 | 補充／圖：連續判讀、依人員調整與觀賽方法 | [攔網與防守](../wiki/topics/blocking-and-defense.md)：連續判讀、自製練習 | S05 Choosing a Defense L003–L016、In the Back L017–L022；S02 VI，印刷 98–106／PDF 102–110；不從未知分工推定失職 |
| C13.1 | 主頁／補充／圖：5–1 基本配置及同一舉球員跨輪次 | [攻擊系統](../wiki/topics/systems-and-transition.md)：先學 5–1 | S03 IV，51–53 頁；S01 7.3–7.4、19，印刷 24–25、42–43／PDF 26–27、44–45；自由球員替換仍適用，全隊六人 |
| C13.2 | 主頁／補充／圖：S 前排兩名／後排三名前排隊友 | [攻擊系統](../wiki/topics/systems-and-transition.md)：5–1 選項 | S03 IV，52–53 頁；S01 13.1–13.3，印刷 33–34／PDF 35–36；只是通常前排選項，不排除 S 或一般後排依法攻擊 |
| C13.3 | 補充：4–2／6–2 基本型態與選擇限制 | [攻擊系統](../wiki/topics/systems-and-transition.md)：系統比較、選擇 | S03 IV，50–53 頁；S02 VIII，印刷 125–127／PDF 129–131；S04 Game Understanding L014–L016；S05 L003–L008；換人變形須另外核對規程 |
| C14.1 | 主頁／補充／圖：救球後到位、組織與反擊 | [攻擊系統](../wiki/topics/systems-and-transition.md)：守起來後接上 | S02 IX，印刷 132–135／PDF 136–139；流程是教學示意，沒有固定唯一跑法 |
| C14.2 | 補充／圖：攻擊掩護與被攔回球 | [攻擊系統](../wiki/topics/systems-and-transition.md)：轉換與掩護 | S02 IX，印刷 132–135／PDF 136–139；能否救起仍看觸球及球路，不保證成功 |
| C14.3 | 補充：年輕球隊的較保守救球目標是教練建議 | [攔網與防守](../wiki/topics/blocking-and-defense.md)；[S05 來源頁](../wiki/sources/s05-defense-as-a-team.md)：情境限制 | S05 In the Back，L020–L022；保留年輕球隊適用情境，不規定所有球隊相同目標 |
| C15.1 | 主頁／補充／圖：S01 接發相對位置時點及身分 | [位置與輪轉](../wiki/topics/rotation-and-positions.md)：站位時點與移動 | S01 7.4、7.6–7.7，印刷 25–26／PDF 27–28；符合相對位置不是禁止所有移動；只比較接發方 |
| C15.2 | 主頁／補充／圖：VNL 2026 鳴笛與開始動作時點 | [版本頁](../wiki/topics/rule-versions-and-tests.md)：差異表；[S06 來源頁](../wiki/sources/s06-fivb-2026-rule-tests.md)：V01 | S06 發布 2026-02-27，Out of rotation error L006–L007；V01 §6.3(b)，印刷 16–17／PDF 17–18；不視為全球一律採用 |
| C15.3 | 補充：八次換人、延續解釋及 CEV 後續範圍 | [版本頁](../wiki/topics/rule-versions-and-tests.md)：差異與後續採用 | S06 L004–L009；V01 §6.3(a,c)，印刷 16–17／PDF 17–18；V02 No.4 §1，印刷 3／合併 PDF 66；測試、解釋及後續採用分項處理 |
| C16.1 | 主頁／補充／圖／停格答案：既有回合、B 三擊、A 攔網與三擊 | [觀賽回合](../wiki/topics/watching-a-rally.md)：自製教學回合步驟 1–7 | S01 6.1.3、9.1、12.4、13.2.1、14.4、19.3.1.1，印刷 22、28、32–35、42／PDF 24、30、34–37、44；S04 L008、L015–L016；S02 IX 印刷 132–135／PDF 136–139。假設動作合法，非實際比賽 |
| C16.2 | 主頁／補充／圖／停格答案：未碰 B 出界、得分與輪轉 | [觀賽回合](../wiki/topics/watching-a-rally.md)：步驟 8–9及檢查題 | S01 8.4.1、6.1.3、7.6.2，印刷 27、22、26／PDF 29、24、28；比分固定 A 20：B 20→A 20：B 21；B 原本接發 |
| C17.1 | Q1 題幹、選項、答案 B、圖及理由 | [觀賽回合](../wiki/topics/watching-a-rally.md)：第 4 個檢查題；[輪轉頁](../wiki/topics/rotation-and-positions.md)：何時輪轉 | S01 6.1.3、7.6.2，印刷 22、26／PDF 24、28；題目 B 已是發球方，連續得分不再輪轉 |
| C17.2 | Q2 題幹、選項、答案 A、圖及理由 | [後排舉球員 query](../wiki/queries/setter-front-row-status.md)：答案及條件表 | S01 7.4.4、13.2–13.3、14.6.2，印刷 25、33–35／PDF 27、35–37；已明示允許移動後，身分仍是後排 |
| C17.3 | Q3 題幹、選項、答案 B、圖及理由 | [觀賽回合](../wiki/topics/watching-a-rally.md)：第 1–2 個檢查題；[觸球頁](../wiki/topics/ball-contacts-and-faults.md) | S01 14.4.1–14.4.2、9.1，印刷 35、28／PDF 37、30；前排完成攔網且其他動作合法，同一攔網者可做第一擊 |
| C18.1 | 主頁／補充：六份來源用途、版本、作者及日期性質 | 六份來源頁的「來源與版本」；[版本頁](../wiki/topics/rule-versions-and-tests.md) | S01 v05；S02 PDF 3 ©2011；S03 年份未確認；S04／S05 原快照 metadata 與作者；S06 2026-02-27。網頁日期不冒稱文件版次 |
| C18.2 | 主頁／補充／圖：Wiki 導覽、六份 ingest 明列範圍 | [索引](../wiki/index.md)；[術語表](../wiki/glossary.md)；[issues](../wiki/issues.md)；[ingest 登錄](../reports/ingest-register.json) | 本專案成果與各來源的處理範圍；V01／V02 為補查，未多計篇數；追溯圖是專案結構，非外部研究主張 |

## 檢查狀態與後續

以上對照已按 [內容稿](content.md) 核對，並保留主張所需條件。實際檢查、修正與限制見 [內容檢查紀錄](../reports/checks/content-review-2026-11-22.md)。H2 尚待使用者確認；正式圖片及 HTML 的正確性，須在後續 G／V／J／K 節點實測。
