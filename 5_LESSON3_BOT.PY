from aiogram import Bot, Dispatcher, types, executor
from config import token
from bs4 import BeautifulSoup
import requests, logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer("Привет напиши /news для получения информации")

@dp.message_handler(commands="news")
async def send_news(message:types.Message):
    await message.answer("Начинаем парсить новости...")
    number = 0
    for page in range(1,150):
        url = f'https://24.kg/page_{page}/'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'lxml')
        all_news = soup.find_all('div', class_='title')
        for news in all_news:
            number += 1
            

    

executor.start_polling(dp, skip_updates=True)