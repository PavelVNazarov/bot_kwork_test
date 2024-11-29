# subscription.py
from aiogram import Bot

async def check_subscription(user_id, bot: Bot):
    chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
    return chat_member.status in ['member', 'administrator', 'creator']