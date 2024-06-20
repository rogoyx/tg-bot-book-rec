import os

from aiogram import Bot, Dispatcher, types, executor
import requests


TOKEN = os.getenv('TG_TOKEN', '')

HELP_COMMAND = '''
/help - command list
/start - start work
'''

START_COMMAND = '''
Here you can get a list of book recommendation. Just give a short description of desired novel.
'''

EXAMPLE_ANSWER = '''
Here is the list of your book recommendations:
1. Winnie-the-Pooh by A. Milne
2. The Tale of the Pie and the Patty Pan by B. Potter
'''

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(text=START_COMMAND)
#    await message.delete()

@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    await message.reply(text=HELP_COMMAND)
    
#@dp.message_handler()
#async def get_recommendation(message: types.Message):
#    response = requests.post(
#        'http://127.0.0.1:8000/get_ml_recommendation',
#        data={'chat_id': message.chat.id, 'tg_message': message.text}
#    )
#    await message.answer(f'{message.text} send to ml back. Status code: {response.status_code}, elapsed {response.elapsed}')

@dp.message_handler()
async def save_logs(message: types.Message):
    response = requests.post(
        'http://127.0.0.1:8000/save_logs',
        data={'chat_id': message.chat.id, 'tg_message': message.text}
    )
    await message.answer(f'{message.text} send to log save. Status code: {response.status_code}, elapsed {response.elapsed}')

if __name__ == '__main__':
    executor.start_polling(dp)