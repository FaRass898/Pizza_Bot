from aiogram import Router, types, F

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

@milkshakes_router.message(F.text.lower() == "фруктовый смузи")
async def fruit_smoothie_order(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_fruit_smoothie"),
                types.InlineKeyboardButton(text="Отмена", callback_data="mocktails_and_milkshakes")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать фруктовый смузи?", reply_markup=keyboard)

@milkshakes_router.message(F.text.lower() == "вишневый фреш")
async def cherry_fresh_order(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_cherry_fresh", ),
                types.InlineKeyboardButton(text="Отмена", callback_data="mocktails_and_milkshakes", )
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать вишневый фреш?", reply_markup=keyboard)


@milkshakes_router.message(F.text.lower() == "клубничный лимонад")
async def strawberry_lemonade_order(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_strawberry_lemonade"),
                types.InlineKeyboardButton(text="Отмена", callback_data="mocktails_and_milkshakes")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать клубничный лимонад?", reply_markup=keyboard)

@milkshakes_router.message(F.text.lower() == "ванильный")
async def vanilla_milkshake_order(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_vanilla_milkshake"),
                types.InlineKeyboardButton(text="Отмена", callback_data="mocktails_and_milkshakes")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать ванильный молочный коктейль?", reply_markup=keyboard)

@milkshakes_router.message(F.text.lower() == "шоколадный")
async def chocolate_milkshake_order(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_chocolate_milkshake"),
                types.InlineKeyboardButton(text="Отмена", callback_data="mocktails_and_milkshakes")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать шоколадный молочный коктейль?", reply_markup=keyboard)

@milkshakes_router.message(F.text.lower() == "клубничный")
async def strawberry_milkshake_order(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_strawberry_milkshake"),
                types.InlineKeyboardButton(text="Отмена", callback_data="mocktails_and_milkshakes")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать клубничный молочный коктейль?", reply_markup=keyboard)
