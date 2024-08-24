from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from . import inline_names as inn


def guests_list(guests) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=f"{ind + 1}. {guest}", callback_data=f"guest_{guest.id}")
        ] for ind, guest in enumerate(guests)
    ]
    buttons.append([InlineKeyboardButton(text=inn.BACK["name"], callback_data=inn.BACK["call_data"])])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def messages_list(messages) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=f"{ind + 1}. {message}", callback_data=f"message_{message.id}")
        ] for ind, message in enumerate(messages)
    ]
    buttons.append([InlineKeyboardButton(text=inn.BACK["name"], callback_data=inn.BACK["call_data"])])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def update_info_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=inn.UPDATE_INFO["name"], callback_data=inn.UPDATE_INFO["call_data"])
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard