import os
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from PIL import Image, ImageDraw, ImageFont

# https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/


# ===== Config =====
chat_url = "https://chatgpt.com/share/6857d56a-855c-8011-a8ea-74dd0670967e"  # Replace this
screenshot_dir = "screens"
pdf_output = "chat_capture.pdf"
scroll_pause = 1.5
viewport_height = 2000
window_width = 1200
title_text = "My ChatGPT Conversation"


# ===== Setup Edge (non-headless) =====
options = Options()
options.use_chromium = True
options.add_argument(f"--window-size={window_width},{viewport_height}")
# Do NOT use --headless here so it runs visibly

driver_path = "./msedgedriver.exe"  # Optional: full path or just the name if in PATH
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)

# ===== Open the page =====
driver.get(chat_url)
time.sleep(5)

# ===== Capture screenshots =====
os.makedirs(screenshot_dir, exist_ok=True)
scroll_height = driver.execute_script("return document.body.scrollHeight")
y = 0
i = 0
screens = []

while y < scroll_height:
    driver.execute_script(f"window.scrollTo(0, {y})")
    time.sleep(scroll_pause)
    path = os.path.join(screenshot_dir, f"screen_{i:03}.png")
    driver.save_screenshot(path)
    screens.append(path)
    y += viewport_height
    i += 1

driver.quit()

# ===== Add title + page numbers, then save to PDF =====
def add_overlays(image_path, page_num, total_pages, title):
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()

    margin = 20
    page_label = f"{title} — Page {page_num + 1} of {total_pages}"

    draw.text((margin, img.height - margin - 30), page_label, font=font, fill="black")
    return img

images = [add_overlays(p, idx, len(screens), title_text) for idx, p in enumerate(screens)]

if images:
    images[0].save(pdf_output, save_all=True, append_images=images[1:])
    print(f"✅ PDF saved: {pdf_output}")
else:
    print("❌ No screenshots were taken.")
