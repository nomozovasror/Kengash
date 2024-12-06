from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

DJANGO_URL = "http://127.0.0.1:8000/test/"  # Django server URL
import requests

BOT_TOKEN = '7381137526:AAFHH7nKHdRFMLaqxb8lmIMRfL-236xVKBY'

print('Bot ishga tushdi')
print(BOT_TOKEN)

async def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                "Boshlash uchun bosing!",
                web_app={"url": "https://bt.tersu.uz/"}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Ilmiy unvonlarga tavsiya etish uchun quyidagi tugmani bosing va hemis login parol bilan identifikatsiyadan o'ting", reply_markup=reply_markup)


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
