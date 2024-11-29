# handlers.py
from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Добро пожаловать! Пожалуйста, проверьте свою подписку.")

def check_subscription(update: Update, context: CallbackContext):
    # Логика проверки подписки
    update.message.reply_text("Проверка подписки...")

def exercise_selection(update: Update, context: CallbackContext):
    # Логика выбора упражнений
    update.message.reply_text("Выберите категорию упражнений.")
