# 附錄 C：CSS 常用屬性速查

## 文字

- `color`：文字顏色
- `font-family`：字體
- `font-size`：字體大小
- `font-weight`：字重
- `line-height`：行高
- `text-align`：對齊

## 盒模型

- `width`、`height`：寬高
- `margin`：外距
- `padding`：內距
- `border`：邊框
- `border-radius`：圓角
- `box-sizing`：盒模型計算方式

## 背景與視覺

- `background`：背景
- `box-shadow`：陰影
- `opacity`：透明度
- `overflow`：超出範圍處理

## 排版

- `display`：顯示模式
- `flex`：彈性排版
- `grid-template-columns`：Grid 欄位
- `gap`：間距
- `align-items`：垂直對齊
- `justify-content`：水平分配

## 響應式

```css
@media (max-width: 800px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
```

## 常用初始設定

```css
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
```
