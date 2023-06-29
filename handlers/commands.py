from aiogram.dispatcher.filters import Text

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import time
from database.dp import sql_command_random
from parser.news import parser

async def start_command(message: types.Message):
    await message.answer(f'Hello {message.from_user.full_name}!')

async def get_random_user(message: types.Message) -> None:
    random_user = await sql_command_random()
    await message.answer(random_user)

async def dice(message: types.Message):
    a = await bot.send_dice(message.chat.id, emoji='🎲')
    await bot.send_message(message.chat.id, 'Ваша кость')
    b = await bot.send_dice(message.chat.id, emoji='🎲')
    await bot.send_message(message.chat.id, 'Кость бота')
    time.sleep(5)
    if a.dice.value < b.dice.value:
        await bot.send_message(message.from_user.id, 'Вы проиграли')
    elif a.dice.value == b.dice.value:
        await bot.send_message(message.from_user.id, 'Ничья')
    else:
        await bot.send_message(message.from_user.id, 'Вы выиграли')

async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, 'Это должно быть ответом на сообщение')

async def quiz_1(message: types.message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Next", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Cколько весит самая крупная жемчужина в мире?"
    answers = [
        "60 килограмм",
        "47 килограмм",
        "21 килограмм",
        "34 килограмм"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        explanation='Очень тяжелый крч',
        type='quiz',
        correct_option_id=3,
        open_period=15,
        reply_markup=markup
    )
async def get_news(message: types.Message) -> None:
    news = parser()
    for i in news:
        await message.answer(
            f"{i['url']}\n"
            f"{i['time']}\n"
            f"{i['title']}\n"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(dice, commands=['dice'])
    dp.register_message_handler(get_random_user, Text(equals="get", ignore_case=True))
    dp.register_message_handler(get_news, commands=['news'])
