import os
import re

hints = {
    '04': {
        'md': '\n\n> 💡 **實作小提示 (Hint)**：你可以先請 AI 產生一個包含 `<ul>` 清單與 `<blockquote>` 區塊的 HTML 骨架，再自己填入內容，會比從零開始打字快很多。',
        'html': '\n      <p>💡 <strong>實作小提示 (Hint)</strong>：你可以先請 AI 產生一個包含 <code>&lt;ul&gt;</code> 清單與 <code>&lt;blockquote&gt;</code> 區塊的 HTML 骨架，再自己填入內容，會比從零開始打字快很多。</p>'
    },
    '06': {
        'md': '\n\n> 💡 **實作小提示 (Hint)**：記得要遵循互動三步驟：1. 用 `querySelector` 抓取重置按鈕；2. 加上 `click` 事件監聽；3. 在大括號內把計數變數設為 `0` 並更新畫面 textContent。',
        'html': '\n      <p>💡 <strong>實作小提示 (Hint)</strong>：記得要遵循互動三步驟：1. 用 <code>querySelector</code> 抓取重置按鈕；2. 加上 <code>click</code> 事件監聽；3. 在大括號內把計數變數設為 <code>0</code> 並更新畫面 textContent。</p>'
    },
    '07': {
        'md': '\n\n> 💡 **實作小提示 (Hint)**：你可以用 JavaScript 選取裝載 prompt 的容器（例如 `<ul>` 元素），然後將它的 `innerHTML` 設為空字串 `""`，就可以達成一鍵清空畫面的效果！',
        'html': '\n      <p>💡 <strong>實作小提示 (Hint)</strong>：你可以用 JavaScript 選取裝載 prompt 的容器（例如 <code>&lt;ul&gt;</code> 元素），然後將它的 <code>innerHTML</code> 設為空字串 <code>""</code>，就可以達成一鍵清空畫面的效果！</p>'
    },
    '08': {
        'md': '\n\n> 💡 **實作小提示 (Hint)**：如果一開始不知道怎麼拆解，可以直接對 AI 說：「我想做一個個人網站，請幫我列出需求拆解表這 5 個問題的範例答案」，再從它的答案中去修改。',
        'html': '\n      <p>💡 <strong>實作小提示 (Hint)</strong>：如果一開始不知道怎麼拆解，可以直接對 AI 說：「我想做一個個人網站，請幫我列出需求拆解表這 5 個問題的範例答案」，再從它的答案中去修改。</p>'
    }
}

for ch_num, texts in hints.items():
    md_path = f'chapters/ch{ch_num}.md'
    html_path = f'chapters/ch{ch_num}.html'
    
    # Process MD
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '實作小提示 (Hint)' not in content and '## 本章練習' in content:
            # Insert before ## 檢查清單
            content = content.replace('## 檢查清單', texts['md'] + '\n\n## 檢查清單')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {md_path}")

    # Process HTML
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '實作小提示 (Hint)' not in content and '<h2>本章練習</h2>' in content:
            # Insert before <div class="book-nav">
            content = content.replace('<div class="book-nav">', texts['html'] + '\n      <div class="book-nav">')
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {html_path}")

# Process BOOK.md
if os.path.exists('BOOK.md'):
    with open('BOOK.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    for ch_num, texts in hints.items():
        ch_pattern = re.compile(f'# 第 {int(ch_num)} 章：.*?(?=# 第 \d+ 章：|$)', re.DOTALL)
        match = ch_pattern.search(content)
        if match:
            ch_content = match.group(0)
            if '實作小提示 (Hint)' not in ch_content and '## 本章練習' in ch_content:
                # Replace the last ## 檢查清單 in this chapter content
                parts = ch_content.rsplit('## 檢查清單', 1)
                if len(parts) == 2:
                    new_ch_content = parts[0] + texts['md'].strip() + '\n\n## 檢查清單' + parts[1]
                    content = content.replace(ch_content, new_ch_content)
    
    with open('BOOK.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated BOOK.md")
