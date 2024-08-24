from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from bot.states.user import User
from bot.keyboards.user import user_main_menu
from bot.inlines.user import update_info_keyboard
from bot.inlines import inline_names as inn
from bot.keyboards import key_names as kn
from bot.models import user as db

router = Router()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    if user := await db.get_user(message.from_user.id):  # Check if user exists in DB
        
        if not user.first_name:
            await message.answer("Iltimos ismingizni kiriting:")
            await state.update_data(update_info=True)
            await state.set_state(User.first_name)
            return

        if not user.last_name:
            await message.answer("Iltimos familiyangizni kiriting:")
            await state.update_data(update_info=True)
            await state.set_state(User.last_name)
            return
        
        if not user.second_name:
            await message.answer("Iltimos sharifingizni kiriting:")
            await state.update_data(update_info=True)
            await state.set_state(User.second_name)
            return
        
        await message.answer("Xush kelibsiz!", reply_markup=user_main_menu())
        await state.set_state(User.main_menu)
        return
        
    await message.answer("Assalomu alaykum!\nIltimos ismingizni kiriting:")
    await state.set_state(User.first_name)


@router.message(User.first_name)
async def process_first_name(message: Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Iltimos familiyangizni kiriting:")
    await state.set_state(User.last_name)


@router.message(User.last_name)
async def process_first_name(message: Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer("Iltimos sharifingizni kiriting:")
    await state.set_state(User.second_name)


@router.message(User.second_name)
async def process_last_name(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_data['second_name'] = message.text
    
    if user_data.get("update_info"):
        del user_data['update_info']
        await message.answer(f"Ma'lumotlaringiz yangilandi!", reply_markup=user_main_menu())
    else:
        await message.answer(f"Xush kelibsiz! Siz muvaffaqiyatli ro'yhatdan o'tdingiz.", reply_markup=user_main_menu())
    
    await db.crete_or_update_user(telegram_id=message.from_user.id, defaults={**user_data})
    
    await state.clear()
    await state.set_state(User.main_menu)


@router.message(User.main_menu, F.text == kn.MY_PROFILE)
async def my_profile(message: Message):
    user = await db.get_user(message.from_user.id)
    await message.answer(
        f"Ismingiz: {user.first_name}\nFamiliyangiz: {user.last_name}\nSharifingiz: {user.second_name}",
        reply_markup=update_info_keyboard()
    )
    

@router.callback_query(User.main_menu, F.data == inn.UPDATE_INFO['call_data'])
async def guest_info(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(update_info=True)
    await callback.message.delete()
    await callback.message.answer("Iltimos ismingizni kiriting:")
    await state.set_state(User.first_name)