from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config import bot, dp
import logging
import random


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f'Hello {message.from_user.full_name}!')

@dp.message_handler(commands=['mem'])
async def mem_command(message: types.message):
    images = ["media/meme1.jpg", "media/meme2.jpg", "media/meme3.jpg"]
    photo = open(random.choice(images), 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.callback_query):

    question = "Сколько человек каждый день становятся миллионерами?"
    answers = [
        "2000",
        "1750",
        "2500",
        "2090"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        explanation="То есть 2 миллионера в минуту!",
        type='quiz',
        correct_option_id=2,
        open_period=20,
    )


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)