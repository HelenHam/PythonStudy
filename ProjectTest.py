# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup as bs
# import pandas as pd
# import re
# import time

# options = Options()
# options.add_argument('--headless')  # GUI 비활성화
# options.add_argument('--disable-gpu') # 
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(options=options)

# main_url = 'https://tickets.interpark.com/contents/genre/concert'
# driver.get(main_url)

# def infinite_scroll(driver, timeout=10):
#     scroll_pause_time = 1
#     last_height = driver.execute_script("return document.body.scrollHeight")
    
#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(scroll_pause_time)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:  # 더 이상 스크롤할 내용이 없으면 종료
#             break
#         last_height = new_height

# infinite_scroll(driver)

# all_info = bs(driver.page_source, "html.parser")
# concert_data = []
# concert_cards = all_info.select("ul[class^='TicketItem_contentsWrap__']")

# for card in concert_cards:
#     try:
#         title = card.find("li", class_="TicketItem_goodsName__Ju76j").get_text(strip=True)
#         place = card.find("li", class_="TicketItem_placeName__ls9c9").get_text(strip=True)
#         date = card.find("li", class_="TicketItem_playDate__5pEr2").get_text(strip=True)
#         detail_url = card.find("a")["href"]

#         if "2024" in date:
#             concert_data.append({"title": title, "place": place, "date": date, "url": detail_url})
#     except AttributeError:
#         continue

# driver.quit()

# df = pd.DataFrame(concert_data)
# print(df)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# Selenium 옵션 설정
options = Options()
options.add_argument('--headless')  # GUI 비활성화
options.add_argument('--disable-gpu') 
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Selenium 드라이버 초기화
driver = webdriver.Chrome(options=options)
main_url = 'https://tickets.interpark.com/contents/genre/concert'
driver.get(main_url)

# 무한 스크롤 함수
def infinite_scroll(driver, scroll_pause_time=1):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # 더 이상 스크롤할 내용이 없으면 종료
            break
        last_height = new_height

infinite_scroll(driver)

all_info = bs(driver.page_source, "html.parser")
concert_data = []

concert_cards = all_info.select("ul[class^='TicketItem_contentsWrap__']")

for card in concert_cards:
    try:
        title = card.find("li", class_="TicketItem_goodsName__Ju76j").get_text(strip=True)
        place = card.find("li", class_="TicketItem_placeName__ls9c9").get_text(strip=True)
        date = card.find("li", class_="TicketItem_playDate__5pEr2").get_text(strip=True)
        detail_url = card.find("a")["href"]
        if not detail_url.startswith("http"):
            detail_url = f"https://tickets.interpark.com{detail_url}"
        
        # 2024년 공연만 추가
        if "2024" in date:
            concert_data.append({"title": title, "place": place, "date": date, "url": detail_url})
    except AttributeError:
        # 일부 정보가 누락된 경우를 대비
        continue

# 드라이버 종료
driver.quit()

# 데이터프레임 생성 및 확인
df = pd.DataFrame(concert_data)
print(df)
