from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from config import TOKEN
from kb_telebot import menu

from parser_ import Client


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здраствуйте {0.first_name}'.format(message.from_user), reply_markup=menu)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('Мы можем отправлять вам адрес')



@dp.message_handler(commands=['parse'])
async def start_parse(message: types.Message):
    await bot.send_message(message.from_user.id, 'start parsing')
    parser = Client()
    parser.run()
    await bot.send_message(message.from_user.id, 'end parsing')


@dp.message_handler(commands=['read_parse'])
async def start_parse(message: types.Message):
    import os
    import pathlib
    path = pathlib.Path(__file__).resolve().parent
    # print(path)
    csv_path = os.path.join(path, 'test.csv')
    # print(csv_path)

    msg = ''
    with open(csv_path) as file:
        # count = int(msg.text)
        for line in file.readlines()[:20]:
                
            price, name, unicode, href = map(
                lambda x: x.rstrip('\n'), 
                line.split(',')
            )
            msg += '\n'.join(
                (
                    f'Цена продукта - {price}',
                    f'Name продукта - {name}\n',
                )
            )
    await bot.send_message(message.from_user.id, msg)    


@dp.message_handler()
async def order_commands(message: types.Message):
    if message.text == '/docs':
        await bot.send_message(message.from_user.id, 'Это Swagger\nhttp://127.0.0.1:8000/docs/')
    elif message.text == '/rooms':
        await bot.send_message(message.from_user.id, 'Это чтобы увидеть данные\nhttp://127.0.0.1:8000/rooms/')
    elif message.text == '/admin':
        await bot.send_message(message.from_user.id, 'Это админка\nhttp://127.0.0.1:8000/admin/')
    elif message.text == '/api_token':
        await bot.send_message(message.from_user.id, 'Тут можно брать api token\nhttp://127.0.0.1:8000/account/api/token/')



            # break




executor.start_polling(dp)