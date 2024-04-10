import telebot
from telebot import types

# Токен вашего бота, который вы получили у @BotFather
TOKEN = '6610853115:AAEY5xl_zGjDsoCi-qxIq2HHIs4zp1_pvoo'

# Словарь для хранения данных пользователей
users = {}

# Функция для создания клавиатуры выбора мест
def create_seating_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=4)
    keyboard.add(types.KeyboardButton("A"), types.KeyboardButton("B"), types.KeyboardButton("C"), types.KeyboardButton("D"))
    return keyboard

# Создание бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    if chat_id not in users:
        users[chat_id] = {'balance': 0, 'seats': []}
        bot.reply_to(message, "Добро пожаловать! Вы успешно зарегистрированы.")
    else:
        bot.reply_to(message, "Вы уже зарегистрированы.")

# Обработчик команды для пополнения баланса
@bot.message_handler(commands=['topup'])
def topup(message):
    chat_id = message.chat.id
    if chat_id in users:
        users[chat_id]['balance'] += 100  # Пополнение баланса на 100
        bot.reply_to(message, f"Ваш баланс пополнен на 100. Текущий баланс: {users[chat_id]['balance']}")
    else:
        bot.reply_to(message, "Сначала зарегистрируйтесь.")

# Обработчик для бронирования места
@bot.message_handler(func=lambda message: message.text.upper() in ['A', 'B', 'C', 'D'])
def book_seat(message):
    chat_id = message.chat.id
    if chat_id in users:
        if len(users[chat_id]['seats']) < 10:
            users[chat_id]['seats'].append(message.text.upper())
            bot.reply_to(message, f"Место {message.text.upper()} успешно забронировано.")
        else:
            bot.reply_to(message, "Извините, все места уже забронированы.")
    else:
        bot.reply_to(message, "Сначала зарегистрируйтесь.")

# Обработчик команды для просмотра забронированных мест
@bot.message_handler(commands=['viewseats'])
def view_seats(message):
    chat_id = message.chat.id
    if chat_id in users:
        bot.reply_to(message, f"Ваши забронированные места: {', '.join(users[chat_id]['seats'])}")
    else:
        bot.reply_to(message, "Сначала зарегистрируйтесь.")

# Запуск бота
bot.polling()
