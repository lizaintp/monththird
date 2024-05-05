from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN
import logging

bot = Bot(TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_inline_buttons = [
    types.InlineKeyboardButton("Русский", callback_data="russhian"),
    types.InlineKeyboardButton("English", callback_data="english"),
]

start_inline_keyboard = types.InlineKeyboardMarkup().add(*start_inline_buttons)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer(f"Привет {message.from_user.first_name}, Вам интересен бренд Chanel? тогда вам к нам. Для начала выберите язык", reply_markup=start_inline_keyboard)

interesting_inline_buttons = [
    types.InlineKeyboardButton("Briefly about the Chanel brand.", callback_data="short_about_chanel"),
    types.InlineKeyboardButton("Chanel clothing", callback_data="clothes_chanel"),
    types.InlineKeyboardButton("Chanel perfumes", callback_data="perfume_chanel"),
    types.InlineKeyboardButton("Chanel Cosmetics", callback_data="cosmetics_chanel")
]

interesting_inline_keyboard = types.InlineKeyboardMarkup().add(*interesting_inline_buttons)

@dp.callback_query_handler(lambda call: call.data == "english")
async def short_about_chanel(callback: types.CallbackQuery):
    await callback.answer("the button works")
    await callback.message.reply("Well.What are you interested in?", reply_markup=interesting_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == "short_about_chanel")
async def short_about_chanel(callback: types.CallbackQuery):
    await callback.answer("the button works")
    await callback.message.reply("Chanel is a French company producing expensive fashion clothing,\nluxury perfumes and cosmetics, jewelry and other luxury goods.\nFounded by fashion designer Coco Chanel in Paris at the beginning of the 20th century.", reply_markup=interesting_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == "clothes_chanel")
async def clothes_chanel(callback: types.CallbackQuery):
    await callback.answer("the button works")
    await callback.message.reply("We provide Chanel brand clothing: ")
    await callback.message.answer_photo("https://www.chanel.com/images/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_682/dress-black-multicolor-tweed-tweed-packshot-default-p77272v68900nw871-9541374214174.jpg")
    await callback.message.answer_photo("https://www.chanel.com/images/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_454/dress-multicolor-glittered-tweed-glittered-tweed-packshot-default-p77273v69002nx086-9541374640158.jpg")
    await callback.message.answer_photo("https://www.chanel.com/images/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_516/dress-ecru-black-pleated-silk-satin-pleated-silk-satin-packshot-default-p77263v27695au739-9541375590430.jpg")
    await callback.message.answer_photo("https://www.chanel.com/images/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_516/dress-pink-navy-blue-white-cotton-wool-tweed-cotton-wool-tweed-packshot-default-p77264v69035nx103-9541372117022.jpg")
    await callback.message.answer_photo("https://www.chanel.com/images/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_516/dress-orange-pink-cotton-tweed-cotton-tweed-packshot-default-p77275v69111nx151-9541374902302.jpg")
    await callback.message.reply("Dresses from the Chanel brand start at $2,000 and up.", reply_markup=interesting_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == "perfume_chanel")
async def perfume_chanel(callback: types.CallbackQuery):
    await callback.answer("the button works")
    await callback.message.reply("We provide Chanel brand perfume: ")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//chance-eau-tendre-eau-de-parfum-spray-3-4fl-oz--packshot-default-126260-9539148546078.jpg")
    await callback.message.answer("CHANCE EAU TENDRE")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//coco-mademoiselle-eau-de-parfum-intense-spray-3-4fl-oz--packshot-default-116660-9539148283934.jpg")
    await callback.message.answer("COCO MADEMOISELLE")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//chance-eau-fraiche-eau-de-toilette-spray-3-4fl-oz--packshot-default-136420-9539148513310.jpg")
    await callback.message.answer("CHANCE EAU FRAÎCHE")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//cristalle-eau-de-parfum-spray-3-4fl-oz--packshot-default-135690-9536314900510.jpg")
    await callback.message.answer("CRISTALLE")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//chance-eau-vive-eau-de-toilette-spray-3-4fl-oz--packshot-default-126560-9539148578846.jpg")
    await callback.message.answer("CHANCE EAU VIVE")
    await callback.message.reply("Chanel brand perfumes start at $80 for 50 milliliters.", reply_markup=interesting_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == "cosmetics_chanel")
async def cosmetics_chanel(callback: types.CallbackQuery):
    await callback.answer("the button works")
    await callback.message.reply("We provide Chanel brand cosmetics: ")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.43,h_0.43,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//roses-coquillage-powder-blush-duo-roses-coquillage-0-31oz--packshot-default-151647-9536301662238.jpg")
    await callback.message.answer("ROSES COQUILLAGE - DOUBLE POWDER BLUSH")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.43,h_0.43,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//baume-essentiel-multi-use-glow-stick-dragee-0-28oz--packshot-default-169055-9516954419230.jpg")
    await callback.message.answer("BAUME ESSENTIEL - MOISTURIZING HIGHLIGHTER STICK FOR FACE, LIPS AND EYES")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//les-beiges-healthy-glow-bronzing-cream-390-soleil-tan-bronze-0-5oz--packshot-default-185514-9542717538334.jpg")
    await callback.message.answer("LES BEIGES - BRONZING CREAM IN TRAVEL FORMAT")
    await callback.message.answer_photo("https://www.chanel.com/images//t_one//w_0.43,h_0.43,c_crop/q_auto:good,f_autoplus,fl_lossy,dpr_1.1/w_840/les-beiges-healthy-glow-foundation-hydration-and-longwear-br32-1fl-oz--packshot-default-184764-9539410886686.jpg")
    await callback.message.answer("LES BEIGES - FOUNDATION WITH A NATURAL RADIANCE EFFECT: HYDRATION AND LASTING.")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.43,h_0.43,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//joues-contraste-powder-blush-64-pink-explosion-0-12oz--packshot-default-168640-9538127036446.jpg")
    await callback.message.answer("JOUES CONTRASTE - POWDER BLUSH")
    await callback.message.reply("Chanel brand cosmetics cost over $30 and up.", reply_markup=interesting_inline_keyboard)


interest_inline_buttons = [
    types.InlineKeyboardButton("Коротко о бренде Шанель.", callback_data="about_chanel"),
    types.InlineKeyboardButton("Одежда от Шанель", callback_data="chanel_clothes"),
    types.InlineKeyboardButton("Парфюмы от Шанель", callback_data="chanel_perfume"),
    types.InlineKeyboardButton("Косметика от Шанель", callback_data="chanel_cosmetics")
]

interest_inline_keyboard = types.InlineKeyboardMarkup().add(*interest_inline_buttons)

@dp.callback_query_handler(lambda call: call.data == "russhian")
async def short_about_chanel(callback: types.CallbackQuery):
    await callback.answer("Кнопка работает")
    await callback.message.reply("Хорошо. Что вас интересует?", reply_markup=interest_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == "about_chanel")
async def short_about_chanel(callback: types.CallbackQuery):
    await callback.answer("Кнопка работает")
    await callback.message.reply("Chanel — французская компания по производству дорогой модной одежды,\nлюксовой парфюмерии и косметики, ювелирных изделий и других предметов роскоши.\nОснована модельером Коко Шанель в Париже в начале XX века.", reply_markup=interest_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == "chanel_clothes")
async def clothes_chanel(callback: types.CallbackQuery):
    await callback.answer("Кнопка работает")
    await callback.message.reply("Мы предоставляем одежду бренда Шанель: ")
    await callback.message.answer_photo("https://www.chanel.com/images/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_682/dress-black-multicolor-tweed-tweed-packshot-default-p77272v68900nw871-9541374214174.jpg")
    await callback.message.answer_photo("https://www.chanel.com/images/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_454/dress-multicolor-glittered-tweed-glittered-tweed-packshot-default-p77273v69002nx086-9541374640158.jpg")
    await callback.message.answer_photo("https://www.chanel.com/images/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_516/dress-ecru-black-pleated-silk-satin-pleated-silk-satin-packshot-default-p77263v27695au739-9541375590430.jpg")
    await callback.message.answer_photo("https://www.chanel.com/images/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_516/dress-pink-navy-blue-white-cotton-wool-tweed-cotton-wool-tweed-packshot-default-p77264v69035nx103-9541372117022.jpg")
    await callback.message.answer_photo("https://www.chanel.com/images/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_516/dress-orange-pink-cotton-tweed-cotton-tweed-packshot-default-p77275v69111nx151-9541374902302.jpg")
    await callback.message.reply("Цены на платья бренда Chanel начинаются от 2000 долларов и выше.", reply_markup=interest_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == "chanel_perfume")
async def perfume_chanel(callback: types.CallbackQuery):
    await callback.answer("Кнопка работает")
    await callback.message.reply("Мы предоставляем парфюмы бренда Шанель: ")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//chance-eau-tendre-eau-de-parfum-spray-3-4fl-oz--packshot-default-126260-9539148546078.jpg")
    await callback.message.answer("CHANCE EAU TENDRE")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//coco-mademoiselle-eau-de-parfum-intense-spray-3-4fl-oz--packshot-default-116660-9539148283934.jpg")
    await callback.message.answer("COCO MADEMOISELLE")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//chance-eau-fraiche-eau-de-toilette-spray-3-4fl-oz--packshot-default-136420-9539148513310.jpg")
    await callback.message.answer("CHANCE EAU FRAÎCHE")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//cristalle-eau-de-parfum-spray-3-4fl-oz--packshot-default-135690-9536314900510.jpg")
    await callback.message.answer("CRISTALLE")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//chance-eau-vive-eau-de-toilette-spray-3-4fl-oz--packshot-default-126560-9539148578846.jpg")
    await callback.message.answer("CHANCE EAU VIVE")
    await callback.message.reply("Стоимость парфюмерии бренда Chanel начинается от 80 долларов за 50 миллилитров.", reply_markup=interest_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == "chanel_cosmetics")
async def cosmetics_chanel(callback: types.CallbackQuery):
    await callback.answer("Кнопка работает")
    await callback.message.reply("Мы предоставляем косметику бренда Шанель: ")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.43,h_0.43,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//roses-coquillage-powder-blush-duo-roses-coquillage-0-31oz--packshot-default-151647-9536301662238.jpg")
    await callback.message.answer("ROSES COQUILLAGE - ДВОЙНЫЕ ПУДРОВЫЕ РУМЯНА.")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.43,h_0.43,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//baume-essentiel-multi-use-glow-stick-dragee-0-28oz--packshot-default-169055-9516954419230.jpg")
    await callback.message.answer("BAUME ESSENTIEL - УВЛАЖНЯЮЩИЙ СТИК-ХАЙЛАЙТЕР ДЛЯ ЛИЦА, ГУБ И ГЛАЗ.")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//les-beiges-healthy-glow-bronzing-cream-390-soleil-tan-bronze-0-5oz--packshot-default-185514-9542717538334.jpg")
    await callback.message.answer("LES BEIGES - БРОНЗИРУЮЩИЙ КРЕМ В ФОРМАТЕ ДЛЯ ПУТЕШЕСТВИЙ.")
    await callback.message.answer_photo("https://www.chanel.com/images//t_one//w_0.43,h_0.43,c_crop/q_auto:good,f_autoplus,fl_lossy,dpr_1.1/w_840/les-beiges-healthy-glow-foundation-hydration-and-longwear-br32-1fl-oz--packshot-default-184764-9539410886686.jpg")
    await callback.message.answer("LES BEIGES - ТОНАЛЬНЫЙ ФЛЮИД С ЭФФЕКТОМ ЕСТЕСТВЕННОГО СИЯНИЯ: УВЛАЖНЕНИЕ И СТОЙКОСТЬ..")
    await callback.message.answer_photo("https://www.chanel.com/images/t_one//w_0.43,h_0.43,c_crop/q_auto:good,f_auto,fl_lossy,dpr_1.1/w_480//joues-contraste-powder-blush-64-pink-explosion-0-12oz--packshot-default-168640-9538127036446.jpg")
    await callback.message.answer("JOUES CONTRASTE - ПУДРОВЫЕ РУМЯНА.")
    await callback.message.reply("Косметика бренда Chanel стоит от 30 долларов и выше.", reply_markup=interest_inline_keyboard)

executor.start_polling(dp, skip_updates=True)