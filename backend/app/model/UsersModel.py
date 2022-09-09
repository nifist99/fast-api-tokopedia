# import from package

from sqlalchemy.orm import Session, aliased
from fastapi import APIRouter, Depends, status
from backend.app.helper.Utils import create_access_token,create_refresh_token,verify_password,get_hashed_password,ACCESS_TOKEN_EXPIRE_MINUTES

# import from file python

from dbconfig.schemas import UsersSchema as schemas
from dbconfig.migrations import UsersMigration as models
from dbconfig.ConnectionDB import Connection
from pydantic import BaseModel

get_db = Connection.get_db()


def get_user(user_id: int,db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(email: str,db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(skip: int = 0, limit: int = 100,db: Session = Depends(get_db)):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
