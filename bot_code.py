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

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text in english_greetings:
        bot.send_message(message.chat.id, f'english_greetings[np.random.randint(len(english_greetings))], {message.from_user.first_name})
    elif message.text in russian_greetings:
        bot.send_message(message.chat.id, f'russian_greetings[np.random.randint(len(russian_greetings))], {message.from_user.first_name})
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Ты попросил помощи, но помочь мне тебе нечем... вот тебе заглушка..', reply_markup=keyboard)




bot.polling(True)
