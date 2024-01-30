import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from AnonXMusic import app  

photo = [
    "https://telegra.ph/file/a2dd26ff9753215e991d6.png",
    "https://telegra.ph/file/d534aaede8b1e78478f50.png",
    "https://telegra.ph/file/8f9f5081806862beada91.png"
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"____________________________________\n\n"
                f"ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                f"ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                f"ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                f"ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome
@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = ( 
                f"{member.id} 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 \n\n"
                f"𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀 : @{member.username}\n"
                f"𝙐𝙎𝙀𝙍 𝙄𝘿 : {member.id}\n"
                f"𝘾𝙃𝘼𝙏 𝙉𝘼𝙈𝙀 : {message.chat.title}\n"
                
                f"𝘾𝙊𝙈𝙋𝙇𝙀𝙏𝙀𝘿 {count} 𝙈𝙀𝙈𝘽𝙀𝙍𝙎"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"𝘼𝘿𝘿 𝙈𝙀", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
