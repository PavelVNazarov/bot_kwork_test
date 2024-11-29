import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.utils import executor

from config import TOKEN
from subscription import check_subscription
from exercises import get_exercise_categories, get_exercise_video
from video_manager import  VideoManager.get_video

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Стартовая команда
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    if await check_subscription(user_id):
        await message.answer("Добро пожаловать! Выберите действие:", reply_markup=main_menu())
    else:
        await message.answer("Пожалуйста, подпишитесь на наш канал, чтобы получить доступ к материалам.")

# Главное меню
def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Выбор упражнения"))
    return keyboard

# Обработка выбора упражнения
@dp.message_handler(lambda message: message.text == "Выбор упражнения")
async def choose_exercise(message: types.Message):
    categories = get_exercise_categories()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories:
        keyboard.add(types.KeyboardButton(category))
    keyboard.add(types.KeyboardButton("Назад"))
    await message.answer("Выберите категорию упражнений:", reply_markup=keyboard)

# Обработка выбора категории
@dp.message_handler(filters.Text(equals=get_exercise_categories()))
async def choose_exercise_category(message: types.Message):
    category = message.text
    exercises = VideoManager.get_video(category)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for exercise in exercises:
        keyboard.add(types.KeyboardButton(exercise))
    keyboard.add(types.KeyboardButton("Назад"))
    await message.answer(f"Выберите упражнение из категории {category}:", reply_markup=keyboard)

# Обработка выбора конкретного упражнения
@dp.message_handler(filters.Text(equals=VideoManager.get_video()))
async def show_exercise_video(message: types.Message):
    exercise = message.text
    video_url = get_exercise_video(exercise)
    await message.answer(f"Вот видео с упражнением {exercise}: {video_url}")

# Обработка кнопки "Назад"
@dp.message_handler(lambda message: message.text == "Назад")
async def back_to_main_menu(message: types.Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=main_menu())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

