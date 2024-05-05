from aiogram import Router,F, types
from aiogram.fsm.context import FSMContext

menu_router = Router()


@menu_router.callback_query(F.data == "menu")
async def menu_callback_query(callback: types.CallbackQuery):
    photo = types.FSInputFile("images/menu.jpg")
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="пицца🍕" , callback_data="pizza"),
                types.InlineKeyboardButton(text="крылашки🍗" , callback_data="nuggets"),
                types.InlineKeyboardButton(text="напитки🍹 ", callback_data="milkshakes")


            ]
        ]
    )
    await callback.answer()
    await callback.message.answer_photo(
        photo=photo,
        caption="🍕 **Меню в Freddy Fazbear's Pizza** 🍕\n\n"
    "🍽️ **Пицца:**\n"
    "От классической Маргариты до авторской - у нас есть пиццы на любой вкус!\n\n"
    "🍗 **Крылашки:**\n"
    "Нежные крылашки - отличный выбор для закуски или основного блюда.\n\n"
    "🍹 **Коктейли:**\n"
    "Освежитесь с нашими разнообразными коктейлями\n\n"
    "Приходите и наслаждайтесь атмосферой уюта и вкусом в Freddy Fazbear's Pizza! 🍴🎉",
        reply_markup=keyboard
    )


@menu_router.callback_query(F.data.startswith("order_"))
async def order_menu(callback: types.CallbackQuery):
    await callback.answer("Товар добавлен в корзину")