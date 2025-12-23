import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import TOKEN

id_list_teachers= []
id_list_students= []

bot = Bot(token=TOKEN)

dp = Dispatcher()

button_1 = KeyboardButton(text = 'учитель')
button_2 = KeyboardButton(text = 'ученик')

keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])



@dp.message(Command('start')) # блок начальной фильрации
async def cmd_start(message: Message):
    await message.answer('Привет!')
    if message.chat.id in id_list_students:
        await message.answer('Здравствуй, учащийся школы Ника!')    
    #id_list.append(message.from_user.id)
    elif message.chat.id in id_list_teachers:
        await message.answer('Здравствуте, уважаемый педагог школы Ника ')
    else:
        await message.answer(text = "Здравствуйте, новый пользователь! Пожалуйста, выберите тип вашей регистрации в боте.",
                                reply_markup=keyboard)
        


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Возникли проблемы?Пиши разработчикам в личку: @NKVDKomissar @NIKOLAYVIRUS')

# @dp.message(F.text == 'Как дела?')
# async def how_are_you(message: Message):
#     await message.answer('ОК')

@dp.message(F.text == 'getidlist') # проверка списков id учеников и учителей
async def how_are_you(message: Message):
    await message.answer(id_list_teachers, id_list_students)

# @dp.message(Command('test')) #блок с кнопками
# async def choose_numbers(message: Message):
#     await message.answer(text = "выберите ряд цифр!",
#                          reply_markup=keyboard
#     )

@dp.message(F.text == 'учитель') # блок регистрации учителей
async def process_dog_answer(message: Message):
    id_list_teachers.append(message.chat.id) 
    await message.answer(
        text='Отлично! Вы зарегистрированы как педагог! Пожалуйста, перезагрузите бота командой /start и продолжите работу',
        reply_markup=ReplyKeyboardRemove()
    )



@dp.message(F.text == 'ученик') # блок регистрации учеников
async def process_cucumber_answer(message: Message):
    id_list_teachers.append(message.chat.id)
    await message.answer(
        text='Отлично! Вы зарегистрированы как ученик! Пожалуйста, перезагрузите бота командой /start и продолжите работу',
        reply_markup=ReplyKeyboardRemove()
    )



# async def cmd_start(message: Message):
#     kb = [
#         [KeyboardButton(text = "Трунов")],
#         [KeyboardButton(text = "Осмоловский")],
#         [KeyboardButton(text = "Комиссаров")],
#         [KeyboardButton(text = "Нечаев")]
#     ]
#     keyboard = ReplyKeyboardMarkup(
#         keyboard = kb,
#         resize_keyboard=True,
#         input_field_placeholder = "Выберите педагога:"

#     )
#     await message.answer("Кто лучший учитель в Нике?", reply_markup=keyboard)
# @dp.message(F == "Трунов") 
# async def trunov_good(message: Message):
#     await message.reply("Пятерка по информатике!")



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")