from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class User(StatesGroup):
    first_name = State()
    last_name = State()
    second_name = State()
    
    main_menu = State()
    guests_list = State()
    messages = State()