# 附錄 E：初學者常見錯誤清單

## HTML

- CSS 檔名寫錯：`style.css` 寫成 `styles.css`
- JavaScript 沒有載入：忘記加 `<script src="script.js"></script>`
- `id` 和 JavaScript 選取名稱不一致
- 標籤沒有正確關閉
- 連結 `href` 寫錯

## CSS

- HTML class 是 `card`，CSS 寫成 `.cards`
- 忘記加 `box-sizing: border-box`
- 固定寬度導致手機版超出畫面
- 樣式被後面的規則覆蓋
- 使用太多顏色與陰影，畫面變亂

## JavaScript

- `querySelector` 找不到元素，回傳 `null`
- script 載入時機太早
- 變數拼字不一致
- 改了資料但沒有重新渲染畫面
- localStorage 讀寫時忘記 `JSON.stringify` 或 `JSON.parse`

## AI Coding

- 一次要求 Codex 做太多事
- 沒有限制技術範圍
- 沒有指定修改檔案
- 沒有提供錯誤訊息
- 看不懂程式碼就直接貼上

## 除錯檢查順序

1. 確認檔案有儲存
2. 重新整理瀏覽器
3. 打開 Console
4. 看錯誤訊息
5. 找到相關檔案
6. 做最小修改
7. 再次測試
