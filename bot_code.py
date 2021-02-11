import telebot
from telebot import types
import numpy as np
bot = telebot.TeleBot('1605880250:AAFlVEe8CQMIuFY1rRYMcPtuW-UtYMlstjk')



keyboard = telebot.types.ReplyKeyboardMarkup(False,True)
keyboard.row('заглушка 1', 'заглушка 2', 'заглушка 3','заглушка 4')

@bot.message_handler(commands=['start'])
def send_welcome(message):
         bot.reply_to(message, f'Привет, {message.from_user.first_name}. Я бот. Чтобы начать, напиши \'Hello\' или \'Привет\'.')

        
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Ты попросил помощи, но помочь мне тебе нечем... вот тебе заглушка..', reply_markup=keyboard)

    
    
   
bot.polling(True)
