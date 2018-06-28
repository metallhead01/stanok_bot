from flask import Flask
#from flask_sslify import SSLify
from flask import jsonify
from flask import request
import requests
import json


app = Flask(__name__)  # Исходя из этого имени Flask будет выстраивать все свои зависимости к шаблонам, файлам и т.д.
#sslifi = SSLify(app)  # в качестве аргумента передадим экземпляр класса Flask


def get_token(file_name: str = 'telegram.token')->str:
    with open(file_name, 'r') as f:
        token = f.read()
        return token


URL = f'https://api.telegram.org/bot{get_token("telegram.token")}'


def write_json(data, file_name='answer.json'):  # Пишем в файл json ответ от сервера Telegram
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_updates()-> json:
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()


def send_message(chat_id, text='bla-bla-bla')-> json:
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


@app.route('/', methods=['POST', 'GET'])
def index()-> str:
    if request.method == 'POST':
        r = request.get_json()
        write_json(r)
        return jsonify(r)
    return '<h1>Аннсергевна - сама красивая!</h1>'


# https://api.telegram.org/bot584772341:AAEzHX5p_MCaqZQFmE-oySdF98bro0IPZgw/setWebhook?url=www.alextelebot.tk
def main():
    pass


if __name__ == '__main__':
    app.run()
