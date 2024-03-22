# import sqlite3
# def create_connection(db_name):
#     connection = sqlite3.connect(db_name)
#     return connection

# create_connection("bmw.db")

# def create_table(conn, sql):
#     cursor = conn.cursor()
#     cursor.execute(sql)

# def create_bmw(conn, bmw: tuple):
#     sql = """ INSERT INTO car
#     (model, price , guarantee)
#     VALUES(?, ?, ?);"""
#     cursor = conn.cursor()
#     cursor.execute(sql,bmw)
#     conn.commit()

# sql_create_table = """
# CREATE TABLE IF NOT EXISTS car(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# model TEXT NOT NULL,
# price INTEGER NOT NULL,
# guarantee TEXT NOT NULL
# );"""

# connection = create_connection("bmw.db")
# if connection:
#     print('успешное подключение')
#     create_table(connection, sql_create_table)
#     create_bmw(connection,("BMW i5", 10213877, "100 лет"))
#     create_bmw(connection,("BMW 5", 7200000, "100 лет"))
#     create_bmw(connection,("BMW X4", 5700000, "100 лет"))
#     create_bmw(connection,("BMW M", 11450000, "100 лет"))

from aiogram import Bot, Dispatcher, types, executor
from config import token
import logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    print(message)
    await message.answer(f"Здравствуйте {message.from_user.first_name},\nЧто желаете? /help" )


help_buttons = [
    types.KeyboardButton("Модели автомобилей"),
    types.KeyboardButton("Цены"),
    types.KeyboardButton("Характеристика"),
    types.KeyboardButton("Доступные предложения")
]

help_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*help_buttons)


@dp.message_handler(commands="help")
async def help(message:types.Message):
    await message.reply(f"{message.from_user.full_name} предоставляем вам выбор: ", reply_markup=help_keyboard)
car_model_buttons = [
    types.KeyboardButton("BMW i5"),
    types.KeyboardButton("BMW 5"),
    types.KeyboardButton("BMW X4"),
    types.KeyboardButton("BMW M"),
    types.KeyboardButton("Назад")
]

car_model_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*car_model_buttons)

@dp.message_handler(text="Модели автомобилей")
async def car_model(message:types.Message):
    await message.reply(f"Вот модели автомобилей:", reply_markup=car_model_keyboard)


@dp.message_handler(text="BMW i5")
async def bmw_i5(message:types.Message):
    await message.reply("Это модель BMW i5")
    await message.reply_photo("https://bmw.scene7.com/is/image/BMW/P001_FB-1_G60-8135_Ext_Dsk_v001?qlt=80&wid=1024&fmt=webp")
    await message.reply_photo("https://di-uploads-pod25.dealerinspire.com/bmwtoronto/uploads/2023/08/P90505514_highRes_the-new-bmw-i5-m60-x.jpg")

@dp.message_handler(text="BMW 5")
async def bmw_5(message:types.Message):
    await message.reply("Это модель BMW 5")
    await message.reply_photo("https://s0.rbk.ru/v6_top_pics/resized/1005xH/media/img/4/87/755905683400874.jpg")
    await message.reply_photo("https://s0.rbk.ru/v6_top_pics/media/img/3/98/346849262273983.jpg")

@dp.message_handler(text="BMW X4")
async def bmw_x4(message:types.Message):
    await message.reply("Это модель BMW X4")
    await message.reply_photo("https://hips.hearstapps.com/hmg-prod/images/2022-bmw-x4-m40i-101-1623176654.jpg?crop=0.577xw:0.645xh;0.319xw,0.281xh&resize=768:*")
    await message.reply_photo("https://www.timesherald.com/wp-content/uploads/migration/2020/03/43f4563a15d3ab05d3855e5b54b5ab66.jpg?w=1024")

@dp.message_handler(text="BMW M")
async def bmw_m(message:types.Message):
    await message.reply("Это модель BMW M")
    await message.reply_photo("https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/series-overview/bmw-m-series-seo-overview-ms-08.jpg")
    await message.reply_photo("https://carexpert.ru/img/int1200/bmw5i20m5-01.jpg")


price_buttons = [
    types.KeyboardButton("Цена BMW i5"),
    types.KeyboardButton("Цена BMW 5"),
    types.KeyboardButton("Цена BMW X4"),
    types.KeyboardButton("Цена BMW M"),
    types.KeyboardButton("Назад")
]

price_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*price_buttons)

@dp.message_handler(text="Цены")
async def price(message:types.Message):
    await message.reply(f"Вот цены:", reply_markup=price_keyboard)

@dp.message_handler(text="Цена BMW i5")
async def bmw_1(message:types.Message):
    await message.reply("Цена BMW i5: от 10.213.877 рублей")

@dp.message_handler(text="Цена BMW 5")
async def bmw_2(message:types.Message):
    await message.reply("Цена BMW 5: от 7.200.000 рублей")

@dp.message_handler(text="Цена BMW X4")
async def bmw_3(message:types.Message):
    await message.reply("Цена BMW X4: 5.700.000 рублей")

@dp.message_handler(text="Цена BMW M")
async def bmw_4(message:types.Message):
    await message.reply("Цена BMW M: от 11.450.000 рублей")


characteristic_buttons = [
    types.KeyboardButton("Характеристика BMW i5"),
    types.KeyboardButton("Характеристика BMW 5"),
    types.KeyboardButton("Характеристика BMW X4"),
    types.KeyboardButton("Характеристика BMW M"),
    types.KeyboardButton("Назад")
]

characteristic_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*characteristic_buttons)

@dp.message_handler(text="Характеристика")
async def characteristic(message:types.Message):
    await message.reply(f"Вот характеристики машин:", reply_markup=characteristic_keyboard)

@dp.message_handler(text="Характеристика BMW i5")
async def bmw_1(message:types.Message):
    await message.reply("""BMW i5 - это электрический автомобиль, выпущенный компанией BMW. В настоящее время в 2024 году BMW i5 все еще находится в стадии разработки, и конкретные технические характеристики могут быть представлены только предварительно на основе ожиданий и планов производителя. Однако, мы можем предположить некоторые возможные основные параметры и характеристики, которые могут соответствовать ожиданиям для электромобиля как BMW i5:
1. **Дальность хода**: Ожидается, что BMW i5 будет иметь достаточно большую дальность хода на одном заряде, вероятно в районе 400-500 км в соответствии с современными стандартами электромобилей.
2. **Силовая установка**: Вероятно, BMW i5 будет оснащен мощным электрическим двигателем или комбинацией двигателей, обеспечивающих устойчивую производительность и динамику.
3. **Скорость зарядки**: Будет важным аспектом знать скорость зарядки BMW i5. Система быстрой зарядки может позволить зарядить аккумулятор автомобиля до определенного уровня всего за несколько минут.
4. **Технологии безопасности и управления**: Ожидается, что BMW i5 будет оснащен передовыми технологиями в области безопасности вождения и управления, такими как автопилот или адаптивный круиз-контроль.
5. **Дизайн и комфорт**: BMW i5, скорее всего, будет иметь стильный и современный дизайн, а также высокий уровень комфорта в салоне.
Именно конечные характеристики BMW i5 будут зависеть от решений разработчиков и технологий, которые будут использованы на момент его выпуска на рынок.""")

@dp.message_handler(text="Характеристика BMW 5")
async def bmw_2(message:types.Message):
    await message.reply("""BMW 5 Series – это представитель среднего класса бизнес-седанов, выпускаемый немецким автопроизводителем BMW с 1972 года. Вот некоторые характеристики BMW 5 Series:
1. Дизайн: Стильный и элегантный внешний вид, характерный для немецких автомобилей высокого класса.
2. Двигатели: BMW 5 Series предлагает широкий выбор бензиновых и дизельных двигателей различной мощности и экономичности.
3. Динамика и комфорт: Отличная управляемость и динамика, что делает езду на BMW 5 Series комфортной и увлекательной.
4. Технологии: Все последние технологии и инновации в области безопасности, комфорта и развлечений доступны в BMW 5 Series.
5. Интерьер: Просторный и роскошный интерьер с высококачественными материалами, обилием опций и современным дизайном.
6. Опции и оборудование: BMW 5 Series предлагает широкий спектр дополнительного оборудования и опций, позволяющих настроить автомобиль под свои потребности.
7. Престиж: BMW 5 Series является символом роскоши, статуса и успеха, что делает его популярным среди бизнесменов и успешных людей.
В целом, BMW 5 Series сочетает в себе спортивный дух, комфорт и роскошь, делая его одним из лучших выборов в сегменте бизнес-седанов.""")

@dp.message_handler(text="Характеристика BMW X4")
async def bmw_3(message:types.Message):
    await message.reply("""BMW X4 - это популярный компактный кроссовер от немецкого производителя BMW, который сочетает в себе спортивный стиль и функциональность SUV. Вот некоторые основные характеристики модели BMW X4:
1. Двигатели: BMW X4 доступен с различными типами двигателей, включая бензиновые и дизельные версии. Мощность двигателей может варьироваться в зависимости от конкретной модификации.
2. Дизайн: BMW X4 имеет динамичный и спортивный дизайн, с плавными линиями и выразительным силуэтом. Он представляет собой кроссовер купе, что придает ему особый стиль.
3. Комфорт и технологии: В салоне BMW X4 используются высококачественные материалы, а также передовые технологии, такие как навигационная система, система адаптивного круиз-контроля, система помощи при парковке и другие. 
4. Динамичность и управляемость: BMW X4 отличается отличной динамикой и управляемостью, что делает его увлекательным для вождения как по городским улицам, так и за пределами города.
5. Безопасность: BMW X4 оборудован различными системами безопасности, включая систему контроля давления в шинах, систему предотвращения столкновений, систему помощи при движении в пробках и другие.
6. Вместимость: В салоне BMW X4 предоставляется достаточно места как для пассажиров, так и для груза, благодаря складывающимся задним сиденьям.
В целом, BMW X4 является привлекательным выбором для тех, кто ищет современный кроссовер с высокой производительностью, стильным дизайном и передовыми технологиями.""")

@dp.message_handler(text="Характеристика BMW M")
async def bmw_4(message:types.Message):
    await message.reply("""BMW M - это подразделение компании BMW, специализирующееся на спортивных автомобилях высшего класса. Основные параметры, которые характеризуют модели BMW M, включают в себя:
1. Мощность: Автомобили BMW M обладают высокой мощностью благодаря спортивным двигателям. Мощность может варьироваться в зависимости от конкретной модели, но часто она превышает 400 лошадиных сил.
2. Динамика: BMW M автомобили обладают отличной динамикой и динамическими характеристиками. Они способны разгоняться до 100 км/ч за считанные секунды.
3. Шасси и подвеска: BMW M модели оснащены спортивной подвеской, способной обеспечить отличное управление и устойчивость на дороге даже при высоких скоростях.
4. Дизайн: BMW M автомобили имеют спортивный и агрессивный дизайн, характерный для машин этого класса. Особое внимание уделяется деталям и аэродинамике.
5. Технологии и инновации: BMW M модели обычно оснащены передовыми технологиями и инновациями в области автомобильной индустрии. Это может включать в себя электронные системы управления, интеллектуальные ассистенты и т.д.
6. Эксклюзивность: BMW M автомобили представляют собой эксклюзивные модели, которые призваны удовлетворять запросы требовательных клиентов, желающих комбинировать спортивные характеристики с роскошью и комфортом.
В целом, BMW M модели отличаются высоким качеством исполнения, спортивными характеристиками и инновационными решениями, делая их популярными среди автолюбителей и энтузиастов спортивных автомобилей.""")


providing_buttons = [
    types.KeyboardButton("Гарантия"),
    types.KeyboardButton("Тест драйв"),
    types.KeyboardButton("Какую машину выбрать"),
    types.KeyboardButton("Назад")
]

providing_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*providing_buttons)

@dp.message_handler(text="Доступные предложения")
async def providing(message:types.Message):
    await message.reply("Доступные предложения:", reply_markup=providing_keyboard)

@dp.message_handler(text="Гарантия")
async def gaurantee(message:types.Message):
    await message.reply("""Гарантийное письмо
Компания Элиза, гарантирует, что новый автомобиль продается с полной гарантией на следующих условиях:
1. Продолжительность гарантии: Гарантия автомобиля распространяется на 1000 лет, считая от даты покупки автомобиля.
2. Техническое обслуживание: Автомобиль гарантируется в случае регулярного технического обслуживания и проведения работ только у официальных дилеров или авторизованных центров обслуживания.
3. Диапазон гарантии: Гарантия распространяется на все неисправности, вызванные дефектами материалов или производственными ошибками в течение срока действия гарантии.
4. Исключения: Гарантия не распространяется на случаи повреждений, вызванные неправильной эксплуатацией, авариями, естественным износом, внешними воздействиями или проведением обслуживания несанкционированными специалистами.
5. Процедура заявления гарантии: Покупатель должен немедленно уведомить официального дилера в случае выявления неисправностей и предоставить все необходимые документы для рассмотрения гарантийного случая.
6. Решение по гарантии: Компания Элиза оставляет за собой право либо провести ремонт, замену компонентов или замену автомобиля в случае неисправностей, подпадающих под гарантию.
7. Дополнительные условия: Дополнительные условия гарантии могут быть оговорены в отдельных документах или соглашениях.
Данная гарантия распространяется только на первого владельца и действительна при соблюдении всех условий и требований, изложенных в данном документе.""")


@dp.message_handler(text="Тест драйв")
async def test(message:types.Message):
    await message.reply("Хотите пройти тест-драйв?\nНапишите нам, и мы устроим незабываемый опыт вождения!\nНаш телеграм:@lizaintpp ")

@dp.message_handler(text="Какую машину выбрать")
async def choice(message:types.Message):
    await message.reply("Нами вам было предоставлено BMW самых разных видов и доступных цен. Советуем ориентироваться на ваше финансовое положение и на ваши желания.")

@dp.message_handler()
async def back(message:types.Message):
    await start(message)

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял")

executor.start_polling(dp)