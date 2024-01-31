from pyrogram import Client, filters
import requests
import random
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  
from AnonXMusic import app

regex_photo = ["neko"]
pht = random.choice(regex_photo)
url = f"https://api.waifu.pics/nsfw/{pht}"

@app.on_message(filters.command("neko"))
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        button = [[InlineKeyboardButton("SUPPORT", url=f"https://t.me/LustxSupport")]]
        markup = InlineKeyboardMarkup(button)
        message.reply_photo(up,caption="BY @riasxrobot",reply_markup=markup)
    else:
        message.reply("Request failed try /again")
