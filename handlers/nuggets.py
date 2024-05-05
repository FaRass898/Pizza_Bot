from aiogram import Router, types, F

nuggets_router = Router()


@nuggets_router.callback_query(F.data == "nuggets")
async def wings_menu(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Острые")
            ],
            [
                types.KeyboardButton(text="Барбекю")
            ],
            [
                types.KeyboardButton(text="Терияки")
            ],
            [
                types.KeyboardButton(text="Чесночные")
            ]
        ],
        resize_keyboard=True
    )
    photo = types.FSInputFile("images/chicken_wings.jpg")
    await callback.answer()
    await callback.message.answer_photo(
        photo=photo,
        caption="🍗 **Куриные крылья:**\n"
        "Наши куриные крылья - это отличный выбор для закуски или основного блюда! "
        "Мы приготавливаем их из свежих куриных крыльев и приправляем различными соусами, "
        "чтобы удовлетворить даже самых взыскательных гурманов.\n\n"
        "🍗 **Виды куриных крыльев:**\n"
        "1. Острые - 350сом\n"
        "        Куриные крылья, обжаренные в острой приправе, приготовленной по нашему секретному рецепту.\n"
        "2. Барбекю - 380сом\n"
        "        Куриные крылья, запеченные с соусом барбекю, придающим им богатый и насыщенный вкус.\n"
        "3. Терияки - 400сом\n"
        "        Куриные крылья, маринованные в соусе терияки и обжаренные до золотистой корочки.\n"
        "4. Чесночные - 370сом\n"
        "        Куриные крылья, запеченные с ароматным чесноком и специями.\n",
        reply_markup=kb
    )


@nuggets_router.message(F.text.lower() == "острые")
async def wings_spicy(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_spicy_wings"),
                types.InlineKeyboardButton(text="Отмена", callback_data="wings")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать острые куриные крылья?", reply_markup=keyboard)


@nuggets_router.message(F.text.lower() == "барбекю")
async def wings_bbq(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_bbq_wings"),
                types.InlineKeyboardButton(text="Отмена", callback_data="wings")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать куриные крылья с соусом барбекю?", reply_markup=keyboard)


@nuggets_router.message(F.text.lower() == "терияки")
async def wings_teriyaki(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_teriyaki_wings"),
                types.InlineKeyboardButton(text="Отмена", callback_data="wings")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать куриные крылья в соусе терияки?", reply_markup=keyboard)


@nuggets_router.message(F.text.lower() == "чесночные")
async def wings_garlic(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_garlic_wings"),
                types.InlineKeyboardButton(text="Отмена", callback_data="wings")
            ]
        ]
    )
    await message.answer("Хотели бы вы заказать куриные крылья с чесночным соусом?", reply_markup=keyboard)
