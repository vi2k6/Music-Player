# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello 👋🏻 there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!""",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Add To Your Group ➕", url="https://t.me/TG_GroupMusicBot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Group", url="https://t.me/"),
            InlineKeyboardButton("Channel 📣", url="https://t.me/GROUPMUSICNEWS")
            ],[
            InlineKeyboardButton("🎛 Commands", url="https://t.me/"),
            InlineKeyboardButton("About👨🏻‍🎓", url="https://t.me/")
            ],[
            InlineKeyboardButton("🌐 Website 🌐", url="https://t.ME/")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/daisysupport_Official")
                ]
            ]
        )
   )

