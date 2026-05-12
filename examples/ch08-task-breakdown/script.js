const siteType = document.querySelector("#siteType");
const audience = document.querySelector("#audience");
const features = document.querySelector("#features");
const scope = document.querySelector("#scope");
const output = document.querySelector("#output");
const generateButton = document.querySelector("#generateButton");

function generateSummary() {
  output.textContent = `我要做一個 ${siteType.value.trim()}，使用者是 ${audience.value.trim()}。

主要功能：
${features.value.trim()}

本次任務範圍：
${scope.value.trim()}

技術限制：
只能使用 HTML、CSS、JavaScript。

請先確認需求拆解，再依照範圍提供程式碼。`;
}

generateButton.addEventListener("click", generateSummary);

generateSummary();
