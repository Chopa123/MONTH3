import random
import sqlite3

db = sqlite3.connect("bot.sqlite33")
cursor = db.cursor()


def sql_create():

    if db:
        print("База данных подключена!")
        db.execute("CREATE TABLE IF NOT EXISTS mentors "
                   "(ID INTEGER PRIMARY KEY,"
                   "fullname VARCHAR (255), "
                   "direction VARCHAR(255), "
                   "age INTEGER, "
                   "groupp VARCHAR(255))")

    db.commit()

async def sql_command_start(state):
    async with state.proxy() as data:
        cursor.execute(
            "INSERT INTO mentors "
            "(ID, fullname, direction, age, groupp) "
            "VALUES (?, ?, ?, ?, ?)",
            tuple(data.values())
        )
        db.commit()


async def sql_command_random():
    users = cursor.execute("SELECT * FROM mentors").fetchall()
    random_users = random.choice(users)
    return random_users


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_all_ids():
    return cursor.execute("SELECT telegram_id FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (user_id,))
    db.commit()
