from PIL import Image, ImageDraw, ImageFont
import os

# Create a new portrait cover image
cover_width = 1600
cover_height = 2400
new_cover = Image.new('RGB', (cover_width, cover_height), (20, 20, 30))

# Open the AI generated image
try:
    bg = Image.open('cover.png')
    # Scale it so its height matches the new cover height
    bg_ratio = bg.width / bg.height
    new_bg_width = int(cover_height * bg_ratio)
    bg = bg.resize((new_bg_width, cover_height), Image.Resampling.LANCZOS)
    
    # Crop the center if it's wider
    left = (new_bg_width - cover_width) // 2
    bg = bg.crop((left, 0, left + cover_width, cover_height))
    
    # Darken the background slightly for text readability
    dark_overlay = Image.new('RGB', (cover_width, cover_height), (0, 0, 0))
    new_cover = Image.blend(bg, dark_overlay, 0.4)
except Exception as e:
    print(f"Error loading background: {e}")
    # Proceed with blank background

draw = ImageDraw.Draw(new_cover)

# Load fonts (try standard Windows Chinese fonts)
font_title = None
font_subtitle = None
font_author = None

try:
    # Microsoft JhengHei UI is usually available on Windows
    font_path = "C:\\Windows\\Fonts\\msjhbd.ttc"
    font_title = ImageFont.truetype(font_path, 200)
    font_subtitle = ImageFont.truetype(font_path, 60)
    font_author = ImageFont.truetype(font_path, 80)
except IOError:
    # Fallback to default
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_author = ImageFont.load_default()

# Texts
title_lines = ["AI Coding", "入門"]
subtitle_lines = ["用 Codex、VS Code、HTML、CSS、", "JavaScript 打造你的第一批網頁專案"]
author_text = "Happy eBook"

# Function to get text bounding box and draw centered
def draw_centered_text(y_pos, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x_pos = (cover_width - w) // 2
    draw.text((x_pos, y_pos), text, font=font, fill=fill)
    return bbox[3] - bbox[1]

# Draw Title
y = 300
for line in title_lines:
    h = draw_centered_text(y, line, font_title, (255, 255, 255))
    y += h + 20

# Draw Subtitle
y += 100
for line in subtitle_lines:
    h = draw_centered_text(y, line, font_subtitle, (200, 200, 230))
    y += h + 20

# Draw Author near the bottom
y = cover_height - 300
draw_centered_text(y, author_text, font_author, (255, 200, 100))

# Save the new cover
new_cover.save('cover_text.png')
print("✅ 封面文字添加完成，儲存為 cover_text.png")
