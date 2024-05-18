from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types, Router, F
from aiogram.filters import Command
from config import database


survey_router = Router()

ratings = ["плохо", "хорошо", "отлично"]


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
    name = message.text
    await state.update_data(name=name)
    await state.set_state(PizzaSurvey.phone_or_instagram)
    await message.answer("Ваш номер телефона или инстаграм")


@survey_router.message(PizzaSurvey.phone_or_instagram)
async def process_phone_or_instagram(message: types.Message, state: FSMContext):
    phone_or_instagram = message.text
    await state.update_data(phone_or_instagram=phone_or_instagram)
    await state.set_state(PizzaSurvey.date_of_visit)
    await message.answer("Дата вашего посещения нашего заведения")


@survey_router.message(PizzaSurvey.date_of_visit)
async def process_date_of_visit(message: types.Message, state: FSMContext):
    date_of_visit = message.text
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите число")
        return
    await state.update_data(date_of_visit=message.text)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="отлично")
            ],
            [
                types.KeyboardButton(text="хорошо")
            ],
            [
                types.KeyboardButton(text="плохо")
            ],

        ]
    )
    await state.update_data(data_of_visit=date_of_visit)
    await state.set_state(PizzaSurvey.food_rating)
    await message.answer("Как оцениваете качество еды?", reply_markup=kb)


@survey_router.message(PizzaSurvey.food_rating, F.text.lower().in_(ratings))
async def process_food_rating(message: types.Message, state: FSMContext):
    food_rating = message.text
    food_rating = ratings.index(food_rating) + 3
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="отлично")
            ],
            [
                types.KeyboardButton(text="хорошо")
            ],
            [
                types.KeyboardButton(text="плохо")
            ],

        ]
    )

    await state.update_data(food_rating=food_rating)
    await state.set_state(PizzaSurvey.cleaning_rating)
    await message.answer("Как оцениваете чистоту заведения?", reply_markup=kb)


@survey_router.message(PizzaSurvey.cleaning_rating, F.text.lower().in_(ratings))
async def process_cleaning_rating(message: types.Message, state: FSMContext):
    cleaning_rating = message.text
    cleaning_rating = ratings.index(cleaning_rating) + 3
    await state.update_data(cleaning_rating=cleaning_rating)
    await state.set_state(PizzaSurvey.comments)
    await message.answer("Дополнительные комментарии")

@survey_router.message(Command("stop"))
async def stop_survey(message: types.Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    await state.clear()
    await database.execute(
        "INSERT INTO surveys (name, phone_or_instagram, date_of_visit, food_rating, cleaning_rating) VALUES (?, ?, ?, ?, ?)",
            (data["name"], data["phone_or_instagram"], data["date_of_visit"], data["food_rating"], data["cleaning_rating"]),
        )
    await state.clear()
    await message.answer("Спасибо за уделённое время!")


