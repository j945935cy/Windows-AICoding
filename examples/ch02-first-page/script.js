const message = document.querySelector("#message");
const startButton = document.querySelector("#startButton");

startButton.addEventListener("click", () => {
  message.textContent = "我正在用 Codex 學 AI coding。";
});
