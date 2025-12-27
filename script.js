let display = document.getElementById("display");
let currentInput = "";

function appendNumber(num) {
  if (display.innerText === "0") {
    currentInput = num;
  } else {
    currentInput += num;
  }
  display.innerText = currentInput;
}

function appendOperator(op) {
  if (currentInput === "") return;
  const lastChar = currentInput.slice(-1);
  if ("+-*/".includes(lastChar)) return;
  currentInput += op;
  display.innerText = currentInput;
}

function clearDisplay() {
  currentInput = "";
  display.innerText = "0";
}

function calculate() {
  try {
    const result = eval(currentInput);
    display.innerText = result;
    currentInput = result.toString();
  } catch {
    display.innerText = "Equation not set. Try again.";
    currentInput = "";
  }
}

