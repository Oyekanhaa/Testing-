from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHIN_MUSIC import app
from config import BOT_USERNAME
from SACHIN_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - MAANAV
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - MAANAV
│├─────────────────╯
├┼─────────────────⦿
├┤~ @maanavbots
├┤~ @ABOUT_MAANAV
├┤~ @aboutkanha
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @oyemaanav
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton(" 𝗠𝗔𝗔𝗡𝗔𝗩", url=f"https://t.me/ABOUT_MAANAV")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/ABOUT_MAANAV"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/ABOUT_MAANAV"),
          ],
               [
                InlineKeyboardButton("ɪɴᴄʀɪᴄɪʙʟᴇ ɴᴇᴛᴡᴏʀᴋ", url=f"https://t.me/ABOUT_MAANAV"),
],
[
InlineKeyboardButton("ᴏғғɪᴄɪᴀʟ ʙᴏᴛ", url=f"https://t.me/maanavXmuziccbot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/pt0ytt.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
