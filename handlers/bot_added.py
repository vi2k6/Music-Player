from . import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.new_chat_members)
async def welcome(client, message):
    try:
        buttons = InlineKeyboardMarkup([[InlineKeyboardButton(text="Channel 🔊", url="https://t.me/GroupMusicXNews")]])
        joiner = await client.get_me()
        for user in message.new_chat_members:
            if int(joiner.id) == int(user.id):
                await message.reply_text(
                    text="Thanks for adding me to your Group :) \nPromote me now",
                    reply_markup=buttons
                )
    except Exception as e:
        print(e)
        await client.send_message(
            chat_id=1711651694,
            text=f"Chat ID: `{message.chat.id}` \nError while Sending Thanks Message: {e}"
        )
