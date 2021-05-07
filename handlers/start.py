from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text.format(update.from_user.first_name)(
        f"""**Hello 👋🏻 {}!\n\nI can play music in voice chats of Telegram Groups.\n\nI have a lot of cool feature that will amaze You!\n\nJoin [Updates Channel](https://t.me/GroupMusicXBotNews) To Get Latest Updates**""",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Add To Your Group ➕", url="https://t.me/GroupMusicXBot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Group", url="https://t.me/MusicBotSupports"),
            InlineKeyboardButton("Channel 📣", url="https://t.me/GroupMusicXNews")
            ],[
            InlineKeyboardButton("🌐 Website 🌐", url="https://t.ME/")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Music player is online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/MusicBotSupports")
                ]
            ]
        )
   )

