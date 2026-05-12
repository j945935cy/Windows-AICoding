# 附錄 D：JavaScript 常用語法速查

## 變數

```js
const name = "AI Coding";
let count = 0;
```

## 選取元素

```js
const button = document.querySelector("#button");
const cards = document.querySelectorAll(".card");
```

## 事件

```js
button.addEventListener("click", () => {
  console.log("clicked");
});
```

## 修改文字與 class

```js
title.textContent = "新的標題";
card.classList.add("active");
card.classList.remove("hidden");
card.classList.toggle("open");
```

## 陣列

```js
const items = ["HTML", "CSS", "JavaScript"];

items.forEach((item) => {
  console.log(item);
});
```

## 物件

```js
const todo = {
  id: 1,
  text: "練習 JavaScript",
  done: false
};
```

## localStorage

```js
localStorage.setItem("todos", JSON.stringify(todos));
const todos = JSON.parse(localStorage.getItem("todos")) || [];
```

## 建立元素

```js
const item = document.createElement("li");
item.textContent = "新項目";
list.append(item);
```
