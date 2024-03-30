from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

start_buttons = [
    types.KeyboardButton('Места где можно поесть'),
    types.KeyboardButton('Достопримечательности'),
    types.KeyboardButton('Оставить отзыв'), 
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    print(message)
    await message.answer('Привет, я от импени Ош! Чем могу помочь?', reply_markup=start_keyboard)
    
@dp.message_handler(text='Помощь')
async def help(message:types.Message):
    await message.reply(f"{message.from_user.full_name} напишите о своей проблеме")
    
@dp.message_handler(text='Места где можно поесть')
async def mesta(message:types.Message):
    await message.answer('Красивые места в Оше!', reply_markup=start_keyboard)
num_buttons = [
    types.KeyboardButton('Ожак Кебаб'),
    types.KeyboardButton('Дархан'),
    types.KeyboardButton('Маленькая Япония'),
    types.KeyboardButton('назад')
]
num_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*num_buttons)

@dp.message_handler(text='Ожак Кебаб')
async def kebab(message:types.Message):
    print(message)
    await message.answer('''Здравствуй дорогой посетитель, вы попали на сайт OSHFOOD, №1 Сервис доставки в городе Ош:\n

неожиданно пришли гости, и у вас ничего не готово?\n
хотите пообедать в кругу коллег, не покидая стен офиса?\n
опаздываете на работу, не успели позавтракать?\n
пропустили обед, из-за важной встречи?\n
задержались на работе, нужно поужинать, но время уже 20:00?\n
Не беда, ведь именно для таких случаев мы запустили уникальный проект OSHFOOD который позволит вам всегда оставаться в тонусе, быть уверенным и не думать о своем желудке. \nКоманда профессионалов в своем роде, поможет вам в этом. Курьеры сервиса OSHFOOD, доставят вам поесть с любого заведения в городе Ош, при этом сохраняя еду свежей и горячей.''', reply_markup=start_keyboard)

numbers_buttons = [
    types.KeyboardButton('Фотография'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('назад')
]
numbers_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*numbers_buttons)

@dp.message_handler(text='Фотография')
async def foto(message:types.Message):
    await message.answer_photo('https://avatars.mds.yandex.net/get-altay/363317/2a00000186b76ce4d21c90a3d835001ec021/XXL_height')
    await message.answer_photo('https://avatars.mds.yandex.net/get-altay/2809325/2a00000186b76d0fe51b87c34dbd78c0fc1f/XXL_heighthttps://avatars.mds.yandex.net/get-altay/1245631/2a00000185e8f0e23dbc50b9ad5021a8da1c/XXL_height')
    await message.answer_photo('https://avatars.mds.yandex.net/get-altay/1245631/2a00000185e8f0e23dbc50b9ad5021a8da1c/XXL_height')
    
@dp.message_handler(text='Адрес')
async def adres(message:types.Message):
    await message.answer('234، 246 Курманжан-Датка ул., Ош')
    await message.answer_location('40.52700949424018, 72.79547184569559')

@dp.message_handler(text='Дархан')
async def darhan(message:types.Message):
    print(message)
    await message.answer('''Тех кто хочет посетить ресторан «Дархан» в городе Ош по адресу Мияшева, 3а, больше всего интересуют цены и позиции в меню. Все это вы можете узнать несколькими способами:\n

Через официальную группу в социальных сетях;\n
посетив лично;\n
по номеру телефона +996 552-06-70-10;+996 770-03-03-00;\n
на официальном сайте «Дархан».\n
Короткая информация о компании:\n

Юридическое лицо:\n
Рейтинг: (из 5)\n
Раздел: Поесть\n
Короткое описание:\n
Способы оплаты: Наличный расчёт\n
Почтовый индекс:\n
Чтобы получить больше информации о ценах или проведении банкета, перейдите на официальный сайт по ссылке или позвоните по номеру телефона «Дархан» +996 552-06-70-10;+996 770-03-03-00. \nПо телефону вам забронируют столик и ответят на другие интересующие вопросы..''', reply_markup=start_keyboard)

number_buttons = [
    types.KeyboardButton('Фотография'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('назад')
]
number_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*number_buttons)

@dp.message_handler(text='Фотография')
async def foto(message:types.Message):
    await message.answer_photo('https://media.kg/wp-content/uploads/2022/05/studenty-4-of-2-scaled-1.jpg')
    await message.answer_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFZ-YnyaXKS4iwX7ZyQFaQcfMAioZ7930Pt_8Mj0NFV2nCLH-1qIRVOcufAeYWyxkU39A&usqp=CAU')
    await message.answer_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAQRZ1VizP3JKSOORMhSsZQ5vgCEqLpVgjMdufb_4tPZI0KSTs_HVONPsg1AlAWbgLdxw&usqp=CAU')
    
@dp.message_handler(text='Адрес')
async def  adres(message:types.Message):
    await message.answer('3 Абсамат Масалиева, Ош 723500')
    await message.answer_location('40.51439005245567, 72.8159233856207')
    
@dp.message_handler(text="Назад")
async def back(message:types.Message):
    await start(message)

executor.start_polling(dp, skip_updates=True)
    