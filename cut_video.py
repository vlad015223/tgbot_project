from aiogram import types
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from os import walk
import os, shutil
from config import dp, bot
from buttons import keyboard, back_to_the_main_menu


folder = 'C:/Dev/tgbot_project/videos'


def cleaning_folder():
    for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


@dp.message_handler(text='Обрезать ютуб-видео')
async def get_url(message: types.Message):
    await message.answer('Отправь ссылку на видео', reply_markup=back_to_the_main_menu)


@dp.message_handler(regexp='https://www.youtube.com/' or 'https://youtu.be')
async def download_720p_mp4_videos(message: types.Message):
    await message.answer('Идёт загрузка. Время загрузки зависит от длительности видео')

    yt = YouTube(str(message))

    yt.streams.filter(file_extension='mp4').get_by_resolution('720p').download(output_path=folder, filename=f'{message.from_user.username}.mp4')

    print('download started')

        #скачиваем видео по ссылке
    try:
        download_720p_mp4_videos(
            str(message.text)
        )
        print('download complete')
        await message.answer('Напиши тайминги в формате 1:30-2:40 (не более 4х минут)', reply_markup=back_to_the_main_menu)

    except:
        await message.answer('Ошибка. Отправь ещё раз', reply_markup=back_to_the_main_menu)
        #чистим папку на всякий случай
        cleaning_folder()


#находим сообщение в формате 1:30-2:40
@dp.message_handler(regexp='\w+:\w+-\w+:\w+')   
async def cut_video(message: types.Message):
    print('subclip started')
    video_title = []
    for filenames in walk(folder):
        video_title.extend(filenames)
        break
    print(video_title)

    video_timings = [message.text]
    for i in video_timings:
        list_of_video_timings = i.split('-')
    print(list_of_video_timings)

    try:
        #переделываем удобные минуты в неудобные секунды
        start = list_of_video_timings[0]
        start_in_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(start.split(':'))))
        end = list_of_video_timings[1]
        end_in_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(end.split(':'))))

        cut = f'{message.from_user.username}'

        #обрезаем видео
        ffmpeg_extract_subclip(f"{folder}/{video_title[-1][-1]}", int(start_in_seconds), int(end_in_seconds), targetname=f"{folder}/{cut}")

        await bot.send_video(message.chat.id, open(f'{folder}/{cut}', 'rb'))
        
        #чистим папку
        cleaning_folder()


    except:
        await message.answer('Не правильно написаны таймкоды :( Напиши, пожалуйста, в формате 2:10-3:15', reply_markup=back_to_the_main_menu)


@dp.message_handler(text=['Вернуться в главное меню'])
async def cut_video(message: types.Message):
    await message.answer('Выбери один из вариантов', reply_markup=keyboard)
    cleaning_folder()