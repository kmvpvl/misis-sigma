import telebot
from telebot import types

id_bot = '7787362795:AAHPCI8elsUlEuES4D8eYgfmguP4z4Eph7Q'
bot = telebot.TeleBot(id_bot)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Каталог ✍️", callback_data="shop")
    markup.add(button)
    mess = f'''
Здравствуйте, <b>{message.from_user.first_name}</b> и добро пожаловать в мир <b>SIGMA & CO</b>! 🎉👋

Мы рады представить вам уникальную возможность приобретать стильные ручки с помощью нашего способа оплаты – <b>"MISIS COIN"</b>! 🪙

'''
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    mess = f'''
Чтобы заказать, вам стоит прописать: 
/shop
    
По всем остальным вопросам пишите сюда: @at_1l1
    '''
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['shop'])
def shop(message):
    markup1 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Купить", callback_data="buy1")
    markup1.add(button1)
    photo1 = open('Мысль понятна?.jpg', 'rb')

    markup2 = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("Купить", callback_data="buy2")
    markup2.add(button2)
    photo2 = open('misis university.jpg', 'rb')

    bot.send_photo(message.chat.id, photo1, caption='Мысль понятна?', reply_markup=markup1)
    bot.send_photo(message.chat.id, photo2, caption='Misis university', reply_markup=markup2)

    mess = '''
Для того, чтобы купить ручки, вам нужно перейти в телеграмм бот <a href="https://t.me/misiscoinbot">@misiscoinbot</a> и присылать ему:
<b><code>/spend sigma 10 v</code></b>
(<u>это можно скопировать при нажатии</u>)  
    '''
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'shop':
        shop(call.message)

    username = call.from_user.username

    if call.data == 'buy1':
        bot.send_message(call.message.chat.id, 'Ваш заказ отправлен администратору.')
        bot.send_message(921640620, f'Вам пришел заказ "Мысль понятна?" от @{username}')

    if call.data == 'buy2':
        bot.send_message(call.message.chat.id, 'Ваш заказ отправлен администратору.')
        bot.send_message(921640620, f'Вам пришел заказ "Мисис ручка" от @{username}')


bot.polling(none_stop=True, interval=0)
