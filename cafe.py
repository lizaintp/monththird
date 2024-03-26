from aiogram import Bot, Dispatcher, types, executor
from config import token
import logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    print(message)
    await message.answer(f"Здравствуйте {message.from_user.first_name},\nЧто желаете? /help")

help_buttons = [
    types.KeyboardButton("О нас"),
    types.KeyboardButton("Меню"),
    types.KeyboardButton("Адрес"),
    types.KeyboardButton("Заказать еду")
]

help_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*help_buttons)

@dp.message_handler(commands="help")
async def help(message:types.Message):
    await message.answer(f"{message.from_user.first_name}, чего желаете", reply_markup=help_keyboard)

@dp.message_handler(text="О нас")
async def about_us(mesage:types.Message):
    await mesage.reply("Сеть ресторанов в турецкой кухне 'Ожак Кебап'.\nМы являемся динамично развиваюшейся,\nа так же крупнейшей сетью турецкой кухни на территории Средней Азии")

menu_buttons = [
    types.KeyboardButton("Завтраки"),
    types.KeyboardButton("Салаты"),
    types.KeyboardButton("Супы"),
    types.KeyboardButton("Кебабы"),
    # types.KeyboardButton("Новые блюда"),
    types.KeyboardButton("Пиццы"),
    # types.KeyboardButton("Детские блюда"),
    types.KeyboardButton("Дессерты"),
    types.KeyboardButton("Напитки"),
    types.KeyboardButton("Назад")
]

menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*menu_buttons)

@dp.message_handler(text="Меню")
async def menu(mesage:types.Message):
    await mesage.reply("Предоставляем вам наше меню", reply_markup=menu_keyboard)

breakfast_buttons = [
    types.KeyboardButton("Омлет с сыром"),
    types.KeyboardButton("Менемен"),
    types.KeyboardButton("Турецкий завтрак на две персоны"),
    types.KeyboardButton("Турецкий завтрак на четыре персоны"),
    types.KeyboardButton("Назад")
]

breakfast_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*breakfast_buttons)

@dp.message_handler(text="Завтраки")
async def breakfast(message:types.Message):
    await message.reply("Вот наши завтраки", reply_markup=breakfast_keyboard)

@dp.message_handler(text="Омлет с сыром")
async def omelet_with_cheese(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e12dcb1966.png")
    await message.reply("Омлет с сыром. Цена: 150 грамм - 200 сом")

@dp.message_handler(text="Менемен")
async def menemen(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cb73990a998.jpg")
    await message.reply("Менемен. Цена: 200 грамм - 250 сом")

@dp.message_handler(text="Турецкий завтрак на две персоны")
async def breakfast_for_2_person(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/643781e3ec568.png")
    await message.reply("Турецкий завтрак на две персоны. Цена: 750 сом")

@dp.message_handler(text="Турецкий завтрак на четыре персоны")
async def breakfast_for_4_person(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e12a1024a6.png")
    await message.reply("Турецкий завтрак на четыре персоны. Цена: 1300 сом")

salads_buttons = [
    types.KeyboardButton("Шакшука"),
    types.KeyboardButton("Микс салат с булгуром"),
    types.KeyboardButton("Чобан салат"),
    types.KeyboardButton("Греческий салат"),
    types.KeyboardButton("Цезарь с курицей"),
    types.KeyboardButton("Свежий салат"),
    types.KeyboardButton("Назад")
]

salads_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*salads_buttons)

@dp.message_handler(text="Салаты")
async def salads(message:types.Message):
    await message.reply("Вот наши салаты", reply_markup=salads_keyboard)

@dp.message_handler(text="Шакшука")
async def shakshuka(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/60f0fbd44dbf7.jpg")
    await message.reply(" Шакшука. Цена: 200 грамм - 220 сом")

@dp.message_handler(text="Микс салат с булгуром")
async def bulgur_salad(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64376eb853cc6.png")
    await message.reply("Микс салат с булгуром. Цена: 300 сом")


@dp.message_handler(text="Чобан салат")
async def choban_salad(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64376d78ef30a.png")
    await message.reply("Чобан салат. Цена: 250 грамм - 250 сом")


@dp.message_handler(text="Греческий салат")
async def greek_salad(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e0763eefe7.png")
    await message.reply("Греческий салат. Цена: 300 грамм -280 сом")


@dp.message_handler(text="Цезарь с курицей")
async def caesar_in_chicken(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64376ff61172e.png")
    await message.reply("Цезарь с курицей. Цена: 300 грамм - 360 сом")

@dp.message_handler(text="Свежий салат")
async def fresh_salad(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc7fb422f9a.png")
    await message.reply("Свежий салат. Цена: 200 грамм - 250 сом")


soup_buttons = [
    types.KeyboardButton("Чечевичный суп"),
    types.KeyboardButton("Келле пача"),
    types.KeyboardButton("Куриный суп лапша"),
    types.KeyboardButton("Ишкембе"),
    types.KeyboardButton("Назад")
]

soup_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*soup_buttons)

@dp.message_handler(text="Супы")
async def soup(message:types.Message):
    await message.reply("Вот наши супы", reply_markup=soup_keyboard)

@dp.message_handler(text="Чечевичный суп")
async def lentil_soup(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc80550ff25.png")
    await message.reply("Чечевичный суп. Цена: 200 грамм - 170 сом, 300 грамм - 260 сом")

@dp.message_handler(text="Келле пача")
async def kelle_pacha(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e105b439ce.png")
    await message.reply("Келле пача. Цена: 300 грамм - 230 сом")

@dp.message_handler(text="Куриный суп лапша")
async def chicken_noodle_soup(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e11e5b44d6.png")
    await message.reply("Куриный суп лапша. Цена: 300 грамм - 170 сом")

@dp.message_handler(text="Ишкембе")
async def ishkembe(message:types.Message):
    # await message.reply_photo("https://dostavka312.kg/public/public/photo/636e0d1f44fa0.png")  #выходит ошибка
    await message.reply("Ишкембе. Цена: 250 грамм - 230 сом")

kebab_buttons = [
    types.KeyboardButton("Урфа"),
    types.KeyboardButton("Шашлык из баранины"),
    types.KeyboardButton("Бейти сарма"),
    types.KeyboardButton("Тавук донер"),
    types.KeyboardButton("Патлыжан кебаб"),
    types.KeyboardButton("Крылышки на мангале"),
    types.KeyboardButton("Форель на мангале"),
    types.KeyboardButton("Искендер"),
    types.KeyboardButton("Чоп шиш"),
    types.KeyboardButton("Назад")
]

kebab_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*kebab_buttons)

@dp.message_handler(text="Кебабы")
async def kebab(message:types.Message):
    await message.reply("Вот наши кебабы",reply_markup=kebab_keyboard)

@dp.message_handler(text="Урфа")
async def urfa(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc8136883d8.jpg")
    await message.reply("Урфа. Цена: 400 грамм - 420 сом")

@dp.message_handler(text="Шашлык из баранины")
async def lamb_kebab(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e1b2ee0c13.png")
    await message.reply("Шашлык из баранины. Цена: 450 грамм - 450 сом")

@dp.message_handler(text="Бейти сарма")
async def beyti_sarma(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e1cffb9752.png")
    await message.reply("Бейти сарма. Цена: 400 грамм - 450 сом")

@dp.message_handler(text="Тавук донер")
async def tavuk_doner(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e1d75f2a08.png")
    await message.reply("Тавук донер. Цена: 400 грамм - 420 сом")

@dp.message_handler(text="Патлыжан кебаб")
async def patlyjan_kebab(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e19257c301.png")
    await message.reply("Патлыжан кебаб. Цена: 450 грамм - 500 сом")

@dp.message_handler(text="Крылышки на мангале")
async def trout_jn_the_grill(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cb768995278.jpg")
    await message.reply("Крылышки на мангале. Цена: 450 грамм - 400 сом")


@dp.message_handler(text="Форель на мангале")
async def wings_on_the_grill(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cb76ec31c14.jpg")
    await message.reply("Форель на мангале. Цена: 900 грамм - 1100 сом")

@dp.message_handler(text="Искендер")
async def iskender(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e1495c5693.png")
    await message.reply("Искендер. Цена: 450 грамм - 480 сом")

@dp.message_handler(text="Чоп шиш")
async def chop_shish(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/636e21f4716df.png")
    await message.reply("Чоп шиш. Цена: 400 грамм - 400 сом")

pizza_buttons = [
    types.KeyboardButton("Донер пицца с курицей"),
    types.KeyboardButton("Маргарита"),
    types.KeyboardButton("Пепперони"),
    types.KeyboardButton("Ассорти"),
    types.KeyboardButton("Донер пицца с говядиной"),
    types.KeyboardButton("Пиде с мясом и сыром"),
    types.KeyboardButton("Пиде с колбасой"),
    types.KeyboardButton("Пиде с сыром"),
    types.KeyboardButton("Лахмаджун"),
    types.KeyboardButton("Назад")
]

pizza_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*pizza_buttons)

@dp.message_handler(text="Пиццы")
async def pizza(message:types.Message):
    await message.reply("Вот наши пиццы", reply_markup=pizza_keyboard)

@dp.message_handler(text="Донер пицца с курицей")
async def chicken_pizza(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc6ecc14bc9.jpg")
    await message.reply("Донер пицца с курицей. Цена: 430 грамм - 450 сом, 680 грамм - 650 сом")

@dp.message_handler(text="Маргарита")
async def margarita(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc6da7638d8.jpg")
    await message.reply("Маргарита. Цена: 440 грамм - 450 сом")

@dp.message_handler(text="Пепперони")
async def pepperoni(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc717cb2610.jpg")
    await message.reply("Пепперони. Цена: 410 грамм - 450 сом, 690 грамм - 650 сом")

@dp.message_handler(text="Ассорти")
async def assorti(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc6fa2878de.jpg")
    await message.reply("Ассорти. Цена: 430 грамм - 450 сом")

@dp.message_handler(text="Донер пицца с говядиной")
async def beef_pizza(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc7094d273c.jpg")
    await message.reply("Донер пицца с говядиной. Цена: 430 грамм - 450 сом, 730 грамм - 650 сом")

@dp.message_handler(text="Пиде с мясом и сыром")
async def pide_with_meat(message:types.Message):
    # await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc6bdd3a381.jpg") #выходит ошибка
    await message.reply("Пиде с мясом и сыром. Цена: 350 грамм - 410 сом")

@dp.message_handler(text="Пиде с колбасой")
async def pide_with_sausage(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc6b8b3b819.jpg")
    await message.reply("Пиде с колбасой. Цена: 350 грамм - 390 сом")

@dp.message_handler(text="Пиде с сыром")
async def pide_with_cheese(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc6b713000a.jpg")
    await message.reply("Пиде с сыром. Цена: 310 грамм - 370 сом")

@dp.message_handler(text="Лахмаджун")
async def lahmajun(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc6ce686fca.jpg")
    await message.reply("Лахмаджун. Цена: 200 грамм - 220 сом")

dessert_buttons = [
    types.KeyboardButton("Султач"),
    types.KeyboardButton("Шоколадный бисквит"),
    types.KeyboardButton("Баклава 0,5(Пахлава)"),
    types.KeyboardButton("Баклава (Пахлава)"),
    types.KeyboardButton("Назад")
]

dessert_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*dessert_buttons)

@dp.message_handler(text="Дессерты")
async def dessert(message:types.Message):
    await message.reply("Вот наши дессерты", reply_markup=dessert_keyboard)

@dp.message_handler(text="Султач")
async def sultach(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc7aeb0cd18.jpg")
    await message.reply("Султач. Цена: 150 грамм - 180 сом")

@dp.message_handler(text="Шоколадный бисквит")
async def chocolate_sponge_cake(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc798073fb4.jpg")
    await message.reply("Шоколадный бисквит. Цена: 150 грамм - 180 сом")

@dp.message_handler(text="Баклава 0,5(Пахлава)")
async def baklava(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc799e4e35d.jpg")
    await message.reply("Баклава 0,5(Пахлава). Цена: 120 сом")

@dp.message_handler(text="Баклава (Пахлава)")
async def baklava(message:types.Message):
    await message.reply_photo("https://dostavka312.kg/public/public/photo/64cc799e4e35d.jpg")
    await message.reply("Баклава (Пахлава). Цена: 190 сом")

drinks_buttons = [
    types.KeyboardButton("Coca-Cola"),
    types.KeyboardButton("Fanta"),
    types.KeyboardButton("Bon Aqua"),
    types.KeyboardButton("Sprite"),
    types.KeyboardButton("Компот"),
    types.KeyboardButton("Назад")
]

drinks_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*drinks_buttons)

@dp.message_handler(text="Напитки")
async def drinks(message:types.Message):
    await message.reply("Вот наши напитки", reply_markup=drinks_keyboard)

@dp.message_handler(text="Coca-Cola")
async def сoca_сola(message:types.Message):
    await message.reply("Coca-Cola. Цена: 1 литр - 130 сом")

@dp.message_handler(text="Fanta")
async def fanta(message:types.Message):
    await message.reply("Fanta. Цена: 1 литр - 130 сом")

@dp.message_handler(text="Bon Aqua")
async def bon_aqua(message:types.Message):
    await message.reply("Bon Aqua. Цена: 1 литр - 70 сом")

@dp.message_handler(text="Sprite")
async def sprite(message:types.Message):
    await message.reply("Sprite. Цена: 1 литр - 130 сом")

@dp.message_handler(text="Компот")
async def compote(message:types.Message):
    await message.reply("Компот. Цена: 1 литр - 100 сом")

@dp.message_handler(text="Адрес")
async def address(message:types.Message):
    await message.reply_location(40.526560023729495, 72.79538783166309)
    await message.reply("улица Курманжан-Датка, Ош")




# class OrderFoodState(StatesGroup):
#     name = State()
#     title = State()
#     phone_number = State()
#     address = State()


# @dp.message_handler(text='Заказать еду')
# async def ordes(message:types.Message):
#     await message.answer('Введите ваше имя')
#     await OrderFoodState.name.set()


# @dp.message_handler(state=OrderFoodState.name)
# async def processtitle(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text

#     await message.answer("Что хотите заказать?")
#     await OrderFoodState.next()

# @dp.message_handler(state=OrderFoodState.title)
# async def process_food(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['title'] = message.text

#     await message.answer("Введите свой номер телефона")
#     await OrderFoodState.next() 
    
    
# @dp.message_handler(state=OrderFoodState.phone_number)
# async def process(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['phone_number'] = message.text

#     await message.answer("Введите свой адрес")
#     await OrderFoodState.next()


# @dp.message_handler(state=OrderFoodState.address)
# async def food_title(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['address'] = message.text


#     async with state.proxy() as data:
#         name = data['name']
    #     title = data['title']
    #     phone_number = data['phone_number']
    #     address = data['address']

    # cursor.execute('''
    #     INSERT INTO orders (name, title, phone_number, address )
    #     VALUES (?, ?, ?, ?)
    # ''', (name, title, phone_number, address))
    # connection.commit()
    # await message.answer("Ваш заказ принять.\nОн когда нибудь приедит")
    # await state.finish()








# @dp.message_handler(text="Заказать еду")
# async def order(message:types.Message):
#   await message.reply("Выберите что хотите заказать", reply_markup=menu_keyboard)
#   if

# @dp.message_handler(text="Ишкембе")
# async def ishkembe(message:types.Message):
#     await message.reply_photo("")
#     await message.reply("Ишкембе. Цена: 250 грамм - 230 сом")

@dp.message_handler()
async def back(message:types.Message):
    await help(message)

@dp.message_handler()
async def not_found(message:types.Message):
    await message.answer("Я вас не понимаю")

executor.start_polling(dp)