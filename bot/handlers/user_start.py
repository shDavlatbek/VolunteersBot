from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from bot.states.user import User
from bot.keyboards.user import user_main_menu
from bot.inlines.user import guests_list
from bot.inlines import inline_names as inn
from bot.keyboards import key_names as kn
from bot.models import user as db
from bot.utils import func

router = Router()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    if await db.check_user_exists(message.from_user.id):  # Check if user exists in DB
        await message.answer("Xush kelibsiz!", reply_markup=user_main_menu())
        await state.set_state(User.main_menu)
        return
    await message.answer("Assalomu alaykum!\nIltimos ismingizni yozing:")
    await state.set_state(User.first_name)


@router.message(User.first_name)
async def process_first_name(message: Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Familiyangiz:")
    await state.set_state(User.last_name)


@router.message(User.last_name)
async def process_last_name(message: Message, state: FSMContext):
    user_data = await state.get_data()
    first_name = user_data['first_name']
    last_name = message.text
    
    await db.save_user_to_db(message.from_user.id, first_name, last_name)  # Save user to DB

    await state.clear()
    await message.answer(f"Xush kelibsiz, {first_name} {last_name}! Siz muvaffaqiyatli ro'yhatdan o'tdingiz.", reply_markup=user_main_menu())
    await state.set_state(User.main_menu)


@router.message(User.main_menu, F.text == kn.MY_PROFILE)
async def my_profile(message: Message):
    user = await db.get_user(message.from_user.id)
    await message.answer(f"Ismingiz: {user.first_name}\nFamiliyangiz: {user.last_name}")