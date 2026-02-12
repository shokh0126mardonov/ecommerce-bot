from telegram.ext import CallbackContext
from telegram import Update

from db import User,SessionLocal
from utils import Register


def start(update:Update,context:CallbackContext):
    db = SessionLocal()
    chat_id = update.message.chat_id

    if not db.query(User).filter_by(chat_id = chat_id).first():
        update.message.reply_text(
            f"Salom {update.effective_user.full_name} ecommerce botga xush kelibsiz! \nRo'yxatdan o'tish uchun ism-sharifingizni yuboring!"
        )
        return Register.full_name
    update.message.reply_text(
            f"Salom {update.effective_user.full_name} ecommerce botga xush kelibsiz!"
        )
