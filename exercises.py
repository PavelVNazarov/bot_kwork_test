# exercises.py
from telegram import Update

def show_exercises(update: Update):
    # Логика отображения категорий и видео
    categories = ["Спина", "Руки", "Грудь", "Ноги", "Плечи"]
    update.message.reply_text("Выберите категорию: " + ", ".join(categories))
    # Здесь можно добавить логику для обработки выбора категории
