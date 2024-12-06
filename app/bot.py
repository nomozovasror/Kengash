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
                "Web Appni ochish",
                web_app={"url": "https://a779-5-133-123-107.ngrok-free.app/"}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Quyidagi tugma orqali Web Appni sinab ko'ring:", reply_markup=reply_markup)


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
