from aiogram import types, Dispatcher
from config import bot, dp

async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)

de fdgjngjn

def register_handlers_extra(dp:Dispatcher):
    dp.register_message_handler(echo)