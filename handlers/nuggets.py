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

nuggets_types = ("острые","барбекю","терияки","чесночные")

@nuggets_router.message(F.text.lower().in_(nuggets_types))
async def nuggets_one (message: types.Message):
    nuggets = message.text
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Заказать", callback_data="order_margarita"),
                types.InlineKeyboardButton(text="Отмена", callback_data="nuggets")
            ]
        ]
    )
    await message.answer(f"Хотели бы вы заказать  {nuggets} нагетсы?", reply_markup=keyboard)
