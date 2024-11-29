import aiohttp
from config import CHANNEL_ID

async def check_subscription(user_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getChatMember?chat_id={CHANNEL_ID}&user_id={user_id}') as response:
            data = await response.json()
            return data['result']['status'] == 'member' or data['result']['status'] == 'administrator'
