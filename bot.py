import asyncio
import time

import nest_asyncio
from aiogram.types import ContentType
from telethon import TelegramClient
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="5310450196:AAG0brtPtXQZoYZBhqcnk7YBBs0DMxk0Deo")
dp = Dispatcher(bot)
nest_asyncio.apply()
client = TelegramClient("client", 14834490, "b392250f1c7031238f11620f75f6707b")


async def register():
    await client.start()
    # await client.log_out()


loop = asyncio.get_event_loop()
loop.run_until_complete(register())


@dp.message_handler(commands=['start'])
async def new_user_joined(message: types.Message):
    print(message.chat.id)


@dp.message_handler(content_types=[ContentType.NEW_CHAT_MEMBERS])
async def new_user_joined(message: types.Message):
    for new_member in message.new_chat_members:
        username = new_member.username
        await client.forward_messages(username, 34, "checkgroupsadding_bot")
        time.sleep(3)
        await client.forward_messages(username, 35, "checkgroupsadding_bot")


executor.start_polling(dp, skip_updates=False)
