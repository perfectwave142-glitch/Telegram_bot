from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def handle_message(update: Update, context):
    user_text = update.message.text

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_text}]
    )

    reply = response['choices'][0]['message']['content']
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
