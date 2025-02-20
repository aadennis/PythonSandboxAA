from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

driver = uc.Chrome()

# Open the Amazon Kindle page
driver.get("https://www.amazon.co.uk/hz/mycd/digital-console/contentlist/booksAll")

# Wait for manual login
input("Log in manually, then press Enter here...")

# Find all the book containers that include both title and author
book_containers = driver.find_elements(By.XPATH, "//div[@class='digital_entity_details']")

# Check if book containers are found
if not book_containers:
    print("No book containers found! Check the page structure and XPath.")
else:
    book_list = []
    for container in book_containers:
        try:
            # Extract title and author from the container
            title = container.find_element(By.CSS_SELECTOR, ".digital_entity_title").text
            author = container.find_element(By.CSS_SELECTOR, ".information_row").text
            book_list.append(f"Title: {title}, Author: {author}")
        except:
            print("Error extracting title/author for one of the books.")
    
    # Save to file
    with open("kindle_books_with_authors.txt", "w") as f:
        for book in book_list:
            f.write(book + "\n")

    print(f"Saved {len(book_list)} books with authors to kindle_books_with_authors.txt")

driver.quit()
