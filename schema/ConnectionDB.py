from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from setuptools import setup, find_packages
setup(
    name = 'ConnectionDB',
    packages = find_packages()
)

DATABASE_URL = 'postgresql://postgres:admin123@localhost/test'
engine = create_engine(DATABASE_URL, poolclass=NullPool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Connection:
    # Dependency
    def get_db():
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()