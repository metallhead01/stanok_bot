import requests

TOKEN = "584772341:AAEzHX5p_MCaqZQFmE-oySdF98bro0IPZgw"
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

r = requests.get(f'{MAIN_URL}/getUpdates')

print(r.json())

payload = {
    'chat_id': '149017157',
    'text': 'Hi man!',
    'reply_to_message_id': 14
}

r_1 = requests.post(f'{MAIN_URL}/sendMessage', data=payload)

