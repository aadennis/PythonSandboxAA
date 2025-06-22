import os
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from PIL import Image, ImageDraw, ImageFont

# ========== CONFIG ==========
chat_url = "https://chatgpt.com/share/6857d56a-855c-8011-a8ea-74dd0670967e"  # Replace
driver_path = "./msedgedriver.exe"  # Update if not in PATH
screenshot_dir = "screens"
pdf_output = "chat_capture.pdf"
title_text = "My ChatGPT Conversation"
font_path = "arial.ttf"  # Optional
scroll_pause = 0.5
scroll_step = 100  # px per scroll
viewport_height = 2000  # match browser window size

# ========== SETUP ==========
options = Options()
options.use_chromium = True
options.add_argument(f"--window-size=1200,{viewport_height}")
# No headless — you want to see it

service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)

driver.get(chat_url)
time.sleep(5)  # wait for full load

# ========== SCROLL + SCREENSHOT ==========
os.makedirs(screenshot_dir, exist_ok=True)
screens = []
seen_positions = set()
screenshot_count = 0

last_height = driver.execute_script("return document.body.scrollHeight")
current_scroll = 0

while True:
    pos = driver.execute_script("return window.scrollY")
    if pos in seen_positions:
        break
    seen_positions.add(pos)

    # Screenshot
    file_path = os.path.join(screenshot_dir, f"screen_{screenshot_count:03}.png")
    driver.save_screenshot(file_path)
    screens.append(file_path)
    screenshot_count += 1

    # Scroll down
    driver.execute_script(f"window.scrollBy(0, {scroll_step})")
    time.sleep(scroll_pause)

    new_height = driver.execute_script("return window.scrollY")
    if new_height + viewport_height >= last_height:
        # Final scroll and capture
        time.sleep(1)
        driver.save_screenshot(os.path.join(screenshot_dir, f"screen_{screenshot_count:03}.png"))
        break

driver.quit()

# ========== OVERLAY + PDF ==========
def add_overlays(image_path, page_num, total_pages, title):
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path, 24)
    except:
        font = ImageFont.load_default()

    label = f"{title} — Page {page_num + 1} of {total_pages}"
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (img.width - text_width) // 2
    y = img.height - text_height - 20

    draw.rectangle([x - 10, y - 5, x + text_width + 10, y + text_height + 5], fill="white")
    draw.text((x, y), label, font=font, fill="black")
    return img

images = [add_overlays(p, i, len(screens), title_text) for i, p in enumerate(screens)]
if images:
    images[0].save(pdf_output, save_all=True, append_images=images[1:])
    print(f"✅ PDF saved as: {pdf_output}")
else:
    print("❌ No screenshots were saved.")
