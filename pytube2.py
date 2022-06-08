import telebot
from pytube import YouTube
import os

token = '5480603651:AAHufk2fZ7GZUFP5YrqncNhF5lNl6xVgH-g'
bot = telebot.TeleBot(token)

current_path = os.path.abspath(os.getcwd())

@bot.message_handler(commands=['start', 'старт'])
def message_send(message):
    us = message.from_user.first_name
    mess = 'Привет '+ us +', просто отправ мне ссылку на видео из YouTube и скачай его!!!'
    bot.send_message(message.chat.id, mess)

@bot.message_handler(content_types='text')
def sendMessage(message):
    url_from = message.text
    down_path = current_path +'/videos/'
    yout = YouTube(url_from) 
    filename = str(yout.title)
    bot.send_message(message.chat.id, 'Пожалуйста подождите! \n Ваше видео ужу в пути...')
    YouTube(url_from).streams.filter(res="720p").first().download(filename=filename, output_path=down_path)
    path_url = down_path + filename
    vid = open(path_url, 'rb')
    bot.send_video(message.chat.id, vid)

# @bot.message_handler(content_types='text')
# def sendMessage(message): 
#     word = message.text.replace(' ', '')
#     wo = len(word)
#     bot.send_message(message.chat.id, f'Количество всех букв {wo}')


print('Бот запушен')
bot.infinity_polling()