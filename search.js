const searchItems = [
  { type: "章節", title: "第 1 章：什麼是 AI Coding", href: "chapters/ch01.html", keywords: "AI coding Codex 分工 入門" },
  { type: "章節", title: "第 2 章：準備開發環境", href: "chapters/ch02.html", keywords: "VS Code index html css js" },
  { type: "章節", title: "第 3 章：第一次和 Codex 協作", href: "chapters/ch03.html", keywords: "prompt 協作 修改 解釋" },
  { type: "章節", title: "第 4 章：HTML 基礎與頁面結構", href: "chapters/ch04.html", keywords: "HTML 語意化 header nav main section" },
  { type: "章節", title: "第 5 章：CSS 基礎與畫面設計", href: "chapters/ch05.html", keywords: "CSS Grid Flexbox 排版 顏色" },
  { type: "章節", title: "第 6 章：JavaScript 基礎", href: "chapters/ch06.html", keywords: "JavaScript DOM querySelector addEventListener" },
  { type: "章節", title: "第 7 章：讓網頁動起來", href: "chapters/ch07.html", keywords: "表單 按鈕 輸入 清單 互動" },
  { type: "章節", title: "第 8 章：AI Coding 的需求拆解方法", href: "chapters/ch08.html", keywords: "需求拆解 prompt 任務 範圍" },
  { type: "章節", title: "第 9 章：個人介紹網站", href: "chapters/ch09.html", keywords: "個人網站 hero 技能 作品" },
  { type: "章節", title: "第 10 章：待辦清單 App", href: "chapters/ch10.html", keywords: "todo localStorage 陣列 新增 刪除" },
  { type: "章節", title: "第 11 章：簡易計算機", href: "chapters/ch11.html", keywords: "計算機 狀態 鍵盤 eval" },
  { type: "章節", title: "第 12 章：圖片展示頁", href: "chapters/ch12.html", keywords: "gallery modal filter grid" },
  { type: "章節", title: "第 13 章：學習儀表板", href: "chapters/ch13.html", keywords: "dashboard progress localStorage 進度條" },
  { type: "章節", title: "第 14 章：閱讀與修改 AI 程式碼", href: "chapters/ch14.html", keywords: "讀碼 修改 HTML CSS JavaScript" },
  { type: "章節", title: "第 15 章：除錯入門", href: "chapters/ch15.html", keywords: "debug console 錯誤 localStorage JSON" },
  { type: "章節", title: "第 16 章：建立 AI Coding 工作流程", href: "chapters/ch16.html", keywords: "workflow 工作流程 prompt 完成標準" },
  { type: "章節", title: "第 17 章：個人作品集網站", href: "chapters/ch17.html", keywords: "portfolio 作品集 篩選 詳情" },
  { type: "章節", title: "第 18 章：下一步學什麼", href: "chapters/ch18.html", keywords: "Git GitHub API 部署 框架" },
  { type: "範例", title: "待辦清單 App", href: "examples/ch10-todo-app/index.html", keywords: "todo localStorage filter" },
  { type: "範例", title: "簡易計算機", href: "examples/ch11-calculator/index.html", keywords: "calculator keyboard percent" },
  { type: "範例", title: "圖片展示頁", href: "examples/ch12-gallery/index.html", keywords: "gallery modal category" },
  { type: "範例", title: "學習儀表板", href: "examples/ch13-learning-dashboard/index.html", keywords: "dashboard progress checkbox" },
  { type: "範例", title: "工作流程產生器", href: "examples/ch16-workflow-builder/index.html", keywords: "workflow prompt copy" },
  { type: "範例", title: "個人作品集", href: "examples/ch17-portfolio/index.html", keywords: "portfolio projects filter" },
  { type: "附錄", title: "Codex Prompt 模板", href: "appendices/a-prompts.html", keywords: "prompt template Codex 除錯 重構" },
  { type: "附錄", title: "HTML 速查", href: "appendices/b-html-cheatsheet.html", keywords: "HTML tag form semantic" },
  { type: "附錄", title: "CSS 速查", href: "appendices/c-css-cheatsheet.html", keywords: "CSS flex grid margin padding" },
  { type: "附錄", title: "JavaScript 速查", href: "appendices/d-js-cheatsheet.html", keywords: "JavaScript DOM event localStorage" },
  { type: "附錄", title: "常見錯誤清單", href: "appendices/e-common-errors.html", keywords: "錯誤 debug querySelector JSON" },
  { type: "附錄", title: "AI Coding 術語表", href: "appendices/f-glossary.html", keywords: "glossary AI Coding prompt DOM state render refactor debug" }
];

const searchInput = document.querySelector("#searchInput");
const searchResults = document.querySelector("#searchResults");
const searchCount = document.querySelector("#searchCount");

function getMatches(query) {
  const normalizedQuery = query.trim().toLowerCase();

  if (normalizedQuery === "") {
    return searchItems;
  }

  return searchItems.filter((item) => {
    const text = `${item.type} ${item.title} ${item.keywords}`.toLowerCase();
    return text.includes(normalizedQuery);
  });
}

function renderResults() {
  const matches = getMatches(searchInput.value);
  searchResults.innerHTML = "";
  searchCount.textContent = `找到 ${matches.length} 筆結果`;

  matches.forEach((item) => {
    const link = document.createElement("a");
    link.className = "search-result-card";
    link.href = item.href;
    link.innerHTML = `<span>${item.type}</span><h2>${item.title}</h2><p>${item.keywords}</p>`;
    searchResults.append(link);
  });
}

searchInput.addEventListener("input", renderResults);
renderResults();
