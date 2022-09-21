import asyncio
from aiogram import Bot, Dispatcher, executor

from config import token, user_id

from pars_av import get_first_car
bot = Bot(token=token)
dp = Dispatcher(bot)

spisok = []

async def start():
    while True:
        new_car = get_first_car()
        url_car = new_car[-1]
        if url_car in spisok:
            continue
        else:
            spisok.append(url_car)
            await bot.send_message(user_id, new_car)
        await asyncio.sleep(2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start())
    executor.start_polling(dp)
