from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.keyboard import cancel_markup, submit_markup, type_of_direction_markup
from config import ADMINS


class FSMMenu(StatesGroup):
    name = State()
    Direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer(" вы не админ")
    else:
        await FSMMenu.name.set()
        await message.answer(" как зовут ментора?", reply_markup=cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMMenu.next()
    await message.answer('Какое у вас направление?', reply_markup=cancel_markup)


async def load_type_of_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Direction'] = message.text
    await FSMMenu.next()
    await message.answer("Скока лет?", reply_markup=cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMMenu.next()
    await message.answer("Все верно?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        # TODO: Запись в БД
        await state.finish()
        await message.answer("Записал в Базу Данных!")
    elif message.text.lower() == 'заново':
        await FSMMenu.name.set()
        await message.answer("Как звать?")
    else:
        await message.answer("Используй кнопки!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Как хочешь, два раза не предлагаем!")
    else:
        await message.answer("Что ты отменяешь?!")


def register_handlers_fsmMenu(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, commands=['cancel'], state='*')
    dp.register_message_handler(cancel_reg, Text(equals="отмена", ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMMenu.name)
    dp.register_message_handler(load_age, state=FSMMenu.age)
    dp.register_message_handler(load_type_of_direction, state=FSMMenu.age)
    dp.register_message_handler(submit, state=FSMMenu.submit)
