# 完整 graph 的 PNG 匯出紀錄

2026-11-22 依使用者要求，將對話中的完整 graph 匯出為 PNG，放入 HW10，並更新 GitHub。這是圖表輸出與閱讀入口的更新，不是新增知識來源或重新計算 ingest 次數。

## 成果

- [PNG 圖片](../assets/workflow/hw10-graph.png)：2692 × 10186 像素，白底長圖，適合插入作業或放大閱讀，約 0.9 MiB。
- [SVG 向量圖](../assets/workflow/hw10-graph.svg)：可供後續縮放。
- [Mermaid 原始檔](../assets/workflow/hw10-graph.mmd)：24 個節點、41 條連線；保留對話原圖的節點文字、方向、條件與回圈，僅調整換行、間距與配色。
- 黃色標出 H1／H2 人工確認；橘色標出本次實作後新增的 J0。三階段是 Wiki 建立、教學簡報製作、保存證據與公開發布。

README 與繳交總覽已加入圖片入口；繳交總覽可展開查看完整圖片。長圖可直接下載，無須登入或啟用 Mermaid 外掛。

## 匯出與檢查

使用 Mermaid 12.3.0、Dagre 排版及已安裝的 Chrome，以 Microsoft JhengHei 字型、2 倍像素密度輸出。依 [Mermaid 官方用法](https://mermaid.js.org/config/usage.html) 使用 renderer；來源檔在本機處理，網站讀圖不依賴 Mermaid CDN。

[匯出檢查 JSON](checks/graph-export-2026-11-22.json) 記錄尺寸、雜湊、節點／連線數、文字邊界與視覺複查。已逐段查看整張 PNG，確認繁體中文、人工確認點、J0 與回圈標籤可讀。

首輪檢查器未去除 Mermaid 12 產生的節點前綴，誤判節點缺少，實際已繪出 24 個節點與 41 條連線；另有空白 SVG 標籤被算入邊界檢查。已修正檢查器再匯出；[首次檢查紀錄](checks/graph-export-initial-2026-11-22.json) 保留原因。這些是匯出工具檢查問題，不回填成原作業反思中的 HTML01–03。

為讓 Markdown 內的圖片在產生的閱讀網頁正確顯示，建置器同步處理圖片 src 的相對路徑；原始來源、排球內容與 18 頁簡報不變。

## 後續重新匯出

先修改 Mermaid 原始檔，再執行：

```text
npm install
npm run export:graph
npm run build
```

匯出需要可用的 Chrome／Edge 或 Playwright Chromium。輸出後仍應查看實際圖片，不把節點數或邊界檢查當作全部語意檢查。
