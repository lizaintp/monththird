from bs4 import BeautifulSoup
import requests

# number = 0
# for page in range(1,15):
#     url = f'https://24.kg/page_{page}/'
#     response = requests.get(url=url)
#     # print(response.text)

#     soup = BeautifulSoup(response.text, 'lxml')
#     all_news = soup.find_all('div', class_='title')
#     # print(all_news)
#     for news in all_news:
#         number += 1
#         print(number, news.text)

number = 0
for page in range(1,10):
    url = f'https://stopgame.ru/news/all/p1'
    response = requests.get(url=url)
    print(response)
    soup = BeautifulSoup(response.text, 'lxml')
    all_news = soup.find_all('a', class_='_title_1vlem_60')
    for news in all_news:
        number +=1
        print(number, news.text)
"""Помоги мнеее помоги мнеее атартаратара лялл ептвою мать назу врот бялва я ебва в рот емае all news"""