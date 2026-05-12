# 維護與擴充規範

這份文件記錄本專案後續新增章節、範例、附錄與網站頁面時的命名與結構規則。

## 基本原則

- 只使用 HTML、CSS、JavaScript。
- 不新增前端框架、打包工具或後端服務。
- 檔案命名使用小寫英文、數字與連字號。
- 中文內容使用繁體中文。
- 每個範例必須可以直接用瀏覽器打開 `index.html`。

## 章節命名

章節 Markdown：

```text
chapters/ch01.md
chapters/ch02.md
...
chapters/ch18.md
```

章節閱讀頁：

```text
chapters/ch01.html
chapters/ch02.html
...
chapters/ch18.html
```

新增章節時，需同步更新：

- `chapters.html`
- `manuscript.html`
- `progress.js`
- `search.js`
- `README.md`

## 範例命名

範例資料夾格式：

```text
examples/ch章號-英文描述/
```

例如：

```text
examples/ch10-todo-app/
```

每個範例至少包含：

```text
index.html
style.css
```

如果有互動，加入：

```text
script.js
```

新增範例時，需同步更新：

- `examples.html`
- `progress.js`
- `search.js`
- `README.md`
- `RELEASE_CHECKLIST.md`

## 附錄命名

附錄 Markdown：

```text
appendices/a-prompts.md
appendices/b-html-cheatsheet.md
```

附錄 HTML：

```text
appendices/a-prompts.html
appendices/b-html-cheatsheet.html
```

新增附錄時，需同步更新：

- `appendices.html`
- `search.js`
- `README.md`
- `RELEASE_CHECKLIST.md`

## 章節內容格式

章節 Markdown 建議使用固定結構：

```text
# 第 N 章：章名

## 本章目標
## 你會做出什麼
## 核心觀念
## 實作步驟
## Codex Prompt 範例
## 常見錯誤
## 本章練習
## 檢查清單
```

專案章節需額外包含：

```text
## 專案檔案
## 實作順序
```

## HTML 頁面規則

所有主要頁面需包含：

- `<meta charset="utf-8">`
- `<meta name="viewport" content="width=device-width, initial-scale=1">`
- `style.css`
- `print.css`，如果是可閱讀內容頁
- 主要導覽列

章節與附錄閱讀頁需使用：

```html
<main class="book-page">
  <article class="book-content">
```

## CSS 規則

- 共用網站樣式放在 `style.css`
- 列印樣式放在 `print.css`
- 各範例自己的樣式放在範例資料夾內
- 卡片圓角維持 `8px`
- 避免厚重陰影
- 避免複雜框架式 class 命名

## JavaScript 規則

- 共用網站互動放在 `script.js`
- 單一頁面功能可獨立放在該頁專用 JS，例如 `progress.js`
- 範例互動放在範例資料夾內的 `script.js`
- 不使用 `eval()`
- 使用清楚函式名稱
- localStorage key 要有明確命名

## 發布前檢查

每次大幅修改後，至少檢查：

- 主頁是否可開啟
- 導覽列是否可用
- 所有本機連結是否存在
- 手機版是否可閱讀
- 章節、範例、附錄數量是否和 README 一致

可搭配 `RELEASE_CHECKLIST.md` 使用。
