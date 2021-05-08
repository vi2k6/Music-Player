from . import *
from pyrogram import *
from pyrogram.types import *

@Client.on_message(filters.new_chat_members)
async def welcome(client, message):
    try:
        joiner = await Client.get_me() 
        for user in message.new_chat_members:
            if int(joiner.id) == int(user.id):
                await message.reply_text("Thanks for adding me to your Group :) \nPromote me now")
    except Exception as e:
        await Client.send_message(int("1414146649"), f"Chat ID: `{message.chat.id}` \nError while Sending Thanks Message: {e}")
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel📣", url="https://t.me/GroupMusicXNews")
                ]
            ]
        ),
