from pyrogram import Client
import pyrogram
import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api_id = 13966124  # بتع حسابك
api_hash = "ffb60460dd6a3e4e087f8b29d3179059"  # app hash
token="7696110235:AAGfHSLfVvH3VUMLahzHNWhHATYuKmxgNkE"

app = Client("gmm", api_id, api_hash, bot_token=token)


@app.on_chat_member_updated()
def handle_message(lient, update):
    if update.old_chat_member:
        user_id = update.from_user.id
        chat_id = update.chat.id
        url = f"https://api.telegram.org/bot{token}/kickChatMember"
        params = {
         "chat_id": chat_id,
         "user_id": user_id
         }

        response = requests.get(url, params=params)
@app.on_message(filters.command("start"))
def start(client, message):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("programmer", url="http://t.me/KOK0KK")],
        [InlineKeyboardButton("قناة البوت", url="https://t.me/Your_uncle_Muhammad")]
    ])
    message.reply_text(
        "منور في بوت حظر مغدرين \n\n"
        "انتا هترفع بوت ادمن و بس كده ♡",
        reply_markup=reply_markup
    )



app.run()
