# handlers.py
from telegram import Update
from telegram.ext import CallbackContext
from subscription import check_subscription
from exercises import show_exercises

def start_handler(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if check_subscription(user_id):
        update.message.reply_text("Добро пожаловать! Выберите упражнение.")
        # Здесь можно вызвать функцию для отображения меню
    else:
        update.message.reply_text("Пожалуйста, подпишитесь на наш канал.")

def exercise_handler(update: Update, context: CallbackContext):
    # Логика выбора упражнения
    show_exercises(update)
