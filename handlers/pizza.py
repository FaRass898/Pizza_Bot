from aiogram import Router,F, types


pizza_router = Router()

@pizza_router.callback_query(F.data == "pizza")
async def pizza_menu(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="маргарита")
            ],
            [
                types.KeyboardButton(text="Пепперони")
            ],
            [
                types.KeyboardButton(text="Гавайская")
            ],
            [
                types.KeyboardButton(text="Мясная")
            ],
            [
                types.KeyboardButton(text="Четыре сыра")
            ],

        ],

        resize_keyboard=True
    )
    photo = types.FSInputFile("images/pizza.jpg")
    await callback.answer()
    await callback.message.answer_photo(
        photo= photo,
        caption="🍕 **Пицца:**\n"
        "Наши пиццы - это настоящий кулинарный шедевр! "
        "Мы предлагаем широкий выбор разнообразных пицц, "
        "приготовленных с использованием только самых свежих ингредиентов "
        "и любовью к деталям. От классической Маргариты до изысканной Гавайской, "
        "у нас есть пицца на любой вкус и настроение!\n\n"
        "🍕 **Виды пицц:**\n"
        "1. Маргарита - 450сом\n"
        "        Классическая пицца с томатным соусом, сыром моцарелла и свежим базиликом.\n"
        "2. Пепперони - 400сом\n"
        "        Пицца с пикантным пепперони и обильным слоем сыра.\n"
        "3. Гавайская -470сом\n "
        "        Пицца с ветчиной, ананасами и сыром моцарелла.\n"
        "4. Мясная - 460сом\n"
        "        Пицца с ассорти мяса, включая ветчину, пепперони, салями и бекон.\n"
        "5. Четыре сыра - 500сом\n"
        "        Пицца с сочетанием четырех видов сыра: моцарелла, пармезан, горгонзола и рикотта.",
        reply_markup=kb

    )


@pizza_router.message(F.text.lower() == "маргарита")
async def pizza_one(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_margarita"),
                types.InlineKeyboardButton(text="Отмена", callback_data="pizza")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать пиццу Маргарита?", reply_markup=keyboard)


@pizza_router.message(F.text.lower() == "пепперони")
async def pizza_two(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_pepperoni"),
                types.InlineKeyboardButton(text="Отмена", callback_data="pizza")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать пиццу Пепперони?", reply_markup=keyboard)


@pizza_router.message(F.text.lower() == "гавайская")
async def pizza_three(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_hawaiian"),
                types.InlineKeyboardButton(text="Отмена", callback_data="pizza")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать пиццу Гавайская?", reply_markup=keyboard)


@pizza_router.message(F.text.lower() == "мясная")
async def pizza_four(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_meat"),
                types.InlineKeyboardButton(text="Отмена", callback_data="pizza")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать пиццу Мясная?", reply_markup=keyboard)


@pizza_router.message(F.text.lower() == "четыре сыра")
async def pizza_five(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_four_cheese"),
                types.InlineKeyboardButton(text="Отмена", callback_data="pizza")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать пиццу Четыре сыра?", reply_markup=keyboard)
