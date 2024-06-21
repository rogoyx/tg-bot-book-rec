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
    return await _services.logging(logs=logs, db=db)

@app.post("/insert_into_database")
async def db_func():
    #conn = psycopg2.connect(host=HOST_DB, port=PORT, database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD)
    #cur = conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXIST test_table (id serial PRIMARY KEY, user VARCHAR (255) NOT NULL, message VARCHAR (255), date DATE)", )
    #cur.execute("INSERT INTO test_table (id, user, message, date) VALUES(%s, %s, %s, %s)", parameters.id, parameters.user, parameters.message, parameters.date)
    #conn.commit()
    #conn.close()
    #cur.close()
    return 'log is added'


@app.post("/get_ml_recommendation")
async def ml_recommend(data=_fastapi.Body()):
    data = data.decode().split('&')
    chat_id = data[0].split('=')[1]
    msg = data[1].split('=')[1]
    recommendations_list = get_ml_recommendation(msg)
    response = requests.post(
        'http://127.0.0.1:8080/tg_send_recommendation',
        data={'chat_id': chat_id, 'recommendations': f'{recommendations_list}'}
    )
    return 'OK recommendations'

@app.post("/save_logs")
async def save_logs(tg_data=_fastapi.Body(),
                    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    data = tg_data.decode().split('&')
    # make a function
    user_id = data[0].split('=')[1]
    first_name = data[1].split('=')[1]
    username = data[2].split('=')[1]
    message_id = data[3].split('=')[1]
    # processing text with +,.)(!?
    text = data[4].split('=')[1].replace("+", " ")
    date = data[5].split('=')[1]
    data = {'user_id': user_id,
            'first_name': first_name,
            'username': username,
            'message_id': message_id,
            'text': text,
            'date':date}
    new_logs = await logging(logs=data, db=db)
    return 'OK save logs'


### ml recommendation engine

# def get_ml_recommendation(text: str, num_neighbors: int = 5) -> List[str]:
def get_ml_recommendation(text: str, num_neighbors: int = 5):
   msg_vector = get_vector_from_msg(text) # np.array([1.1, 5.3, 3.8, ...])
   closest_vectors = get_book_vector_neighbors(msg_vector, num_neighbors) # np.array([[1.1, ...], [1.0, ...] ...])
   book_recomend_list = get_books_from_vectors(closest_vectors) # ['Winnie-the-Pooh by A. Milne', 'The Tale ...']
   return book_recomend_list

def get_vector_from_msg(text: str) -> np.ndarray:
   return np.zeros(len(text))

def get_book_vector_neighbors(msg_vector, num_neighbors):
    return np.repeat(msg_vector[:, np.newaxis], num_neighbors, axis=1).reshape(num_neighbors, len(msg_vector))

def get_books_from_vectors(closest_vectors):
    return ['aaa'] * len(closest_vectors)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
    init_db()
