import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from SACHIN_MUSIC import app
from SACHIN_MUSIC.misc import _boot_
from SACHIN_MUSIC.plugins.sudo.sudoers import sudoers_list
from SACHIN_MUSIC.utils.database import get_served_chats, get_served_users, get_sudoers
from SACHIN_MUSIC.utils import bot_sys_stats
from SACHIN_MUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from SACHIN_MUSIC.utils.decorators.language import LanguageStart
from SACHIN_MUSIC.utils.formatters import get_readable_time
from SACHIN_MUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

NEXIO = [
    "https://files.catbox.moe/jrupn9.jpg",
    "https://files.catbox.moe/5z141p.jpg",
    "https://files.catbox.moe/fnl0h7.jpg",
    "https://files.catbox.moe/1lz1go.jpg",
    "https://files.catbox.moe/avackl.jpg",
    "https://files.catbox.moe/1yrzwz.jpg",
    "https://files.catbox.moe/6y22qw.jpg",
    "https://files.catbox.moe/gnnsf2.jpg",
    "https://files.catbox.moe/ss6r60.jpg",
    "https://files.catbox.moe/yuob18.jpg",
    "https://files.catbox.moe/i9xrrp.jpg",
    "https://files.catbox.moe/a9tx8f.jpg"
    "https://files.catbox.moe/wlt26x.jpg",
    "https://files.catbox.moe/c1lylh.jpg",
    "https://files.catbox.moe/82eymp.jpg",
]

HIMANSHI = [
    "CAACAgUAAxkBAAKOmmkz-ntJaFPXb0carGSNRtKHl69sAAL7HQACNIWhVdDyUdqb8yMtHgQ",
    "CAACAgUAAxkBAAKOm2kz-nsnFNG9zS0eyjaE9mEriTN2AAKLHQACXmKhVWRYc-mThaGHHgQ",
    "CAACAgUAAxkBAAKOnGkz-ny89GKzIC8y38Gqdg_ujQg4AAIkHAAChPKgVcjV8fUfimNGHgQ",
    "CAACAgUAAxkBAAKOnWkz-nz5cZGEYLoWfp7QZgIbf9HbAAIRHQAC_jOgVdqhnaopN_EJHgQ", 
    "CAACAgUAAxkBAAKOnmkz-n013B233W24UyE4KiAtEbRlAAKAGwAC0VOgVe_Z1cRSzI-sHgQ", 
    "CAACAgUAAxkBAAKOn2kz-n2FSJi7MKC9q0Wy6T7CilM8AALTHAACvgABoFXBEMums5ywdR4E", 
    "CAACAgUAAxkBAAKOoGkz-n7ENOqTjvLOaCZFSkOZLiYCAAJaGwACWXKgVaxKbq4HeZ4MHgQ",
    "CAACAgUAAxkBAAKOoWkz-n7JfmZjgzI7n5srNEY_bkyGAAINGgACbpigVSc4KH8aMEshHgQ", 
    "CAACAgUAAxkBAAKOomkz-n-62srSaAOYMPKLHPevi8FBAAJvHAACcwmgVbva9WxHwDJIHgQ", 
    "CAACAgUAAxkBAAKOo2kz-oBmaCHZ96BNQafgepRINZKYAAKjGwACeZmgVSPTNWP_M9WLHgQ", 
]


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            await message.reply_sticker(
            random.choice(HIMANSHI),)
            return await message.reply_photo(
                random.choice(NEXIO),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"✦ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>✦ ᴜsᴇʀ ɪᴅ ➠</b> <code>{message.from_user.id}</code>\n<b>✦ ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(

chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"✦ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n✦ <b>ᴜsᴇʀ ɪᴅ ➠</b> <code>{message.from_user.id}</code>\n✦ <b>ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        await message.reply_sticker(
        random.choice(HIMANSHI),)
        await message.reply_photo(
            random.choice(NEXIO),
            caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM,served_users,served_chats),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"✦ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n✦ <b>ᴜsᴇʀ ɪᴅ ➠</b> <code>{message.from_user.id}</code>\n✦ <b>ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_sticker(
    random.choice(HIMANSHI),)
    await message.reply_photo(
        random.choice(NEXIO),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_sticker(
                random.choice(HIMANSHI),)
                await message.reply_photo(
                    random.choice(NEXIO),
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
