const display = document.querySelector("#display");
const numberButtons = document.querySelectorAll("[data-number]");
const operatorButtons = document.querySelectorAll("[data-operator]");
const actionButtons = document.querySelectorAll("[data-action]");

let currentValue = "0";
let previousValue = null;
let currentOperator = null;
let shouldResetDisplay = false;

function updateDisplay() {
  display.textContent = currentValue;
}

function inputNumber(number) {
  if (shouldResetDisplay) {
    currentValue = number;
    shouldResetDisplay = false;
    updateDisplay();
    return;
  }

  currentValue = currentValue === "0" ? number : currentValue + number;
  updateDisplay();
}

function inputDecimal() {
  if (shouldResetDisplay) {
    currentValue = "0.";
    shouldResetDisplay = false;
    updateDisplay();
    return;
  }

  if (!currentValue.includes(".")) {
    currentValue += ".";
    updateDisplay();
  }
}

function clearCalculator() {
  currentValue = "0";
  previousValue = null;
  currentOperator = null;
  shouldResetDisplay = false;
  updateDisplay();
}

function backspace() {
  if (shouldResetDisplay || currentValue.length === 1) {
    currentValue = "0";
  } else {
    currentValue = currentValue.slice(0, -1);
  }

  updateDisplay();
}

function calculate(firstNumber, operator, secondNumber) {
  if (operator === "+") {
    return firstNumber + secondNumber;
  }

  if (operator === "-") {
    return firstNumber - secondNumber;
  }

  if (operator === "*") {
    return firstNumber * secondNumber;
  }

  if (operator === "/") {
    if (secondNumber === 0) {
      return "不能除以 0";
    }

    return firstNumber / secondNumber;
  }

  return secondNumber;
}

function chooseOperator(operator) {
  const inputValue = Number(currentValue);

  if (previousValue !== null && currentOperator && !shouldResetDisplay) {
    const result = calculate(previousValue, currentOperator, inputValue);

    if (typeof result === "string") {
      currentValue = result;
      previousValue = null;
      currentOperator = null;
      shouldResetDisplay = true;
      updateDisplay();
      return;
    }

    currentValue = String(Number(result.toFixed(10)));
    previousValue = result;
  } else {
    previousValue = inputValue;
  }

  currentOperator = operator;
  shouldResetDisplay = true;
  updateDisplay();
}

function performEquals() {
  if (previousValue === null || currentOperator === null) {
    return;
  }

  const result = calculate(previousValue, currentOperator, Number(currentValue));
  currentValue = typeof result === "string" ? result : String(Number(result.toFixed(10)));
  previousValue = null;
  currentOperator = null;
  shouldResetDisplay = true;
  updateDisplay();
}

function percent() {
  currentValue = String(Number(currentValue) / 100);
  updateDisplay();
}

numberButtons.forEach((button) => {
  button.addEventListener("click", () => {
    inputNumber(button.dataset.number);
  });
});

operatorButtons.forEach((button) => {
  button.addEventListener("click", () => {
    chooseOperator(button.dataset.operator);
  });
});

actionButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const action = button.dataset.action;

    if (action === "clear") {
      clearCalculator();
    }

    if (action === "backspace") {
      backspace();
    }

    if (action === "decimal") {
      inputDecimal();
    }

    if (action === "equals") {
      performEquals();
    }

    if (action === "percent") {
      percent();
    }
  });
});

document.addEventListener("keydown", (event) => {
  if (event.key >= "0" && event.key <= "9") {
    inputNumber(event.key);
  }

  if (event.key === ".") {
    inputDecimal();
  }

  if (["+", "-", "*", "/"].includes(event.key)) {
    chooseOperator(event.key);
  }

  if (event.key === "Enter" || event.key === "=") {
    event.preventDefault();
    performEquals();
  }

  if (event.key === "Backspace") {
    backspace();
  }

  if (event.key === "Escape") {
    clearCalculator();
  }
});

updateDisplay();
