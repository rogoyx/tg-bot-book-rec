
# ml functions (in folder) to be imported to ml_backend/app.py

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
