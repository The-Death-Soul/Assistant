# Powered By: © Love_Dear_Comrades
# Copyright (C) 2022 @The_Death_Soul

from telethon import TelegramClient
from assistant.Conf import Config
import logging
 
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

bot = TelegramClient('Sammy', api_id=Config.APP_ID, api_hash=Config.API_HASH)
Sammy = bot.start(bot_token=Config.TOKEN)
