const workflowForm = document.querySelector("#workflowForm");
const goalInput = document.querySelector("#goalInput");
const scopeInput = document.querySelector("#scopeInput");
const filesInput = document.querySelector("#filesInput");
const doneInput = document.querySelector("#doneInput");
const workflowOutput = document.querySelector("#workflowOutput");
const copyButton = document.querySelector("#copyButton");

function buildWorkflow() {
  const goal = goalInput.value.trim();
  const scope = scopeInput.value.trim();
  const files = filesInput.value.trim();
  const done = doneInput.value.trim();

  return `任務摘要
目標：${goal}
本次範圍：${scope}
允許修改：${files}
完成標準：${done}

建議實作順序
1. 先確認目前功能可以正常運作。
2. 找出需要修改的 HTML、CSS、JavaScript 區塊。
3. 先做最小 HTML 或資料結構修改。
4. 再補 JavaScript 邏輯。
5. 最後補必要樣式。
6. 逐項測試完成標準。

可交給 Codex 的 Prompt
我正在做一個只使用 HTML、CSS、JavaScript 的專案。
目前目標：${goal}
這次範圍：${scope}
允許修改：${files}
不要修改：未提到的功能與既有可運作流程。
完成標準：${done}

請先簡短說明修改計劃，再提供程式碼。`;
}

function renderWorkflow() {
  workflowOutput.textContent = buildWorkflow();
}

workflowForm.addEventListener("submit", (event) => {
  event.preventDefault();
  renderWorkflow();
});

copyButton.addEventListener("click", async () => {
  await navigator.clipboard.writeText(workflowOutput.textContent);
  copyButton.textContent = "已複製";

  setTimeout(() => {
    copyButton.textContent = "複製 Prompt";
  }, 1500);
});

renderWorkflow();
