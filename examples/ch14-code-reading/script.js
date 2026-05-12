const tabButtons = document.querySelectorAll(".tab-button");
const notePanels = document.querySelectorAll(".note-panel");

function showPanel(targetId) {
  notePanels.forEach((panel) => {
    panel.classList.toggle("active", panel.id === targetId);
  });

  tabButtons.forEach((button) => {
    button.classList.toggle("active", button.dataset.target === targetId);
  });
}

tabButtons.forEach((button) => {
  button.addEventListener("click", () => {
    showPanel(button.dataset.target);
  });
});
