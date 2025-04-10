import requests
import time
from kaktus_data import BOT_TOKEN, API_URL


API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL = ' https://random.dog/woof.json'
API_FOXES_URL = 'https://randomfox.ca/floof/'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('


offset = -2
counter = 0
cat_response: requests.Response
cat_link: str


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            text = f'"{result['message']['text']}" это конечно хорошо, но как насчёт котика?'
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']

                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1

PATCH /comments/3 HTTP/1.1
HOST: hexlet.local
Content-Lenth: 20
Content-Type: application/json
{"text": "I got it!"}
            {"id":3,"user_id":12,"text":"I got it!"}

            GET/comments
            HTTP/1.1
            HOST: hexlet.local
