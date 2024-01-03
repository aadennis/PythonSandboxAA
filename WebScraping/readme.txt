# For MJ values, see https://chat.openai.com/c/d29aee44-81ea-4ee1-9e02-25b9ee15b019 and
# "https://thaeyne.com/2023/11/02/200-words-or-phrases-for-midjourney-photo-prompts/"

https://chat.openai.com/c/9918b896-c547-44a1-9481-b56704528326

pip install requests
pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv

# Replace 'xxxx' with the actual username in the URL
url = "https://www.goodreads.com/review/list/xxxx?per_page=infinite&print=true&shelf=to-read&utf8=%E2%9C%93"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the book elements on the page
    books = soup.find_all("tr", class_="bookalike review")

    # Create a CSV file to write the data
    with open("goodreads_to_read_books.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Title", "Author", "ISBN"])

        for book in books:
            title = book.find("a", class_="bookTitle").get_text(strip=True)
            author = book.find("a", class_="authorName").get_text(strip=True)
            isbn = book.find("div", class_="smallText").get_text(strip=True).split("ISBN")[1].strip()

            csv_writer.writerow([title, author, isbn])

    print("Data has been scraped and saved to 'goodreads_to_read_books.csv'.")
else:
    print("Failed to retrieve the web page. Please check the URL or your internet connection.")

