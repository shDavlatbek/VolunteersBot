import asyncio
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
from django.conf import settings

if not settings.configured:
    django.setup()

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage

from .config_reader import config
from bot.handlers import user_start, guest_list, messages


def create_bot() -> Bot:
    return Bot(
        token=config.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher(storage=RedisStorage(config.redis_url.get_secret_value()))
    dp.include_routers(user_start.router)
    dp.include_routers(guest_list.router)
    dp.include_routers(messages.router)
    return dp


async def run_bot(bot: Bot, dp: Dispatcher):
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    bot = create_bot()
    dp = create_dispatcher()
    asyncio.run(run_bot(bot, dp))