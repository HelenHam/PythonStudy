import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://tickets.interpark.com/contents/ranking?genre=CONCERT"

response = requests.get(url)
response.raise_for_status()
soup = bs(response.text, "html.parser")

concert_data = []

concert_cards = soup.select("div.responsive-ranking-list_rankingItemInner__mMLXe")

for card in concert_cards:
    try:
        title = card.select_one("li.responsive-ranking-list_goodsName__aHH6Y").get_text(strip=True)
        place = card.select_one("li.responsive-ranking-list_placeName__9HN2O").get_text(strip=True)
        date = card.select_one("li.responsive-ranking-list_dateWrap__jBu5n").get_text(strip=True)        
        concert_data.append({"Title": title, "Place": place, "Date": date})
    except AttributeError:
        continue

df = pd.DataFrame(concert_data)

print(df)