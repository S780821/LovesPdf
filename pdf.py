# This file is part of nabilanavab/LovesPdf [a completely free software]


# Repository:  : [LOVES💜PDF]
# Author:      : Salim Ansari 
# Email:       : .....
# Telegram:    : https://telegram.dog/LOVES_PDF_BOT
# GitHub:      : https://github.com/S780821/LoversPdf
# Coding       : !/usr/bin/python3, utf-8, copyright ©️ 2021 PERFECT SALIM


# ABOUT SOURCE-CODE:
#     Inspired from an old Telegram Bot [@JPG2PDFBot] by @spechide
# 



LovesPdf = '''
  _   _                  ___  ___  ____ ™
 | | | |   _____ _____  | _ \|   \|  __| 
 | | | |__/ _ \ V / -_) |  _/| |) |  _|  
 |_| |___,\___/\_/\___| |_|  |___/|_|    
                         [Perfect Salim] 
                         Email: ........
                         Telegram: @Xmartperson
'''


import asyncio
import logging
from pyromod import listen
from configs.dm import Config
from configs.db import isMONGOexist
from pyrogram import Client as LovesPdf
from telebot.async_telebot import AsyncTeleBot
from configs.db import BANNED_USR_DB, BANNED_GRP_DB
from configs.images import CUSTOM_THUMBNAIL_U, CUSTOM_THUMBNAIL_C
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

if isMONGOexist:
    from database import db


# LOGGING INFO: DEBUG
logger=logging.getLogger(__name__)
logging.basicConfig(
                   level=logging.DEBUG,
                   format="%(levelname)s:%(name)s:%(message)s" # %(asctime)s:
                   )
logging.getLogger("pyrogram").setLevel(logging.ERROR)
# SOMEONE TOLD ME PRO DEV. NEVER USE PRINT FOR TRACKING ERRORS. SO, import logging :|

# GLOBAL VARIABLES

PDF = {}            # save images for generating pdf
myID = None
PROCESS = []        # to check current process
invite_link = None


# TELEBOT (pyTelegramBotAPI) Asyncio
pyTgLovePDF = AsyncTeleBot(
                           Config.API_TOKEN,
                           parse_mode = "Markdown"
                           )
pyTgLovePDF.polling()

# PYROGRAM
class Bot(LovesPdf):
    
    def __init__(self):
        super().__init__(
            session_name = "LovesPdf",
            api_id = Config.API_ID,
            api_hash = Config.API_HASH,
            bot_token = Config.API_TOKEN,
            plugins = {
                      "root": "plugins"
                      }
            )
    
    async def start(self):
        if isMONGOexist:
            global myID
            # Loading Banned UsersId to List
            b_users, b_chats = await db.get_banned()
            BANNED_USR_DB.extend(b_users)
            BANNED_GRP_DB.extend(b_chats)
            
            # Loading UsersId with custom THUMBNAIL
            users = await db.get_all_users()   # Get all user Data
            async for user in users:
                if user.get("thumbnail", False):
                    CUSTOM_THUMBNAIL_U.append(user["id"])
            groups = await db.get_all_chats()
            async for group in groups:
                if group.get("thumbnail", False):
                    CUSTOM_THUMBNAIL_C.append(group["id"])
            
        # Pyrogram Client Starting
        await super().start()
        myID = await app.get_me()
        logger.debug(
                    f"BOT ID : {myID.id} | BOT NAME: {myID.first_name} |"
                    f" BOT USERNAME: {myID.username}\n\n"
                    f"BOT GETS STARTED..\n"
                    f"Thanks @xmartperson for this Awesome repo\n"
                    f"Telegram Update Channel: @LOVES_PDF_Channel\n\n"
                    f"{LovesPdf}"
                    )
        # Bot Restarted Message to ADMINS
        for admin in Config.ADMINS:
            try:
                await app.send_message(
                                      chat_id = admin,
                                      text = "Bot Restarted Sar.. 😅",
                                      reply_markup = InlineKeyboardMarkup(
                                            [[
                                                InlineKeyboardButton("◍ close ◍",
                                                               callback_data="close")
                                            ]]
                                      ))
            except Exception: pass
    
    async def stop(self, *args):
        await super().stop()


if __name__ == "__main__":
    app=Bot()
    app.run()


#                                                         OPEN SOURCE TELEGRAM PDF BOT 🐍
#                                                              by: nabilanavab [LovesPdf]
