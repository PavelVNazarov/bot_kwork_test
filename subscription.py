   
# /telegram_bot/
# │
# ├── bot.py                # Основной файл бота
# ├── config.py             # Файл конфигурации с токеном
# ├── handlers.py           # Обработчики команд и сообщений
# ├── subscription.py       # Логика проверки подписки
# ├── exercises.py          # Логика работы с упражнениями
# ├── video_manager.py
# └── requirements.txt
        
# subscription.py
from telegram import Bot
from config import CHANNEL_ID

def check_subscription(user_id):
    bot = Bot(token='YOUR_TELEGRAM_BOT_TOKEN')
    try:
        chat_member = bot.get_chat_member(CHANNEL_ID, user_id)
        return chat_member.status in ['member', 'administrator']
    except Exception as e:
        return False  # Обработка ошибок, если пользователь не подписан
