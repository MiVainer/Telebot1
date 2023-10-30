from telebot import *
import psutil
import os
from subprocess import check_output

import config

#main variables
TOKEN = "6916850744:AAF3bgfcmOtmIfp-Tn7nC2NEViMQ_97rLJs"
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(config.chatid, 'Привет бро, я бот для мониторинга твоего сервера! Что будем мониторить? \n'
                                    '/id - ChatID бота\n'
                                    '/cpu - инфа о процессоре\n')

@bot.message_handler(commands=['id'])
def iden(message):
    bot.send_message(config.chatid, f'Твой ChatID - {message.chat.id}')

@bot.message_handler(commands=['cpu'])
def la(message):
    if message.chat.id == config.chatid:
        try:
            sysload = str(psutil.getloadavg())
            cpuutil = str(psutil.cpu_percent(percpu=True))
            cpu = ("*System load (1,5,15 min):* _") + sysload + ("_\n*CPU utilization %:* _") + cpuutil + "_"
            bot.send_message(config.chatid, text=cpu, parse_mode='Markdown')
        except:
            bot.send_message(config.chatid, "Can't get CPU info")
        else:
            pass

@bot.message_handler(content_types=["text"])
def main(message):
   if message.chat.id == config.chatid:
      comand = message.text  #текст сообщения
      try: #если команда невыполняемая - check_output выдаст exception
         bot.send_message(message.chat.id, check_output(comand, shell = True))
      except:
         bot.send_message(message.chat.id, "Invalid input") #если команда некорректна

bot.polling()