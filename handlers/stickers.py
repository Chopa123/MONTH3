from aiogram import Bot, dispatcher, types, executor

from config import TOKEN

bot=Bot(TOKEN)
dp=dispatcher(bot)

@dp.message_handler(commands=['give'])
async def send_sticker(message:types.message):
    await message.answer(" Милый бот😍")
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJk-hko8aIisYByYA-butKAAHEMLgulfEAAk8MAAIlNMBLcIez7ohUIiUvBA")

@dp.message_handler()
async def send_sticker(message:types.message):
    if message.text == "😍  ":
        await message.answer("😏  ")

if __name__ == "__main__":
    executor.start_polling(dp)
