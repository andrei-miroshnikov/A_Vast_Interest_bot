import telebot
from telebot import types
import numpy as np
bot = telebot.TeleBot('1605880250:AAFlVEe8CQMIuFY1rRYMcPtuW-UtYMlstjk')

@bot.message_handler(commands=['start','go'])

def message_help(message):
    # Создаем кнопку
    startmenu = types.ReplyKeyboardMarkup(True, True)
    startmenu.row('Нажимай! 😇')
    # Отправляем сообщение и отправляем подключение клавиатуры
    bot.send_message(message.chat.id,'Добро пожаловать!✋ \nЯ бесплатный бот-помощник!', reply_markup=startmenu)
@bot.message_handler(content_types=['text'])

def bot_greeting(message):
    if "привет" in message.text.lower() or "hello" in message.text.lower() or "здравствуй" in message.text.lower() or "hi" in message.text.lower():
        bot.send_message(message.chat.id, 'Приветсвую тебя в лучшем бот-помощнике для лаборотории!')
    else:
        bot.send_message(message.chat.id, "Поприветствуй меня!😇")


bot.polling()
