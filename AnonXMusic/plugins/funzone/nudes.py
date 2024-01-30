import requests
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from AnonXMusic import app

@app.on_message(filters.command("nudes"))
async def es_img(_, message):
    url = "http://api.nekos.fun:8080/api/4k"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image = data["image"]
        await message.reply_photo(image, caption=f"BY @riasxrobot")
    else:
        await message.reply_text("Website gyi")
