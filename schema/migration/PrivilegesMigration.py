from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text,DateTime,Date
from . import Base

class Privileges(Base):
    __tablename__       = "privileges"
    id                  = Column(Integer, primary_key=True, index=True)
    name                = Column(String(250))
    created_at          = Column(DateTime)
    updated_at          = Column(DateTime)