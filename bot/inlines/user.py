from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from . import inline_names as inn


def guests_list_keyboard(guests) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=f"{ind + 1}. {guest}", callback_data=f"guest_{guest.id}")
        ] for ind, guest in enumerate(guests)
    ]
    buttons.append([InlineKeyboardButton(text=inn.BACK["name"], callback_data=inn.BACK["call_data"])])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def messages_list_keyboard(messages) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=f"{ind + 1}. {message}", callback_data=f"message_{message.id}")
        ] for ind, message in enumerate(messages)
    ]
    buttons.append([InlineKeyboardButton(text=inn.BACK["name"], callback_data=inn.BACK["call_data"])])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def message_info_keyboard(message_id) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=inn.ANSWER_TO_MESSAGE["name"], callback_data=inn.ANSWER_TO_MESSAGE['call_data'].format(message_id)),
            InlineKeyboardButton(text=inn.BACK["name"], callback_data=inn.BACK["call_data"])
        ]
    ])


def update_info_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=inn.UPDATE_INFO["name"], callback_data=inn.UPDATE_INFO["call_data"])
        ]
    ])


def back() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=inn.BACK["name"], callback_data=inn.BACK["call_data"])
        ]
    ])