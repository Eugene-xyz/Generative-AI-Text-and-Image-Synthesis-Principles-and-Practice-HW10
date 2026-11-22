# 看懂排球：從基本規則到場上戰術

HW10：用 LLM Wiki 建立知識庫，再製作讓初學者理解室內六人排球的教學 HTML 簡報。

**作業核心與公開網站已完成。** 老師或評閱者可先看 [線上繳交總覽](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/site/docs/SUBMISSION.html)，或 [Markdown 版](SUBMISSION.md)。本人仍需補上繳交標題的身分資訊並在課程平台提交。

## 成果入口

| 成果 | 開啟方式 |
| --- | --- |
| 18 頁教學簡報 | [公開簡報](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/slides/index.html)／[本機版](slides/index.html) |
| LLM Wiki | [公開 Wiki](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/site/index.html)／[本機版](site/index.html)／[Markdown 索引](wiki/index.md) |
| 簡報 → Wiki → 原始來源 | [網頁來源對照](site/slide-sources.html)／[54 組主張對照](slides/source-map.md) |
| loop／graph | [完整 PNG 流程圖](assets/workflow/hw10-graph.png)／[Wiki workflow](reports/workflow.md)／[簡報 graph v1.1](reports/slides-graph.md) |
| 實際執行與修正 | [Wiki log](wiki/log.md)／[HTML 檢查與截圖](reports/checks/html-review-2026-11-22.md) |
| 反思 | [節點問題、前移檢查及複查結果](reports/reflection.md) |

本專案已啟用 GitHub Pages，從 main 分支根目錄發布，使用 HTTPS。公開簡報與 Wiki 已實際開啟，翻頁、鍵盤、補充、測驗及來源連結通過檢查；[發布紀錄](reports/deployment.md) 保留證據。[GitHub 儲存庫](https://github.com/Eugene-xyz/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10)／[後續維護方式](GITHUB.md)。

## 作業內容與證據

- **6 份有效 ingest**：S01–S06 均有原文、明列閱讀範圍、來源摘要與主題整合；超過至少 5 份要求。長手冊未宣稱全文精讀，補充規程未重複計篇數。[ingest 登錄](reports/ingest-register.json)
- **23 頁 Wiki**：12 個主題、6 個來源、4 個維護頁、1 個跨頁 query。Markdown 為知識維護主檔，網頁由其產生。
- **18 頁 HTML**：沿已確認的大綱與整份內容稿，預估主講 18:20；含 18 組自製 SVG／31 個狀態、分步回合與三題測驗。保留補充、講解提示與逐頁來源。[圖解素材紀錄](assets/credits.md)
- **先討論後生成**：來源提案、graph、大綱 H1、全文 H2 依序確認；沒有在大綱尚未核准時直接做最終簡報。
- **真實檢查紀錄**：Chrome 三種視窗實測，182 項完整檢查及修正後 19 項局部複查通過；保留失敗、修正及代表畫面。最後一次資料夾整理與網站路徑複查見 [整理紀錄](reports/repository-cleanup.md)。

高分項目已有對應證據，實際成績仍由教授判定。正式繳交前，填好「學校 學號 系級 姓名 主題」，將公開簡報、Wiki 與繳交總覽連結交到課程平台。試講時間與真實初學者理解測試尚未執行，可作為進一步改善。

## 使用方式

- 前後頁按鈕、←／→、Page Up／Page Down 翻頁；Home／End 到首頁／末頁；目錄可跳頁。
- 點「展開補充」自讀，點「講解提示」看講者備註；展開後可向下捲動。
- 點圖放大；圖下小箭頭只換圖解步驟。第 04、06、10、16 頁有多個狀態。
- 第 17 頁可選答案、顯示理由及回看。Tab、Enter／空白鍵支援控制項，Esc 關閉對話框。
- 本機核心圖文與導覽可離線使用；開啟官方來源網站需網路。搬移時請保留整個資料夾的相對位置。

## 資料夾結構

```text
HW10/
  README.md / SUBMISSION.md / GITHUB.md   成果、繳交與上傳入口
  AGENTS.md                             合作規範與確認節點
  index.html / .nojekyll                 靜態網站入口與 Pages 設定
  wiki/                                 23 頁知識主檔
  slides/                               核准大綱、內容、來源表、HTML
  assets/                               SVG、CSS、JS 與素材紀錄
  site/                                 從 Markdown 產生的閱讀網頁
  raw/                                  原始來源、文字與取得證據
  reports/                              graph、反思、閱讀／ingest 登錄
    checks/                             真實檢查結果與保留的代表截圖
  scripts/                              取得、建置與檢查工具
  package.json / requirements.txt       維護環境依賴
```

保留 raw 與歷史紀錄，是為了讓有效 ingest、來源定位與反思可查證。整理刪除了 62 個過渡截圖、快取與一次性工具，約 6.49 MiB；清單、雜湊與保留理由見 [cleanup manifest](reports/cleanup-manifest.json)。各歷史 JSON 中的截圖清單記錄當時產生的檔案，不代表整理後仍保留每張。

## 維護

一般瀏覽及 Pages 部署直接使用已生成檔案。修改知識或簡報時，先改 wiki、slides/content.md 或來源對照，再重建。

```text
npm install
npm run build
python -m pip install -r requirements.txt
npm run check:content
npm run check:wiki
npm run check:browser -- new-check-name
```

工具及瀏覽器安裝細節見 [GITHUB.md](GITHUB.md)。自動檢查只輔助結構、顯示與操作，不能代替排球規則和圖解語意核對。`verify_review.py` 是「正式入庫前」的歷史檢查工具，不應拿來判定目前成果。

S01–S06 原文著作權屬各來源機構／作者；本專案以自寫摘要與自製圖解教學，沒有替第三方原始資料宣告新授權。來源與適用範圍見各來源頁；尚待釐清事項保留在 [issues](wiki/issues.md)。
