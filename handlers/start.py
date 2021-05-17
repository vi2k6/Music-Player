from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command(["start", "start@GroupMusicXBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello 👋🏻 {}!**\n\nI **Can Play Music In Voice Chats of Telegram Groups.**\n\nI Have A **lot of cool feature that will amaze You!**\n\n**Click /cmdlist For More Help On My Usage ❤**\n\nJoin [Updates Channel](https://t.me/GroupMusicXNews) To Get Latest Updates**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Add To Your Group ➕", url="https://t.me/GroupMusicXBot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Group", url="https://t.me/MusicBotSupports"),
            InlineKeyboardButton("Channel 📣", url="https://t.me/GroupMusicXNews")
            ],[
            InlineKeyboardButton("Commands 🛠", url="https://telegra.ph/Music-Bot-05-07"),
            InlineKeyboardButton("Credits ❤", url="https://telegra.ph/Group-Music-X-Bot-05-17")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command(["start", "start@GroupMusicXBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
          text="",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/MusicBotSupports")
              ]]
          )
      )

@Client.on_message(filters.command(["cmdlist", "cmdlist@GroupMusicXBot"]) & ~filters.private & ~filters.channel)
async def cmdlist_, message: Message):
      await message.reply_text(
          text="**Group Music Bot : Help Menu**

__× First Add Me To Your Group..
× Promote Me As Admin In Your Group With All Permission..__

**🏷 Common Commands.**

• `/play` - Song Name : __Plays Via Youtube__
• `/dplay` - Song Name : __Play Via Deezer__
• `/splay` - Song Name : __Play Via Jio Saavn__
• `/playlist` - __Show now playing list__
• `/current` - __Show now playing__

• `/song` - Song Name : __Get The Song From YouTube__
• `/vid` - Video Name : __Get The Video From YouTube__
• `/deezer` - song name : __download songs you want quickly via deezer__
• `/saavn` - song name : __download songs you want quickly via saavn__
• `/search` - YouTube Title : __(Get YouTube Search Query)__

**🏷 Group Admin Commands.**

• `/skip` : Skips Music
• `/pause` : Pause Playing Music
• `/resume` : Resume Playing Music
• `/end` : Stops playing Music
• `/reload` : Reloads Admin List
• `/userbotjoin` : Assistant Joins The Group
• `/userbotleave` : Assistant Leaves From The Group.",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/MusicBotSupports")
              ]]
          )
      )
