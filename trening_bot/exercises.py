# exercises.py

from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher import State, StatesGroup
from aiogram.dispatcher.filters.state import State, StatesGroup
from video_manager import VideoManager

# Состояния для FSM
class Form(StatesGroup):
    category = State()
    exercise = State()

# Список категорий и упражнений
EXERCISES = {
    "Спина": ["Тяга штанги", "Тяга гантели"],
    "Руки": ["Подъем штанги", "Французский жим"],
    "Грудь": ["Жим штанги", "Разводка гантелей"],
    "Ноги": ["Приседания", "Жим ногами"],
    "Плечи": ["Жим гантелей", "Подъемы в стороны"]
}
# Пример структуры данных для упражнений
EXERCISES = {
    "Спина": {
        "Тяга штанги": "video_url_1",
        "Тяга гантели": "video_url_2",
    },
    "Руки": {
        "Сгибание рук с гантелями": "video_url_3",
        "Французский жим": "video_url_4",
    },
    "Грудь": {
        "Жим штанги": "video_url_5",
        "Разводка гантелей": "video_url_6",
    },
    "Ноги": {
        "Приседания": "video_url_7",
        "Жим ногами": "video_url_8",
    },
    "Плечи": {
        "Жим гантелей": "video_url_9",
        "Подъем гантелей": "video_url_10",
    },
}

def get_exercise_categories():
    return list(EXERCISES.keys())

def get_exercise_video(category, exercise):
    return EXERCISES.get(category, {}).get(exercise, None)
# Инициализация VideoManager
video_manager = VideoManager()

async def start_exercise_selection(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in EXERCISES.keys():
        keyboard.add(types.KeyboardButton(category))
    await message.answer("Выберите категорию упражнений:", reply_markup=keyboard)
    await Form.category.set()

async def select_exercise(message: types.Message, state: FSMContext):
    category = message.text
    if category in EXERCISES:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for exercise in EXERCISES[category]:
            keyboard.add(types.KeyboardButton(exercise))
        keyboard.add(types.KeyboardButton("Назад"))
        await message.answer(f"Выберите упражнение из категории '{category}':", reply_markup=keyboard)
        await Form.exercise.set()
        await state.update_data(category=category)
    else:
        await message.answer("Пожалуйста, выберите корректную категорию.")

async def show_video(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    category = user_data.get('category')
    exercise = message.text

    if exercise in EXERCISES[category]:
        video_url = video_manager.get_video_url(category, exercise)
        await message.answer(f"Вот видео с упражнением '{exercise}': {video_url}")
    elif exercise == "Назад":
        await start_exercise_selection(message)
    else:
        await message.answer("Пожалуйста, выберите корректное упражнение.")

def register_handlers_exercises(dp: Dispatcher):
    dp.register_message_handler(start_exercise_selection, commands=['start'], state='*')
    dp.register_message_handler(select_exercise, state=Form.category)
    dp.register_message_handler(show_video, state=Form.exercise)

