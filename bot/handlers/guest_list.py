from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from bot.states.user import User
from bot.keyboards.user import user_main_menu
from bot.inlines.user import guests_list_keyboard, back
from bot.inlines import inline_names as inn
from bot.keyboards import key_names as kn
from bot.models import user as db
from bot.utils import func

router = Router()


@router.message(User.main_menu, F.text == kn.ADDED_GUESTS)
async def added_guests(message: Message, state: FSMContext):
    if guests := await db.get_guests(await db.get_user(message.from_user.id)):
        await message.answer(
            text=f"Sizga {len(guests)} ta mehmon biriktirilgan",
            reply_markup=ReplyKeyboardRemove()
        )
        await message.answer(
            text="Mehmonlar ma'lumotlarini ko'rish uchun birini tanlang:",
            reply_markup=guests_list_keyboard(guests)
        )
        await state.set_state(User.guests_list)
    else:
        await message.answer("Sizga biriktirilgan mehmonlar mavjud emas")
        return


@router.callback_query(User.guests_list, F.data.startswith("guest_"))
async def guest_info(callback: types.CallbackQuery, state: FSMContext):
    guest_id = callback.data.split("_")[1]
    guest_info = await db.get_guest_info(guest_id)
    await callback.answer()
    await callback.message.edit_text(f"Mehmon haqida ma'lumot:\n{await func.guest_info(guest_info)}", reply_markup=back())
    await state.set_state(User.guest_info)


@router.callback_query(User.guest_info, F.data == inn.BACK["call_data"])
async def back_to_main_menu(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    if guests := await db.get_guests(await db.get_user(message.chat.id)):
        await message.edit_text(
            text="Mehmonlar ma'lumotlarini ko'rish uchun birini tanlang:",
            reply_markup=guests_list_keyboard(guests)
        )
        await state.set_state(User.guests_list)
    else:
        await message.delete()
        await message.answer("Sizga biriktirilgan mehmonlar mavjud emas", reply_markup=user_main_menu())
        await state.set_state(User.main_menu)


@router.callback_query(User.guests_list, F.data == inn.BACK["call_data"])
async def back_to_main_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer("Asosiy menyu", reply_markup=user_main_menu())
    await state.set_state(User.main_menu)