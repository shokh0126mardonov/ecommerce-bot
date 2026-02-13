from telegram.ext import Updater,CommandHandler,MessageHandler,ConversationHandler,Filters,CallbackQueryHandler

from handlers import start,get_age,get_contact,get_full_name,confirm_data
from utils import settings,Register
from db import create_models

create_models()

def main():
    updater = Updater(settings.TOKEN)
    dispatcher = updater.dispatcher

    register_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            Register.full_name : [MessageHandler(Filters.text,get_full_name)],
            Register.age : [MessageHandler(Filters.text,get_age)],
            Register.contact : [MessageHandler(Filters.contact,get_contact)],
            Register.confirm:[CallbackQueryHandler(confirm_data, pattern=r"^confirm_")]
        },
        fallbacks=[dispatcher.add_handler(CommandHandler('start', start))],
    )
    dispatcher.add_handler(register_handler)
    # dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()