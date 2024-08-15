from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from . import key_names as kn

def user_main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=kn.ADDED_GUESTS)
    kb.button(text=kn.MESSAGES)
    kb.button(text=kn.MY_PROFILE)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def back() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=kn.BACK)
    return kb.as_markup(resize_keyboard=True)