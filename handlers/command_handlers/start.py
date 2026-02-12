from telegram.ext import CallbackContext,ConversationHandler
from telegram import Update

from db import User,SessionLocal
from utils import Register
from ..message_handlers import send_menu

def start(update: Update, context: CallbackContext):
    db = SessionLocal()
    chat_id = update.effective_user.id

    user = db.query(User).filter_by(chat_id=chat_id).first()

    if not user:
        update.message.reply_text(
            f"Salom {update.effective_user.full_name}! "
            "Ecommerce botga xush kelibsiz.\n"
            "Ro'yxatdan o'tish uchun ism-sharifingizni yuboring!"
        )
        return Register.full_name

    send_menu(update, context)
    return ConversationHandler.END