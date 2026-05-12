const statusText = document.querySelector("#statusText");
const countText = document.querySelector("#countText");
const completeButton = document.querySelector("#completeButton");
const resetButton = document.querySelector("#resetButton");

let completedCount = 0;

function updateStatus() {
  countText.textContent = `完成數量：${completedCount}`;

  if (completedCount === 0) {
    statusText.textContent = "今天還沒有完成任務。";
  } else if (completedCount < 3) {
    statusText.textContent = "很好，繼續累積小進度。";
  } else {
    statusText.textContent = "今天已經完成三項以上，節奏很穩。";
  }
}

completeButton.addEventListener("click", () => {
  completedCount += 1;
  updateStatus();
});

resetButton.addEventListener("click", () => {
  completedCount = 0;
  updateStatus();
});
