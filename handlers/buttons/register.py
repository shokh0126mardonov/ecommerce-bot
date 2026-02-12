from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton

def confirm():
    keyboard = [
        [
            InlineKeyboardButton("✅ Tasdiqlash", callback_data="confirm_yes"),
            InlineKeyboardButton("🔁 Qaytadan", callback_data="confirm_retry"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def contact():
    keyboard = [[KeyboardButton(
    text="📞 Contactni yuborish",
    request_contact=True
    )]]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )