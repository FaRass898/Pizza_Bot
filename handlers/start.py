from aiogram import Router,F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    photo = types.FSInputFile("images/photo_2024-05-04_20-59-51.jpg")
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Меню', callback_data='menu')
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="/about_us"),
                types.InlineKeyboardButton(text="наш сайт", url="https://ru.wikipedia.org/wiki/Five_Nights_at_Freddy%E2%80%99s")
            ],
            [
                types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/fnafmovie/'),
                types.InlineKeyboardButton(text='Twitter', url='https://twitter.com/FNAFMovie')
            ]
        ]

    )
    await message.answer_photo(
        photo=photo,
        caption=f"**Добро пожаловать {message.from_user.first_name} в Freddy Fazbear's !**\n\n"
                "Приветствуем тебя, друг Фреди! 🍕 Мы рады видеть тебя здесь. В нашей пицерии ты найдешь самые вкусные пиццы, "
                "приготовленные с любовью и заботой, прямо у нас в Фреди Пазбер!\n\n"
                "Не знаешь, что выбрать? Не беспокойся! Наш бот готов помочь тебе с выбором. Просто спроси его о чем-то, "
                "и он подскажет самую идеальную пиццу под твои желания.\n\n"
                "Приятного аппетита и отличного времяпрепровождения в Пазбер Пицерии! 🍴✨\n\n",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "/about_us")
async def about_us(callback: types.CallbackQuery):
    photo = types.FSInputFile("images/about_us.jpg")
    await callback.answer()
    await callback.message.answer_photo(
        photo=photo,
        caption=f"**Добро пожаловать в Freddy Fazbear's !**\n\n"
                "Наша цель в Freddy's — развлекать! Наслаждайтесь приготовленным вручную тестом, замешанным "
                "собственными силами,"
                "с использованием только самых свежих ингредиентов! Здесь единственным ограничением типов начинок для "
                "вашей пиццы является ваше воображение!"
                "Хотите пиццу с шоколадной крошкой и взбитыми сливками? Вы можете иметь один!\n\n"
                "Или, если вы предпочитаете отбросить все притворства, мы также предлагаем десерты, такие как кексы и праздничные торты! "
                "Пока вы наслаждаетесь едой, вас ждет выступление нашей собственной группы: Freddy Fazbear and Friends! "
                "С участием Фредди и его друзей Бонни и Чики.\n\n"
                "Все это и многое другое ждет вас в Freddy Fazbear's Pizza! Расположен в Come on Down, и пусть веселится начинать! Или позвоните нам по телефону:1-800-083"

    )