from aiogram import Bot, Dispatcher
from yandex_music import Client

TOKEN_API = '6038040501:AAF0oDt-TtESHnwucv-sZra0YgznTQYVA34'

music_token = 'AQAAAAAx154uAAG8XvQ6lxavIUhboStHhtmkOi0'
client = Client(music_token).init()

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)