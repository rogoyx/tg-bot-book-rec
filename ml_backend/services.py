import database as _database
import models as _models
import schemas as _schemas
from sqlalchemy.orm import Session


def _create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    with _database.SessionLocal() as db:
        yield db

async def create_contact(contact: _schemas.CreateContact, 
                         db: "Session"):
    contact = _models.Contact(**contact)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return _schemas.Contact.from_orm(contact)

async def get_all_contacts(db: "Session"):
    contacts = db.query(_models.Contact).all()
    return list(map(_schemas.Contact.from_orm, contacts))

async def get_contact(contact_id: int, 
                      db: "Session"):
    contact = db.query(_models.Contact).filter(_models.Contact.id == contact_id).first()
    return contact
