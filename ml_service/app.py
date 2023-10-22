from fastapi import FastAPI, Request, Body
import requests
from pydantic import BaseModel
import uvicorn
import json


class Item(BaseModel):
    name: str
    description: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/get_ml_recommendation")
async def ml_recommend(data=Body()):
    msg = data.decode().split('=')[1]
    a = get_ml_recommendation(msg)
    return {"message": msg} # answer in tg

@app.post("/hello")
def hello(data=Body()):
    data = json.loads(data.decode())
    name = data['name']
    age = data['age']
    return {"message": f"{name}, ваш возраст - {age}"}

@app.post("/items")
async def create_item(item: Item):
    return item


### ml recommendation engine

def get_ml_recommendation(text: str, num_neighbors: int = 5) -> List[str]:
   msg_vector = get_vector_from_msg(text) # np.array([1.1, 5.3, 3.8, ...])
   closest_vectors = get_book_vector_neighbors(msg_vector, num_neighbors) # np.array([[1.1, ...], [1.0, ...] ...])
   book_recomend_list = get_books_from_vectors(closest_vectors) # ['Winnie-the-Pooh by A. Milne', 'The Tale ...']
   return book_recomend_list

def get_vector_from_msg(text: str) -> np.ndarray:
   return np.zeros(len(text))

def get_book_vector_neighbors(msg_vector, num_neighbors):
    return msg_vector * num_neighbors

def get_books_from_vectors(closest_vectors):
    return 'aaa' * len(closest_vectors)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
