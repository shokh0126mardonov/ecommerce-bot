from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Bot ishlayapti")

updater = Updater("8301674119:AAGQqrjGkLI4w02hRNt9oRxTEg5NB1wBELM", use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
