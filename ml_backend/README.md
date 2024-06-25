ml back -- service for processing user answers and connecting to database

endpoints:
/api/logs -- orm. writes logs from tg messages to db
/process_log -- gets users' messages and 1) put it into db 2) sends them to tg_backend to get list of recommendations


