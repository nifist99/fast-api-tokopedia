from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text,DateTime,Date
from xavier.dbconfig.ConnectionDB import Base

class Oauth(Base):
    __tablename__       = "oauth_access_token"
    id                  = Column(Integer, primary_key=True, index=True)
    users_id            = Column(Integer)
    name                = Column(String(250),nullable=True)
    token               = Column(String(1000))
    screet_key          = Column(String(250),nullable=True)
    expired_at          = Column(DateTime)
    last_used_at        = Column(DateTime,nullable=True)
    created_at          = Column(DateTime)
    updated_at          = Column(DateTime,nullable=True)

    # def __repr__(self):
    #     return self.token
    
    # def __init__(self,id,users_id,name,token,screet_key,expired_at,last_used_at,created_at,updated_at):
    #     self.id                 = id
    #     self.users_id           = users_id
    #     self.name               = name
    #     self.token              = token
    #     self.screet_key         = screet_key
    #     self.expired_at         = expired_at
    #     self.last_used_at       = last_used_at
    #     self.created_at         = created_at
    #     self.updated_at         = updated_at
