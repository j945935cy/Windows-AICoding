const roadmapItems = [
  {
    id: "git",
    title: "第 1 週：Git 與 GitHub",
    detail: "學會 commit、branch、push，保存每一次可運作版本。"
  },
  {
    id: "api",
    title: "第 2 週：API 基礎",
    detail: "用 fetch 取得資料，做一個天氣、書單或匯率小工具。"
  },
  {
    id: "deploy",
    title: "第 3 週：網站部署",
    detail: "把作品集部署到線上，確認手機和桌面都能正常瀏覽。"
  },
  {
    id: "portfolio",
    title: "第 4 週：作品集改版",
    detail: "補上真實作品說明、截圖、學習心得與下一步計劃。"
  },
  {
    id: "framework",
    title: "延伸：前端框架",
    detail: "基礎穩定後，再用 React 或其他框架重做一個既有作品。"
  },
  {
    id: "workflow",
    title: "延伸：AI Coding 流程升級",
    detail: "建立自己的 prompt 範本、除錯流程與改版檢查清單。"
  }
];

const roadmapList = document.querySelector("#roadmapList");
const completedCount = document.querySelector("#completedCount");
const remainingCount = document.querySelector("#remainingCount");
const percentText = document.querySelector("#percentText");
const progressBar = document.querySelector("#progressBar");
const resetButton = document.querySelector("#resetButton");

const storageKey = "ai-coding-next-roadmap";
let completedItems = JSON.parse(localStorage.getItem(storageKey)) || [];

function saveProgress() {
  localStorage.setItem(storageKey, JSON.stringify(completedItems));
}

function isDone(id) {
  return completedItems.includes(id);
}

function toggleItem(id) {
  if (isDone(id)) {
    completedItems = completedItems.filter((itemId) => itemId !== id);
  } else {
    completedItems.push(id);
  }

  saveProgress();
  render();
}

function renderSummary() {
  const done = completedItems.length;
  const total = roadmapItems.length;
  const percent = Math.round((done / total) * 100);

  completedCount.textContent = done;
  remainingCount.textContent = total - done;
  percentText.textContent = `${percent}%`;
  progressBar.style.width = `${percent}%`;
}

function renderItems() {
  roadmapList.innerHTML = "";

  roadmapItems.forEach((item) => {
    const card = document.createElement("label");
    card.className = `roadmap-card${isDone(item.id) ? " done" : ""}`;

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = isDone(item.id);

    const content = document.createElement("div");
    const title = document.createElement("h3");
    const detail = document.createElement("p");

    title.textContent = item.title;
    detail.textContent = item.detail;

    checkbox.addEventListener("change", () => {
      toggleItem(item.id);
    });

    content.append(title, detail);
    card.append(checkbox, content);
    roadmapList.append(card);
  });
}

function render() {
  renderSummary();
  renderItems();
}

resetButton.addEventListener("click", () => {
  completedItems = [];
  saveProgress();
  render();
});

render();
