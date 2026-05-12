import os

phase3_data = {
    '03': {
        'target_md': '## 協作流程',
        'target_html': '<h2>協作流程</h2>',
        'md': '## 角色扮演 (Role-playing) 技巧\n為了讓 AI 產生更符合業界標準、更專業的程式碼，你可以在 Prompt 的開頭賦予它一個角色。\n例如：**「請以一位資深前端工程師的角度...」** 或是 **「你是一位擅長教學的程式導師...」**。這能顯著提升 AI 輸出的穩定性與程式碼品質。\n\n',
        'html': '<h2>角色扮演 (Role-playing) 技巧</h2>\n<p>為了讓 AI 產生更符合業界標準、更專業的程式碼，你可以在 Prompt 的開頭賦予它一個角色。</p>\n<p>例如：<strong>「請以一位資深前端工程師的角度...」</strong> 或是 <strong>「你是一位擅長教學的程式導師...」</strong>。這能顯著提升 AI 輸出的穩定性與程式碼品質。</p>\n'
    },
    '08': {
        'target_md': '## 拆解方法',
        'target_html': '<h2>拆解方法</h2>',
        'md': '## 提供範例 (Few-shot Prompting)\n除了描述需求，給予 AI 具體的「範例」是提升準確率最強大的技巧。\n與其從零開始要 AI 寫一個按鈕，不如貼上一段你目前既有的 HTML 結構，然後告訴它：「請參考這段程式碼的命名風格，幫我加上一個新的『送出』按鈕」。這就是所謂的 Few-shot Prompting，能避免 AI 產出跟你原本專案格格不入的程式碼。\n\n',
        'html': '<h2>提供範例 (Few-shot Prompting)</h2>\n<p>除了描述需求，給予 AI 具體的「範例」是提升準確率最強大的技巧。</p>\n<p>與其從零開始要 AI 寫一個按鈕，不如貼上一段你目前既有的 HTML 結構，然後告訴它：「請參考這段程式碼的命名風格，幫我加上一個新的『送出』按鈕」。這就是所謂的 Few-shot Prompting，能避免 AI 產出跟你原本專案格格不入的程式碼。</p>\n'
    },
    '14': {
        'target_md': '## 修改前檢查',
        'target_html': '<h2>修改前檢查</h2>',
        'md': '## 如何辨識 AI 幻覺 (Hallucinations)\nAI 有時候會「一本正經地胡說八道」，這被稱為幻覺。在寫程式時，AI 可能會發明根本不存在的 HTML 標籤（例如 `<carousel>`）或是不支援的 CSS 屬性。\n預防幻覺的方法：\n1. **保持懷疑**：不要 AI 給什麼就全盤接受。\n2. **查閱文件**：如果看到不認識的標籤或語法，丟上 Google 或 MDN (Mozilla Developer Network) 快速搜尋一下。\n3. **小步測試**：一次只貼上一小段程式碼並立刻測試，如果畫面出錯，立刻回報給 AI 並要求修正。\n\n',
        'html': '<h2>如何辨識 AI 幻覺 (Hallucinations)</h2>\n<p>AI 有時候會「一本正經地胡說八道」，這被稱為幻覺。在寫程式時，AI 可能會發明根本不存在的 HTML 標籤（例如 <code>&lt;carousel&gt;</code>）或是不支援的 CSS 屬性。</p>\n<p>預防幻覺的方法：</p>\n<ol>\n<li><strong>保持懷疑</strong>：不要 AI 給什麼就全盤接受。</li>\n<li><strong>查閱文件</strong>：如果看到不認識的標籤或語法，丟上 Google 或 MDN 快速搜尋一下。</li>\n<li><strong>小步測試</strong>：一次只貼上一小段程式碼並立刻測試，如果畫面出錯，立刻回報給 AI 並要求修正。</li>\n</ol>\n'
    },
    '15': {
        'target_md': '## 常見錯誤類型',
        'target_html': '<h2>常見錯誤類型</h2>',
        'md': '## 完美除錯 Prompt 模板\n當你遇到 bug 時，不要只丟一句「程式壞了怎麼辦？」。請使用以下模板，這能幫你省下大量的溝通時間：\n```text\n我遇到了一個錯誤，請幫我除錯。\n1. **我的目標是**：[例如：點擊按鈕後要顯示隱藏的文字]\n2. **目前的行為是**：[例如：點擊按鈕完全沒反應]\n3. **Console 顯示的錯誤訊息**：[貼上完整的紅色錯誤訊息]\n4. **相關的程式碼如下**：\n[貼上 HTML 與 JS 的相關片段]\n```\n\n',
        'html': '<h2>完美除錯 Prompt 模板</h2>\n<p>當你遇到 bug 時，不要只丟一句「程式壞了怎麼辦？」。請使用以下模板，這能幫你省下大量的溝通時間：</p>\n<pre><code>我遇到了一個錯誤，請幫我除錯。\n1. 我的目標是：[例如：點擊按鈕後要顯示隱藏的文字]\n2. 目前的行為是：[例如：點擊按鈕完全沒反應]\n3. Console 顯示的錯誤訊息：[貼上完整的紅色錯誤訊息]\n4. 相關的程式碼如下：\n[貼上 HTML 與 JS 的相關片段]</code></pre>\n'
    },
    '16': {
        'target_md': '## 工作節奏',
        'target_html': '<h2>工作節奏</h2>',
        'md': '## 本地版本備份 (Version Backup) 防呆機制\n在你還沒學會 Git 等專業版本控制工具之前，最簡單的防呆機制就是「**複製整個資料夾**」。\n當你完成了一個能正常運作的功能，準備讓 AI 大幅修改前，請先在電腦裡把專案資料夾複製一份，命名為 `ch16-project-v1-ok`。\n這個小動作能確保當 AI 把程式碼改得亂七八糟時，你永遠有一個「會動的版本」可以退回，大幅減輕心理壓力。\n\n',
        'html': '<h2>本地版本備份 (Version Backup) 防呆機制</h2>\n<p>在你還沒學會 Git 等專業版本控制工具之前，最簡單的防呆機制就是「<strong>複製整個資料夾</strong>」。</p>\n<p>當你完成了一個能正常運作的功能，準備讓 AI 大幅修改前，請先在電腦裡把專案資料夾複製一份，命名為 <code>ch16-project-v1-ok</code>。</p>\n<p>這個小動作能確保當 AI 把程式碼改得亂七八糟時，你永遠有一個「會動的版本」可以退回，大幅減輕心理壓力。</p>\n'
    }
}

for ch_num, data in phase3_data.items():
    md_path = f'chapters/ch{ch_num}.md'
    html_path = f'chapters/ch{ch_num}.html'
    
    # Check if we should insert the text
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f: content = f.read()
        if '角色扮演' not in content and '提供範例' not in content and '幻覺' not in content and '完美除錯' not in content and '防呆機制' not in content:
            if data['target_md'] in content:
                content = content.replace(data['target_md'], data['md'] + data['target_md'])
                with open(md_path, 'w', encoding='utf-8') as f: f.write(content)
                print(f"Updated {md_path}")
            
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f: content = f.read()
        if '角色扮演' not in content and '提供範例' not in content and '幻覺' not in content and '完美除錯' not in content and '防呆機制' not in content:
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
            if ' 3 ' in line: current_chapter = '03'
            elif ' 8 ' in line: current_chapter = '08'
            elif ' 14 ' in line: current_chapter = '14'
            elif ' 15 ' in line: current_chapter = '15'
            elif ' 16 ' in line: current_chapter = '16'
            else: current_chapter = None
            
        if current_chapter and line.startswith(phase3_data[current_chapter]['target_md']):
            last_lines = "".join(new_lines[-10:])
            if not any(k in last_lines for k in ['角色扮演', '提供範例', '幻覺', '完美除錯', '防呆機制']):
                new_lines.append(phase3_data[current_chapter]['md'])
        
        new_lines.append(line)
        
    with open('BOOK.md', 'w', encoding='utf-8') as f: f.write("".join(new_lines))
    print("Updated BOOK.md")
