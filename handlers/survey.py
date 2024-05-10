from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types, Router, F
from aiogram.filters import Command

survey_router = Router()


class PizzaSurvey(StatesGroup):
    name = State()
    phone_or_instagram = State()
    date_of_visit = State()
    food_rating = State()
    cleaning_rating = State()
    comments = State()

@survey_router.callback_query(F.data == "survey")
async def start_survey(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(PizzaSurvey.name)
    await callback.answer()
    await callback.message.answer("Как вас зовут?")


@survey_router.message(PizzaSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(PizzaSurvey.phone_or_instagram)
    await message.answer("Ваш номер телефона или инстаграм")


@survey_router.message(PizzaSurvey.phone_or_instagram)
async def process_phone_or_instagram(message: types.Message, state: FSMContext):
    await state.set_state(PizzaSurvey.date_of_visit)
    await message.answer("Дата вашего посещения нашего заведения")

@survey_router.message(PizzaSurvey.date_of_visit)
async def process_date_of_visit(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите число")
        return
    await state.update_data(data_of_visit=message.text)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Oтлично")
            ],
            [
                types.KeyboardButton(text="Хорошо")
            ],
            [
                types.KeyboardButton(text="Плохо")
            ],
            [
                types.KeyboardButton(text="Очень плохо")
            ]
        ]
    )

    await state.set_state(PizzaSurvey.food_rating)
    await message.answer("Как оцениваете качество еды?", reply_markup=kb)


@survey_router.message(PizzaSurvey.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Oтлично")
            ],
            [
                types.KeyboardButton(text="Хорошо")
            ],
            [
                types.KeyboardButton(text="Плохо")
            ],
            [
                types.KeyboardButton(text="Очень плохо")
            ]
        ]
    )

    await state.set_state(PizzaSurvey.cleaning_rating)
    await message.answer("Как оцениваете чистоту заведения?", reply_markup=kb)


@survey_router.message(PizzaSurvey.cleaning_rating)
async def process_cleaning_ratingen(message: types.Message, state: FSMContext):
    await state.set_state(PizzaSurvey.comments)
    await message.answer("Дополнительные комментарии")

@survey_router.message(Command("stop"))
async def stop_survey(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за уделённое время!")