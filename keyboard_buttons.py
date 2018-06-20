from telebot import types
"""
level_1_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_1 = types.KeyboardButton('1. Проблема со станком')
menu_2 = types.KeyboardButton('2. Нечеткое задание (проблемы оформления)')
menu_3 = types.KeyboardButton('3. Склад')
menu_4 = types.KeyboardButton('4. Операторы')
menu_5 = types.KeyboardButton('5. Нет задания – огрехи планирования')
level_1_menu.row(menu_1, menu_2)
level_1_menu.row(menu_3, menu_4, menu_5)

level_2_stanki = types.ReplyKeyboardMarkup(resize_keyboard=True)
stanok_1_1 = types.KeyboardButton('Highflex 1650 FC')
stanok_2_1 = types.KeyboardButton('HPL 300/38/22')
stanok_3_1 = types.KeyboardButton('KTD 720')
stanok_4_1 = types.KeyboardButton('Назад')
level_2_stanki.row(stanok_1_1, stanok_2_1, stanok_3_1, stanok_4_1)

level_3_stanki = types.ReplyKeyboardMarkup(row_width=2)
stanok_1_2 = types.KeyboardButton('a. Компьютер завис')
stanok_2_2 = types.KeyboardButton('b. Клеенаносящий узел')
stanok_3_2 = types.KeyboardButton('c. Подфуговка')
stanok_4_2 = types.KeyboardButton('d. Торцовка')
stanok_5_2 = types.KeyboardButton('e. Радиусная обработка фрезами')
stanok_6_2 = types.KeyboardButton('f. Раунд – фрезы')
stanok_7_2 = types.KeyboardButton('g. Цикли')
stanok_8_2 = types.KeyboardButton('Назад')
level_3_stanki.add(stanok_1_2, stanok_2_2, stanok_3_2, stanok_4_2)
level_3_stanki.add(stanok_5_2, stanok_6_2, stanok_7_2, stanok_8_2)

level_2_zadanie = types.ReplyKeyboardMarkup()
task_1 = types.KeyboardButton('a. Указать номер заказа')
task_2 = types.KeyboardButton('Назад')

level_2_sklad = types.ReplyKeyboardMarkup()
storage_1 = types.KeyboardButton('a. Мало кромки')
storage_2 = types.KeyboardButton('b. Нет кромки вообще к заказу')
storage_3 = types.KeyboardButton('Назад')

level_2_operatori = types.ReplyKeyboardMarkup()
operator_1 = types.KeyboardButton('a. Перекур не по графику')
operator_2 = types.KeyboardButton('b. Кривые руки')
operator_3 = types.KeyboardButton('Назад')
"""


def level_1_menu():
    level_1_menu_keyboard = types.InlineKeyboardMarkup()
    level_1_menu_buttons = [
        types.InlineKeyboardButton(text='1. Проблема со станком', callback_data='Problem with machine'),
        types.InlineKeyboardButton(text='2. Нечеткое задание (проблемы оформления)', callback_data='Wrong task'),
        types.InlineKeyboardButton(text='3. Склад', callback_data='Warehouse'),
        types.InlineKeyboardButton(text='4. Операторы', callback_data='Operators'),
        types.InlineKeyboardButton(text='5. Нет задания – огрехи планирования', callback_data='No task')]
    level_1_menu_keyboard.add(level_1_menu_buttons[0])
    level_1_menu_keyboard.add(level_1_menu_buttons[1])
    level_1_menu_keyboard.add(level_1_menu_buttons[2])
    level_1_menu_keyboard.add(level_1_menu_buttons[3])
    level_1_menu_keyboard.add(level_1_menu_buttons[4])
    return level_1_menu_keyboard


def level_2_menu():
    level_2_menu_keyboard = types.InlineKeyboardMarkup()
    level_2_menu_buttons = [
    types.InlineKeyboardButton(text='a. Компьютер завис', callback_data='level_2_PC_down'),
    types.InlineKeyboardButton(text='b. Клеенаносящий узел', callback_data='level_2_Uzel_Kley'),
    types.InlineKeyboardButton(text='c. Подфуговка', callback_data='level_2_Podfugovka'),
    types.InlineKeyboardButton(text='d. Торцовка', callback_data='level_2_Torec'),
    types.InlineKeyboardButton(text='e. Радиусная обработка фрезами', callback_data='level_2_Radius'),
    types.InlineKeyboardButton(text='f. Раунд – фрезы', callback_data='level_2_Round'),
    types.InlineKeyboardButton(text='g. Цикли', callback_data='level_2_Cicles'),
    types.InlineKeyboardButton(text='Назад', callback_data='level_2_Back')]
    level_2_menu_keyboard.add(level_2_menu_buttons[0])
    level_2_menu_keyboard.add(level_2_menu_buttons[1])
    level_2_menu_keyboard.add(level_2_menu_buttons[2])
    level_2_menu_keyboard.add(level_2_menu_buttons[3])
    level_2_menu_keyboard.add(level_2_menu_buttons[4])
    level_2_menu_keyboard.add(level_2_menu_buttons[5])
    level_2_menu_keyboard.add(level_2_menu_buttons[6])
    level_2_menu_keyboard.add(level_2_menu_buttons[7])
    return level_2_menu_keyboard


"""
menu_1 = types.InlineKeyboardButton(text='1. Проблема со станком', callback_data='1. Проблема со станком')
menu_2 = types.InlineKeyboardButton(text='2. Нечеткое задание (проблемы оформления)', callback_data='2. Нечеткое задание (проблемы оформления)')
menu_3 = types.InlineKeyboardButton(text='3. Склад', callback_data='3. Склад')
menu_4 = types.InlineKeyboardButton(text='4. Операторы', callback_data='4. Операторы')
menu_5 = types.InlineKeyboardButton(text='5. Нет задания – огрехи планирования', callback_data='5. Нет задания – огрехи планирования')

level_1_menu.row(menu_1, menu_2)
level_1_menu.row(menu_3, menu_4, menu_5)

level_2_stanki = types.InlineKeyboardMarkup(row_width=2)
stanok_1_1 = types.InlineKeyboardButton('Highflex 1650 FC')
stanok_2_1 = types.InlineKeyboardButton('HPL 300/38/22')
stanok_3_1 = types.InlineKeyboardButton('KTD 720')
stanok_4_1 = types.InlineKeyboardButton('Назад')
level_2_stanki.row(stanok_1_1, stanok_2_1, stanok_3_1, stanok_4_1)

level_2_stanki = types.InlineKeyboardMarkup(row_width=8)
stanok_1_2 = types.InlineKeyboardButton('a. Компьютер завис')
stanok_2_2 = types.InlineKeyboardButton('b. Клеенаносящий узел')
stanok_3_2 = types.InlineKeyboardButton('c. Подфуговка')
stanok_4_2 = types.InlineKeyboardButton('d. Торцовка')
stanok_5_2 = types.InlineKeyboardButton('e. Радиусная обработка фрезами')
stanok_6_2 = types.InlineKeyboardButton('f. Раунд – фрезы')
stanok_7_2 = types.InlineKeyboardButton('g. Цикли')
stanok_8_2 = types.InlineKeyboardButton('Назад')
level_3_stanki.add(stanok_1_2, stanok_2_2, stanok_3_2, stanok_4_2)
level_3_stanki.add(stanok_5_2, stanok_6_2, stanok_7_2, stanok_8_2)

level_2_zadanie = types.ReplyKeyboardMarkup()
task_1 = types.KeyboardButton('a. Указать номер заказа')
task_2 = types.KeyboardButton('Назад')

level_2_sklad = types.ReplyKeyboardMarkup()
storage_1 = types.KeyboardButton('a. Мало кромки')
storage_2 = types.KeyboardButton('b. Нет кромки вообще к заказу')
storage_3 = types.KeyboardButton('Назад')

level_2_operatori = types.ReplyKeyboardMarkup()
operator_1 = types.KeyboardButton('a. Перекур не по графику')
operator_2 = types.KeyboardButton('b. Кривые руки')
operator_3 = types.KeyboardButton('Назад')
"""