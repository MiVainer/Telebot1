from telebot import *
import psutil
import os
from subprocess import check_output

import config

#main variables
TOKEN = "6916850744:AAF3bgfcmOtmIfp-Tn7nC2NEViMQ_97rLJs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start1(message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Сведения об ОС', callback_data='btn1')
    btn2 = types.InlineKeyboardButton(text='Значение LA', callback_data='btn2')
    btn3 = types.InlineKeyboardButton(text='Место на диске', callback_data='btn3')
    btn4 = types.InlineKeyboardButton(text='Количество inodes', callback_data='btn4')
    btn5 = types.InlineKeyboardButton(text='Время работы системы', callback_data='btn5')
    kb.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(config.chatid, 'Привет бро! Что будем мониторить?', reply_markup=kb)

@bot.callback_query_handler(func = lambda call: True)
def inlinekeyboards(call):
    if call.from_user.id == config.chatid:
        if call.data == "btn1":
            a = check_output(args='uname -a', shell=True)
            bot.send_message(config.chatid, a)
        elif call.data == "btn2":
            b = list(psutil.getloadavg())
            b = f'1 мин - {b[0]}, 5 мин - {b[1]}, 15 мин - {b[2]}'
            bot.send_message(config.chatid, b)
        elif call.data == "btn3":
            c = list(psutil.disk_usage('/'))
            c = f'Диск занят на - {c[3]} %, доступно {int(c[2]/1024/1024/1024)} Гб'
            bot.send_message(config.chatid, c)
        if call.data == "btn4":
            d = check_output(args='df -i', shell=True)
            bot.send_message(config.chatid, d)
        if call.data == "btn5":
            e = check_output(args='uptime -p', shell=True)
            bot.send_message(config.chatid, e)




'''@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    btn1 = types.KeyboardButton(text='uname -a')
    btn2 = types.KeyboardButton(text='/cpu')
    btn3 = types.KeyboardButton(text='df -h')
    btn4 = types.KeyboardButton(text='df -i')
    btn5 = types.KeyboardButton(text='uptime')
    kb.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(config.chatid, 'Привет бро, я бот для мониторинга твоего сервера! Что будем мониторить?', reply_markup=kb)'''
'''
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
'''
@bot.message_handler(content_types=["text"])
def main(message):
   if message.chat.id == config.chatid:
      comand = message.text  #текст сообщения
      try: #если команда невыполняемая - check_output выдаст exception
         bot.send_message(message.chat.id, check_output(comand, shell=True))
      except:
         bot.send_message(message.chat.id, "Команда введена некорректно") #если команда некорректна


# Мониторинг оперативной памяти
MEMORY_THRESHOLD = 80
def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    if memory_percent >= MEMORY_THRESHOLD:
        message = f'Оперативка слишком загружена бро!: {memory_percent}%'
        bot.send_message(config.chatid, text=message)

if __name__ == '__main__':
    check_memory_usage()


bot.polling()