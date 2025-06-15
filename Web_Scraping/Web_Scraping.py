import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    all_books = []

    for page in range(1, 51):
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        if not books:
            break

        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            link = "https://books.toscrape.com/catalogue/" + book.h3.a['href']
            all_books.append({'Title': title, 'Price': price, 'Link': link})

    df = pd.DataFrame(all_books)
    df.to_csv("all_books_data.csv", index=False)
    print("✅ Done! Data saved to all_books_data.csv")

if __name__ == "__main__":
    scrape_books()