const completeBtn = document.querySelector("#completeBtn");
const resetBtn = document.querySelector("#resetBtn");
const countSpan = document.querySelector("#count");
const statusMsg = document.querySelector("#statusMsg");

let currentCount = 0;

// 完成按鈕事件
completeBtn.addEventListener("click", function() {
    currentCount += 1;
    countSpan.textContent = currentCount;
    statusMsg.textContent = "目前狀態：學習中！";
});

// 重置按鈕事件 (對應 Chapter 6 練習)
resetBtn.addEventListener("click", function() {
    currentCount = 0;
    countSpan.textContent = currentCount;
    statusMsg.textContent = "目前狀態：尚未開始";
});
