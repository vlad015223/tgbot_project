from aiogram import types

main_kb = [
        [types.KeyboardButton(text='Обрезать ютуб-видео')],
        [types.KeyboardButton(text='Получить аудио из Я. Музыки')],
        [types.KeyboardButton(text='Третья кнопка')],
        [types.KeyboardButton(text='Четвертая кнопка')],
        [types.KeyboardButton(text='Пятая кнопка')],
        [types.KeyboardButton(text='Шестая кнопка')]
    ]

keyboard = types.ReplyKeyboardMarkup(
        keyboard=main_kb,
        resize_keyboard=True,
        one_time_keyboard=True,
    )

back_to_the_main_menu = [
    [types.KeyboardButton(text='Вернуться в главное меню')]
]

back_to_the_main_menu = types.ReplyKeyboardMarkup(
        keyboard=back_to_the_main_menu,
        resize_keyboard=True,
        one_time_keyboard=True,
    )