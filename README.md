# AI Coding 入門

這個專案是《AI Coding 入門：用 Codex、VS Code、HTML、CSS、JavaScript 打造你的第一批網頁專案》的第一版網站與範例程式。

全專案只使用 HTML、CSS、JavaScript，不需要框架、建置工具、Node.js 或後端服務。

## 如何開啟

直接用瀏覽器打開：

```text
index.html
```

主要入口：

- `index.html`：書籍首頁
- `chapters.html`：18 章章節導覽
- `projects.html`：專案展示
- `examples.html`：16 個可執行範例總覽
- `appendices.html`：附錄速查資料
- `progress.html`：18 章學習進度追蹤
- `manuscript.html`：18 章 Markdown 與 HTML 書稿總覽
- `search.html`：章節、範例、附錄搜尋
- `print.html`：列印與 PDF 輸出說明
- `BOOK.md`：合併版完整書稿
- `book.html`：全書單頁 HTML，可用瀏覽器列印

## 內容結構

```text
chapters/
  ch01.md 到 ch18.md
  ch01.html 到 ch18.html

examples/
  ch02-first-page/
  ch04-html-structure/
  ch05-css-cards/
  ch06-js-interaction/
  ch07-prompt-notes/
  ch08-task-breakdown/
  ch09-personal-site/
  ch10-todo-app/
  ch11-calculator/
  ch12-gallery/
  ch13-learning-dashboard/
  ch14-code-reading/
  ch15-debug-workbench/
  ch16-workflow-builder/
  ch17-portfolio/
  ch18-next-roadmap/

appendices/
  a-prompts.md
  a-prompts.html
  b-html-cheatsheet.md
  b-html-cheatsheet.html
  c-css-cheatsheet.md
  c-css-cheatsheet.html
  d-js-cheatsheet.md
  d-js-cheatsheet.html
  e-common-errors.md
  e-common-errors.html
  f-glossary.md
  f-glossary.html
```

## 已完成範圍

- 18 章 Markdown 書稿
- 18 章 HTML 閱讀頁
- 16 個可執行範例
- 6 份附錄速查資料
- 首頁、章節頁、專案頁、範例總覽頁、附錄頁
- 學習進度頁與 localStorage 進度保存
- 書稿總覽頁，集中連結章節 Markdown 與閱讀頁
- 搜尋頁，可搜尋章節、範例與附錄
- 列印樣式：`print.css`
- 全書單頁 HTML：`book.html`
- 手機版導覽
- Prompt 複製、章節篩選、FAQ、回頂部等基本互動

## 設計方向

視覺風格採清爽、留白充足的科技教學網站方向，色調以白色、淡灰、淺藍、淺紫為主。

主要樣式集中在：

```text
style.css
```

主要共用互動集中在：

```text
script.js
```

各章範例有自己的 `index.html`、`style.css`、`script.js`，彼此獨立，方便讀者單獨打開與修改。

## 後續建議

1. 補強每章 HTML 閱讀頁內容，讓它接近完整書稿。
2. 替每個範例加上「起始版本」與「完成版本」。
3. 將 `chapters/*.md` 轉成正式電子書或教學文章。
4. 為作品集範例補上真實作品截圖與連結。
5. 部署到 GitHub Pages 或其他靜態網站服務。

## 發布檢查

發布與校稿工作可參考：

```text
RELEASE_CHECKLIST.md
```

## 匯出書稿

合併版 Markdown 與 PDF 輸出方式可參考：

```text
EXPORT.md
```

## 維護規範

後續新增章節、範例或附錄時，請參考：

```text
CONTRIBUTING.md
```

## 專案檢查

可用 PowerShell 執行完整性檢查：

```powershell
powershell -ExecutionPolicy Bypass -File tools/check-project.ps1
```

## 校稿計劃

第一版內容完成後的校稿與第二版改版，可參考：

```text
EDITORIAL_REVIEW.md
```
