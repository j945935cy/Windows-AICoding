import os

challenges = {
    '09': {
        'md': '\n### 進階挑戰 (Bonus Challenge)\n當你完成基礎版本後，請挑戰加入**深色模式 (Dark Mode)** 切換功能：\n- 在右上角新增一個「切換主題」按鈕。\n- 用 CSS 變數定義淺色與深色背景/文字顏色。\n- 用 JavaScript 監聽點擊，並在 `<body>` 切換 `dark` class，同時存入 `localStorage`。\n',
        'html': '\n      <h3>進階挑戰 (Bonus Challenge)</h3>\n      <p>當你完成基礎版本後，請挑戰加入<strong>深色模式 (Dark Mode)</strong> 切換功能：</p>\n      <ul>\n        <li>在右上角新增一個「切換主題」按鈕。</li>\n        <li>用 CSS 變數定義淺色與深色背景/文字顏色。</li>\n        <li>用 JavaScript 監聽點擊，並在 <code>&lt;body&gt;</code> 切換 <code>dark</code> class，同時存入 <code>localStorage</code>。</li>\n      </ul>\n'
    },
    '10': {
        'md': '\n### 進階挑戰 (Bonus Challenge)\n當你完成基礎版本後，請挑戰加入**類別標籤 (Tags)** 功能：\n- 新增待辦事項時，可以選擇它屬於「工作」、「學習」或「生活」。\n- 在清單畫面上顯示不同的顏色標籤。\n- 嘗試加入另一個篩選器，讓使用者只看特定標籤的項目。\n',
        'html': '\n      <h3>進階挑戰 (Bonus Challenge)</h3>\n      <p>當你完成基礎版本後，請挑戰加入<strong>類別標籤 (Tags)</strong> 功能：</p>\n      <ul>\n        <li>新增待辦事項時，可以選擇它屬於「工作」、「學習」或「生活」。</li>\n        <li>在清單畫面上顯示不同的顏色標籤。</li>\n        <li>嘗試加入另一個篩選器，讓使用者只看特定標籤的項目。</li>\n      </ul>\n'
    },
    '11': {
        'md': '\n### 進階挑戰 (Bonus Challenge)\n當你完成基礎版本後，請挑戰加入**歷史紀錄面板 (History Tape)**：\n- 在計算機右側或下方新增一個清單。\n- 每次按下等號時，把完整的算式 (例如 `12 + 5 = 17`) 記錄到陣列中，並渲染到歷史紀錄面板。\n- 加入「清除歷史紀錄」按鈕。\n',
        'html': '\n      <h3>進階挑戰 (Bonus Challenge)</h3>\n      <p>當你完成基礎版本後，請挑戰加入<strong>歷史紀錄面板 (History Tape)</strong>：</p>\n      <ul>\n        <li>在計算機右側或下方新增一個清單。</li>\n        <li>每次按下等號時，把完整的算式 (例如 <code>12 + 5 = 17</code>) 記錄到陣列中，並渲染到歷史紀錄面板。</li>\n        <li>加入「清除歷史紀錄」按鈕。</li>\n      </ul>\n'
    },
    '12': {
        'md': '\n### 進階挑戰 (Bonus Challenge)\n當你完成基礎版本後，請挑戰加入**平滑過場動畫 (CSS Transitions)**：\n- 切換分類時，被隱藏的圖片不要瞬間消失，而是透過 `opacity` 與 `transform: scale()` 淡出縮小。\n- 使用 JavaScript 的 `setTimeout` 或監聽 `transitionend` 事件，等動畫結束後再真正給予 `display: none`。\n',
        'html': '\n      <h3>進階挑戰 (Bonus Challenge)</h3>\n      <p>當你完成基礎版本後，請挑戰加入<strong>平滑過場動畫 (CSS Transitions)</strong>：</p>\n      <ul>\n        <li>切換分類時，被隱藏的圖片不要瞬間消失，而是透過 <code>opacity</code> 與 <code>transform: scale()</code> 淡出縮小。</li>\n        <li>使用 JavaScript 的 <code>setTimeout</code> 或監聽 <code>transitionend</code> 事件，等動畫結束後再真正給予 <code>display: none</code>。</li>\n      </ul>\n'
    },
    '13': {
        'md': '\n### 進階挑戰 (Bonus Challenge)\n當你完成基礎版本後，請挑戰加入**純 CSS 圓餅圖 (Pie Chart)** 來視覺化總進度：\n- 用一個 `<div>` 並設定 `border-radius: 50%` 變成圓形。\n- 使用 CSS `conic-gradient`，配合 JavaScript 動態修改角度（例如 `conic-gradient(#2563eb 0% X%, #e5e7eb X% 100%)`）。\n',
        'html': '\n      <h3>進階挑戰 (Bonus Challenge)</h3>\n      <p>當你完成基礎版本後，請挑戰加入<strong>純 CSS 圓餅圖 (Pie Chart)</strong> 來視覺化總進度：</p>\n      <ul>\n        <li>用一個 <code>&lt;div&gt;</code> 並設定 <code>border-radius: 50%</code> 變成圓形。</li>\n        <li>使用 CSS <code>conic-gradient</code>，配合 JavaScript 動態修改角度（例如 <code>conic-gradient(#2563eb 0% X%, #e5e7eb X% 100%)</code>）。</li>\n      </ul>\n'
    },
    '17': {
        'md': '\n### 進階挑戰 (Bonus Challenge)\n當你完成基礎版本後，請挑戰加入**專案部署狀態與原始碼連結**：\n- 在每張專案卡片上，新增兩個小連結：「GitHub 原始碼」與「線上預覽」。\n- 替還沒部署的專案加上一個灰色或橘色的「未部署 / 開發中」狀態標籤。\n',
        'html': '\n      <h3>進階挑戰 (Bonus Challenge)</h3>\n      <p>當你完成基礎版本後，請挑戰加入<strong>專案部署狀態與原始碼連結</strong>：</p>\n      <ul>\n        <li>在每張專案卡片上，新增兩個小連結：「GitHub 原始碼」與「線上預覽」。</li>\n        <li>替還沒部署的專案加上一個灰色或橘色的「未部署 / 開發中」狀態標籤。</li>\n      </ul>\n'
    }
}

# Update individual chapter MD and HTML files
for ch_num, texts in challenges.items():
    md_path = f'chapters/ch{ch_num}.md'
    html_path = f'chapters/ch{ch_num}.html'
    
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if '進階挑戰' not in content:
            content = content.replace('## 檢查清單', texts['md'] + '\n## 檢查清單')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {md_path}")
            
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if '進階挑戰' not in content:
            content = content.replace('<div class="book-nav">', texts['html'] + '      <div class="book-nav">')
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
            if ' 9 ' in line: current_chapter = '09'
            elif ' 10 ' in line: current_chapter = '10'
            elif ' 11 ' in line: current_chapter = '11'
            elif ' 12 ' in line: current_chapter = '12'
            elif ' 13 ' in line: current_chapter = '13'
            elif ' 17 ' in line: current_chapter = '17'
            else: current_chapter = None
            
        if line.startswith('## 檢查清單') and current_chapter:
            # Check if we already inserted it slightly before
            if '進階挑戰' not in "".join(new_lines[-10:]):
                new_lines.append(challenges[current_chapter]['md'])
        
        new_lines.append(line)
        
    with open('BOOK.md', 'w', encoding='utf-8') as f:
        f.write("".join(new_lines))
    print("Updated BOOK.md")
