import os
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from PIL import Image, ImageDraw, ImageFont

# ======== USER CONFIGURABLE ========
chat_url = "https://chatgpt.com/share/6857d56a-855c-8011-a8ea-74dd0670967e"  # 🔁 Replace with your actual shared chat link
driver_path = "./msedgedriver.exe"  # 🔁 Use full path if not in PATH
screenshot_dir = "screens"
pdf_output = "chat_capture.pdf"
title_text = "My ChatGPT Conversation"
scroll_pause = 1.2  # seconds between scrolls
overlap_ratio = 0.1  # 10% overlap for stitching
font_path = "arial.ttf"  # fallback to default if not found

# ======== BROWSER SETUP ========
options = Options()
options.use_chromium = True
options.add_argument("--window-size=1200,2000")  # viewport size
# Do NOT add --headless, we want to see it

service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)

# ======== LOAD PAGE ========
driver.get(chat_url)
time.sleep(5)  # allow initial load

# ======== SCROLL AND SCREENSHOT ========
os.makedirs(screenshot_dir, exist_ok=True)
viewport_height = driver.execute_script("return window.innerHeight")
scroll_height = driver.execute_script("return document.body.scrollHeight")
step = int(viewport_height * (1 - overlap_ratio))

screens = []
y = 0
i = 0

while y + viewport_height < scroll_height:
    driver.execute_script(f"window.scrollTo(0, {y})")
    time.sleep(scroll_pause)
    path = os.path.join(screenshot_dir, f"screen_{i:03}.png")
    driver.save_screenshot(path)
    screens.append(path)
    y += step
    i += 1

# Final screen at the bottom
driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight)")
time.sleep(scroll_pause)
path = os.path.join(screenshot_dir, f"screen_{i:03}.png")
driver.save_screenshot(path)
screens.append(path)

driver.quit()

# ======== ADD OVERLAY: PAGE NUMBERS + TITLE ========
def add_overlays(image_path, page_num, total_pages, title):
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path, 24)
    except:
        font = ImageFont.load_default()

    margin = 20
    label = f"{title} — Page {page_num + 1} of {total_pages}"

    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (img.width - text_width) // 2
    y = img.height - margin - text_height

    draw.rectangle([x - 10, y - 5, x + text_width + 10, y + text_height + 5], fill="white")
    draw.text((x, y), label, font=font, fill="black")
    return img


total_pages = len(screens)
images = [add_overlays(p, idx, total_pages, title_text) for idx, p in enumerate(screens)]

if images:
    images[0].save(pdf_output, save_all=True, append_images=images[1:])
    print(f"✅ PDF saved as: {pdf_output}")
else:
    print("❌ No screenshots were saved.")
