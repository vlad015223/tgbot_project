from aiogram import Bot, Dispatcher
from yandex_music import Client
from decouple import config

TOKEN_API = config('TOKEN_API')
music_token = config('music_token')
client = Client(music_token).init()

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
