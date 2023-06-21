from aiogram import types, Dispatcher
from config import bot, ADMINS
from random import choice


async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)

    if message.from_user.id in ADMINS and message.text.startswith('game'):
        emoji = ['🎲', '🎯', '⚽️', '🏀', '🎰', '🎳']
        random_emoji = choice(emoji)
        await bot.send_dice(message.chat.id, emoji=random_emoji)
    elif message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
