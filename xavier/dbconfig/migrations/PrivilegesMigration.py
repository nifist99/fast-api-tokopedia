from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text,DateTime,Date
from xavier.dbconfig.ConnectionDB import Base

class Privileges(Base):
    __tablename__       = "privileges"
    id                  = Column(Integer, primary_key=True, index=True)
    name                = Column(String(250))
    created_at          = Column(DateTime)
    updated_at          = Column(DateTime,nullable=True)

    # def __repr__(self):
    #     return self.name
    
    # def __init__(self,id,name,created_at,updated_at):
    #     self.id                 = id
    #     self.name               = name
    #     self.created_at         = created_at
    #     self.updated_at         = updated_at