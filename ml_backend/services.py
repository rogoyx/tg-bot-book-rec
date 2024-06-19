import database as _database
import models as _models
import schemas as _schemas
from sqlalchemy.orm import Session


def _create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

#def get_db():
#    db = _database.SessionLocal
#    try:
#        yield db
#    finally:
#        db.close()
        
def get_db():
    with _database.SessionLocal() as db:
        yield db



async def create_contact(contact: _schemas.CreateContact, 
                         db: "Session"):
    contact = _models.Contact(**contact.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return _schemas.Contact.from_orm(contact)


