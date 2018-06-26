import email_handler
import time
import requests
import telebot
from telebot.types import Message
import keyboard_buttons
from contracts import contract
import logging


with open('telegram.token', 'r') as f:
    token = f.read()
TOKEN = token
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
USER_STATE_dict = {}

bot = telebot.TeleBot(TOKEN)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.


@contract()
def update_state(state: 'str'):
    """обновляет статус текущего сеанса - первое сообщение ставит статус 'CONFIRMED'"""
    USER_STATE_dict[0] = {state}


@contract()
def get_state()->'str':
    return USER_STATE_dict[0]


print(f'User_State: {def get_state()}')


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    keyboard = keyboard_buttons.level_1_menu()
    bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=keyboard)
    update_state("PROCESSED")


@bot.callback_query_handler(func=lambda query: True)
def callback_handler(callback_query):
    if get_state() == "PROCESSED":
        print(f'User_State: {get_state()}')
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
            keyboard = keyboard_buttons.confirm()
            bot.send_message(message.chat.id, 'Подтвердите действие:', reply_markup=keyboard)
        elif data == 'back':
            keyboard = keyboard_buttons.level_1_menu()
            bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=keyboard)
        elif data == 'yes':
            bot.send_message(message.chat.id, '✅  Сохранено в базу данных')
            update_state("CONFIRMED")  # обновим статус отчета по станку.
        else:
            keyboard = keyboard_buttons.confirm()
            bot.send_message(message.chat.id, 'Подтвердите действие:', reply_markup=keyboard)

    elif get_state() == "CONFIRMED":  # обработаем попытку нажать кнопки после подтверждения
        message = callback_query.message
        bot.send_message(message.chat.id, '⚠️  Уже сохранено.')
        print(f'User_State: {get_state()}')


"""
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

    else:
        print('wait')

    time.sleep(60)
"""
bot.polling()  # Настройки таймаута, выбираем в зависимости от качества Интернет-соединения timeout=60


