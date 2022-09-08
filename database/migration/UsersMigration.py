from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text,DateTime,Date
from database.ConnectionDB import Base

class Users(Base):
    __tablename__       = "users"
    id                  = Column(Integer, primary_key=True, index=True)
    privileges_id       = Column(Integer)
    name                = Column(String(250))
    email               = Column(String(250), unique=True)
    email_verified_at   = Column(DateTime,nullable=True)
    status              = Column(String(250))
    remember_token      = Column(String(250),nullable=True)
    created_at          = Column(DateTime)
    updated_at          = Column(DateTime)