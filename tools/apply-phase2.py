import os

phase2_data = {
    '04': {
        'target_md': '## 常用標籤',
        'target_html': '<h2>常用標籤</h2>',
        'md': '## DOM Tree 視覺化概念\n你可以把 HTML 想像成一棵倒長的樹（DOM Tree）。最外面是 `<html>`，裡面包著 `<head>` 和 `<body>`，而 `<body>` 裡面再包著標題、段落等。\n這棵樹的結構非常重要，因為後續的 CSS 和 JavaScript 都是靠這個「層級關係」來找到對應的元素的。\n\n',
        'html': '<h2>DOM Tree 視覺化概念</h2>\n<p>你可以把 HTML 想像成一棵倒長的樹（DOM Tree）。最外面是 <code>&lt;html&gt;</code>，裡面包著 <code>&lt;head&gt;</code> 和 <code>&lt;body&gt;</code>，而 <code>&lt;body&gt;</code> 裡面再包著標題、段落等。</p>\n<p>這棵樹的結構非常重要，因為後續的 CSS 和 JavaScript 都是靠這個「層級關係」來找到對應的元素的。</p>\n'
    },
    '05': {
        'target_md': '## 常用 CSS',
        'target_html': '<h2>常用 CSS</h2>',
        'md': '## Box Model (盒模型) 重點\n初學者最常遇到的排版問題都來自「Box Model」。請記住這個口訣：**「內容是核心，Padding 往內擠，Border 是邊界，Margin 往外推。」**\n- **Content (內容)**：文字或圖片的實際大小。\n- **Padding (內距)**：內容到邊框的距離（會改變元素的整體大小）。\n- **Border (邊框)**：元素的實際邊界。\n- **Margin (外距)**：與其他元素之間的距離（不屬於元素內部）。\n建議在 CSS 最開頭加上 `* { box-sizing: border-box; }`，這能讓寬高計算包含 Padding 和 Border，大幅減少排版破版的機會。\n\n',
        'html': '<h2>Box Model (盒模型) 重點</h2>\n<p>初學者最常遇到的排版問題都來自「Box Model」。請記住這個口訣：<strong>「內容是核心，Padding 往內擠，Border 是邊界，Margin 往外推。」</strong></p>\n<ul>\n<li><strong>Content (內容)</strong>：文字或圖片的實際大小。</li>\n<li><strong>Padding (內距)</strong>：內容到邊框的距離（會改變元素的整體大小）。</li>\n<li><strong>Border (邊框)</strong>：元素的實際邊界。</li>\n<li><strong>Margin (外距)</strong>：與其他元素之間的距離（不屬於元素內部）。</li>\n</ul>\n<p>建議在 CSS 最開頭加上 <code>* { box-sizing: border-box; }</code>，這能讓寬高計算包含 Padding 和 Border，大幅減少排版破版的機會。</p>\n'
    },
    '06': {
        'target_md': '## 常用語法',
        'target_html': '<h2>常用語法</h2>',
        'md': '## 沒有 JS vs 有 JS 的差異\n- **沒有 JS 時的死網頁**：按鈕按了沒反應，內容永遠是寫死的。\n- **有 JS 後的活網頁**：\n  1. 監聽點擊：「當使用者按下按鈕時...」\n  2. 執行邏輯：「把目前數量加 1...」\n  3. 更新畫面：「把新的數字顯示在畫面上。」\n這三個步驟就是前端互動的核心。\n\n',
        'html': '<h2>沒有 JS vs 有 JS 的差異</h2>\n<ul>\n<li><strong>沒有 JS 時的死網頁</strong>：按鈕按了沒反應，內容永遠是寫死的。</li>\n<li><strong>有 JS 後的活網頁</strong>：\n<ol>\n<li>監聽點擊：「當使用者按下按鈕時...」</li>\n<li>執行邏輯：「把目前數量加 1...」</li>\n<li>更新畫面：「把新的數字顯示在畫面上。」</li>\n</ol>\n</li>\n</ul>\n<p>這三個步驟就是前端互動的核心。</p>\n'
    },
    '07': {
        'target_md': '## 實作步驟',
        'target_html': '<h2>實作步驟</h2>',
        'md': '## 互動流程對比：表單驗證\n想像一個沒有檢查機制的表單：使用者就算輸入空白，資料也會被送出，導致後端收到一堆無效資料。\n加入 JavaScript 後的互動流程：\n- **Before**：點擊送出 -> 直接更新。\n- **After**：點擊送出 -> **JavaScript 攔截並檢查「輸入框是否為空？」** -> 若為空，中斷流程並顯示紅字警告 -> 若有值，才允許更新並清空輸入框。\n這層「防護網」是 JS 在前端非常重要的任務。\n\n',
        'html': '<h2>互動流程對比：表單驗證</h2>\n<p>想像一個沒有檢查機制的表單：使用者就算輸入空白，資料也會被送出，導致後端收到一堆無效資料。</p>\n<p>加入 JavaScript 後的互動流程：</p>\n<ul>\n<li><strong>Before</strong>：點擊送出 -&gt; 直接更新。</li>\n<li><strong>After</strong>：點擊送出 -&gt; <strong>JavaScript 攔截並檢查「輸入框是否為空？」</strong> -&gt; 若為空，中斷流程並顯示紅字警告 -&gt; 若有值，才允許更新並清空輸入框。</li>\n</ul>\n<p>這層「防護網」是 JS 在前端非常重要的任務。</p>\n'
    }
}

# Update individual chapter MD and HTML files
for ch_num, data in phase2_data.items():
    md_path = f'chapters/ch{ch_num}.md'
    html_path = f'chapters/ch{ch_num}.html'
    
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if '視覺化概念' not in content and 'Box Model' not in content and '差異' not in content and '互動流程對比' not in content:
            if data['target_md'] in content:
                content = content.replace(data['target_md'], data['md'] + data['target_md'])
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {md_path}")
            
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if '視覺化概念' not in content and 'Box Model' not in content and '差異' not in content and '互動流程對比' not in content:
            # HTML summarizing might not have the target headings if manually created. Let's check.
            if data['target_html'] in content:
                content = content.replace(data['target_html'], data['html'] + data['target_html'])
            else:
                # If target heading not found, append before <h2>本章練習</h2>
                if '<h2>本章練習</h2>' in content:
                    content = content.replace('<h2>本章練習</h2>', data['html'] + '<h2>本章練習</h2>')
            
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {html_path}")

# Update BOOK.md
if os.path.exists('BOOK.md'):
    with open('BOOK.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_chapter = None
    new_lines = []
    
    for i, line in enumerate(lines):
        if line.startswith('# 第 '):
            if ' 4 ' in line: current_chapter = '04'
            elif ' 5 ' in line: current_chapter = '05'
            elif ' 6 ' in line: current_chapter = '06'
            elif ' 7 ' in line: current_chapter = '07'
            else: current_chapter = None
            
        if current_chapter and line.startswith(phase2_data[current_chapter]['target_md']):
            # Check if we already inserted it slightly before
            if '視覺化概念' not in "".join(new_lines[-10:]) and 'Box Model' not in "".join(new_lines[-10:]) and '差異' not in "".join(new_lines[-10:]) and '互動流程對比' not in "".join(new_lines[-10:]):
                new_lines.append(phase2_data[current_chapter]['md'])
        
        new_lines.append(line)
        
    with open('BOOK.md', 'w', encoding='utf-8') as f:
        f.write("".join(new_lines))
    print("Updated BOOK.md")
