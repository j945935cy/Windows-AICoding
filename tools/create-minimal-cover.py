from PIL import Image, ImageDraw, ImageFont
import os

width = 1600
height = 2400

# Create a solid dark tech background (Slate 900)
bg_color = (15, 23, 42)
cover = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(cover)

# Draw a subtle tech accent (cyan gradient-like line at the top)
accent_color = (6, 182, 212) # Cyan 500
draw.rectangle([0, 0, width, 20], fill=accent_color)
draw.rectangle([0, 20, width, 40], fill=(8, 145, 178)) # Cyan 600
draw.rectangle([0, 40, width, 60], fill=(14, 116, 144)) # Cyan 700

# Draw some subtle dots (tech feel)
for x in range(100, width, 100):
    for y in range(100, height, 100):
        draw.ellipse([x-2, y-2, x+2, y+2], fill=(30, 41, 59)) # Slate 800 dots

# Try to load Windows fonts
try:
    # Use Segoe UI for a modern, clean look
    font_title = ImageFont.truetype("C:\\Windows\\Fonts\\msjhbd.ttc", 180)
    font_subtitle = ImageFont.truetype("C:\\Windows\\Fonts\\msjh.ttc", 65)
    font_author = ImageFont.truetype("C:\\Windows\\Fonts\\msjh.ttc", 70)
    font_small = ImageFont.truetype("C:\\Windows\\Fonts\\msjh.ttc", 40)
except IOError:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_author = ImageFont.load_default()
    font_small = ImageFont.load_default()

def draw_centered(y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (width - w) // 2
    draw.text((x, y), text, font=font, fill=fill)
    return bbox[3] - bbox[1]

# Title texts
title_text = "AI Coding 入門"
subtitle_lines = [
    "用 Codex、VS Code、HTML、CSS、JavaScript",
    "打造你的第一批網頁專案"
]

# Draw title
y = 500
draw_centered(y, title_text, font_title, (255, 255, 255))
y += 250

# Draw a thin separator line under title
draw.line([400, y, width - 400, y], fill=(51, 65, 85), width=4)
y += 80

# Draw subtitle
for line in subtitle_lines:
    h = draw_centered(y, line, font_subtitle, (148, 163, 184)) # Slate 400
    y += h + 30

# Draw author block at the bottom
author_y = height - 400
draw_centered(author_y, "Author", font_small, (100, 116, 139))
draw_centered(author_y + 60, "Happy eBook", font_author, accent_color)

# Save
cover.save('cover_text.png')
print("Successfully generated minimalist solid color cover.")
