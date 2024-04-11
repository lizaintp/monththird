from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from config import token 
import sqlite3, requests, time, logging, re

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect('codex.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS user(
    firstname VARCHAR (100),
    lastname VARCHAR (100),
    phone INTEGER ,
    direction VARCHAR (100)
);
""")
connection.commit()

start_inline_buttons = [ 
    types.InlineKeyboardButton('Регистрация', callback_data="registr")
]

start_inline_keyboard = types.InlineKeyboardMarkup().add(*start_inline_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.reply("Привет давай пройдем регистрацию", reply_markup=start_inline_keyboard)

class UserState(StatesGroup):
    firstname = State()
    lastname = State()
    phone = State()
    direction = State()


@dp.callback_query_handler(lambda call: call.data == 'registr')
async def start_add_info(callback:types.CallbackQuery):
    await callback.answer("Кнопка работает")
    await callback.message.answer("Введите имя")
    await UserState.firstname.set()

@dp.message_handler(state=UserState.firstname)
async def process_first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await message.answer("Введите вашу Фамилию:")
    await UserState.next()

@dp.message_handler(state=UserState.lastname)
async def process_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await message.answer("Введите номер телефона в формате +996XXXXXXXXX:")
    await UserState.next()

@dp.message_handler(state=UserState.phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone_pattern = re.compile(r'^\+\d{12}$')
    if not phone_pattern.match(message.text):
        await message.answer("Введите номер в формате +996XXXXXXXXX")
        return
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer("Напишите ваше направление:")
    await UserState.next()

@dp.message_handler(state=UserState.direction)
async def end_register_user(message:types.Message, state:FSMContext):
    data = await state.get_data()
    user_data = (message.from_user.id, data['firstname'], data['lastname'], data['phone'], data['direction'], time.strftime("%Y-%m-%d %H:%M:%S"))
    cursor.execute("INSERT INTO user (id, firstname, lastname, phone, direction) VALUES (?, ?, ?, ?, ?, ?)", user_data)
    connection.commit()
    await message.answer("Спасибо за регистрацию! Ваша информация успешно сохранена.")
    result = cursor.fetchall()
    await bot.send_message(-4134523818, f"Вот ваша информация {result[0][0]}")
    await state.finish()

executor.start_polling(dp, skip_updates=True)
