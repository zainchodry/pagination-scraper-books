import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = {
    "rating": [],
    "link": [],
    "price": [],
    "stock": []
}

for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve page {page}")
        break

    print(f"Scraping page {page}...")

    soup = BeautifulSoup(response.content, 'html.parser')

    books = soup.select('article.product_pod')

    for book in books:
        # Rating (as class)
        rating = book.select_one('p.star-rating')['class'][1]

        # Link
        link = book.find('h3').find('a')['href']
        full_link = "https://books.toscrape.com/catalogue/" + link

        # Price
        price = book.select_one('p.price_color').get_text(strip=True)

        # Stock status
        stock = book.select_one('p.instock.availability').get_text(strip=True)

        print(f"Rating: {rating}, Link: {full_link}, Price: {price}, Stock: {stock}")

        data["rating"].append(rating)
        data["link"].append(full_link)
        data["price"].append(price)
        data["stock"].append(stock)

# Save to CSV and Excel after scraping all pages
df = pd.DataFrame(data)
df.to_csv('books.csv', index=False)
df.to_excel('books.xlsx', index=False)

print("All pages scraped and data saved successfully.")
