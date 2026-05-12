import os

exp_data = {
    '02': {
        'target_md': '## 實作步驟',
        'target_html': '<h2>實作步驟</h2>',
        'md': '### 基礎程式碼 (Boilerplate)\n這三個檔案一開始不是空白的。你可以把這三段程式碼當作起手式，複製貼上到對應的檔案中：\n\n**1. `index.html`**\n負責告訴瀏覽器這是一個網頁，並載入 CSS 和 JS：\n```html\n<!DOCTYPE html>\n<html>\n<head>\n    <meta charset="UTF-8">\n    <title>我的第一個網頁</title>\n    <link rel="stylesheet" href="style.css">\n</head>\n<body>\n    <h1 id="title">歡迎來到 AI Coding</h1>\n    <button id="myBtn">點擊我</button>\n    <script src="script.js"></script>\n</body>\n</html>\n```\n\n**2. `style.css`**\n讓畫面不要太單調：\n```css\nbody { font-family: sans-serif; text-align: center; margin-top: 50px; }\nbutton { padding: 10px 20px; font-size: 16px; cursor: pointer; }\n```\n\n**3. `script.js`**\n負責按鈕點擊後的魔法：\n```javascript\n// 這裡目前是空的，等一下我們要寫互動邏輯\n```\n\n',
        'html': '<h3>基礎程式碼 (Boilerplate)</h3>\n<p>這三個檔案一開始不是空白的。你可以把這三段程式碼當作起手式，複製貼上到對應的檔案中：</p>\n<p><strong>1. <code>index.html</code></strong></p>\n<p>負責告訴瀏覽器這是一個網頁，並載入 CSS 和 JS：</p>\n<pre><code class="language-html">&lt;!DOCTYPE html&gt;\n&lt;html&gt;\n&lt;head&gt;\n    &lt;meta charset="UTF-8"&gt;\n    &lt;title&gt;我的第一個網頁&lt;/title&gt;\n    &lt;link rel="stylesheet" href="style.css"&gt;\n&lt;/head&gt;\n&lt;body&gt;\n    &lt;h1 id="title"&gt;歡迎來到 AI Coding&lt;/h1&gt;\n    &lt;button id="myBtn"&gt;點擊我&lt;/button&gt;\n    &lt;script src="script.js"&gt;&lt;/script&gt;\n&lt;/body&gt;\n&lt;/html&gt;</code></pre>\n<p><strong>2. <code>style.css</code></strong></p>\n<p>讓畫面不要太單調：</p>\n<pre><code class="language-css">body { font-family: sans-serif; text-align: center; margin-top: 50px; }\nbutton { padding: 10px 20px; font-size: 16px; cursor: pointer; }</code></pre>\n<p><strong>3. <code>script.js</code></strong></p>\n<p>負責按鈕點擊後的魔法：</p>\n<pre><code class="language-javascript">// 這裡目前是空的，等一下我們要寫互動邏輯</code></pre>\n'
    },
    '06': {
        'target_md': '## 常用語法',
        'target_html': '<h2>常用語法</h2>',
        'md': '### 認識開發者工具 (Developer Tools)\n在真正寫 JS 之前，你要先知道怎麼看到 JS 的錯誤訊息與輸出。\n請在瀏覽器（如 Chrome 或 Edge）按下 `F12` 鍵，或者在網頁上點擊右鍵選擇「檢查 (Inspect)」，然後切換到 **Console (主控台)** 標籤頁。\n\n你可以試著在這個 Console 輸入你人生的第一行 JS 程式碼並按下 Enter：\n```javascript\nconsole.log("Hello AI Coding!");\n```\n如果你看到它在下一行印出了 `Hello AI Coding!`，恭喜你，這就是 JS 跟瀏覽器溝通的橋樑！未來所有除錯、變數檢查，都會在這裡進行。\n\n',
        'html': '<h3>認識開發者工具 (Developer Tools)</h3>\n<p>在真正寫 JS 之前，你要先知道怎麼看到 JS 的錯誤訊息與輸出。<br>請在瀏覽器（如 Chrome 或 Edge）按下 <code>F12</code> 鍵，或者在網頁上點擊右鍵選擇「檢查 (Inspect)」，然後切換到 <strong>Console (主控台)</strong> 標籤頁。</p>\n<p>你可以試著在這個 Console 輸入你人生的第一行 JS 程式碼並按下 Enter：</p>\n<pre><code class="language-javascript">console.log("Hello AI Coding!");</code></pre>\n<p>如果你看到它在下一行印出了 <code>Hello AI Coding!</code>，恭喜你，這就是 JS 跟瀏覽器溝通的橋樑！未來所有除錯、變數檢查，都會在這裡進行。</p>\n'
    },
    '07': {
        'target_md': '## 實作步驟',
        'target_html': '<h2>實作步驟</h2>',
        'md': '### 實際的事件監聽器範例\n讓我們把前面的概念具象化。在 JS 中，監聽一個按鈕點擊的程式碼通常長這樣：\n```javascript\n// 1. 選取畫面上的元素 (假設按鈕的 id 是 submitBtn)\nconst btn = document.querySelector(\'#submitBtn\');\n\n// 2. 監聽點擊事件 (addEventListener)\nbtn.addEventListener(\'click\', function() {\n    // 3. 當點擊發生時，執行大括號裡面的邏輯\n    alert("按鈕被點擊了！");\n});\n```\n這段程式碼就是前端互動的靈魂。未來你請 AI 幫忙寫的互動邏輯，有八成都是建立在這個架構之上。\n\n',
        'html': '<h3>實際的事件監聽器範例</h3>\n<p>讓我們把前面的概念具象化。在 JS 中，監聽一個按鈕點擊的程式碼通常長這樣：</p>\n<pre><code class="language-javascript">// 1. 選取畫面上的元素 (假設按鈕的 id 是 submitBtn)\nconst btn = document.querySelector(\'#submitBtn\');\n\n// 2. 監聽點擊事件 (addEventListener)\nbtn.addEventListener(\'click\', function() {\n    // 3. 當點擊發生時，執行大括號裡面的邏輯\n    alert("按鈕被點擊了！");\n});</code></pre>\n<p>這段程式碼就是前端互動的靈魂。未來你請 AI 幫忙寫的互動邏輯，有八成都是建立在這個架構之上。</p>\n'
    },
    '08': {
        'target_md': '## Prompt 模板',
        'target_html': '<h2>Prompt 模板</h2>',
        'md': '### 具體情境演練：番茄鐘\n讓我們用一個「番茄鐘計時器」來示範如何回答這 5 個問題：\n1. **這個網頁是給誰用的？** 需要專注讀書的學生。\n2. **使用者進來第一眼要看到什麼？** 一個大大的 25:00 倒數計時數字。\n3. **頁面需要哪些區塊？** 時間顯示區、開始與暫停按鈕區。\n4. **哪些地方需要互動？** 點擊「開始」時數字要每秒遞減；點擊「暫停」時要停止。\n5. **這次只要完成哪一小步？** 我只要先做好「時間顯示區和按鈕的 HTML/CSS 版面就好，先不要做會動的計時功能」。\n\n將這樣具體的答案餵給 AI，它就不會擅作主張幫你寫出一堆你看不懂的複雜邏輯了！\n\n',
        'html': '<h3>具體情境演練：番茄鐘</h3>\n<p>讓我們用一個「番茄鐘計時器」來示範如何回答這 5 個問題：</p>\n<ol>\n<li><strong>這個網頁是給誰用的？</strong> 需要專注讀書的學生。</li>\n<li><strong>使用者進來第一眼要看到什麼？</strong> 一個大大的 25:00 倒數計時數字。</li>\n<li><strong>頁面需要哪些區塊？</strong> 時間顯示區、開始與暫停按鈕區。</li>\n<li><strong>哪些地方需要互動？</strong> 點擊「開始」時數字要每秒遞減；點擊「暫停」時要停止。</li>\n<li><strong>這次只要完成哪一小步？</strong> 我只要先做好「時間顯示區和按鈕的 HTML/CSS 版面就好，先不要做會動的計時功能」。</li>\n</ol>\n<p>將這樣具體的答案餵給 AI，它就不會擅作主張幫你寫出一堆你看不懂的複雜邏輯了！</p>\n'
    },
    '16': {
        'target_md': '## 常見錯誤',
        'target_html': '<h2>常見錯誤</h2>',
        'md': '### 實戰情境：為待辦清單加上「一鍵清除」\n假設你之前做了一個待辦清單，現在想加上一個「清除全部」的按鈕。你的工作節奏會是：\n1. **備份**：把整個專案資料夾複製一份。\n2. **定位問題**：找出 `index.html`，在適當的位置加上 `<button id="clearAll">清除全部</button>`。\n3. **限縮 Prompt 範圍**：把 `index.html` 和 `script.js` 的程式碼貼給 AI，並寫下 Prompt：\n   > 「這是我目前的待辦清單程式碼。我剛剛在 HTML 加上了一個 id 為 clearAll 的按鈕。請只修改 JavaScript 的部分，幫我加上監聽點擊這個按鈕的功能，當點擊時，清空清單陣列，並更新畫面。」\n4. **小範圍替換**：AI 會給你一段新的 JS。請只把這段新的 JS 貼入你的 `script.js` 中，不要動到其他的程式碼。\n5. **測試驗證**：打開網頁，隨便新增幾個項目，然後點擊「清除全部」，確認是否正常運作。如果出錯了，馬上複製 Console 的紅字報錯，用前面章節學過的除錯 Prompt 丟給 AI。\n\n',
        'html': '<h3>實戰情境：為待辦清單加上「一鍵清除」</h3>\n<p>假設你之前做了一個待辦清單，現在想加上一個「清除全部」的按鈕。你的工作節奏會是：</p>\n<ol>\n<li><strong>備份</strong>：把整個專案資料夾複製一份。</li>\n<li><strong>定位問題</strong>：找出 <code>index.html</code>，在適當的位置加上 <code>&lt;button id="clearAll"&gt;清除全部&lt;/button&gt;</code>。</li>\n<li><strong>限縮 Prompt 範圍</strong>：把 <code>index.html</code> 和 <code>script.js</code> 的程式碼貼給 AI，並寫下 Prompt：<br>\n<blockquote>「這是我目前的待辦清單程式碼。我剛剛在 HTML 加上了一個 id 為 clearAll 的按鈕。請只修改 JavaScript 的部分，幫我加上監聽點擊這個按鈕的功能，當點擊時，清空清單陣列，並更新畫面。」</blockquote></li>\n<li><strong>小範圍替換</strong>：AI 會給你一段新的 JS。請只把這段新的 JS 貼入你的 <code>script.js</code> 中，不要動到其他的程式碼。</li>\n<li><strong>測試驗證</strong>：打開網頁，隨便新增幾個項目，然後點擊「清除全部」，確認是否正常運作。如果出錯了，馬上複製 Console 的紅字報錯，用前面章節學過的除錯 Prompt 丟給 AI。</li>\n</ol>\n'
    }
}

for ch_num, data in exp_data.items():
    md_path = f'chapters/ch{ch_num}.md'
    html_path = f'chapters/ch{ch_num}.html'
    
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f: content = f.read()
        if '基礎程式碼' not in content and '開發者工具' not in content and '事件監聽器範例' not in content and '具體情境演練' not in content and '實戰情境' not in content:
            if data['target_md'] in content:
                content = content.replace(data['target_md'], data['md'] + data['target_md'])
                with open(md_path, 'w', encoding='utf-8') as f: f.write(content)
                print(f"Updated {md_path}")
            
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f: content = f.read()
        if '基礎程式碼' not in content and '開發者工具' not in content and '事件監聽器範例' not in content and '具體情境演練' not in content and '實戰情境' not in content:
            if data['target_html'] in content:
                content = content.replace(data['target_html'], data['html'] + data['target_html'])
            else:
                if '<h2>本章練習</h2>' in content:
                    content = content.replace('<h2>本章練習</h2>', data['html'] + '<h2>本章練習</h2>')
            with open(html_path, 'w', encoding='utf-8') as f: f.write(content)
            print(f"Updated {html_path}")

# Update BOOK.md
if os.path.exists('BOOK.md'):
    with open('BOOK.md', 'r', encoding='utf-8') as f: lines = f.readlines()
    current_chapter = None
    new_lines = []
    
    for i, line in enumerate(lines):
        if line.startswith('# 第 '):
            if ' 2 ' in line: current_chapter = '02'
            elif ' 6 ' in line: current_chapter = '06'
            elif ' 7 ' in line: current_chapter = '07'
            elif ' 8 ' in line: current_chapter = '08'
            elif ' 16 ' in line: current_chapter = '16'
            else: current_chapter = None
            
        if current_chapter and line.startswith(exp_data[current_chapter]['target_md']):
            last_lines = "".join(new_lines[-10:])
            if not any(k in last_lines for k in ['基礎程式碼', '開發者工具', '事件監聽器範例', '具體情境演練', '實戰情境']):
                new_lines.append(exp_data[current_chapter]['md'])
        
        new_lines.append(line)
        
    with open('BOOK.md', 'w', encoding='utf-8') as f: f.write("".join(new_lines))
    print("Updated BOOK.md")
