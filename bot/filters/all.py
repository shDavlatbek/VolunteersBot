from aiogram.filters import BaseFilter
from aiogram import types
from aiogram.fsm.context import FSMContext


class CustomFilter(BaseFilter):
    async def __call__(self, m: types.Message):
        # return True or False
        pass