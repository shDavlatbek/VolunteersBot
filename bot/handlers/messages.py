from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from bot.states.user import User
from bot.keyboards.user import user_main_menu
from bot.inlines.user import messages_list
from bot.inlines import inline_names as inn
from bot.keyboards import key_names as kn
from bot.models import user as db
from bot.utils import func


router = Router()


@router.message(User.main_menu, F.text == kn.MESSAGES)
async def message_list(message: Message, state: FSMContext):
    if messages := await db.get_messages(await db.get_user(message.from_user.id)):
        await message.answer(
            text=f"Sizda {len(messages)} ta xabar bor",
            reply_markup=ReplyKeyboardRemove()
        )
        await message.answer(
            text="Xabarni batafsil ko'rish uchun birini tanlang:",
            reply_markup=messages_list(messages)
        )
        await state.set_state(User.messages)
    else:
        await message.answer("Sizda xabarlar mavjud emas")
        return


@router.callback_query(User.messages, F.data.startswith("message_"))
async def message_info(callback: types.CallbackQuery, state: FSMContext):
    message_id = callback.data.split("_")[1]
    message_info = await db.get_message_info(message_id)
    await callback.answer()
    await callback.message.answer(await func.message_info(message_info))


@router.callback_query(User.messages, F.data == inn.BACK["call_data"])
async def back_to_main_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Asosiy menyu", reply_markup=user_main_menu())
    await state.set_state(User.main_menu)