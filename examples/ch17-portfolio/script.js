const projects = [
  {
    id: "personal",
    category: "page",
    title: "個人介紹網站",
    summary: "用單頁網站介紹自己與學習目標。",
    tech: "HTML / CSS / JavaScript",
    learned: "練習頁面結構、導覽列、響應式版面與作品卡片互動。"
  },
  {
    id: "todo",
    category: "tool",
    title: "待辦清單 App",
    summary: "管理新增、完成、刪除與資料保存。",
    tech: "JavaScript / localStorage",
    learned: "練習陣列狀態、重新渲染、篩選與 localStorage。"
  },
  {
    id: "calculator",
    category: "tool",
    title: "簡易計算機",
    summary: "不用 eval 實作基本計算邏輯。",
    tech: "JavaScript 狀態管理",
    learned: "練習數字輸入、運算子、錯誤防護與鍵盤事件。"
  },
  {
    id: "gallery",
    category: "page",
    title: "圖片展示頁",
    summary: "建立作品網格、分類與 modal。",
    tech: "CSS Grid / DOM",
    learned: "練習 Grid 排列、data 屬性、篩選與 modal 開關。"
  },
  {
    id: "dashboard",
    category: "tool",
    title: "學習儀表板",
    summary: "追蹤課程進度並保存完成狀態。",
    tech: "JavaScript / localStorage",
    learned: "練習資料驅動畫面、進度計算與狀態保存。"
  },
  {
    id: "workflow",
    category: "workflow",
    title: "AI Coding 工作流程",
    summary: "把目標整理成可交給 Codex 的任務。",
    tech: "Prompt / JavaScript",
    learned: "練習任務拆解、完成標準與可複製 prompt。"
  }
];

const menuButton = document.querySelector(".menu-button");
const siteNav = document.querySelector(".site-nav");
const filterButtons = document.querySelectorAll(".filter-button");
const projectGrid = document.querySelector("#projectGrid");
const projectDetail = document.querySelector("#projectDetail");

let currentFilter = "all";

function getVisibleProjects() {
  if (currentFilter === "all") {
    return projects;
  }

  return projects.filter((project) => project.category === currentFilter);
}

function renderProjects() {
  projectGrid.innerHTML = "";

  getVisibleProjects().forEach((project, index) => {
    const card = document.createElement("button");
    card.className = "project-card";
    card.type = "button";
    card.dataset.id = project.id;

    card.innerHTML = `
      <span>${String(index + 1).padStart(2, "0")} / ${project.tech}</span>
      <h3>${project.title}</h3>
      <p>${project.summary}</p>
    `;

    card.addEventListener("click", () => {
      showProjectDetail(project);
      document.querySelectorAll(".project-card").forEach((item) => item.classList.remove("active"));
      card.classList.add("active");
    });

    projectGrid.append(card);
  });
}

function showProjectDetail(project) {
  projectDetail.innerHTML = `
    <p class="eyebrow">Selected Project</p>
    <h3>${project.title}</h3>
    <p><strong>使用技術：</strong>${project.tech}</p>
    <p><strong>學到能力：</strong>${project.learned}</p>
  `;
}

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    currentFilter = button.dataset.filter;
    filterButtons.forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    renderProjects();
  });
});

menuButton.addEventListener("click", () => {
  const isOpen = siteNav.classList.toggle("open");
  menuButton.setAttribute("aria-expanded", String(isOpen));
});

siteNav.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    siteNav.classList.remove("open");
    menuButton.setAttribute("aria-expanded", "false");
  });
});

renderProjects();
