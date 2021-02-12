import telebot
from telebot import types
import numpy as np
import os

bot = telebot.TeleBot(os.environ.get('TOKEN'))

english_greetings = ['Hi', 'Hey' 'Hello', 'Good to see you', 'I greet you']
russian_greetings = ['Привет', 'Здравствуй', 'Приветствую', 'Салют', 'Рад тебя видеть']

keyboard = telebot.types.ReplyKeyboardMarkup(False,True)
keyboard.row('команда 1', 'команда 2', 'команда 3','команда 4')


@bot.message_handler(commands=['start'])
def send_welcome(message):
         bot.reply_to(message, f'Привет, {message.from_user.first_name}. Инициализация прошла успешно. Для списка доступных команд напишите /help')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Ты попросил помощи, но помочь мне тебе нечем... вот тебе заглушка..', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    for i in english_greetings:
        if message.text == i:
            bot.send_message(message.chat.id, english_greetings[np.random.random_integers(len(english_greetings))], ',', {message.from_user.first_name})
    for n in russian_greetings:
        if message.text == n:
            bot.send_message(message.chat.id, russian_greetings[np.random.random_integers(len(russian_greetings))], ',', {message.from_user.first_name})





bot.polling(True)
