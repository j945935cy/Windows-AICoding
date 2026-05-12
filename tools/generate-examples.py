import os

examples = {
    'ch02-first-page': {
        'index.html': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>我的第一個網頁</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1 id="title">歡迎來到 AI Coding</h1>
    <button id="myBtn">點擊我</button>
    <script src="script.js"></script>
</body>
</html>''',
        'style.css': '''body { font-family: sans-serif; text-align: center; margin-top: 50px; }
button { padding: 10px 20px; font-size: 16px; cursor: pointer; }''',
        'script.js': '''// 這裡目前是空的，等一下我們要寫互動邏輯'''
    },
    'ch04-html-structure': {
        'index.html': '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>AI Coding 學習筆記</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>AI Coding 學習筆記</h1>
        <nav>
            <a href="#">首頁</a>
            <a href="#">筆記</a>
        </nav>
    </header>
    
    <main>
        <section>
            <h2>學習目標</h2>
            <ul>
                <li>目標 1：...</li>
                <li>目標 2：...</li>
            </ul>
        </section>
        
        <section>
            <h2>常用 Prompt</h2>
            <blockquote>請先產生 HTML 骨架...</blockquote>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2026 我的學習紀錄</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>''',
        'style.css': '''body { font-family: sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
main { max-width: 800px; margin: 0 auto; }''',
        'script.js': ''''''
    },
    'ch06-js-interaction': {
        'index.html': '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>JavaScript 互動練習</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
        <h1>學習狀態卡</h1>
        <p id="statusMsg">目前狀態：尚未開始</p>
        <p>已完成數量：<span id="count">0</span></p>
        
        <button id="completeBtn">完成一項</button>
        <button id="resetBtn">重置</button>
    </main>
    <script src="script.js"></script>
</body>
</html>''',
        'style.css': '''body { font-family: sans-serif; text-align: center; padding-top: 50px; }
button { padding: 10px 20px; margin: 5px; cursor: pointer; }''',
        'script.js': '''const completeBtn = document.querySelector("#completeBtn");
const resetBtn = document.querySelector("#resetBtn");
const countSpan = document.querySelector("#count");
const statusMsg = document.querySelector("#statusMsg");

let currentCount = 0;

// 完成按鈕事件
completeBtn.addEventListener("click", function() {
    currentCount += 1;
    countSpan.textContent = currentCount;
    statusMsg.textContent = "目前狀態：學習中！";
});

// 重置按鈕事件 (對應 Chapter 6 練習)
resetBtn.addEventListener("click", function() {
    currentCount = 0;
    countSpan.textContent = currentCount;
    statusMsg.textContent = "目前狀態：尚未開始";
});
'''
    }
}

base_dir = 'examples'
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

for folder, files in examples.items():
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    for filename, content in files.items():
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
print("✅ 成功生成 examples/ 目錄與起手式專案！")
