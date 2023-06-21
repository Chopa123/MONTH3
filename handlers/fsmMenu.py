# =====================================================================================================================
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from config import ADMINS
from keyboards.keyboard import cancel_markup, submit_markup, start_markup
from database.dp import sql_command_start

class FSMadmin(StatesGroup):
    ID = State()
    Name = State()
    Direction = State()
    Age = State()
    Group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('Ты не админ!')

    else:
        await FSMadmin.ID.set()
        await message.answer('ID ментора ?', reply_markup=cancel_markup)


async def load_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ID'] = message.text
    await FSMadmin.next()
    await message.answer('Имя ментора ?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Name'] = message.text
    await FSMadmin.next()
    await message.answer('Направление ментора ?')


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Direction'] = message.text
    await FSMadmin.next()
    await message.answer('Возраст ментора ?')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Age'] = message.text
    await FSMadmin.next()
    await message.answer('Группа ментора ?')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Group'] = message.text
        await message.answer(f"Информация о менторе: \n\n"
                             f"ID-ментора: {data['ID']} \n"
                             f"Имя ментора: {data['Name']} \n"
                             f"Направление ментора: {data['Direction']} \n"
                             f"Возраст ментора: {data['Age']} \n"
                             f"Группа ментора: {data['Group']} \n")

    await FSMadmin.next()
    await message.answer('Всё верно ?', reply_markup=submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_start(state)
        await message.answer('Готово!', reply_markup=start_markup)
        await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('Ну ладно :(', reply_markup=start_markup)
        await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Canceled', reply_markup=start_markup)  # Чтоб после отмены сразу показывались все кнпопки


def register_mentor(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='отмена', ignore_case=True),
                                state='*')

    dp.register_message_handler(fsm_start, commands=['reg_mentor'])
    dp.register_message_handler(load_ID, state=FSMadmin.ID)
    dp.register_message_handler(load_name, state=FSMadmin.Name)
    dp.register_message_handler(load_direction, state=FSMadmin.Direction)
    dp.register_message_handler(load_age, state=FSMadmin.Age)
    dp.register_message_handler(load_group, state=FSMadmin.Group)
    dp.register_message_handler(load_submit, state=FSMadmin.submit)
