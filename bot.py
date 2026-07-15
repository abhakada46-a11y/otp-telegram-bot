import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Request a Number", "Check Balance"],
                ["Top-up", "Rates"],
                ["Check Availability"]]
    await update.message.reply_text("Welcome to OTP Seller!", 
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Request a Number":
        await update.message.reply_text("Anong app? Ex: Shopee, Telegram")
    elif text == "Check Balance":
        await update.message.reply_text("Balance: ₱0.00")
    elif text == "Top-up":
        await update.message.reply_text("GCash: 09xx xxx xxxx")
    elif text == "Rates":
        await update.message.reply_text("PH: ₱15\nUS: ₱25")
    elif text == "Check Availability":
        await update.message.reply_text("Available: PH, US, IN")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
