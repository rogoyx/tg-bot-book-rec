import os

from urllib.parse import unquote, unquote_plus

from fastapi import FastAPI, Body
import uvicorn
from httpx import AsyncClient

app = FastAPI()

TG_BACK_PORT = 8080 # TODO: move to config
TOKEN = os.getenv('TG_TOKEN', '')

@app.post('/tg_send_recommendation')
async def tg_send_recommendation(data=Body()):
    data = data.decode().split('&')
    chat_id = data[0].split('=')[1]
    list_string = data[1].split('=')[1]
    rec_list = unquote_plus(unquote(list_string)).replace("'", '').strip('[]').split(', ')
    tg_msg = {'chat_id': chat_id, 'text': rec_list, 'parse_mode': 'Markdown'}
    API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    async with AsyncClient() as client:
        await client.post(API_URL, json=tg_msg)
    return 'ok'


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=TG_BACK_PORT)
