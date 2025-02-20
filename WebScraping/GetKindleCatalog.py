from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc

driver = uc.Chrome() #browser_executable_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")


# Set up the WebDriver (replace with your browser's driver)
driver = webdriver.Chrome()  # Change to webdriver.Edge() if using Edge

# Open Amazon Manage Your Content & Devices
driver.get("https://www.amazon.co.uk/hz/mycd/digital-console/contentlist/booksAll")

# Wait for manual login (Amazon blocks automation login easily)
input("Log in manually and then press Enter here...")

# Give time for the page to fully load
time.sleep(5)

# Scroll down to load all books
for _ in range(10):  # Adjust depending on how many books you have
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)

# Get book titles and authors
books = driver.find_elements(By.CSS_SELECTOR, "span[data-testid='title']")
authors = driver.find_elements(By.CSS_SELECTOR, "span[data-testid='author']")

# Extract text
book_list = []
for title, author in zip(books, authors):
    book_list.append(f"{title.text} - {author.text}")

# Save to a text file
with open("kindle_books.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(book_list))

print(f"Saved {len(book_list)} books to kindle_books.txt")

# Close the browser
driver.quit()
