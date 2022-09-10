from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text,DateTime,Date
from sqlalchemy import insert
from xavier.dbconfig.ConnectionDB import Base

class Users(Base):
    __tablename__       = "users"
    id                  = Column(Integer, primary_key=True, index=True)
    privileges_id       = Column(Integer)
    name                = Column(String(250))
    email               = Column(String(250), unique=True)
    email_verified_at   = Column(DateTime,nullable=True)
    status              = Column(String(250))
    password            = Column(String(250))
    remember_token      = Column(String(250),nullable=True)
    created_at          = Column(DateTime)
    updated_at          = Column(DateTime,nullable=True)

    # def __repr__(self):
    #     return self.name
    
    # def __init__(self,id,privileges_id,name,password,email,email_verified_at,status,remember_token,created_at,updated_at):
    #     self.id                 = id
    #     self.name               = name
    #     self.privileges_id      = privileges_id
    #     self.email              = email
    #     self.email_verified_at  = email_verified_at
    #     self.status             = status
    #     self.remember_token     = remember_token
    #     self.created_at         = created_at
    #     self.updated_at         = updated_at
    #     self.password           = password


