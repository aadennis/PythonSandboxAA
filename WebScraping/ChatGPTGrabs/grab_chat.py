import os
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# Config
chat_url = "https://chat.openai.com/share/67eea10b-2b6c-8011-b43a-47e59d17208b"
driver_path = "./geckodriver.exe"
screenshot_dir = "screenshots"
output_pdf = "chat_capture.pdf"
viewport_height = 900  # tweak to your window size
scroll_pause = 1.5

# Setup driver
options = Options()
options.headless = False
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Your Firefox path
service = Service(driver_path)
driver = webdriver.Firefox(service=service, options=options)
driver.set_window_size(1200, viewport_height)

os.makedirs(screenshot_dir, exist_ok=True)

driver.get(chat_url)
time.sleep(5)  # initial load

# Scroll and capture multiple screenshots
screenshots = []
scroll_pos = 0
max_scroll = driver.execute_script("return document.body.scrollHeight")

while scroll_pos + viewport_height < max_scroll:
    driver.execute_script(f"window.scrollTo(0, {scroll_pos})")
    time.sleep(scroll_pause)
    file_path = os.path.join(screenshot_dir, f"scroll_{scroll_pos}.png")
    driver.save_screenshot(file_path)
    screenshots.append(file_path)
    scroll_pos += viewport_height // 2  # 50% overlap to avoid gaps
    max_scroll = driver.execute_script("return document.body.scrollHeight")

# Final screenshot at bottom
driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight)")
time.sleep(scroll_pause)
final_path = os.path.join(screenshot_dir, f"scroll_final.png")
driver.save_screenshot(final_path)
screenshots.append(final_path)
driver.quit()

# Stitch images vertically
imgs = [Image.open(s) for s in screenshots]

total_height = sum(img.height for img in imgs)
max_width = max(img.width for img in imgs)
stitched_img = Image.new("RGB", (max_width, total_height))

y_offset = 0
for img in imgs:
    stitched_img.paste(img, (0, y_offset))
    y_offset += img.height

# Save stitched image and convert to PDF
stitched_img.save("chat_full.png", "PNG")
stitched_img.save(output_pdf, "PDF")

print(f"✅ Done! Saved stitched image and PDF")
