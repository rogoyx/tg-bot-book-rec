from typing import List
import numpy as np
# ml functions (in folder) to be imported to ml_backend/app.py

def get_ml_recommendation(text: str, num_neighbors: int = 5) -> List[str]:
   msg_vector = get_vector_from_msg(text) # np.array([1.1, 5.3, 3.8, ...])
   closest_vectors = get_book_vector_neighbors(msg_vector, num_neighbors) # np.array([[1.1, ...], [1.0, ...] ...])
   book_recomend_list = get_books_from_vectors(closest_vectors) # ['Winnie-the-Pooh by A. Milne', 'The Tale ...']
   return book_recomend_list

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

def get_vector_from_msg(text: str) -> np.ndarray:
   # text_emb = lang_model.vectorize(text)
   return np.zeros(len(text))

def get_book_vector_neighbors(msg_vector, num_neighbors):
    return msg_vector * num_neighbors

def get_books_from_vectors(closest_vectors):
    return 'aaa' * len(closest_vectors)
