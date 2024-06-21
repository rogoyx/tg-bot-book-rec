import datetime as _dt 
import pydantic as _pydantic


class _BaseContact(_pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str

class Contact(_BaseContact):
    id: int
    date_created: _dt.datetime
    
    class Config:
        from_attributes = True

class CreateContact(_BaseContact):
    pass

class _BaseLogs(_pydantic.BaseModel):
    user_id: int
    first_name: str
    username: str
    message_id: int
    text: str
    date:str

class Logs(_BaseLogs):
    id: int
    date_created: _dt.datetime
    
    class Config:
        from_attributes = True

class Logging(_BaseLogs):
    pass
