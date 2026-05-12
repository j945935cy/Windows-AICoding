const lessons = [
  { id: "ch01", title: "第 1 章：什麼是 AI Coding", group: "入門" },
  { id: "ch02", title: "第 2 章：準備開發環境", group: "入門" },
  { id: "ch03", title: "第 3 章：第一次和 Codex 協作", group: "入門" },
  { id: "ch04", title: "第 4 章：HTML 基礎", group: "基礎" },
  { id: "ch05", title: "第 5 章：CSS 基礎", group: "基礎" },
  { id: "ch06", title: "第 6 章：JavaScript 基礎", group: "基礎" },
  { id: "ch07", title: "第 7 章：讓網頁動起來", group: "互動" },
  { id: "ch08", title: "第 8 章：需求拆解方法", group: "互動" },
  { id: "ch09", title: "第 9 章：個人介紹網站", group: "專案" },
  { id: "ch10", title: "第 10 章：待辦清單 App", group: "專案" },
  { id: "ch11", title: "第 11 章：簡易計算機", group: "專案" },
  { id: "ch12", title: "第 12 章：圖片展示頁", group: "專案" },
  { id: "ch13", title: "第 13 章：學習儀表板", group: "專案" }
];

const lessonList = document.querySelector("#lessonList");
const percentText = document.querySelector("#percentText");
const completedText = document.querySelector("#completedText");
const remainingText = document.querySelector("#remainingText");
const progressBar = document.querySelector("#progressBar");
const resetButton = document.querySelector("#resetButton");

const storageKey = "ai-coding-dashboard-progress";
let completedLessons = JSON.parse(localStorage.getItem(storageKey)) || [];

function saveProgress() {
  localStorage.setItem(storageKey, JSON.stringify(completedLessons));
}

function isCompleted(id) {
  return completedLessons.includes(id);
}

function toggleLesson(id) {
  if (isCompleted(id)) {
    completedLessons = completedLessons.filter((lessonId) => lessonId !== id);
  } else {
    completedLessons.push(id);
  }

  saveProgress();
  renderDashboard();
}

function renderSummary() {
  const completedCount = completedLessons.length;
  const totalCount = lessons.length;
  const remainingCount = totalCount - completedCount;
  const percent = Math.round((completedCount / totalCount) * 100);

  percentText.textContent = `${percent}%`;
  completedText.textContent = completedCount;
  remainingText.textContent = remainingCount;
  progressBar.style.width = `${percent}%`;
}

function renderLessons() {
  lessonList.innerHTML = "";

  lessons.forEach((lesson) => {
    const card = document.createElement("label");
    card.className = `lesson-card${isCompleted(lesson.id) ? " done" : ""}`;

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = isCompleted(lesson.id);

    const content = document.createElement("div");
    const title = document.createElement("h3");
    const group = document.createElement("p");

    title.textContent = lesson.title;
    group.textContent = lesson.group;

    checkbox.addEventListener("change", () => {
      toggleLesson(lesson.id);
    });

    content.append(title, group);
    card.append(checkbox, content);
    lessonList.append(card);
  });
}

function renderDashboard() {
  renderSummary();
  renderLessons();
}

resetButton.addEventListener("click", () => {
  completedLessons = [];
  saveProgress();
  renderDashboard();
});

renderDashboard();
