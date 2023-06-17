import random
from aiogram import types
from config import bot, Dispatcher, ADMINS


async def game(message: types.Message):
    if message.from_user.id in ADMINS and message.text.startswith('game'):
        emoji = ['🎲', '🎯', '⚽️', '🏀', '🎰', '🎳']
        random_emoji = random.choice(emoji)
        await bot.send_dice(message.chat.id, emoji=random_emoji)
    elif message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(game)