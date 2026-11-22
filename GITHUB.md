# 上傳 GitHub 與啟用簡報網址

這份資料夾已包含建置好的 HTML；瀏覽與 GitHub Pages 發布不需要先安裝 Node.js 或 Python。2026-11-22 已上傳至 [Eugene-xyz 的 HW10 儲存庫](https://github.com/Eugene-xyz/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10)，並從 main 分支的根目錄啟用 Pages。以下是後續維護說明，這些首次發布步驟已完成。

- [公開簡報](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/slides/index.html)
- [公開 Wiki](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/site/index.html)
- [六項繳交總覽](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/site/docs/SUBMISSION.html)
- [實際發布與驗證紀錄](reports/deployment.md)

## 1. 上傳完整資料夾內容

將 **HW10 裡面的檔案與子資料夾**放到儲存庫根目錄，使根目錄能直接看到 `index.html`、`README.md`、`.nojekyll`、`slides/`、`wiki/`、`site/`、`assets/`、`raw/`、`reports/` 和 `scripts/`。不要多包一層 HW10，也不要只上傳 `slides/index.html`。

可使用 GitHub Desktop 或 Git 一次提交整個目錄。若使用網頁拖放，GitHub 每次最多 100 個檔案、單檔上限 25 MiB；本專案檔數超過 100，需分批並保留路徑。目前最大原始 PDF 約 15.13 MiB，未超過單檔限制。[GitHub 官方上傳說明](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)

`.gitignore` 排除套件、快取與本機設定；`.gitattributes` 保留檔案原有位元組，避免換行自動轉換影響原始快照雜湊。這兩個設定檔及 `.nojekyll` 都應保留。此目錄沒有放入 node_modules 或完整執行環境。

## 2. 啟用 GitHub Pages

1. 開啟儲存庫的 **Settings → Pages**。
2. Source 選 **Deploy from a branch**。
3. 選實際存放檔案的分支（通常是 `main`），資料夾選 **/(root)**，儲存。
4. 等部署成功後，使用 Pages 畫面的 **Visit site** 取得實際網址。

根目錄已有 `index.html`，會導向簡報；`.nojekyll` 讓已生成的靜態內容直接發布。這符合 GitHub 的分支／根目錄發布方式。[發布來源設定](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)、[建立 Pages 網站](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

本專案的已驗證根網址為 [GitHub Pages 網站](https://eugene-xyz.github.io/Generative-AI-Text-and-Image-Synthesis-Principles-and-Practice-HW10/)，會導向簡報。Settings → Pages 顯示網站已上線，HTTPS 已啟用。

## 3. 部署後再核對並填入作業

從實際網站根網址進入下列路徑：

| 用途 | 相對路徑 |
| --- | --- |
| 18 頁簡報 | `slides/index.html` |
| Wiki | `site/index.html` |
| 來源對照 | `site/slide-sources.html` |
| 六項繳交總覽 | `site/docs/SUBMISSION.html` |
| 反思 | `site/docs/reports/reflection.html` |

這次已確認翻頁、展開補充、測驗、Wiki 及來源連結可用，並已更新 [SUBMISSION.md](SUBMISSION.md)。後續更新請仍做公開網址複查。本人繳交時補上學校、學號、系級、姓名；GitHub 的 `blob/.../index.html` 原始碼頁不能代替簡報網站網址。

## 需要修改與重新建置時

請先改 Wiki／內容主檔，再重建；不用直接手改生成的網頁。

```text
npm install
npm run build
python -m pip install -r requirements.txt
npm run check:content
npm run check:wiki
npm run check:browser -- my-check-name
```

建置使用 Node.js 24 或更新版本；Python 檢查以 3.12 執行。固定使用的套件版本列在 package.json 與 requirements.txt。原頁圖片重新渲染另需 Poppler 的 `pdftoppm`。

瀏覽器檢查會選已安裝的 Chrome／Edge；也可用 `HW10_BROWSER_EXECUTABLE` 指定瀏覽器路徑。若系統沒有可用瀏覽器，執行 `npx playwright install chromium` 後再檢查。新的測試請使用新名稱，避免覆寫歷史證據。
