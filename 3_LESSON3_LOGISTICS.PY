from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from config import token 
import logging, sqlite3, time, re

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect('logistics.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(100),
    age INTEGER,
    created VARCHAR(100)
);
""")

start_buttons = [
    types.KeyboardButton('Регистрация'),
    types.KeyboardButton('Шаблон регистрации')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("""Привет! Я чат-бот карго компании Geeks Express.
Данный бот поможет вам получить персональный код и правильно заполнить адрес склада в Китае 🇨🇳
С Уважением команда Geeks Express :)
""", reply_markup=start_keyboard)

class RegisterState(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    age = State()

@dp.message_handler(text="Регистрация")
async def start_register(message:types.Message):
    await message.answer(f"{message.from_user.full_name} давайте начнем регистрацию")
    await message.answer("Введите имя:")
    await RegisterState.first_name.set()

@dp.message_handler(state=RegisterState.first_name)
async def get_user_lastname(message:types.Message, state:FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Введите фамилию:")
    await RegisterState.last_name.set()

@dp.message_handler(state=RegisterState.last_name)
async def get_user_phone(message:types.Message, state:FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer("Введите свой номер:")
    await RegisterState.phone.set()

@dp.message_handler(state=RegisterState.phone)
async def get_user_age(message:types.Message, state:FSMContext):
    phone_pattern = re.compile(r'^\+\d{12}$')
    if not phone_pattern.match(message.text):
        await message.answer("Неверный формат номера. Введите номер в формате +996XXXXXXXXX")
        return
    await state.update_data(phone=message.text)
    await message.answer("Введите возраст:")
    await RegisterState.age.set()

@dp.message_handler(state=RegisterState.age)
async def end_register_user(message:types.Message, state:FSMContext):
    age = int(message.text)
    if age < 14:
        await message.answer("Возраст должен быть не меньше 14 лет")
        return
    await state.update_data(age=age)
    data = await state.get_data()
    user_data = (message.from_user.id, data['first_name'], data['last_name'], data['phone'], data['age'], time.strftime("%Y-%m-%d %H:%M:%S"))
    cursor.execute("INSERT INTO users (id, first_name, last_name, phone, age, created) VALUES (?, ?, ?, ?, ?, ?)", user_data)
    connection.commit()
    await message.answer("Спасибо за регистрацию! Ваша информация успешно сохранена.")
    await state.finish()

@dp.message_handler()
async def not_found(message:types.Message):
    await message.answer("Я вас не понял, введите /start")

executor.start_polling(dp, skip_updates=True)
