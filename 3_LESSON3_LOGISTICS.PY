from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from config import token
import logging, sqlite3, time

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect("logistics.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
               id INTEGER,
               first_name VARCHAR (100),
               last_name VARCHAR (100),
               numder VARCHAR (100),
               age INTEGER NOT NULL, 
               created VARCHAR (100)
);
""")

start_buttons = [
    types.KeyboardButton("Регистрация"),
    types.KeyboardButton("Шаблон регистрации")
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)


@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer("""Привет! Я чат-бот карго компании Geeks_express.
Данный бот поможет вам получить персональный код и правильно заполнить адрес склада в Китае 
С Уважением команда Geeks_Express""", reply_markup=start_keyboard)

@dp.message_handler(text="Шаблон регистрации")
async def shablon_registr(message:types.Message):
    await message.reply("""Дла регистрации в нашей карго компании вам нужно:
1)Указать свое имя: 
2)Указать свою фамилию:
3)Указать рабочий номер телефона в международном формате +996706634966: 
4)Указать ваш возраст: 
И вы автоматически получите код клиента :D
""")

class RegistrationState(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    age = State()



@dp.message_handler(text="Регистрация")
async def registr(message:types.Message):
    await message.answer(f"Регистрация {message.from_user.first_name} давайте начнем регистрацию")
    await message.answer("Введите свое имя: ")
    await RegistrationState.first_name.set()

@dp.message_handler(state=RegistrationState.first_name)
async def get_user_lastname(message:types.Message, state:FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Введите фамилию: ")
    await RegistrationState.last_name.set()

@dp.message_handler(state=RegistrationState.last_name)
async def get_user_phone(message:types.Message, state:FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer("Введите рабочий номер телефона в международном формате +996706634966: ")
    await RegistrationState.phone.set()

@dp.message_handler(state=RegistrationState.phone)
async def get_user_age(message:types.Message, state:FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введите возраст: ")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def end_registr_user(message:types.Message, state:FSMContext):
    await state.update_data(age=message.text)
    result = await storage.get_data(user=message.from_user.id)
    await message.answer(f"{result}")



@dp.message_handler()
async def back(message:types.Message):
    await start(message)

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понимаю, введите /start")


executor.start_polling(dp, skip_updates=True)
