import os
import re

replacements = {
    '01': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：一次要求 AI 做太多事**\n    ✅ **解法**：請將需求拆解成小塊，例如先要求「只要 HTML 結構」。\n*   ❌ **錯誤：沒有限制使用的技術**\n    ✅ **解法**：在 Prompt 中明確加上：「請只使用純 HTML、CSS 和 Vanilla JavaScript」。\n*   ❌ **錯誤：沒有說明輸出格式**\n    ✅ **解法**：明確告訴 AI「只輸出程式碼，不要解釋」或「請逐行加上註解」。\n*   ❌ **錯誤：沒有測試就繼續加功能**\n    ✅ **解法**：每次 AI 給出程式碼，務必存檔測試，確認沒問題才繼續。\n*   ❌ **錯誤：看不懂程式碼也直接複製貼上**\n    ✅ **解法**：請馬上問 AI：「請用初學者的角度解釋這段在做什麼？」。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：一次要求 AI 做太多事</strong><br>✅ <strong>解法</strong>：請將需求拆解成小塊，例如先要求「只要 HTML 結構」。</li>\n  <li>❌ <strong>錯誤：沒有限制使用的技術</strong><br>✅ <strong>解法</strong>：在 Prompt 中明確加上：「請只使用純 HTML、CSS 和 Vanilla JavaScript」。</li>\n  <li>❌ <strong>錯誤：沒有說明輸出格式</strong><br>✅ <strong>解法</strong>：明確告訴 AI「只輸出程式碼，不要解釋」或「請逐行加上註解」。</li>\n  <li>❌ <strong>錯誤：沒有測試就繼續加功能</strong><br>✅ <strong>解法</strong>：每次 AI 給出程式碼，務必存檔測試，確認沒問題才繼續。</li>\n  <li>❌ <strong>錯誤：看不懂程式碼也直接複製貼上</strong><br>✅ <strong>解法</strong>：請馬上問 AI：「請用初學者的角度解釋這段在做什麼？」。</li>\n</ul>\n'
    },
    '02': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：CSS 檔名和 HTML 連結不一致**\n    ✅ **解法**：確保 `<link href="style.css">` 中的檔名與資料夾內完全一致（注意大小寫）。\n*   ❌ **錯誤：JS 沒有用 `<script>` 載入**\n    ✅ **解法**：確保在 `</body>` 結束前加上 `<script src="script.js"></script>`。\n*   ❌ **錯誤：修改後忘記儲存**\n    ✅ **解法**：VS Code 頁籤上有圓點代表未存檔，請養成隨手按 `Ctrl + S` 的習慣。\n*   ❌ **錯誤：瀏覽器沒有重新整理**\n    ✅ **解法**：存檔後記得切換回瀏覽器按下 `F5` 才能看到最新畫面。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：CSS 檔名和 HTML 連結不一致</strong><br>✅ <strong>解法</strong>：確保 <code>&lt;link href="style.css"&gt;</code> 中的檔名與資料夾內完全一致。</li>\n  <li>❌ <strong>錯誤：JS 沒有用 &lt;script&gt; 載入</strong><br>✅ <strong>解法</strong>：確保在 <code>&lt;/body&gt;</code> 結束前加上 <code>&lt;script src="script.js"&gt;&lt;/script&gt;</code>。</li>\n  <li>❌ <strong>錯誤：修改後忘記儲存</strong><br>✅ <strong>解法</strong>：VS Code 頁籤上有圓點代表未存檔，請養成隨手按 <code>Ctrl + S</code> 的習慣。</li>\n  <li>❌ <strong>錯誤：瀏覽器沒有重新整理</strong><br>✅ <strong>解法</strong>：存檔後記得切換回瀏覽器按下 <code>F5</code> 才能看到最新畫面。</li>\n</ul>\n'
    },
    '03': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：沒有說「只修改哪個檔案」**\n    ✅ **解法**：AI 可能會把 HTML 和 CSS 混在一起。一定要聲明：「請只給我 style.css 的修改內容」。\n*   ❌ **錯誤：同時要求新增功能、改版面、修 bug**\n    ✅ **解法**：遵守「一次一事」原則。先修 bug，確認會動後，再開新的 Prompt 要求改版面。\n*   ❌ **錯誤：不看錯誤訊息，只說「不能用」**\n    ✅ **解法**：把 Console 紅色錯誤訊息複製下來餵給 AI，比單純說「壞了」更有效率。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：沒有說「只修改哪個檔案」</strong><br>✅ <strong>解法</strong>：一定要聲明：「請只給我 style.css 的修改內容」。</li>\n  <li>❌ <strong>錯誤：同時要求多種任務</strong><br>✅ <strong>解法</strong>：遵守「一次一事」原則。先修 bug，確認會動後，再要求改版面。</li>\n  <li>❌ <strong>錯誤：不看錯誤訊息，只說「不能用」</strong><br>✅ <strong>解法</strong>：把 Console 錯誤訊息複製下來餵給 AI，比單純說「壞了」更有效。</li>\n</ul>\n'
    },
    '04': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：用太多沒有意義的 `<div\>`**\n    ✅ **解法**：這被稱為「div 湯」。盡量使用具備語意的標籤如 `<header>`, `<main>`, `<article>`, `<footer>` 來取代。\n*   ❌ **錯誤：為了字變大而亂用標題層級**\n    ✅ **解法**：`<h1>` 到 `<h6>` 代表文章結構。如果要讓字變大，請使用 CSS `font-size`。\n*   ❌ **錯誤：忘記替連結加上 `href`**\n    ✅ **解法**：沒有 `href` 屬性的 `<a>` 無法點擊。請確保寫成 `<a href="...">`。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：用太多沒有意義的 &lt;div&gt;</strong><br>✅ <strong>解法</strong>：盡量使用具備語意的標籤如 <code>&lt;header&gt;</code>, <code>&lt;main&gt;</code> 來取代。</li>\n  <li>❌ <strong>錯誤：為了字變大而亂用標題層級</strong><br>✅ <strong>解法</strong>：如果要讓字變大，請使用 CSS <code>font-size</code>。</li>\n  <li>❌ <strong>錯誤：忘記替連結加上 href</strong><br>✅ <strong>解法</strong>：沒有 <code>href</code> 屬性的連結無法點擊。確保寫成 <code>&lt;a href="..."&gt;</code>。</li>\n</ul>\n'
    },
    '05': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：所有元素都直接指定固定寬度**\n    ✅ **解法**：使用 `max-width: 100%` 可以讓元素在手機螢幕上自動縮小，避免破版。\n*   ❌ **錯誤：忘記處理手機版**\n    ✅ **解法**：撰寫 CSS 時要養成習慣，記得加入 `@media (max-width: 768px)` 來處理手機排版。\n*   ❌ **錯誤：圓角與陰影太重**\n    ✅ **解法**：陰影用極淡透明黑 (`rgba(0,0,0,0.1)`)、圓角不要超過 `16px`，畫面會更有質感。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：所有元素都直接指定固定寬度</strong><br>✅ <strong>解法</strong>：使用 <code>max-width: 100%</code> 讓元素自動適應手機螢幕。</li>\n  <li>❌ <strong>錯誤：忘記處理手機版</strong><br>✅ <strong>解法</strong>：記得加入 <code>@media (max-width: 768px)</code> 來處理手機排版。</li>\n  <li>❌ <strong>錯誤：圓角與陰影太重</strong><br>✅ <strong>解法</strong>：陰影用極淡的 <code>rgba(0,0,0,0.1)</code>，圓角適度即可。</li>\n</ul>\n'
    },
    '06': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：JS 執行時 HTML 元素還不存在**\n    ✅ **解法**：確保 `<script>` 放在 `</body>` 前面，這樣 JS 執行時畫面標籤都已經準備好了。\n*   ❌ **錯誤：`id` 名稱和 `querySelector` 不一致**\n    ✅ **解法**：如果在 HTML 中是 `<button id="myBtn">`，JS 裡面一定要用 `querySelector("#myBtn")`，注意那個 `#` 字號。\n*   ❌ **錯誤：忘記把數字更新回畫面**\n    ✅ **解法**：變數加一不代表畫面會動。記得加上 `element.textContent = 變數` 才能更新畫面。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：JS 執行時 HTML 元素還不存在</strong><br>✅ <strong>解法</strong>：確保 <code>&lt;script&gt;</code> 放在 <code>&lt;/body&gt;</code> 前面。</li>\n  <li>❌ <strong>錯誤：id 名稱和 querySelector 不一致</strong><br>✅ <strong>解法</strong>：若 HTML 是 <code>id="btn"</code>，JS 裡一定要用 <code>querySelector("#btn")</code>。</li>\n  <li>❌ <strong>錯誤：忘記把數字更新回畫面</strong><br>✅ <strong>解法</strong>：記得加上 <code>element.textContent = 變數</code> 才能真正改變畫面。</li>\n</ul>\n'
    },
    '07': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：沒有阻止空白內容加入清單**\n    ✅ **解法**：在 JS 中加上 `if (input.value.trim() === "") return;` 就能提前擋下空白輸入。\n*   ❌ **錯誤：每次新增都覆蓋掉舊內容**\n    ✅ **解法**：不要使用 `innerHTML =`，應該使用 `innerHTML +=` 或 `insertAdjacentHTML` 來附加內容。\n*   ❌ **錯誤：按鈕沒有設定事件監聽**\n    ✅ **解法**：檢查是否有正確綁定 `addEventListener("click", function)`。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：沒有阻止空白內容加入清單</strong><br>✅ <strong>解法</strong>：加上 <code>if (input.value.trim() === "") return;</code> 攔截空白。</li>\n  <li>❌ <strong>錯誤：每次新增都覆蓋掉舊內容</strong><br>✅ <strong>解法</strong>：使用 <code>innerHTML +=</code> 而非單純等號，才能附加新內容。</li>\n  <li>❌ <strong>錯誤：按鈕沒有設定事件監聽</strong><br>✅ <strong>解法</strong>：檢查是否有正確綁定 <code>addEventListener("click", ...)</code>。</li>\n</ul>\n'
    },
    '08': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：還沒規劃就要求直接寫完整專案**\n    ✅ **解法**：先要求 AI 提供「開發架構與步驟清單」，你確認過後再一步步請它產出程式碼。\n*   ❌ **錯誤：沒有定義驗收標準**\n    ✅ **解法**：在 Prompt 中加上「成功標準：點擊 X 按鈕時，Y 區塊必須變成藍色」，避免結果含糊。\n*   ❌ **錯誤：一次要求太多互動功能**\n    ✅ **解法**：一次只做一個按鈕或一個區塊的邏輯，積少成多最穩當。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：還沒規劃就要求直接寫完整專案</strong><br>✅ <strong>解法</strong>：先要求 AI 提供「步驟清單」，確認後再一步步產出程式碼。</li>\n  <li>❌ <strong>錯誤：沒有定義驗收標準</strong><br>✅ <strong>解法</strong>：加上「成功標準：點擊 X 時，Y 必須變成藍色」的明確定義。</li>\n  <li>❌ <strong>錯誤：一次要求太多互動功能</strong><br>✅ <strong>解法</strong>：一次只做一個按鈕邏輯，積少成多最穩當。</li>\n</ul>\n'
    },
    '09': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：一開始就要求同時完成 HTML/CSS/JS**\n    ✅ **解法**：拆成三個 Prompt，第一步只要 HTML，第二步要 CSS，最後再處理邏輯。\n*   ❌ **錯誤：Hero 標題太抽象**\n    ✅ **解法**：首頁大標語應該一秒鐘告訴別人「你是誰、能做什麼」，避免空泛詞彙。\n*   ❌ **錯誤：手機版導覽列無法使用**\n    ✅ **解法**：請確保向 AI 特別要求：「請確保導覽列在手機版時有漢堡選單可以點擊展開」。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：一開始就要求同時完成 HTML/CSS/JS</strong><br>✅ <strong>解法</strong>：拆成三步驟：第一步要 HTML，第二步要 CSS，最後要 JS。</li>\n  <li>❌ <strong>錯誤：Hero 標題太抽象</strong><br>✅ <strong>解法</strong>：大標語應該一秒鐘告訴別人「你是誰、能做什麼」。</li>\n  <li>❌ <strong>錯誤：手機版導覽列無法使用</strong><br>✅ <strong>解法</strong>：明確向 AI 要求「在手機版時需有漢堡選單可展開」。</li>\n</ul>\n'
    },
    '10': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：改了資料，忘記重新渲染畫面**\n    ✅ **解法**：在 JS 中寫好一個 `renderList()` 函數，每次陣列資料有變動，最後一定要呼叫它。\n*   ❌ **錯誤：儲存到 `localStorage` 前沒有轉成字串**\n    ✅ **解法**：必須使用 `JSON.stringify(陣列)` 轉成文字格式才能存入 LocalStorage。\n*   ❌ **錯誤：每個項目沒有唯一 `id`**\n    ✅ **解法**：待辦事項請加上 `id: Date.now()` 這種時間戳記，這樣在刪除或打勾時才不會搞混。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：改了資料，忘記重新渲染畫面</strong><br>✅ <strong>解法</strong>：每次陣列有變動，最後一定要呼叫 <code>renderList()</code> 更新畫面。</li>\n  <li>❌ <strong>錯誤：儲存前沒有轉成 JSON 字串</strong><br>✅ <strong>解法</strong>：必須使用 <code>JSON.stringify()</code> 轉成文字格式才能存入 LocalStorage。</li>\n  <li>❌ <strong>錯誤：每個項目沒有唯一 id</strong><br>✅ <strong>解法</strong>：新增項目時加上時間戳記 <code>id</code>，刪除時才不會誤刪。</li>\n</ul>\n'
    },
    '11': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：連續輸入多個小數點**\n    ✅ **解法**：輸入前加上判斷式 `if (currentText.includes(".")) return;`。\n*   ❌ **錯誤：按完等號後再輸入數字沒有重置**\n    ✅ **解法**：設定一個 `isEvaluated` 布林變數，若為 true 則在下一次輸入時清空舊數字。\n*   ❌ **錯誤：用 `eval()` 逃避狀態邏輯**\n    ✅ **解法**：這容易產生安全風險且不易除錯，請乖乖用變數紀錄前後數字與運算子來運算。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：連續輸入多個小數點</strong><br>✅ <strong>解法</strong>：輸入前判斷 <code>if (currentText.includes(".")) return;</code>。</li>\n  <li>❌ <strong>錯誤：按完等號後輸入數字沒有重置</strong><br>✅ <strong>解法</strong>：利用布林變數判斷，若是等號後第一次輸入就清空畫面。</li>\n  <li>❌ <strong>錯誤：用 eval() 逃避邏輯</strong><br>✅ <strong>解法</strong>：這有安全風險，請用變數老老實實記錄前後數字來運算。</li>\n</ul>\n'
    },
    '12': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：分類按鈕的值和卡片 `data-category` 不一致**\n    ✅ **解法**：檢查 HTML 中的拼字，確保 `data-category="nature"` 對應的也是 `nature`。\n*   ❌ **錯誤：modal 開啟後沒有提供關閉方式**\n    ✅ **解法**：燈箱效果必須提供「點擊叉叉按鈕」與「點擊黑色背景」也能關閉的事件監聽。\n*   ❌ **錯誤：手機版圖片太小或排列擠在一起**\n    ✅ **解法**：使用 CSS Grid 排版時，設定 `grid-template-columns: 1fr` 讓手機版維持單欄顯示。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：按鈕值和資料屬性不一致</strong><br>✅ <strong>解法</strong>：檢查 HTML 中的拼字，確保 <code>data-category</code> 值能對應上。</li>\n  <li>❌ <strong>錯誤：modal 開啟後無法關閉</strong><br>✅ <strong>解法</strong>：燈箱必須提供點擊 X 按鈕或點擊背景關閉的功能。</li>\n  <li>❌ <strong>錯誤：手機版圖片太小**</strong><br>✅ <strong>解法</strong>：使用 CSS Grid，手機版設定為 <code>1fr</code> 單欄顯示。</li>\n</ul>\n'
    },
    '13': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：進度條只改文字，沒有改寬度**\n    ✅ **解法**：在 JS 中不只要改 `textContent`，還要用 `style.width = X + "%"` 來動態調整視覺進度條。\n*   ❌ **錯誤：完成狀態存在畫面上，沒存在資料中**\n    ✅ **解法**：畫面打勾時，陣列物件裡的 `isCompleted` 也要改成 true 並存入 localStorage。\n*   ❌ **錯誤：課程資料和畫面內容重複寫兩份**\n    ✅ **解法**：HTML 裡不需要預設寫死內容，應該在網頁載入時用 JS 動態生成。這樣修改資料才方便。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：進度條只改文字，沒有改寬度</strong><br>✅ <strong>解法</strong>：在 JS 中使用 <code>style.width = X + "%"</code> 來動態調整。</li>\n  <li>❌ <strong>錯誤：狀態沒有存入 localStorage</strong><br>✅ <strong>解法</strong>：畫面打勾時，陣列中的狀態也要更新並同步儲存。</li>\n  <li>❌ <strong>錯誤：資料重複寫死在 HTML 中</strong><br>✅ <strong>解法</strong>：HTML 保持乾淨，讓 JS 在網頁載入時動態生成課程資料。</li>\n</ul>\n'
    },
    '14': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：還沒看懂檔案分工就開始改**\n    ✅ **解法**：修改前一定要先找出這顆按鈕是 HTML 哪一行、綁定了哪個 JS function。\n*   ❌ **錯誤：一次要求 AI 大幅重構**\n    ✅ **解法**：千萬不要跟 AI 說「幫我把整個專案重構成模組化」。這樣通常會壞成一片。\n*   ❌ **錯誤：不保存可運作版本**\n    ✅ **解法**：這是災難。請永遠在讓 AI 修改前複製一份你的專案資料夾。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：還沒看懂就開始改</strong><br>✅ <strong>解法</strong>：修改前要先看懂對應的 HTML 標籤在哪、綁定了哪個 JS 功能。</li>\n  <li>❌ <strong>錯誤：一次要求大幅重構</strong><br>✅ <strong>解法</strong>：不要要求 AI 將全站改版，請一小塊一小塊逐步替換。</li>\n  <li>❌ <strong>錯誤：不保存可運作版本</strong><br>✅ <strong>解法</strong>：讓 AI 修改前，請務必複製一份資料夾當作本地備份。</li>\n</ul>\n'
    },
    '15': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：程式碼沒貼全**\n    ✅ **解法**：遇到錯誤要發問時，確保同時貼上 HTML 元素與對應的 JS 邏輯給 AI 看。\n*   ❌ **錯誤：看不懂錯誤訊息就重開機**\n    ✅ **解法**：學會閱讀紅色錯誤訊息（如 `Cannot read property of null` 表示元素沒抓到）。\n*   ❌ **錯誤：AI 一給新解法就全盤覆蓋**\n    ✅ **解法**：AI 也會猜錯。覆蓋前先用註解隱藏舊程式碼，萬一 AI 給的方法沒用，你還能還原舊版繼續找原因。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：程式碼沒貼全</strong><br>✅ <strong>解法</strong>：發問時確保貼上 HTML 元素與對應的 JS 邏輯給 AI 參考。</li>\n  <li>❌ <strong>錯誤：看不懂錯誤訊息就放棄</strong><br>✅ <strong>解法</strong>：學會認出關鍵字，例如 <code>null</code> 通常代表元素沒抓到。</li>\n  <li>❌ <strong>錯誤：一拿到解法就全盤覆蓋</strong><br>✅ <strong>解法</strong>：先用註解隱藏舊程式碼再測試新版，萬一新版無效還能還原。</li>\n</ul>\n'
    },
    '16': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：還沒測試就連續加功能**\n    ✅ **解法**：加了「清除全部」確認會動之後，才能繼續加「編輯功能」，切忌貪心。\n*   ❌ **錯誤：一次要求改太多檔案**\n    ✅ **解法**：加功能時，在 Prompt 明確指出：「這段 CSS 不用動，請只更新 JS」。\n*   ❌ **錯誤：出錯後直接要求重寫**\n    ✅ **解法**：遇到 bug 不要意氣用事要 AI 重寫。冷靜使用前面教過的「除錯 Prompt」把它修好才是真本領。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：還沒測試就連續加功能</strong><br>✅ <strong>解法</strong>：確認當前新功能能跑後，才能繼續要求下一個新功能。</li>\n  <li>❌ <strong>錯誤：一次要求改太多檔案</strong><br>✅ <strong>解法</strong>：在 Prompt 明確限制範圍，例如「請只修改 JS 邏輯」。</li>\n  <li>❌ <strong>錯誤：出錯後直接要求重寫</strong><br>✅ <strong>解法</strong>：不要急著重寫，冷靜把錯誤訊息貼給 AI 修復才是最佳解。</li>\n</ul>\n'
    },
    '17': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：作品只有標題，沒有說明學到什麼**\n    ✅ **解法**：面試官最看重的是「解決問題的能力」。加上一句「克服了 LocalStorage 的格式轉換難題」會大加分。\n*   ❌ **錯誤：卡片太多資訊，難以掃讀**\n    ✅ **解法**：作品集不是論文。多用條列式、留白與按鈕引導讀者視線。\n*   ❌ **錯誤：分類篩選後沒有更新 active 狀態**\n    ✅ **解法**：使用者點擊按鈕時，別忘了用 JS 替當前按鈕加上深色樣式表示「目前選擇這項」。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：作品沒有說明學到什麼</strong><br>✅ <strong>解法</strong>：在專案簡介加上「學會了 LocalStorage」或「克服了排版困難」會大加分。</li>\n  <li>❌ <strong>錯誤：卡片太多資訊難以閱讀</strong><br>✅ <strong>解法</strong>：減少文字，多用條列式、適度留白與按鈕來排版。</li>\n  <li>❌ <strong>錯誤：篩選後沒有更新 active 狀態</strong><br>✅ <strong>解法</strong>：點擊分類時，記得用 JS 給當前按鈕加上「選取中」的明顯樣式。</li>\n</ul>\n'
    },
    '18': {
        'md': '## 常見錯誤\n\n*   ❌ **錯誤：還沒熟悉基礎就急著學框架**\n    ✅ **解法**：React/Vue 很強大，但沒有扎實的 JS 基礎與 AI 協作經驗，你會在框架裡迷失。\n*   ❌ **錯誤：學了很多工具但沒有作品**\n    ✅ **解法**：工具永遠學不完。最重要的是「用 AI 做出了什麼可以展示的東西」。\n*   ❌ **錯誤：每次都開新專案，沒有深化舊作品**\n    ✅ **解法**：把一個陽春待辦清單，慢慢擴充成有日曆、雲端登入的專業專案，這遠比做 100 個半成品有意義。\n',
        'html': '<h2>常見錯誤</h2>\n<ul>\n  <li>❌ <strong>錯誤：基礎不穩就急著學框架</strong><br>✅ <strong>解法</strong>：沒有扎實的 JS 基礎與 AI 協作經驗，去學 React 會非常挫折。</li>\n  <li>❌ <strong>錯誤：學了一堆工具卻沒有產出</strong><br>✅ <strong>解法</strong>：工具永遠學不完。最重要的是你實際上線了什麼專案。</li>\n  <li>❌ <strong>錯誤：不斷開新專案而不深化</strong><br>✅ <strong>解法</strong>：把待辦清單優化到完美，比做 10 個半成品的學習效益更高。</li>\n</ul>\n'
    }
}

for ch_num, texts in replacements.items():
    md_path = f'chapters/ch{ch_num}.md'
    html_path = f'chapters/ch{ch_num}.html'
    
    # Process MD
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '## 常見錯誤' in content:
            # We want to replace everything from ## 常見錯誤 up to the next ##
            parts = content.split('## 常見錯誤')
            head = parts[0]
            tail = '## ' + parts[1].split('## ', 1)[1] if '## ' in parts[1] else ''
            
            new_content = head + texts['md'] + '\n' + tail
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {md_path}")

    # Process HTML
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '<h2>常見錯誤</h2>' in content:
            # Replace the <h2>...</h2> and the <ul>...</ul> following it
            import re
            pattern = re.compile(r'<h2>常見錯誤</h2>.*?</ul>', re.DOTALL)
            new_content = pattern.sub(texts['html'].strip(), content)
            
            # If there was no <ul> (ch15 had something weird)
            if new_content == content and '<h2>常見錯誤</h2>' in content:
                pattern2 = re.compile(r'<h2>常見錯誤</h2>.*?(?=<h2>|$)', re.DOTALL)
                new_content = pattern2.sub(texts['html'].strip() + '\n      ', content)

            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {html_path}")

# Process BOOK.md
if os.path.exists('BOOK.md'):
    with open('BOOK.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Iterate chapters in BOOK.md to replace the right section
    for ch_num, texts in replacements.items():
        ch_pattern = re.compile(f'# 第 {int(ch_num)} 章：.*?(?=# 第 \d+ 章：|$)', re.DOTALL)
        match = ch_pattern.search(content)
        if match:
            ch_content = match.group(0)
            if '## 常見錯誤' in ch_content:
                parts = ch_content.split('## 常見錯誤')
                head = parts[0]
                tail_match = re.search(r'\n## ', parts[1])
                if tail_match:
                    tail = parts[1][tail_match.start():]
                else:
                    tail = ''
                
                new_ch_content = head + texts['md'].strip() + '\n' + tail
                content = content.replace(ch_content, new_ch_content)
    
    with open('BOOK.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated BOOK.md")
