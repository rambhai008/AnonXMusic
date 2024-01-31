from pyrogram import Client, filters
import requests
import random
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  
from AnonXMusic import app

regex_gif = ["blowjob"]
pht = random.choice(regex_gif)
url = f"https://api.waifu.pics/nsfw/{pht}"

@app.on_message(filters.command("blowjob"))
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        button = [[InlineKeyboardButton("SUPPORT", url=f"https://t.me/LustxSupport")]]
        markup = InlineKeyboardMarkup(button)
       sent_message = await message.reply_video(video=image, caption=f"BY @riasxrobot")
       time.sleep(10)
       await sent_message.delete()
        
