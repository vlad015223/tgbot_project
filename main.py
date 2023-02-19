from aiogram import types, executor
from config import dp
from buttons import keyboard
from cut_video import *


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=keyboard)


@dp.message_handler(text=['Вернуться в главное меню'])
async def start(message: types.Message):
    await message.answer('Выбери один из вариантов', reply_markup=keyboard)


if __name__ ==  '__main__':
    executor.start_polling(dp)
