# from aiogram import Bot, Dispatcher, types, executor
# from config import TOKEN
# import logging

# bot = Bot(TOKEN)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)

# start_buttons = [
#     types.KeyboardButton("Помощь"),
#     types.KeyboardButton("Курсы"),
#     types.KeyboardButton("О нас"),
#     types.KeyboardButton("Пробные уроки"),
#     types.KeyboardButton("Мероприятия"),
#     types.KeyboardButton("Адрес")
# ]
# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     print(message)
#     await message.answer(f"Привет {message.from_user.first_name}, на связи Гикс!\n Чем могу помочь?", reply_markup=start_keyboard)
# @dp.message_handler(text='Помощь')
# async def help(message:types.Message):
#     await message.reply(f"{message.from_user.full_name} напишите о своей проблеме")

# @dp.message_handler(text='О нас')
# async def about_us(message:types.Message):
#     await message.reply(f"Geeks это айти курсы в Бишкеке , в Оше, в Кара-Балте, в Ташкенте с 2018 года")

# @dp.message_handler(text='Адрес')
# async def address(message:types.Message):
#     await message.reply(f"Ош , Мырзалы Аматова 1Б (БЦ Томирис)")
#     await message.reply_location(40.51931838327587, 72.80288233491035)

# @dp.message_handler(text='Мероприятия')
# async def event(message:types.Message):
#     await message.reply("23 марта пройдет Весенняя ярмарка в честь Нооруз. Время проведения: 13:00.\n Главный виновник Сумолок")


# @dp.message_handler(text='Пробные уроки')
# async def lesson(message:types.Message):
#     await message.reply("Backend - понедельник")

# courses_buttons = [
#     types.KeyboardButton("Backend"),
#     types.KeyboardButton("Frontend"),
#     types.KeyboardButton("Android"),
#     types.KeyboardButton("UX UI"),
#     types.KeyboardButton("Назад")
# ]
# courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

# @dp.message_handler(text='Курсы')
# async def courses(message:types.Message):
#     await message.reply("Вот все курсы:", reply_markup=courses_keyboard)

# @dp.message_handler(text="Backend")
# async def backend(message:types.Message):
#     await message.reply("Backend это серверная сторона сайта или приложения.\n Длиться 5 месяцев.\n Цена : 10тыс в месяц ")

# @dp.message_handler(text="Frontend")
# async def frontend(message:types.Message):
#     await message.reply("Frontend создает интерфейсы веб-сайтов и приложений. \n Длиться 5 месяцев.\n Цена : 10тыс в месяц")

# @dp.message_handler(text="Android")
# async def android(message:types.Message):
#     await message.reply("Android создает приложения для Android.\n Длиться 7 месяцев.\n Цена : 10тыс в месяц")

# @dp.message_handler(text="UX UI")
# async def ux_ui(message:types.Message):
#     await message.reply("UX UI дизайнеры создают дизайн для веб-сайтов и приложений.\n Длиться 3 месяца.\n Цена : 10тыс в месяц")



# @dp.message_handler()
# async def back(message:types.Message):
#     await start(message)

# @dp.message_handler()
# async def not_found(message:types.Message):
#     await message.reply("Я вас не понял")


# executor.start_polling(dp)

