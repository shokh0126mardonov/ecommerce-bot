from telegram import ReplyKeyboardMarkup,KeyboardButton


def button_menu():
    keyboard = [
        [KeyboardButton('🛍 Mahsulotlar')],
        [KeyboardButton('🔥 Aksiyalar / Tavsiyalar')],
        [KeyboardButton('📦 Buyurtmalarim')],
        [KeyboardButton('👤 Profil'), KeyboardButton('📞 Yordam')],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )