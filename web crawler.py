
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "http://books.toscrape.com/"

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)

print(f"Status code: {response.status_code}")
print(f"Final URL: {response.url}")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    print("Page title:", soup.title.string)

    books = soup.find_all('article', class_='product_pod')

    for idx, book in enumerate(books, 1):
        title = book.h3.a['title']
        relative_url = book.h3.a['href']
        full_url = urljoin(url, relative_url)
        price = book.find('p', class_='price_color').text

        print(f"{idx}. {title}")
        print(f"Price: {price}")
        print(f"Link: {full_url}\n")

else:
    print(
        f"Failed to retrieve page, status code: "
        f"{response.status_code}"
    )
