from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command(["start", "start@GroupMusicXBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello 👋🏻 {}!\n\nI can play music in voice chats of Telegram Groups.\n\nI have a lot of cool feature that will amaze You!\n\nJoin [Updates Channel](https://t.me/GroupMusicXNews) To Get Latest Updates**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Add To Your Group ➕", url="https://t.me/GroupMusicXBot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Group", url="https://t.me/MusicBotSupports"),
            InlineKeyboardButton("Channel 📣", url="https://t.me/GroupMusicXNews")
            ],[
            InlineKeyboardButton("🎛 Commands 🎛", url="https://telegra.ph/Music-Bot-05-07")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command(["start", "start@GroupMusicXBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
          text="**Music player is online ✅**",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/MusicBotSupports")
              ]]
          )
      )
