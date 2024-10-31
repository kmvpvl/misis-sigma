import telebot
from telebot import types
import os

id_bot = os.getenv("TOKEN")
bot = telebot.TeleBot(id_bot)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'''
Здравствуйте, <b>{message.from_user.first_name}</b> и добро пожаловать в мир <b>SIGMA & CO</b>! 🎉👋

Мы рады представить вам уникальную возможность приобретать стильные ручки и блокноты с помощью нашего способа оплаты – <b>"MISIS COIN"</b>! 🪙

В нашем магазине вы найдёте широкий ассортимент товаров, от классических решений до современных трендов. Просто выберите понравившиеся позиции, и оплатите их с помощью <b>"MISIS COIN"</b> – это просто и удобно!

Если у вас возникнут вопросы или нужна помощь - загляните в меню. 😉 Приятных покупок! 🛍️
'''
    bot.send_message(message.chat.id, mess, parse_mode='html')
    if (message.from_user.first_name == 'сашка') or (message.from_user.first_name == 'at') or (message.from_user.first_name == 'Edgar'):
        mess1 = 'Здравстуй, Хозяин!'
        bot.send_message(message.chat.id, mess1, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    mess = f'''
Чтобы заказать, вам стоит прописать: 
/shop
    
По всем остальным вопросам пишите сюда: @at_1l1
    '''
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(func=lambda msg: msg.text == '/coin')
def coin(message):
    mess = '''<b>MISIS COIN</b> - это система баллов в виде "бобов", которые позже превраться в баллы.'''
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['shop'])
# def shop(message):
#     photo1 = open('', 'rb')
#     photo2 = open('', 'rb')
#     bot.send_photo(message.chat.id, photo1, caption='Ручки мисис 1')
#     bot.send_photo(message.chat.id, photo2, caption='Ручки мисис 2')


@bot.message_handler(func=lambda msg: msg.text == '/shop')
def get_user_photo(message):
    photo1 = open('мысль понятна.jpg', 'rb')
    photo2 = open('ух ручка б.jpg', 'rb')
    bot.send_photo(message.chat.id, photo1, caption='Ручки мисис 1')
    bot.send_photo(message.chat.id, photo2, caption='Ручки мисис 2')
    mess = '''
Для того, чтобы купить ручки, вам нужно перейти в телеграмм бот (@misiscoinbot 🪙) и присылать ему:
<b><code>/spend sigma 10 v</code></b>
(<u>это можно скопировать при нажатии</u>)

После чего вы пишите (@at_1l1) за подтверждением оплаты и уточнением выбранного товара. 😉  
    '''
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True, interval=0)
