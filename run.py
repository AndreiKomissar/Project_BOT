import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from config import TOKEN

bot = Bot(token=TOKEN)

dp = Dispatcher()

answers = {
    "Трунов": "ответ"
}
#print(answers["Трунов"])
#answers[" Ytxftd"] = "other answer"

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.answer('Это 1 сообщение!')

@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

@dp.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('ОК')

@dp.message(Command('test')) #блок с кнопками
async def cmd_start(message: Message):
    kb = [
        [KeyboardButton(text = "Трунов")],
        [KeyboardButton(text = "Осмоловский")],
        [KeyboardButton(text = "Комиссаров")],
        [KeyboardButton(text = "Нечаев")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard = kb,
        resize_keyboard=True,
        input_field_placeholder = "Выберите педагога:"

    )
    await message.answer("Кто лучший учитель в Нике?", reply_markup=keyboard)
@dp.message(F == "Трунов") 
async def trunov_good(message: Message):
    await message.reply("Пятерка по информатике!")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")