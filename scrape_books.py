import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "http://books.toscrape.com/"  # Books to Scrape

response = requests.get(url)

# Step 2: Parse the HTML
if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Extract data (e.g., book titles and prices)
    books = soup.find_all('article', class_='product_pod')  # Find all books

    with open('books_data.txt', 'w') as file:
     
        for book in books:

            title = book.h3.a['title']  # Get the title attribute

            price = book.find('p', class_='price_color').text# Get the price

            rating = book.p['class'][1] # Extract rating class

            relative_url = book.h3.a['href']

            book_url = url + relative_url

            file.write(f"Title: {title}, Price: {price}, URL: {book_url}\n")

    print("Book data has been saved to books_data.txt.")

else:

    print("Failed to retrieve the page")
