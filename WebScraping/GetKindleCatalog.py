import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

driver = uc.Chrome()

# Open the Amazon Kindle page
driver.get("https://www.amazon.co.uk/hz/mycd/digital-console/contentlist/booksAll")

# Wait for manual login
input("Log in manually, then press Enter here...")

book_list = []
while True:
    # Find all the book containers that include both title and author
    book_containers = driver.find_elements(By.XPATH, "//div[@class='digital_entity_details']")

    # Extract title and author from each container
    for container in book_containers:
        try:
            title = container.find_element(By.CSS_SELECTOR, ".digital_entity_title").text
            author = container.find_element(By.CSS_SELECTOR, ".information_row").text
            book_list.append(f"Title: {title}, Author: {author}")
        except Exception as e:
            print(f"Error extracting title/author for a book: {e}")

    # Try to locate the "Next" button with the new selector
    try:
        # Use the new selector you found for the "Next" button
        next_button = driver.find_element(By.XPATH, "//a[@id='page-RIGHT_PAGE']")
        next_button.click()  # Click the "Next" button
        time.sleep(3)  # Wait for the page to load
    except Exception as e:
        print("No more pages or error navigating: ", e)
        break  # No "Next" button, exit the loop

# Save to file
with open("kindle_books_with_authors.txt", "w") as f:
    for book in book_list:
        f.write(book + "\n")

print(f"Saved {len(book_list)} books with authors to kindle_books_with_authors.txt")

driver.quit()
