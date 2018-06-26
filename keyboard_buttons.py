from telebot import types


def level_1_menu():
    level_1_menu_keyboard = types.InlineKeyboardMarkup()
    level_1_menu_buttons = [
        types.InlineKeyboardButton(text='⚙  Проблема со станком ️', callback_data='problem_with_machine'),
        types.InlineKeyboardButton(text='❓  Нечеткое задание (проблемы оформления)', callback_data='wrong_task'),
        types.InlineKeyboardButton(text='🏠  Склад ', callback_data='warehouse'),
        types.InlineKeyboardButton(text='👷  Операторы ', callback_data='operators'),
        types.InlineKeyboardButton(text='🛑  Нет задания – огрехи планирования', callback_data='no_task')]
    level_1_menu_keyboard.add(level_1_menu_buttons[0])
    level_1_menu_keyboard.add(level_1_menu_buttons[1])
    level_1_menu_keyboard.add(level_1_menu_buttons[2])
    level_1_menu_keyboard.add(level_1_menu_buttons[3])
    level_1_menu_keyboard.add(level_1_menu_buttons[4])
    return level_1_menu_keyboard


def level_2_machine_errors():
    level_2_menu_keyboard = types.InlineKeyboardMarkup()
    level_2_menu_buttons = [
    types.InlineKeyboardButton(text='a. Компьютер завис', callback_data='level_2_PC_down'),
    types.InlineKeyboardButton(text='b. Клеенаносящий узел', callback_data='level_2_Uzel_Kley'),
    types.InlineKeyboardButton(text='c. Подфуговка', callback_data='level_2_Podfugovka'),
    types.InlineKeyboardButton(text='d. Торцовка', callback_data='level_2_Torec'),
    types.InlineKeyboardButton(text='e. Радиусная обработка фрезами', callback_data='level_2_Radius'),
    types.InlineKeyboardButton(text='f. Раунд – фрезы', callback_data='level_2_Round'),
    types.InlineKeyboardButton(text='g. Цикли', callback_data='level_2_Cicles'),
    types.InlineKeyboardButton(text='⬅ Назад', callback_data='back')]
    level_2_menu_keyboard.add(level_2_menu_buttons[0])
    level_2_menu_keyboard.add(level_2_menu_buttons[1])
    level_2_menu_keyboard.add(level_2_menu_buttons[2])
    level_2_menu_keyboard.add(level_2_menu_buttons[3])
    level_2_menu_keyboard.add(level_2_menu_buttons[4])
    level_2_menu_keyboard.add(level_2_menu_buttons[5])
    level_2_menu_keyboard.add(level_2_menu_buttons[6])
    level_2_menu_keyboard.add(level_2_menu_buttons[7])
    return level_2_menu_keyboard


def level_2_task():
    level_2_task_keyboard = types.InlineKeyboardMarkup()
    level_2_task_buttons = [
        types.InlineKeyboardButton(text='a. Указать номер заказа', callback_data='set_order_number'),
        types.InlineKeyboardButton(text='⬅ Назад', callback_data='back')]
    level_2_task_keyboard.add(*level_2_task_buttons)
    return level_2_task_keyboard

def level_2_warehouse():
    level_2_warehouse_keyboard = types.InlineKeyboardMarkup()
    level_2_warehouse_buttons = [
        types.InlineKeyboardButton(text='a. Мало кромки', callback_data='malo_kromki'),
        types.InlineKeyboardButton(text='b. Нет кромки вообще к заказу', callback_data='net_kromki'),
        types.InlineKeyboardButton(text='⬅ Назад', callback_data='back')]
    level_2_warehouse_keyboard.add(level_2_warehouse_buttons[0])
    level_2_warehouse_keyboard.add(level_2_warehouse_buttons[1])
    level_2_warehouse_keyboard.add(level_2_warehouse_buttons[2])
    return level_2_warehouse_keyboard


def level_2_operators():
    level_2_operators_keyboard = types.InlineKeyboardMarkup()
    level_2_operators_buttons = [
        types.InlineKeyboardButton(text='🚭  Перекур не по графику', callback_data='perekur'),
        types.InlineKeyboardButton(text='¯\_(ツ)_/¯  Кривые руки', callback_data='krivie_ruki'),
        types.InlineKeyboardButton(text='⬅ Назад', callback_data='back')]
    level_2_operators_keyboard.add(level_2_operators_buttons[0])
    level_2_operators_keyboard.add(level_2_operators_buttons[1])
    level_2_operators_keyboard.add(level_2_operators_buttons[2])
    return level_2_operators_keyboard


def confirm():
    confirm_keyboard = types.InlineKeyboardMarkup()
    confirm_buttons = [
        types.InlineKeyboardButton(text='🆗 Да', callback_data='yes'),
        types.InlineKeyboardButton(text='⬅ Назад / Нет', callback_data='back')]
    confirm_keyboard.add(*confirm_buttons)
    return confirm_keyboard
