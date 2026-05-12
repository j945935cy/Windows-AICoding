# 匯出說明

本專案目前提供兩種書稿輸出方式。

## 方式一：合併版 Markdown

合併版書稿：

```text
BOOK.md
```

內容包含：

- 書名
- 第 1 章到第 18 章
- 附錄 A 到附錄 F

適合用途：

- 整本校稿
- 匯入 Markdown 編輯器
- 轉成 PDF、EPUB 或其他電子書格式

## 方式二：瀏覽器列印

打開：

```text
print.html
```

再依照說明進入章節或附錄頁，使用瀏覽器列印功能另存成 PDF。

適合用途：

- 單章校稿
- 單份附錄輸出
- 快速產生可閱讀 PDF

## 方式三：全書單頁 HTML

打開：

```text
book.html
```

再使用瀏覽器列印並另存成 PDF。

適合用途：

- 一次輸出整本書
- 快速預覽完整內容
- 檢查章節順序與附錄順序

## 重新產生 BOOK.md

如果章節或附錄內容有更新，可以重新合併：

```powershell
$chapterFiles = Get-ChildItem -Path chapters -Filter 'ch*.md' | Sort-Object Name
$appendixFiles = Get-ChildItem -Path appendices -Filter '*.md' | Sort-Object Name
```

再依序把內容合併到 `BOOK.md`。

## 注意事項

- `BOOK.md` 是由章節與附錄檔合併而來。
- `book.html` 是由章節與附錄檔產生的全書單頁版。
- 修改內容時，優先修改 `chapters/*.md` 或 `appendices/*.md`。
- 修改後再重新產生 `BOOK.md` 與 `book.html`，避免輸出版和來源檔不同步。
