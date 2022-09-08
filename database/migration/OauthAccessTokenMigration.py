from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text,DateTime,Date
from database.ConnectionDB import Base

class Oauth(Base):
    __tablename__       = "oauth_access_token"
    id                  = Column(Integer, primary_key=True, index=True)
    name                = Column(String(250))
    token               = Column(String(1000))
    screet_key          = Column(String(250))
    expired_at          = Column(DateTime)
    last_used_at        = Column(DateTime)
    created_at          = Column(DateTime)
    updated_at          = Column(DateTime)
