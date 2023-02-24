from aiogram import types
import os
from config import dp, bot, client
from buttons import back_to_the_main_menu

directory = 'C:/Dev/tgbot_project'


@dp.message_handler(text='Получить аудио из Я. Музыки')
async def get_url(message: types.Message):
    await message.answer('Отправь ссылку на аудио', reply_markup=back_to_the_main_menu)


"""
TODO:
Исправить ошибку которая выходит если в названии есть / (https://music.yandex.ru/album/12697519/track/73259141)
FileNotFoundError: [Errno 2] No such file or directory: "Hollywood's Bleeding / Numb"
"""
@dp.message_handler(regexp='https://music.yandex.ru')
async def download_track(message: types.Message):
    track_id = message.text.split('/')[6] + ':' + message.text.split('/')[4]
    audio_title = client.tracks([track_id])[0]['title']
    client.tracks([track_id])[0].download(f'{audio_title}')

    final_directory = f'{directory}/{audio_title}'
    audio = open(final_directory, 'rb')
    await bot.send_audio(message.chat.id, audio)
    
    audio.close()
    os.remove(final_directory)


@dp.message_handler(regexp='utm_medium=copy_link')
async def download_track_mobile(message: types.Message):
    track_id = message.text[:-21].split('/')[6] + ':' + message.text[:-21].split('/')[4]
    audio_title = client.tracks([track_id])[0]['title']
    client.tracks([track_id])[0].download(f'{audio_title}')

    final_directory = f'{directory}/{audio_title}'
    audio = open(final_directory, 'rb')
    await bot.send_audio(message.chat.id, audio)
    
    audio.close()
    os.remove(final_directory)
