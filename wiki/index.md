---
title: 看懂排球：從基本規則到場上戰術
status: verified
updated: 2026-11-22
---

# 看懂排球：從基本規則到場上戰術

這是一份以原始資料持續整理的 **LLM Wiki**，面向第一次想看懂室內六人排球的人。你可以依教學順序閱讀，也可以從問題跳到主題，再沿引用找到來源條號、頁碼與原始檔。

本批已完成 **S01–S06 共 6 份有效 ingest**，建立 12 個主題頁；已達成作業「至少 5 份」的資料入庫要求。**來源的實際完成狀態**見下表、[ingest 登錄](../reports/ingest-register.json) 與 [操作紀錄](log.md)；長手冊的處理範圍有明列，沒有宣稱全部精讀。

## 建議閱讀順序

| 順序 | 主題 | 讀完能回答什麼？ | 狀態 |
| --- | --- | --- | --- |
| 1 | [排球全貌](topics/volleyball-overview.md) | 一個回合在做什麼？ | verified |
| 2 | [場地與計分](topics/court-and-scoring.md) | 怎麼得分、贏局、贏比賽？ | verified |
| 3 | [位置與輪轉](topics/rotation-and-positions.md) | 何時輪轉，為什麼能換位？ | verified |
| 4 | [球員角色](topics/player-roles.md) | 舉球、主攻、攔中、接應如何分工？ | verified |
| 5 | [自由球員](topics/libero.md) | 不同球衣代表哪些權利與限制？ | verified |
| 6 | [觸球與常見犯規](topics/ball-contacts-and-faults.md) | 三次擊球、碰網和後排限制怎麼看？ | verified |
| 7 | [發球與接發](topics/serve-and-reception.md) | 第一球如何影響攻擊？ | verified |
| 8 | [舉球與攻擊](topics/setting-and-attack.md) | 如何把來球變成出手機會？ | verified |
| 9 | [攔網與防守](topics/blocking-and-defense.md) | 網前與後排如何合作？ | verified |
| 10 | [攻擊系統與攻防轉換](topics/systems-and-transition.md) | 5–1、4–2、6–2 如何分工？ | verified |
| 11 | [看懂一個回合](topics/watching-a-rally.md) | 能否把規則與分工連起來？ | verified |
| 12 | [規則版本與賽事差異](topics/rule-versions-and-tests.md) | 規則書與某場比賽為何看起來不同？ | verified |

## 六份來源

| ID | 來源頁 | 在 Wiki 中的用途 | 狀態 |
| --- | --- | --- | --- |
| S01 | [FIVB 官方規則 2025–2028](sources/s01-fivb-rules-2025-2028.md) | 規則基準及條件核對 | ingested |
| S02 | [FIVB Coaches Manual Level I](sources/s02-fivb-coaches-level-i.md) | 基礎技術、陣形與團隊配合 | ingested |
| S03 | [FIVB Coaches Manual Level II](sources/s03-fivb-coaches-level-ii.md) | 角色、系統、戰術與圖解比較 | ingested |
| S04 | [Recipe for a Setter](sources/s04-recipe-for-a-setter.md) | 舉球員的能力與攻擊組織 | ingested |
| S05 | [Defense is More Than Just Another Team System](sources/s05-defense-as-a-team.md) | 防守判讀與攔防配合 | ingested |
| S06 | [FIVB 2026 測試公告](sources/s06-fivb-2026-rule-tests.md) | 測試、解釋及賽事適用範圍 | ingested |

V01、V02 與官方目錄快照只作補充核對，不額外湊來源篇數。同一手冊的不同章節、同文章的兩個網址仍各算一份。

## 查詢與維護

- [已執行的跨頁查詢：後排舉球員跑到網前，就變成前排嗎？](queries/setter-front-row-status.md)
- [術語表](glossary.md)：中英名稱、台灣常見別稱與概念連結。
- [問題清單](issues.md)：未知出版年、賽事措辭差異、未涵蓋範圍及已解決問題。
- [操作紀錄](log.md)：依時間追加 ingest、query、lint 與流程變更。
- [流程與回圈](../reports/workflow.md)：哪些檢查已執行、失敗後退回哪一步。
- [本輪實際檢查](../reports/checks/ingest-2026-11-22.md)：結構檢查、內容核對與修正證據。

使用 AI 查詢時，先讀本索引，再讀相關主題，回查來源頁；遇到缺口先查原文，未確認內容放進 issues。不要跳過 Wiki 直接以模型記憶新增確定性敘述。

## 閱讀界線

正式規則、賽事測試、技戰術解說、教練觀點與自製情境已分開標示。`verified` 指本輪列明範圍已檢查，並不保證永遠無須更新。HTML 簡報與 Wiki 瀏覽網站屬後續工作；目前主要成果是可追溯的 Markdown 知識庫。[專案入口](../README.md)
