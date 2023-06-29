from aiogram.utils import executor
from config import dp, bot, ADMINS
import logging
from handlers import commands, callback, extra, fsmMenu, notifications
from database.dp import sql_create


commands.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmMenu.register_mentor(dp)
extra.register_handlers_extra(dp)


async def on_startup(dp):
    sql_create()
    await bot.send_message(ADMINS[0], "Hello!")
    await notifications.set_scheduler()


async def on_shutdown(dp):
    await bot.send_message(ADMINS[0], "BYE BYE!")



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
