import datetime as _dt 
import sqlalchemy as _sql

import database as _database 


class Contact(_database.Base):
    __tablename__ = "contacts"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    first_name = _sql.Column(_sql.String, index=True)
    last_name = _sql.Column(_sql.String, index=True, unique=True)
    email = _sql.Column(_sql.String, index=True, unique=True)
    phone_number = _sql.Column(_sql.String, index=True, unique=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

class Logs(_database.Base):
    __tablename__ = "logs"

    id = _sql.Column(_sql.Integer, primary_key=True)
    user_id = _sql.Column(_sql.Integer, index=True)
    first_name = _sql.Column(_sql.String)
    username = _sql.Column(_sql.String)
    message_id = _sql.Column(_sql.Integer)
    text = _sql.Column(_sql.String)
    date = _sql.Column(_sql.String)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

class Users(_database.Base):
    __tablename__ = "users"

    id = _sql.Column(_sql.Integer, primary_key=True)
    user_id = _sql.Column(_sql.Integer, index=True)
    username = _sql.Column(_sql.String)
    
class Descriptions(_database.Base):
    __tablename__ = "descriptions"

    id = _sql.Column(_sql.Integer, primary_key=True)
    user_id = _sql.Column(_sql.Integer, index=True)
    description_text = _sql.Column(_sql.String)
    date = _sql.Column(_sql.String)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

class BotAnswers(_database.Base):
    __tablename__ = "bot_answers"

    id = _sql.Column(_sql.Integer, primary_key=True)
    user_id = _sql.Column(_sql.Integer, index=True)
    log_id = _sql.Column(_sql.Integer, index=True)
    text = _sql.Column(_sql.String)
    book_ids_array = _sql.Column(_sql.String)
    date = _sql.Column(_sql.String)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
