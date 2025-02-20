from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

driver = uc.Chrome()

# Open the Amazon Kindle page
driver.get("https://www.amazon.co.uk/hz/mycd/digital-console/contentlist/booksAll")

# Wait for manual login
input("Log in manually, then press Enter here...")

# Find all the book titles using the class 'digital_entity_title'
titles = driver.find_elements(By.CSS_SELECTOR, ".digital_entity_title")

# Check if any titles are found
if not titles:
    print("No books found. Check the page structure and CSS selectors.")
else:
    book_list = []
    for title in titles:
        book_list.append(title.text)  # Get the title text

    # Save to file
    with open("kindle_books.txt", "w") as f:
        for book in book_list:
            f.write(book + "\n")

    print(f"Saved {len(book_list)} books to kindle_books.txt")

driver.quit()
