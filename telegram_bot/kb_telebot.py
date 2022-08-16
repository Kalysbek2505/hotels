from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/docs')
b3 = KeyboardButton('/rooms')
b4 = KeyboardButton('/admin')
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(b1,b2,b3,b4)



