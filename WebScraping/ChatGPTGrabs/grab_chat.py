import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image, ImageDraw, ImageFont

# ======== CONFIG ========
chat_url = "https://chat.openai.com/share/67eea10b-2b6c-8011-b43a-47e59d17208b"

driver_path = "./geckodriver.exe"  # Adjust path if needed
output_image = "fullpage.png"
pdf_output = "chat_capture.pdf"
title_text = "My ChatGPT Conversation"
font_path = "arial.ttf"  # Optional: set to a font on your system

# ======== BROWSER SETUP ========
options = Options()
options.headless = False  # set to True if you want silent capture
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # <-- Adjust to your Firefox install path

service = Service(driver_path)
driver = webdriver.Firefox(service=service, options=options)
driver.set_window_size(1200, 2000)

print("📄 Opening page...")
driver.get(chat_url)

# ======== WAIT FOR CHAT TO LOAD ========
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "markdown"))
    )
    print("✅ Chat content detected.")
except:
    print("❌ Timeout: Chat content not found.")
    driver.quit()
    exit(1)

# Give animation/scripts a bit more time
time.sleep(3)

# ======== FULL PAGE SCREENSHOT ========
print("📸 Capturing full page screenshot...")
driver.get_full_page_screenshot_as_file(output_image)
driver.quit()

# ======== ADD OVERLAY AND SAVE TO PDF ========
def add_overlay(image_path, title):
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path, 28)
    except:
        font = ImageFont.load_default()

    label = f"{title} — Page 1 of 1"
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (img.width - text_width) // 2
    y = img.height - text_height - 20

    draw.rectangle([x - 10, y - 5, x + text_width + 10, y + text_height + 5], fill="white")
    draw.text((x, y), label, font=font, fill="black")
    return img

print("🖋️ Adding footer and saving to PDF...")
image = add_overlay(output_image, title_text)
image.save(pdf_output, "PDF")

print(f"✅ Done! PDF saved as: {pdf_output}")
