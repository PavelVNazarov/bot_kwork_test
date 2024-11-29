# bot.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TOKEN
from handlers import start_handler, exercise_handler

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(CommandHandler("exercise", exercise_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
