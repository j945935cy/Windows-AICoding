import os
import glob

html_files = glob.glob('chapters/*.html') + glob.glob('appendices/*.html')

prism_css = '  <!-- Prism.js Syntax Highlighting Theme -->\n  <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />\n</head>'
prism_js = '  <!-- Prism.js Syntax Highlighting Script -->\n  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>\n</body>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'prism.min.css' not in content:
        content = content.replace('</head>', prism_css)
        content = content.replace('</body>', prism_js)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
