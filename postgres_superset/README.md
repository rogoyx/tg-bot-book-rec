## Tables in Postgres Database

1. logs — raw data from Telegram API JSON. 
* id: PK
* user_id
* first_name
* username
* message_id
* text
* date
2. books — raw book data.
* book_id: PK
* isbn
* book_name
* author
* publisher
* year
* blurb
3. book_vectors — pre-computed book vectors.
* book_id: PK and FK referencing books table
* vector
4. bot_answers — sent recommendations. 
* id: PK
* user_id: FK referencing users table
* text
* book_ids_array: which books was used in this recommendation
* date
5. description_vectors — descriptions in vector form. 
* vector_id: PK
* description_vector
* description_id: FK referencing descriptions table
6. descriptions table — user desired books descriptions in text format
* id: PK
* description_text
* date
* user_id: FK referencing users table
7. users table — user information
* id: PK
* username: what name user uses in Telegram
* user_id: id from Telegram