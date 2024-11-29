# handlers.py
from aiogram import Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from subscription import check_subscription
from exercises import get_exercise_categories, get_exercise_video
from aiogram import Bot

# Инициализация бота и диспетчера
from config import TOKEN

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Состояния для FSM
class Form:
    category = "category"
    exercise = "exercise"

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    if await check_subscription(message.from_user.id):
        await message.answer("Добро пожаловать! Выберите упражнение:", reply_markup=await get_exercise_categories())
    else:
        await message.answer("Пожалуйста, подпишитесь на наш канал, чтобы получить доступ к материалам.")

@dp.callback_query_handler(lambda c: c.data == 'select_exercise')
async def process_select_exercise(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await Form.category.set()
    await callback_query.message.answer("Выберите категорию упражнений:", reply_markup=await get_exercise_categories())

@dp.callback_query_handler(lambda c: c.data in ['back'], state='*')
async def process_back(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer("Вы вернулись в главное меню.")

@dp.callback_query_handler(lambda c: c.data in ['spine', 'arms', 'chest', 'legs', 'shoulders'], state=Form.category)
async def process_category(callback_query: types.CallbackQuery, state: FSMContext):
    await Form.exercise.set()
    await bot.answer_callback_query(callback_query.id)
    exercises = await get_exercise_video(callback_query.data)
    await callback_query.message.answer(f"Выберите упражнение из категории {callback_query.data}:", reply_markup=exercises)

@dp.callback_query_handler(state=Form.exercise)
async def process_exercise(callback_query: types.CallbackQuery, state: FSMContext):
    video_url = await get_exercise_video(callback_query.data)
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer(f"Вот видео с упражнением: {video_url}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

