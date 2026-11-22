# GitHub Pages 發布與公開驗證

記錄時間：2026-11-22 17:45 +08:00（Asia/Taipei）。使用者明確授權上傳 HW10 至已建立的 GitHub 專案，啟用 Pages，並提供可繳交的簡報和 Wiki 公開連結。

## 發布結果

- 儲存庫：[Eugene-xyz/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10](https://github.com/Eugene-xyz/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10)，公開。
- Pages：Deploy from a branch → main → /(root)，HTTPS 已啟用。
- [公開簡報](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/slides/index.html)、[公開 Wiki](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/site/index.html)、[六項繳交總覽](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/site/docs/SUBMISSION.html)。
- 保留原有 Initial commit `2d56abe`，接續提交 `3aee1313a8b6aacf0ff72b694ad132487d896abc`；首次上傳 244 個檔案，沒有多包一層 HW10。
- [首次部署工作](https://github.com/Eugene-xyz/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/actions/runs/45008733642) 於 17:41:38 +08:00 顯示 completed / success。Pages 設定畫面顯示實際公開網址。

## 實際檢查

| 檢查 | 結果與證據 |
| --- | --- |
| 無登入公開請求 | 17:45:04 +08:00，89 個檢查全通過；83 個 HTML／CSS／JS／SVG 的 HTTP 200 與 SHA-256 符合本機檔案，6 份原始來源的 HEAD 回應均為 200。[JSON](checks/pages-2026-11-22/initial-http.json) |
| 瀏覽器操作 | 根網址導向簡報；下一頁、右方向鍵、展開補充、目錄跳頁、圖解放大／關閉均成功。三題測驗 B、A、B 均顯示正確回饋與理由。[操作觀察](checks/pages-2026-11-22/browser-observations.json) |
| 來源追溯 | 點 C03.1 後新分頁開啟公開來源對照，列出對應 Wiki、S01 條號與頁碼；再進 Wiki 索引可看到 6 份 ingest 與主題清單。 |
| 版面 | 實際查看公開簡報首頁與 Wiki 首頁，圖文及導覽可讀；短視窗以捲動閱讀下方補充。保留 [簡報畫面](checks/pages-2026-11-22/slides-live.jpg)、[Wiki 畫面](checks/pages-2026-11-22/wiki-live.jpg)、[Pages 設定](checks/pages-2026-11-22/pages-settings.jpg)。 |

公開檔案驗證使用 [check_pages.cjs](../scripts/check_pages.cjs)，不帶帳號、Cookie 或權杖。GET 比對內容雜湊，HEAD 只確認原始檔可取得；沒有將 HEAD 說成全文驗證。這次是在公開網址抽查操作；原先的 18 頁／三種視窗完整檢查仍見 [HTML 實測](checks/html-review-2026-11-22.md)。

## 紀錄範圍與後續更新

這份紀錄記載首次公開版本的驗證。後續補上 README、SUBMISSION 與 GITHUB 的正式網址、此發布紀錄及檢查證據，重新產生文件閱讀網頁；核准教學內容、簡報程式、圖解及原始來源不改。歷史完成度審查保留當時「尚未部署」的判定，另加後續狀態，避免把新結果回填成先前已驗證。

上傳過程的 Git 空白檢查把保留的 CRLF 與原文空白列為提示；未修改原始快照來消除提示。改以保留換行設定及既有內容／連結／雜湊檢查確認可發布。

正式交作業仍由本人填寫「學校 學號 系級 姓名 主題」，並在課程平台提交；本次沒有代填未知身分或代交課程平台。
