const cases = {
  html: {
    type: "HTML",
    title: "HTML 路徑錯誤",
    error: "GET file:///.../styles.css net::ERR_FILE_NOT_FOUND",
    cause: "HTML 中連結的檔名和實際 CSS 檔名不一致，例如寫成 styles.css，但檔案叫 style.css。",
    fix: "檢查 link 標籤的 href，確認路徑、資料夾和檔名完全一致。",
    prompt: "我的 HTML 載入 CSS 失敗，Console 顯示 net::ERR_FILE_NOT_FOUND。請幫我檢查可能的路徑問題，不要重寫整個檔案。"
  },
  css: {
    type: "CSS",
    title: "CSS 選擇器錯誤",
    error: "畫面沒有套用預期樣式，但 Console 沒有錯誤。",
    cause: "HTML 使用 class=\"card\"，但 CSS 寫成 .cards，導致選擇器沒有選到元素。",
    fix: "對照 HTML class 與 CSS 選擇器名稱，確認拼字完全一致。",
    prompt: "我的 CSS 沒有套用到卡片。HTML class 和 CSS 選擇器可能不一致。請幫我指出應該檢查哪些名稱。"
  },
  js: {
    type: "JavaScript",
    title: "JavaScript 找不到元素",
    error: "Cannot read properties of null (reading 'addEventListener')",
    cause: "querySelector 找不到指定元素，可能是 id 拼錯，或 script 在元素建立前執行。",
    fix: "確認 HTML 中有對應 id，並把 script 放在 body 結尾或使用 DOMContentLoaded。",
    prompt: "Console 顯示 Cannot read properties of null (reading 'addEventListener')。請解釋原因，並告訴我如何檢查 querySelector 和 HTML id。"
  },
  storage: {
    type: "JavaScript",
    title: "localStorage JSON 錯誤",
    error: "Unexpected token ... is not valid JSON",
    cause: "讀取 localStorage 後用 JSON.parse 解析，但裡面的內容不是合法 JSON 字串。",
    fix: "確認儲存時使用 JSON.stringify，讀取時再 JSON.parse；必要時清除壞掉的 localStorage 資料。",
    prompt: "我的 localStorage 讀取時出現 JSON parse 錯誤。請幫我分析可能原因，並提供最小修復方式。"
  }
};

const caseButtons = document.querySelectorAll(".case-button");
const caseType = document.querySelector("#caseType");
const caseTitle = document.querySelector("#caseTitle");
const caseError = document.querySelector("#caseError");
const caseCause = document.querySelector("#caseCause");
const caseFix = document.querySelector("#caseFix");
const casePrompt = document.querySelector("#casePrompt");

function renderCase(caseKey) {
  const currentCase = cases[caseKey];

  caseType.textContent = currentCase.type;
  caseTitle.textContent = currentCase.title;
  caseError.textContent = currentCase.error;
  caseCause.textContent = currentCase.cause;
  caseFix.textContent = currentCase.fix;
  casePrompt.textContent = currentCase.prompt;

  caseButtons.forEach((button) => {
    button.classList.toggle("active", button.dataset.case === caseKey);
  });
}

caseButtons.forEach((button) => {
  button.addEventListener("click", () => {
    renderCase(button.dataset.case);
  });
});

renderCase("html");
