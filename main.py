from telegram.ext import Updater,CommandHandler,MessageHandler

from handlers import start
from utils import settings

def main():
    updater = Updater(settings.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start',start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()