from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from config import token 
import logging, sqlite3, time

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect('feedbacks.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(100),
    feedback TEXT,
    created VARCHAR(100)
);
""")

start_buttons = [
    types.KeyboardButton("Места, где можно поесть"),
    types.KeyboardButton("Достопримечательности"),
    types.KeyboardButton("Оставить отзыв")
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    print(message)
    await message.answer(f"Здравствуйте {message.from_user.first_name} я бот города Ош, чего желаете?", reply_markup=start_keyboard)

places_for_eat_buttons = [
    types.KeyboardButton("Borsok"),
    types.KeyboardButton("Ожак Кебаб"),
    types.KeyboardButton("Царский двор"),
    types.KeyboardButton("Назад")
]

places_for_eat_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*places_for_eat_buttons)

@dp.message_handler(text="Места, где можно поесть")
async def places_for_eat(message:types.Message):
    await message.reply("Какое кафе хотите посетить?", reply_markup=places_for_eat_keyboard)

@dp.message_handler(text="Borsok")
async def borsok(message:types.Message):
    await message.reply_photo("https://cachizer1.2gis.com/reviews-photos/5b031904-5382-4db8-ac45-d71d74c97dad.jpg?w=1920")
    await message.reply("https://maps.app.goo.gl/rySs2RpZFcYbzVGs9")

@dp.message_handler(text="Ожак Кебаб")
async def ojak_kebab(message:types.Message):
    await message.reply_photo("https://avatars.mds.yandex.net/get-altay/2809325/2a00000186b76d0fe51b87c34dbd78c0fc1f/L_height")
    await message.reply("https://maps.app.goo.gl/jYEWtJQCDSN8zNGD7")


@dp.message_handler(text="Царский двор")
async def imperial(message:types.Message):
    await message.reply_photo("https://st-1.akipress.org/cdn-st-0/qeY/9/2385472.c1603f051266ae42bd0411ebe75e9b09.jpg")
    await message.reply("https://maps.app.goo.gl/PdU17z2KCQWs6H5C8")

attractions_buttons = [
    types.KeyboardButton("Сулайман Тоо"),
    types.KeyboardButton("Национальный парк Кара-Шоро"),
    types.KeyboardButton("Пик Ленина"),
    types.KeyboardButton("Назад")
]

attractions_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*attractions_buttons)

@dp.message_handler(text="Достопримечательности")
async def attractions(message:types.Message):
    await message.reply("Какое место хотите посетить?", reply_markup=attractions_keyboard)

@dp.message_handler(text="Сулайман Тоо")
async def mountain_sulaiman(message:types.Message):
    await message.reply_photo("https://bestofosh.com/wp-content/uploads/2022/04/%D1%81%D1%83%D0%BB%D0%B0%D0%B9%D0%BC%D0%B0%D0%BD-%D1%82%D0%BE%D0%BE.jpg")
    await message.reply("https://maps.app.goo.gl/Rk8fg4fpGUs4QBJd8")

@dp.message_handler(text="Пик Ленина")
async def lenin_peak(message:types.Message):
    await message.reply_photo("https://asiamountains.net/assets/cache_image/assets/lib/resized/23/1600x1104_0x0_d0b.jpg")
    await message.reply("https://maps.app.goo.gl/LmYZMD3FwbHNodpe6")

@dp.message_handler(text="Национальный парк Кара-Шоро")
async def park(message:types.Message):
    await message.reply_photo("https://triptokyrgyzstan.com/sites/default/files/media/image/ulukbek1.jpg")
    await message.reply("https://maps.app.goo.gl/Ea4wjpaoGiffmu2DA")

class RegisterState(StatesGroup):
    name = State()
    phone = State()
    feedback = State()


@dp.message_handler(text="Оставить отзыв")
async def leave_feedback(message:types.Message):
    await message.reply(f"Хорошо {message.from_user.full_name}")
    await message.answer("Введите имя: ")
    await RegisterState.name.set()

@dp.message_handler(state=RegisterState.name)
async def get_user_phone(message:types.Message, state:FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите свой номер: ")
    await RegisterState.phone.set()

@dp.message_handler(state=RegisterState.phone)
async def get_feedback(message:types.Message, state:FSMContext):
    await state.update_data(phone=message.text)
    await RegisterState.feedback.set()
    data = await state.get_data()
    user_data = (message.from_user.id, data['name'], data['phone'], data['feedback'], time.strftime("%Y-%m-%d %H:%M:%S"))
    cursor.execute("INSERT INTO users (id, name, phone, feedback, created) VALUES (?, ?, ?, ?, ?)", user_data)
    connection.commit()
    await message.answer("Спасибо за регистрацию! Ваш отзыв успешно сохранен.")
    await state.finish()





@dp.message_handler()
async def back(message:types.Message):
    await start(message)

executor.start_polling(dp)
