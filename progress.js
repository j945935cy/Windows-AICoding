const chapters = [
  { id: "ch01", phase: "入門", title: "什麼是 AI Coding", href: "chapters/ch01.html" },
  { id: "ch02", phase: "入門", title: "準備開發環境", href: "chapters/ch02.html", example: "examples/ch02-first-page/index.html" },
  { id: "ch03", phase: "入門", title: "第一次和 Codex 協作", href: "chapters/ch03.html" },
  { id: "ch04", phase: "基礎", title: "HTML 基礎與頁面結構", href: "chapters/ch04.html", example: "examples/ch04-html-structure/index.html" },
  { id: "ch05", phase: "基礎", title: "CSS 基礎與畫面設計", href: "chapters/ch05.html", example: "examples/ch05-css-cards/index.html" },
  { id: "ch06", phase: "基礎", title: "JavaScript 基礎", href: "chapters/ch06.html", example: "examples/ch06-js-interaction/index.html" },
  { id: "ch07", phase: "基礎", title: "讓網頁動起來", href: "chapters/ch07.html", example: "examples/ch07-prompt-notes/index.html" },
  { id: "ch08", phase: "基礎", title: "AI Coding 的需求拆解方法", href: "chapters/ch08.html", example: "examples/ch08-task-breakdown/index.html" },
  { id: "ch09", phase: "專案", title: "個人介紹網站", href: "chapters/ch09.html", example: "examples/ch09-personal-site/index.html" },
  { id: "ch10", phase: "專案", title: "待辦清單 App", href: "chapters/ch10.html", example: "examples/ch10-todo-app/index.html" },
  { id: "ch11", phase: "專案", title: "簡易計算機", href: "chapters/ch11.html", example: "examples/ch11-calculator/index.html" },
  { id: "ch12", phase: "專案", title: "圖片展示頁", href: "chapters/ch12.html", example: "examples/ch12-gallery/index.html" },
  { id: "ch13", phase: "專案", title: "學習儀表板", href: "chapters/ch13.html", example: "examples/ch13-learning-dashboard/index.html" },
  { id: "ch14", phase: "流程", title: "閱讀與修改 AI 程式碼", href: "chapters/ch14.html", example: "examples/ch14-code-reading/index.html" },
  { id: "ch15", phase: "流程", title: "除錯入門", href: "chapters/ch15.html", example: "examples/ch15-debug-workbench/index.html" },
  { id: "ch16", phase: "流程", title: "建立 AI Coding 工作流程", href: "chapters/ch16.html", example: "examples/ch16-workflow-builder/index.html" },
  { id: "ch17", phase: "流程", title: "個人作品集網站", href: "chapters/ch17.html", example: "examples/ch17-portfolio/index.html" },
  { id: "ch18", phase: "流程", title: "下一步學什麼", href: "chapters/ch18.html", example: "examples/ch18-next-roadmap/index.html" }
];

const list = document.querySelector("#progressList");
const percentText = document.querySelector("#progressPercent");
const doneText = document.querySelector("#progressDone");
const leftText = document.querySelector("#progressLeft");
const fill = document.querySelector("#progressFill");
const resetButton = document.querySelector("#resetProgress");
const storageKey = "ai-coding-book-progress";

let doneChapters = JSON.parse(localStorage.getItem(storageKey)) || [];

function save() {
  localStorage.setItem(storageKey, JSON.stringify(doneChapters));
}

function isDone(id) {
  return doneChapters.includes(id);
}

function toggle(id) {
  if (isDone(id)) {
    doneChapters = doneChapters.filter((chapterId) => chapterId !== id);
  } else {
    doneChapters.push(id);
  }

  save();
  render();
}

function renderSummary() {
  const done = doneChapters.length;
  const total = chapters.length;
  const percent = Math.round((done / total) * 100);

  percentText.textContent = `${percent}%`;
  doneText.textContent = done;
  leftText.textContent = total - done;
  fill.style.width = `${percent}%`;
}

function renderList() {
  list.innerHTML = "";

  chapters.forEach((chapter, index) => {
    const item = document.createElement("article");
    item.className = `chapter-progress-card${isDone(chapter.id) ? " done" : ""}`;

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = isDone(chapter.id);
    checkbox.addEventListener("change", () => toggle(chapter.id));

    const content = document.createElement("div");
    const title = document.createElement("h2");
    const meta = document.createElement("p");
    const links = document.createElement("div");

    title.textContent = `${String(index + 1).padStart(2, "0")} ${chapter.title}`;
    meta.textContent = chapter.phase;
    links.className = "progress-links";
    links.innerHTML = `<a href="${chapter.href}">閱讀章節</a>${chapter.example ? `<a href="${chapter.example}">打開範例</a>` : ""}`;

    content.append(title, meta, links);
    item.append(checkbox, content);
    list.append(item);
  });
}

function render() {
  renderSummary();
  renderList();
}

resetButton.addEventListener("click", () => {
  doneChapters = [];
  save();
  render();
});

render();
