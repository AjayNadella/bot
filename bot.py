import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Get the token from Railway's environment variables

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id, f"Bot working! Your chat ID is: {chat_id}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot running on Railway...")
    app.run_polling()
