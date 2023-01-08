import conf

from UTDownloader import UToT

import pathlib

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


class Teletube:

    bot = Bot(token=conf.api_Key)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=["start"])
    async def start_command(message: types.Message):
        await message.reply("Введите ссылку на YouTube видео для пересылки в телеграм")

    @dp.message_handler()
    async def send_video(message: types.Message):
        try:
            downl = UToT(message.text)
            fileName = downl.save_video()
            with open(fileName, 'rb') as video:
                await message.answer_video(video)
            await message.reply(f"Скачал для вас файл {fileName}")
            pathlib.Path(fileName).unlink()
        except Exception as ex:
            await message.reply(ex)


if __name__ == "__main__":
    tt = Teletube
    executor.start_polling(tt.dp)