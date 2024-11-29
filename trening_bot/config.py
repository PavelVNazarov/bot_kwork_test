# config.py

import os

# Получаем токен бота из переменной окружения или задаем его напрямую
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Указываем ID канала для проверки подписки
CHANNEL_ID = '@your_channel_id_here'

# Настройки базы данных (если требуется)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///your_database.db')

# Другие конфигурации могут быть добавлены здесь