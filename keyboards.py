from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from configs import CATEGORIES


def buttons_category():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = []
    for category in CATEGORIES.keys():
        btn = KeyboardButton(text=category)
        buttons.append(btn)
    markup.add(*buttons)
    return markup


def button_link(link):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='Tugamani bosing 👉🏻', url=link)
    markup.add(btn)
    return markup
