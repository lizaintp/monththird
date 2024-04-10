from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from config import token 
import sqlite3, requests, time, logging

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect('codes.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS code(
    code INT,
    title_film VARCHAR(255)
);
""")

start_inline_buttons = [
    types.InlineKeyboardButton('Фильм', callback_data='get_film'),
    types.InlineKeyboardButton('Загрузить', callback_data='add_film'),
    types.InlineKeyboardButton('TikTok', url='https://tiktok.com/@codex_kg/')
]
start_inline_keyboard = types.InlineKeyboardMarkup().add(*start_inline_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.reply("Привет отправь мне код, а я тебе название фильма", reply_markup=start_inline_keyboard)

class AddFilmState(StatesGroup):
    code = State()
    title_film = State()

@dp.callback_query_handler(lambda call: call.data == 'add_film')
async def start_add_film(callback:types.CallbackQuery):
    await callback.answer("Кнопка работает")
    await callback.message.answer("Отправьте код для фильма")
    await AddFilmState.code.set()

@dp.message_handler(state=AddFilmState.code)
async def get_title_film(message:types.Message, state:FSMContext):
    if message.text.isdigit():
        await state.update_data(code=message.text)
        await message.answer("Введите название фильма")
        await AddFilmState.title_film.set()
    else:
        await message.answer("Введите цифры")

@dp.message_handler(state=AddFilmState.title_film)
async def get_code_title_and_to_db(message:types.Message, state:FSMContext):
    await state.update_data(title_film=message.text)
    result = await storage.get_data(user=message.from_user.id)
    await message.answer("Загружаю в Базу Данных...")
    await message.answer(f"{result}")
    cursor.execute("INSERT INTO code VALUES (?, ?);",
                   (result['code'], result['title_film']))
    cursor.connection.commit()
    await state.finish()

class SendFilmState(StatesGroup):
    code = State()

@dp.callback_query_handler(lambda call: call.data == "get_film")
async def start_get_film(callback:types.CallbackQuery):
    await callback.message.answer("Введите код фильма")
    await SendFilmState.code.set()

@dp.message_handler(state=SendFilmState.code)
async def find_film_send(message:types.Message, state:FSMContext):
    await message.answer(f"Ищу фильм по коду {message.text}")
    cursor.execute(f"SELECT title_film FROM code WHERE code = {message.text};")
    result = cursor.fetchall()
    if result != []:
        await message.answer(f"Фильм найден {result[0][0]}")
    else:
        await message.answer("Мы не нашли фильм")
    await state.finish()

executor.start_polling(dp)
