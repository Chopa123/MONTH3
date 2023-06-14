from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp



async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Next", callback_data="button_call_2")
    markup.add(button_call_1)

    question = "Самый долгий полёт курицы?"
    answers = [
        "1 минута",
        "13 секунд",
        "3 секунды",
        "28 секунд"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        explanation='Курица это птица',
        type='quiz',
        correct_option_id=1,
        open_period=10,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):

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



def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")