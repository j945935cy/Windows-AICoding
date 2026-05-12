import os, re

chapters_dir = 'chapters'
buy_url = 'https://books.google.com.tw/books/about?id=kmvYEQAAQBAJ&redir_esc=y'

cta_html = f'''
      <div class="purchase-cta">
        <h3>🔒 內容已鎖定</h3>
        <p>此章節為正式版內容。購買完整版後即可解鎖所有專案實作教學與 AI Coding 完整工作流程。</p>
        <a class="button primary" href="{buy_url}" target="_blank">在 Google Play 圖書購買完整版</a>
      </div>
'''

def lock_chapter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the range between eyebrow/h1 and book-nav
    # Match everything inside book-content
    match = re.search(r'(<article class="book-content">.*?)(\s+<div class="book-nav">.*?</article>)', content, re.DOTALL)
    if not match:
        print(f'Skipping {file_path}: structure not found')
        return

    header_part = match.group(1)
    nav_part = match.group(2)
    
    # Extract title and eyebrow
    title_match = re.search(r'(<p class="eyebrow">.*?</p>\s+<h1>.*?</h1>)', header_part, re.DOTALL)
    if title_match:
        top_part = title_match.group(1)
    else:
        # Fallback if h1 is different
        h1_match = re.search(r'(<h1>.*?</h1>)', header_part, re.DOTALL)
        top_part = h1_match.group(1) if h1_match else ''

    # Find lead paragraph if exists
    lead_match = re.search(r'<p class="lead">(.*?)</p>', header_part, re.DOTALL)
    lead_text = lead_match.group(1) if lead_match else "此章節內容僅限完整版閱讀。以下為本章重點目錄："

    h2s = re.findall(r'<h2>(.*?)</h2>', header_part)
    
    locked_body = top_part + f'\n      <p class="lead">{lead_text}</p>\n'
    for h2 in h2s:
        # Remove any HTML tags from h2 title for the list
        clean_h2 = re.sub(r'<[^>]+>', '', h2)
        locked_body += f'      <h2>{clean_h2} <span class="locked-badge">🔒 鎖定</span></h2>\n      <div class="locked-content"><p>詳細教學內容、實作步驟與範例程式碼已鎖定，請購買完整版解鎖。</p></div>\n'
    
    locked_body += cta_html
    
    new_content = content[:match.start()] + '<article class="book-content">\n' + locked_body + nav_part + content[match.end():]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Locked {file_path}')

for i in range(8, 19):
    fname = f'ch{i:02d}.html'
    fpath = os.path.join(chapters_dir, fname)
    if os.path.exists(fpath):
        lock_chapter(fpath)
