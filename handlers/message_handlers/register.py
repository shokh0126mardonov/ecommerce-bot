from telegram import Update,ReplyKeyboardRemove
from telegram.ext import CallbackContext

from utils import Register
from ..buttons import confirm,contact
from db import User,SessionLocal
from .ecommerce_menu import send_menu

def get_full_name(update:Update,context:CallbackContext):
    context.user_data['full_name'] = update.message.text.strip()

    update.message.reply_text(
        'Yoshizni yuboring!'
    )
    return Register.age


def get_age(update:Update,context:CallbackContext):
    context.user_data['age'] = update.message.text 

    update.message.reply_text(
        'Contactingizni yuboring!',
        reply_markup=contact()
    )

    return Register.contact 

def get_contact(update:Update,context:CallbackContext):
    context.user_data['contact'] = update.message.contact.phone_number
    data = (
    f"Ism: {context.user_data['full_name']}\n"
    f"Yosh: {context.user_data['age']}\n"
    f"Telefon: {context.user_data['contact']}"
    )
    update.message.reply_text(
        f'Malumotlaringizni tasdiqlang!\n{data}',
        reply_markup=confirm())
    
    return Register.confirm

def confirm_data(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    action = query.data  
    db = SessionLocal()
    if action == "confirm_yes":
        new_user = User(
        chat_id = int(update.effective_user.id),
        phone = context.user_data['contact'],
        age = int(context.user_data['age']),
        full_name = context.user_data['full_name'],
        username = update.effective_user.username,
        )

        db.add(new_user)
        db.commit()
        query.edit_message_text("✅ Ma'lumotlar saqlandi")
        context.user_data.clear()
        send_menu(update,context)

    elif action == "confirm_retry":
        query.edit_message_text("Ism-sharifingizni yuboring!")
        context.user_data.clear()
        return Register.full_name
