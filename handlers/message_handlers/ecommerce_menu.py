from telegram import Update,ReplyKeyboardRemove
from telegram.ext import CallbackContext
from ..buttons import button_menu


def send_menu(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Menu",
        reply_markup = button_menu()
    )
