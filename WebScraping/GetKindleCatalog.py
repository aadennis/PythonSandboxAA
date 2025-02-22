"""
Write the title and author of my Kindle books to a text file, by querying 
the content list page on Amazon (uk).
Exclude any book summaries that include the string 'Acquired by', as this
indicates an invitation to read, not a book I own.

Put a copy of [chrome-win64.zip] in the current folder. Add to gitignore.
https://developer.chrome.com/docs/chromedriver/downloads
https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.126/win64/chrome-win64.zip
"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

driver = uc.Chrome()

# Open the Amazon Kindle page
driver.get("https://www.amazon.co.uk/hz/mycd/digital-console/contentlist/booksAll/authorAsc")

# Wait for manual login
input("Log in manually, then press Enter here...")

book_list = []
while True:
    # Find all the book containers that include both title and author
    book_containers = driver.find_elements(By.XPATH, "//div[@class='digital_entity_details']")

    # Extract title and author from each container, but skip if "Acquired by..." is present
    for container in book_containers:
        try:
            # Check if "Acquired by" exists in the container
            acquired_by_text = container.text
            if "Acquired by" in acquired_by_text:
                print("Skipping book due to 'Acquired by' text.")
                continue  # Skip this book container

            title = container.find_element(By.CSS_SELECTOR, ".digital_entity_title").text
            author = container.find_element(By.CSS_SELECTOR, ".information_row").text
            book_list.append(f"Author: {author}, Title: {title}")
        except Exception as e:
            print(f"Error extracting title/author for a book: {e}")

    # Try to locate the pagination container
    try:
        pagination = driver.find_element(By.ID, "pagination")
        page_links = pagination.find_elements(By.CSS_SELECTOR, "a.page-item")  # All page links
        current_page = driver.find_element(By.CSS_SELECTOR, "a.page-item.active").text  # Get current active page
        
        next_page = None
        # Find the next page number
        for i, link in enumerate(page_links):
            if link.text == str(int(current_page) + 1):  # Look for the next number
                next_page = link
                break

        if next_page:
            print(f"Clicking on page {int(current_page) + 1}...")
            next_page.click()  # Click the next page number
            time.sleep(3)  # Wait for the page to load
        else:
            print("No more pages found. Stopping...")
            break  # No more pages, exit the loop
    except Exception as e:
        print(f"Error navigating pagination: {e}")
        break  # If there's an error navigating pagination, exit the loop

# Save to file
with open("kindle_books_with_authors.txt", "w") as f:
    for book in book_list:
        f.write(book + "\n")

print(f"Saved {len(book_list)} books with authors to kindle_books_with_authors.txt")

driver.quit()
