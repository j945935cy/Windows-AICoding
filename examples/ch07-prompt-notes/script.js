const promptInput = document.querySelector("#promptInput");
const addButton = document.querySelector("#addButton");
const clearButton = document.querySelector("#clearButton");
const promptList = document.querySelector("#promptList");
const feedback = document.querySelector("#feedback");

function addPrompt() {
  const value = promptInput.value.trim();

  if (value === "") {
    feedback.textContent = "請先輸入 prompt。";
    return;
  }

  const item = document.createElement("li");
  item.textContent = value;
  promptList.append(item);

  promptInput.value = "";
  feedback.textContent = "";
  promptInput.focus();
}

addButton.addEventListener("click", addPrompt);

promptInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    addPrompt();
  }
});

clearButton.addEventListener("click", () => {
  promptList.innerHTML = "";
  feedback.textContent = "";
});
