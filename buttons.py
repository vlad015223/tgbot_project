from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

b1 = KeyboardButton('Перевод текста')
b2 = KeyboardButton('Обрезать ютуб-видео')
b3 = KeyboardButton('Отправить mp3 файл из ютуб-видео')
b4 = KeyboardButton('Получить аудио из Я. Музыки')
b5 = KeyboardButton('Игра камень-ножницы-бумага')
b6 = KeyboardButton('Отправить анекдот')
b7 = KeyboardButton('Отправить погоду')
b8 = KeyboardButton('Режим агрессии')

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.row(b1, b2).row(b3, b4, b5).row(b6, b7, b8)

back_to_the_main_menu = [
    [types.KeyboardButton(text='Вернуться в главное меню')]
]

back_to_the_main_menu = types.ReplyKeyboardMarkup(
        keyboard=back_to_the_main_menu,
        resize_keyboard=True,
        one_time_keyboard=True,
    )