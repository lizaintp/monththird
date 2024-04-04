from aiogram import Bot, Dispatcher, types, executor
from config import token
from bs4 import BeautifulSoup
import requests, logging


#Первое

# bot = Bot(token=token)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)

# @dp.message_handler(commands="start")
# async def start(message:types.Message):
#     await message.answer("Привет напиши /gamenews для получения информации")

# @dp.message_handler(commands="gamenews")
# async def send_gamenews(message:types.Message):
#     await message.answer("Начинаем парсить игровые новости...")
#     number = 0
#     for page in range(1,6):
#         url = 'https://stopgame.ru/news/all/p1'
#         response = requests.get(url=url)
#         soup = BeautifulSoup(response.text, 'lxml')
#         all_news = soup.find_all('a', class_='_title_1vlem_60')
#         for news in all_news:
#             number += 1
#             await message.answer(f"{number}, {news.text}")

# executor.start_polling(dp, skip_updates=True )

#Второе

bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer(f"Здравствуйте {message.from_user.first_name}, нажмите /money чтобы узнать курсы валют")

@dp.message_handler(commands='money')
async def send_currency_rates(message):
    url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    currencies = soup.find_all('td', class_='exrate')
    await message.answer(f"Приветствую! Я бот, который поможет вам узнать текущие курсы валют.\n"
                                                  f"Курс USD: {currencies[0].text}\n"
                                                  f"Курс EUR: {currencies[2].text}\n"
                                                  f"Курс RUB: {currencies[4].text}\n"
                                                  f"Курс KZT: {currencies[6].text}")

executor.start_polling(dp, skip_updates=True)
