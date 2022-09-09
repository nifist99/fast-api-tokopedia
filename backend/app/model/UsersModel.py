# import from package

from sqlalchemy.orm import Session, aliased
from fastapi import APIRouter, Depends, status
from backend.app.helper.Utils import create_access_token,create_refresh_token,verify_password,get_hashed_password,ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.responses import JSONResponse
# import from file python

from backend.dbconfig.schemas import UsersSchema as schemas
from backend.dbconfig.migrations import UsersMigration as models
from backend.dbconfig.ConnectionDB import Connection,engine
from pydantic import BaseModel, EmailStr,ValidationError, validator
from sqlalchemy.exc import SQLAlchemyError

#helper
from backend.app.helper.date import ConfigDate


class body_auth_login(BaseModel):       
    email: EmailStr
    password : str

class body_auth_register(BaseModel):
    name : str       
    email: EmailStr
    password : str

class UsersModel:

    def getUsers(user_id: int,db: Session = Depends(Connection.get_db)):
        return db.query(models.Users).filter(models.Users.id == user_id).first()


    def getUsersByEmail(email: str,db: Session = Depends(Connection.get_db)):
        return db.query(models.Users).filter(models.Users.email == email).first()


    def getAllUsers(skip: int = 0, limit: int = 100,db: Session = Depends(Connection.get_db)):
        return db.query(models.Users).offset(skip).limit(limit).all()


    def createUsers(body):
        try:
            db = Session(bind=engine,expire_on_commit=False)

            password_encryption = get_hashed_password(body.password)
            data = models.Users(
                                name=body.name,
                                email=body.email, 
                                password=password_encryption, 
                                status="active",
                                privileges_id=1,
                                created_at= ConfigDate.carbonDateTime()
                                )
            db.add(data)
            db.commit()
            db.close()
            return {
                "status":True,
                "message":"success register users : "+data.email,
            }
        except SQLAlchemyError as e:
            errMsg = str(e.__dict__['orig'])
            db.rollback()
            db.close()
            return {
                "status":False,
                "message":errMsg,
            }
