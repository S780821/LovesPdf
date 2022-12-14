# fileName : Plugins/dm/photo.py
# copyright ÂŠī¸ 2021xmartperson

# LOGGING INFO: INFO
import logging
logger=logging.getLogger(__name__)
logging.basicConfig(
                   level=logging.INFO,
                   format="%(levelname)s:%(name)s:%(message)s" # %(asctime)s:
                   )

import os
from PIL import Image
from pyrogram.types import (
                           InlineKeyboardButton,
                           InlineKeyboardMarkup
                           )
from pyrogram import filters
from configs.dm import Config
from pdf import PDF, invite_link
from pyrogram import Client as LovesPdf
from configs.images import WELCOME_PIC, BANNED_PIC

UPDATE_CHANNEL = Config.UPDATE_CHANNEL

#--------------->
#--------> LOCAL VARIABLES
#------------------->

imageAdded = """`Added {} page/'s to your pdf..`đ¤

fileName: `{}.pdf` đ¤"""

forceSubMsg = """Wait [{}](tg://user?id={})..!!

Due To The Huge Traffic Only Channel Members Can Use this Bot đļ

This Means You Need To Join The Below Mentioned Channel for Using Me!

hit on "retry âģī¸" after joining.. đ"""

#--------------->
#--------> REPLY TO IMAGES
#------------------->

@LovesPdf.on_message(
                    filters.photo &
                    filters.private &
                    ~filters.edited &
                    filters.incoming
                    )
async def images(bot, message):
    try:
        global invite_link
        await message.reply_chat_action("typing")
        # CHECK USER IN CHANNEL (IF UPDATE_CHANNEL ADDED)
        if UPDATE_CHANNEL:
            try:
                userStatus = await bot.get_chat_member(
                                                      str(UPDATE_CHANNEL),
                                                      message.chat.id
                                                      )
                # IF USER BANNED FROM CHANNEL
                if userStatus.status == 'banned':
                     return await message.reply_photo(
                                                     photo = BANNED_PIC, quote = True,
                                                     caption = "For Some Reason You Can't Use This Bot"
                                                               "\n\nContact Bot Owner đ¤",
                                                     reply_markup = InlineKeyboardMarkup(
                                                                          [[
                                                                                 InlineKeyboardButton(
                                                                                                     "Owner đ",
                                                                                 url="https://t.me/xmartperdon")
                                                                          ]]
                                                                    )
                                                     )
            except Exception:
                if invite_link == None:
                    invite_link = await bot.create_chat_invite_link(
                                                                   int(UPDATE_CHANNEL)
                                                                   )
                return await message.reply_photo(
                                         photo = WELCOME_PIC,
                                         quote = True,
                                         caption = forceSubMsg.format(
                                             message.from_user.first_name, message.chat.id
                                         ),
                                         reply_markup = InlineKeyboardMarkup(
                                             [[
                                                 InlineKeyboardButton("đ JOIN CHANNEL đ",
                                                             url = invite_link.invite_link)
                                             ],[
                                                 InlineKeyboardButton("Refresh âģī¸",
                                                              callback_data = "refreshImg")
                                             ]]
                                         ))
        imageReply = await message.reply_text(
                                             "`Downloading your Image..âŗ`",
                                             quote=True
                                             )
        if not isinstance(PDF.get(message.chat.id), list):
            PDF[message.chat.id] = []
        await message.download(
                              f"{message.chat.id}/{message.chat.id}.jpg"
                              )
        img = Image.open(
            f"{message.chat.id}/{message.chat.id}.jpg"
        ).convert("RGB")
        PDF[message.chat.id].append(img)
        await imageReply.edit(
                             imageAdded.format(
                                              len(PDF[message.chat.id]),
                                              message.chat.id
                                              ),
                             reply_markup = InlineKeyboardMarkup(
                                                                [[
                                                                    InlineKeyboardButton(
                                                                                        "GENERATE đ",
                                                                                        callback_data="generate"
                                                                                        ),
                                                                    InlineKeyboardButton(
                                                                                        "RENAME âī¸",
                                                                                        callback_data="generateREN"
                                                                                        )
                                                                ]]
                                            )
                             )
    
    except Exception as e:
        logger.exception(
                        "PHOTO:CAUSES %(e)s ERROR",
                        exc_info=True
                        )

#                                                                                              Telegram: @xmartperdon
