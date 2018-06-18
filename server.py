import email_handler
import time
import requests
import bot

with open('telegram.token', 'r') as f:
    token = f.read()

TOKEN = token
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

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
