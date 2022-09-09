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

    def getUsers(user_id: int):
        try:
            db = Session(bind=engine,expire_on_commit=False)
            return {
                    "status":True,
                    "data":db.query(models.Users).filter(models.Users.id == user_id).first(),
            }
        except SQLAlchemyError as e:
            errMsg = str(e.__dict__['orig'])
            db.rollback()
            db.close()
            return {
                "status":False,
                "message":errMsg,
            }

    def getUsersByEmail(email: str):
        try:
            db = Session(bind=engine,expire_on_commit=False)
            data = db.query(models.Users).filter(models.Users.email == email).first()
            if data is not None:
                return {
                        "status":True,
                        "message":"success get data",
                        "data":{
                            "email":data.email,
                            "password":data.password,
                            "id":data.id,
                            "status":data.status
                        },
                }
            else:
                return {
                        "status":False,
                        "message":"email not found"
                }
        except SQLAlchemyError as e:
            errMsg = str(e.__dict__['orig'])
            db.rollback()
            db.close()
            return {
                "status":False,
                "message":errMsg,
            }


    def getAllUsers(skip: int = 0, limit: int = 100):
        try:
            db = Session(bind=engine,expire_on_commit=False)
            return {
                "status":True,
                "data":db.query(models.Users).offset(skip).limit(limit).all(),
            }
        except SQLAlchemyError as e:
            errMsg = str(e.__dict__['orig'])
            db.rollback()
            db.close()
            return {
                "status":False,
                "message":errMsg,
            }

    def deleteUsers(user_id: int):
        try:
            db = Session(bind=engine,expire_on_commit=False)
            check = db.query(models.Users).filter(models.Users.id == user_id).first()
            if check:
                db.delete(check)
                db.commit()
                db.close()
                return {
                    "status":True,
                    "message":"success delete data",
                }
            else:
                return {
                    "status":False,
                    "message":"failed delete, data not found",
                }
        except SQLAlchemyError as e:
            errMsg = str(e.__dict__['orig'])
            db.rollback()
            db.close()
            return {
                "status":False,
                "message":errMsg,
            }

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

