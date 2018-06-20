import telebot
from telebot.types import Message
from telebot import types
import keyboard_buttons


with open('telegram.token', 'r') as f:
    token = f.read()
TOKEN = token
STICKER_ID = 'CAADAgADEQIAAvJ-ggwzgX6aU1rEAwI'
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    keyboard = keyboard_buttons.level_1_menu()
    bot.send_message(message.chat.id, "Выберите вариант:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda x: True)
def callback_handler(callback_query):
    message = callback_query.message
    data = callback_query.data
    if data == 'Problem with machine':
        keyboard = keyboard_buttons.level_2_menu()
        bot.send_message(message.chat.id, "Укажите причину:", reply_markup=keyboard)

"""
# Объявим функцию, которая будет отвечать на сообщения
@bot.edited_channel_post_handler(content_types=['text']) # одну и ту же функцию мы можем декорировать несколькими декораторами
@bot.message_handler(content_types=['text'])
def echo_messages(message: Message):
    print(message.text)
    text = message.text
    if text == '1. Станки':
        bot.send_message(message.chat.id, "Выберите модель:", reply_markup=level_2_stanki)
        bot.register_next_step_handler(message.chat.id, "Выберите модель:", reply_markup=level_2_stanki)
    elif text == 'Highflex 1650 FC':
        bot.send_message(message.chat.id, "Выберите причину:", reply_markup=level_3_stanki)
    elif text == 'HPL 300/38/22':
        bot.send_message(message.chat.id, "Выберите причину:", reply_markup=level_3_stanki)
    elif text == 'KTD 720':
        bot.send_message(message.chat.id, "Выберите причину:", reply_markup=level_3_stanki)
    elif text == 'Назад':
        bot.send_message(message.chat.id, "Выберите вариант:", reply_markup=level_1_menu)
    else:
        bot.send_message(message.chat.id, "Неверный выбор")



# Попробуем отправить стикер
@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    print(message)
    print(message.sticker)
    print(message.chat.id)
    # bot.send_sticker(message.chat.id, STICKER_ID) # если нужно отвечать конкретным стикером
    bot.send_sticker(message.chat.id, message.sticker)

"""
bot.polling(timeout=60)  # Настройки таймаута, выбираем в зависимости от качества Интернет-соединения timeout=60

