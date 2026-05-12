const todoForm = document.querySelector("#todoForm");
const todoInput = document.querySelector("#todoInput");
const todoList = document.querySelector("#todoList");
const statusText = document.querySelector("#statusText");
const filterButtons = document.querySelectorAll(".filter-button");

const storageKey = "ai-coding-todos";
let todos = JSON.parse(localStorage.getItem(storageKey)) || [];
let currentFilter = "all";

function saveTodos() {
  localStorage.setItem(storageKey, JSON.stringify(todos));
}

function getVisibleTodos() {
  if (currentFilter === "active") {
    return todos.filter((todo) => !todo.done);
  }

  if (currentFilter === "done") {
    return todos.filter((todo) => todo.done);
  }

  return todos;
}

function renderTodos() {
  todoList.innerHTML = "";

  const visibleTodos = getVisibleTodos();

  visibleTodos.forEach((todo) => {
    const item = document.createElement("li");
    item.className = `todo-item${todo.done ? " done" : ""}`;

    const toggleButton = document.createElement("button");
    toggleButton.className = "toggle-button";
    toggleButton.type = "button";
    toggleButton.textContent = todo.done ? "↺" : "✓";
    toggleButton.setAttribute("aria-label", "切換完成狀態");

    const text = document.createElement("span");
    text.className = "todo-text";
    text.textContent = todo.text;

    const deleteButton = document.createElement("button");
    deleteButton.className = "delete-button";
    deleteButton.type = "button";
    deleteButton.textContent = "×";
    deleteButton.setAttribute("aria-label", "刪除待辦");

    toggleButton.addEventListener("click", () => {
      todo.done = !todo.done;
      saveTodos();
      renderTodos();
    });

    deleteButton.addEventListener("click", () => {
      todos = todos.filter((itemTodo) => itemTodo.id !== todo.id);
      saveTodos();
      renderTodos();
    });

    item.append(toggleButton, text, deleteButton);
    todoList.append(item);
  });

  const activeCount = todos.filter((todo) => !todo.done).length;
  statusText.textContent = todos.length === 0
    ? "尚未新增待辦事項。"
    : `共有 ${todos.length} 項，剩下 ${activeCount} 項未完成。`;
}

todoForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const text = todoInput.value.trim();

  if (text === "") {
    todoInput.focus();
    return;
  }

  todos.push({
    id: Date.now(),
    text,
    done: false
  });

  todoInput.value = "";
  saveTodos();
  renderTodos();
});

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    currentFilter = button.dataset.filter;
    filterButtons.forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    renderTodos();
  });
});

renderTodos();
