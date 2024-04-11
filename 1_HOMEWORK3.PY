# from aiogram import Bot, Dispatcher, executor, types
# import random

# from config import TOKEN

# bot = Bot(TOKEN) # определаем бота что это имменно бот с нашим токеном
# dp = Dispatcher(bot)

# b = [1,2,3]
# c = random.choice(b)

# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.answer('Выберите число: 1,2,3')

# @dp.message_handler(text='1')
# async def cmd_1(message: types.Message):
#     if c == 1:
#         await message.reply('Вы отгадали')
#         await message.reply_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
#     else:
#         await message.reply('Вы лох')
#         await message.reply_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

# @dp.message_handler(text='2')
# async def cmd_2(message: types.Message):
#     if c == 2:
#         await message.reply('Вы отгадали')
#         await message.reply_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
#     else:
#         await message.reply('Вы лох')
#         await message.reply_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

# @dp.message_handler(text='3')
# async def cmd_3(message: types.Message):
#     if c == 3:
#         await message.reply('Вы отгадали')
#         await message.reply('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
#     else:
#         await message.reply('Вы лох')
#         await message.reply_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')
# executor.start_polling(dp)

num = 1
num2 = 2
print(num+num2)