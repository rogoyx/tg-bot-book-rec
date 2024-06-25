from typing import List
import json

import numpy as np
import fastapi as _fastapi
import requests
import uvicorn
import psycopg2
import sqlalchemy.orm as _orm
from sqlalchemy.orm import Session

import schemas as _schemas
import services as _services
#from tg_backend.app import TG_BACK_PORT
#from ml_backend.ml_engine import get_ml_recommendation


ML_BACK_PORT = 8000 # TODO: move to config

app = _fastapi.FastAPI()

@app.post("/api/contacts/", response_model=_schemas.Contact)
async def create_contact(contact: _schemas.CreateContact, 
                         db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.create_contact(contact=contact, db=db)

@app.get("/api/contacts/", response_model=List[_schemas.Contact])
async def get_all_contacts(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_contacts(db=db)

@app.get("/api/contacts/{contact_id}", response_model=_schemas.Contact)
async def get_contact(contact_id: int, 
                      db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_contact(contact_id=contact_id, db=db)

@app.post("/api/logs", response_model=_schemas.Logs)
async def logging(logs: _schemas.Logging,
                  db: _orm.Session = _fastapi.Depends(_services.get_db)):
    ''' write logs from tg message to db '''
    return await _services.logging(logs=logs, db=db)

@app.post('/process_log')
async def process_log(tg_data=_fastapi.Body(),
                          db: _orm.Session = _fastapi.Depends(_services.get_db)):
    ''' sends user information to database and sends a list of recomendations to user back
    '''
    data = process_raw_tg(tg_data)

    # 1. save log to db
    new_logs = await logging(logs=data, db=db)

    # 2. get ml rec
    recommendations_list = get_ml_recommendation(data)
    response = requests.post(
        f'http://127.0.0.1:8080/tg_send_recommendation', # f'http://127.0.0.1:{TG_BACK_PORT}/tg_send_recommendation'
        data={'chat_id': data['user_id'], 'recommendations': f'{recommendations_list}'}
    )
    return 'OK save logs and get ml recommendations'

async def ml_recommend(data=_fastapi.Body()):
    ''' sends a list of recomendations back to user via tg_backend fastapi app
    '''
    data = data.decode().split('&')
    chat_id = data[0].split('=')[1]
    msg = data[1].split('=')[1]
    recommendations_list = get_ml_recommendation(msg)
    response = requests.post(
        f'http://127.0.0.1:8080/tg_send_recommendation', # f'http://127.0.0.1:{TG_BACK_PORT}/tg_send_recommendation'
        data={'chat_id': chat_id, 'recommendations': f'{recommendations_list}'}
    )
    return 'OK recommendations'

# TODO put this functions into the ml_engine
def process_raw_tg(tg_data): # TODO make a function processing text with +,.)(!? and date format
    data = tg_data.decode().split('&')
    user_id = data[0].split('=')[1]
    first_name = data[1].split('=')[1]
    username = data[2].split('=')[1]
    message_id = data[3].split('=')[1]
    text = data[4].split('=')[1].replace("+", " ")
    date = data[5].split('=')[1]
    return {'user_id': user_id,
            'first_name': first_name,
            'username': username,
            'message_id': message_id,
            'text': text,
            'date':date}

def get_ml_recommendation(text: str, num_neighbors: int = 5) -> List[str]:
   msg_vector = get_vector_from_msg(text) # np.array([1.1, 5.3, 3.8, ...])
   closest_vectors = get_book_vector_neighbors(msg_vector, num_neighbors) # np.array([[1.1, ...], [1.0, ...] ...])
   book_recomend_list = get_books_from_vectors(closest_vectors) # ['Winnie-the-Pooh by A. Milne', 'The Tale ...']
   return book_recomend_list

def get_vector_from_msg(text: str) -> np.ndarray:
   # text_emb = lang_model.vectorize(text)
   return np.zeros(len(text))

def get_book_vector_neighbors(msg_vector, num_neighbors):
    return msg_vector * num_neighbors

def get_books_from_vectors(closest_vectors):
    return 'aaa' * len(closest_vectors)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=ML_BACK_PORT)
    init_db()
