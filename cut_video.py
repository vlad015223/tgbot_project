from aiogram.utils import executor
from aiogram import types
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from os import walk
import os, shutil
from config import dp, bot
from buttons import back_to_the_main_menu

folder = 'C:/Dev/tgbot_proect/videos'


@dp.message_handler(text='Обрезать ютуб-видео')
async def get_url(message: types.Message):
    await message.answer('Отправь ссылку на видео', reply_markup=back_to_the_main_menu)


@dp.message_handler(regexp='https://www.youtube.com/' or 'https://youtu.be')
async def download_720p_mp4_videos(message: types.Message):
    print('start_download')
    await message.answer('Идёт загрузка. Время загрузки зависит от длительности видео')

    yt = YouTube(str(message))

    yt.streams.filter(file_extension='mp4').get_by_resolution('720p').download(folder)

    print('download started')

    try:
        #скачиваем видео по ссылке
        download_720p_mp4_videos(
            str(message.text)
        )
        print('download complete')
        await message.answer('Напиши тайминги в формате 1:30-2:40 (не более 4х минут)', reply_markup=back_to_the_main_menu)

    except:
        #чистим папку на всякий случай если вышла ошибка
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


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

        cut = f'{message.from_user.username}.mp4'

        #обрезаем видео
        ffmpeg_extract_subclip(f"{folder}/{video_title[-1][-1]}", int(start_in_seconds), int(end_in_seconds), targetname=f"{folder}/{cut}")

        if message.from_user.username == cut.split('.mp4')[0]:
            await bot.send_video(message.chat.id, open(f'{folder}/{cut}', 'rb'))
        else:
            await message.answer('Упс.. не получилось😢 Отправь ссылку ещё раз', reply_markup=back_to_the_main_menu)
        
        #чистим папку
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    except:
        await message.answer('Не правильно написаны таймкоды :( Напиши, пожалуйста, в формате 2:10-3:15', reply_markup=back_to_the_main_menu)


if __name__ == '__main__':
    executor.start_polling(dp)