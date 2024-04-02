from aiogram import Bot, Dispatcher, types, executor
from config import token
from bs4 import BeautifulSoup
import requests, logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer("Привет напиши /gamenews для получения информации")

@dp.message_handler(commands="gamenews")
async def send_gamenews(message:types.Message):
    await message.answer("Начинаем парсить игровые новости...")
    number = 0
    for page in range(1,6):
        url = 'https://stopgame.ru/news/all/p1'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'lxml')
        all_news = soup.find_all('a', class_='_title_1vlem_60')
        for news in all_news:
            number += 1
            await message.answer(f"{number}, {news.text}")

executor.start_polling(dp, skip_updates=True )
