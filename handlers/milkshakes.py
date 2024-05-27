from aiogram import Router, types, F
from aiogram.handlers import MessageHandler

milkshakes_router = Router()


@milkshakes_router.callback_query(F.data == "milkshakes")
async def mocktails_and_milkshakes_menu(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Фруктовый смузи")
            ],
            [
                types.KeyboardButton(text="Вишневый фреш")
            ],
            [
                types.KeyboardButton(text="Клубничный лимонад")
            ],
            [
                types.KeyboardButton(text="Ванильный")
            ],
            [
                types.KeyboardButton(text="Шоколадный")
            ],
            [
                types.KeyboardButton(text="Клубничный")
            ]
        ],
        resize_keyboard=True
    )
    photo = types.FSInputFile("images/mocktails_and_milkshakes.jpg")
    await callback.answer()
    await callback.message.answer_photo(
        photo=photo,
        caption="🍹 **Детские коктейли и молочные коктейли:**\n"
        "Наши напитки - это отличное сочетание вкуса и качества! "
        "От фруктового смузи до нежного ванильного молочного коктейля, "
        "мы предлагаем широкий выбор напитков для каждого вкуса и настроения!\n\n"
        "🍹 **Виды детских коктейлей:**\n"
        "1. Фруктовый смузи - 250сом\n"
        "        Смесь свежих фруктов и йогурта, приготовленная в виде освежающего напитка.\n"
        "2. Вишневый фреш - 200сом\n"
        "        Сочный фреш из спелых вишен с добавлением лимонного сока.\n"
        "3. Клубничный лимонад - 180сом\n"
        "        Легкий и освежающий напиток на основе свежей клубники и лимонада.\n\n"
        "🥤 **Виды молочных коктейлей:**\n"
        "1. Ванильный - 280сом\n"
        "        Кремовый коктейль с нежным ванильным вкусом.\n"
        "2. Шоколадный - 300сом\n"
        "        Изысканный коктейль с натуральным какао и молоком.\n"
        "3. Клубничный - 320сом\n"
        "        Ароматный коктейль с натуральными клубничными ягодами.\n",
        reply_markup=kb
    )

milkshakes_types = ("Фруктовый смузи","Вишневый фреш","Клубничный лимонад","Ванильный","Шоколадный","Клубничный")

@milkshakes_router.message(F.text.lower().in_(milkshakes_types))
async def milkshakes_order(message: types.Message):
    milkshakes = message.text
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_fruit_smoothie"),
                types.InlineKeyboardButton(text="Отмена", callback_data="mocktails_and_milkshakes")
            ]
        ]
    )
    await message.answer(f"Хотели бы вы заказать {milkshakes}?", reply_markup=keyboard)


