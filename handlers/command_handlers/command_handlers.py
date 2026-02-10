from telegram.ext import CallbackContext
from telegram import Update


def start(update:Update,context:CallbackContext):
    update.message.reply_text(
        f"Salom {update.effective_user.full_name} ecommerce botga xush kelibsiz!"
    )