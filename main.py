import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, F, types

dp = Dispatcher()

buffer = 0


@dp.message(F.text.contains("?"))
async def sosal_msg(message: types.Message):
    global buffer
    if buffer == 5:
        await message.answer("Сосал?")
        buffer = 0
    else:
        buffer += 1


@dp.message((F.text == "Да") | (F.text == "да") | (F.text == "ДА"))
async def sosal_ans(message: types.Message):
    if buffer == 0:
        await message.answer("🫵🤣")


async def main():
    TOKEN = str(os.getenv("BOT_TOKEN"))
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
