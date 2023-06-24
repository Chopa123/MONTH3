import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import ADMINS, bot
from database.dp import sql_command_all_ids
from apscheduler.triggers.cron import CronTrigger
async def time_to_sleep(text):
    users = await sql_command_all_ids()
    for users in users:
        await bot.send_message(
            users[0], f"ВставАААй {text}!"
        )
async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(
        time_to_sleep,
        CronTrigger(day_of_week=5, hour=19, minute=23))
    scheduler.start()
