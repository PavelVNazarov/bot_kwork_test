import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Укажите Ваш токен
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHANNEL_USERNAME = '@your_channel_username'

# Проверка подписки
def check_subscription(user_id):
    # Здесь должна быть логика проверки подписки
    return True  # Замените на реальную проверку

# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if not check_subscription(user_id):
        update.message.reply_text("Пожалуйста, подпишитесь на наш канал, чтобы получить доступ к материалам.")
        return
    show_main_menu(update)

# Показать главное меню
def show_main_menu(update: Update) -> None:
    keyboard = [
        [InlineKeyboardButton("Выбор упражнения", callback_data='select_exercise')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Добро пожаловать! Выберите опцию:', reply_markup=reply_markup)

# Обработка нажатий кнопок
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    if query.data == 'select_exercise':
        show_exercise_categories(query)

# Показать категории упражнений
def show_exercise_categories(query) -> None:
    keyboard = [
        [InlineKeyboardButton("Спина", callback_data='back')],
        [InlineKeyboardButton("Руки", callback_data='arms')],
        [InlineKeyboardButton("Грудь", callback_data='chest')],
        [InlineKeyboardButton("Ноги", callback_data='legs')],
        [InlineKeyboardButton("Плечи", callback_data='shoulders')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Выберите категорию:", reply_markup=reply_markup)

# Основная функция
def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Список для хранения видео по категориям
exercise_videos = {
    'Спина': [],
    'Руки': [],
    'Грудь': [],
    'Ноги': [],
    'Плечи': []
}

# Проверка подписки на канал
def check_subscription(user_id):
    # Здесь должна быть логика проверки подписки
    # Например, можно использовать API Telegram для проверки
    return True  # Замените на реальную проверку

# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if not check_subscription(user_id):
        update.message.reply_text("Пожалуйста, подпишитесь на наш канал, чтобы получить доступ к материалам.")
        return
    show_main_menu(update)

# Показать главное меню
def show_main_menu(update: Update) -> None:
    keyboard = [
        [InlineKeyboardButton("Выбор упражнения", callback_data='select_exercise')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Добро пожаловать! Выберите действие:', reply_markup=reply_markup)

# Обработка выбора упражнения
def select_exercise(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Спина", callback_data='back')],
        [InlineKeyboardButton("Руки", callback_data='arms')],
        [InlineKeyboardButton("Грудь", callback_data='chest')],
        [InlineKeyboardButton("Ноги", callback_data='legs')],
        [InlineKeyboardButton("Плечи", callback_data='shoulders')],
        [InlineKeyboardButton("Назад", callback_data='back_to_main')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text('Выберите категорию упражнений:', reply_markup=reply_markup)

# Обработка выбора категории
def handle_category_selection(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    category = query.data
    if category in exercise_videos:
        # Здесь можно добавить логику для отображения видео
        query.edit_message_text(text=f"Вы выбрали категорию: {category}. Здесь будут видео.")
    elif category == 'back_to_main':
        show_main_menu(update)

# Добавление видео в категорию
def add_video(category, video_url):
    if category in exercise_videos:
        exercise_videos[category].append(video_url)

def main() -> None:
    updater = Updater("YOUR_TOKEN_HERE")
    
    # Регистрация обработчиков
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(handle_category_selection))
    
    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
