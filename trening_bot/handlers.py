# handlers.py
from aiogram import Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from subscription import check_subscription
from exercises import get_exercise_categories, get_exercise_video
from config import CHANNEL_ID

async def start_command(message: types.Message):
    await message.answer("Привет! Пожалуйста, подпишитесь на наш канал: " + CHANNEL_ID)

async def choose_exercise(message: types.Message):
    categories = get_exercise_categories()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories:
        keyboard.add(category)
    await message.answer("Выберите категорию упражнений:", reply_markup=keyboard)

async def handle_category_selection(message: types.Message):
    category = message.text
    # Здесь можно добавить логику выбора конкретного упражнения
    await message.answer(f"Вы выбрали категорию: {category}. Теперь выберите упражнение.")

async def handle_exercise_selection(message: types.Message):
    # Здесь должна быть логика получения видео по выбранному упражнению
    video_url = get_exercise_video("Спина", "Тяга")  # Пример
    await message.answer(f"Вот видео: {video_url}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(choose_exercise, filters.Text(equals='Выбор упражнения'))
    dp.register_message_handler(handle_category_selection)
    dp.register_message_handler(handle_exercise_selection)
