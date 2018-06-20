import email_handler
import time
import requests
import telebot
from telebot.types import Message
import keyboard_buttons



with open('telegram.token', 'r') as f:
    token = f.read()

TOKEN = token
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    keyboard = keyboard_buttons.level_1_menu()
    bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda x: True)
def callback_handler(callback_query):
    message = callback_query.message
    data = callback_query.data
    if data == 'problem_with_machine':
        keyboard = keyboard_buttons.level_2_machine_errors()
        bot.send_message(message.chat.id, 'Укажите причину:', reply_markup=keyboard)
    elif data == 'wrong_task':
        keyboard = keyboard_buttons.level_2_task()
        bot.send_message(message.chat.id, 'Укажите причину:', reply_markup=keyboard)
    elif data == 'warehouse':
        keyboard = keyboard_buttons.level_2_warehouse()
        bot.send_message(message.chat.id, 'Укажите причину:', reply_markup=keyboard)
    elif data == 'operators':
        keyboard = keyboard_buttons.level_2_operators()
        bot.send_message(message.chat.id, 'Укажите причину:', reply_markup=keyboard)
    elif data == 'no_task':
        pass
    elif data == 'back':
        keyboard = keyboard_buttons.level_1_menu()
        bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=keyboard)
    else:
        pass


while True:
    li_st = email_handler.read_email_from_gmail()
    i = 0
    if li_st:
        while i <= len(li_st):
            element = li_st.pop()
            payload = {
                'chat_id': '149017157',
                'text': element[2],
            }
            try:
                r = requests.post(f'{MAIN_URL}/sendMessage', data=payload)
                i += 1
            except Exception as e:
                print(str(e))

        bot.polling(timeout=60)  # Настройки таймаута, выбираем в зависимости от качества Интернет-соединения timeout=60
    else:
        print('wait')

    time.sleep(60)




