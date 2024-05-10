import requests 
from bs4 import BeautifulSoup
def deal_find(search_query):
    url = f"https://www.amazon.com/s?k={search_query}&ref=nb_sb_noss"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error fetching:", e)
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    offers = []
    products = soup.select("div[data-component-type='s-search-result']")

    for prod in products:
        title_elem = prod.select_one(".a-size-medium")
        price_elem = prod.select_one(".a-offscreen")
        link_elem = prod.select_one("a.a-link-normal")

        if title_elem and price_elem and link_elem:
            title = title_elem.get_text(strip=True)
            price = price_elem.get_text(strip=True)
            link = "https://www.amazon.com" + link_elem.get("href", "")
            offers.append({"title": title, "price": price, "link": link})

    return deals

search_query = "laptop"
offers = deal_find(search_query)

for deal in offers:
    print("Title:", deal["title"])
    print("Price:", deal["price"])
    print("Link:", deal["link"])
    print()
