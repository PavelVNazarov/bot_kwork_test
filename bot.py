# bot.py
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TOKEN
from handlers import start, check_subscription, exercise_selection

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("check_subscription", check_subscription))
    dp.add_handler(CommandHandler("exercise_selection", exercise_selection))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
