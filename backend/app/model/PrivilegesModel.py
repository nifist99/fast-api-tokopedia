# import from package

from datetime import date, datetime
from sqlalchemy.orm import Session, aliased
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
# import from file python

from backend.dbconfig.migrations import OauthAccessTokenMigration as models
from backend.dbconfig.ConnectionDB import Connection,engine
from pydantic import BaseModel, EmailStr,ValidationError, validator
from sqlalchemy.exc import SQLAlchemyError

from backend.dbconfig.migrations import PrivilegesMigration as models

#helper
from backend.app.helper.date import ConfigDate

class body_privileges(BaseModel):       
    name : str

class PrivilegesModel:

    def getAllPrivileges(skip: int = 0, limit: int = 10):
        try:
            db = Session(bind=engine,expire_on_commit=False)
            data= db.query(models.Privileges).offset(skip).limit(limit).all()
            return {
                    "status":True,
                    "data":data,
            }
        except SQLAlchemyError as e:
            errMsg = str(e.__dict__['orig'])
            db.rollback()
            db.close()
            return {
                "status":False,
                "message":errMsg,
            }
    
    def getPrivilegesById(id: int):
        try:
            db = Session(bind=engine,expire_on_commit=False)

            data = db.query(models.Privileges).filter(models.Privileges.id == id).first()
            return {
                    "status":True,
                    "data":{
                            "name":data.name,
                            "created_at":data.created_at,
                            "updated_at":data.updated_at,
                        },
            }
        except SQLAlchemyError as e:
            errMsg = str(e.__dict__['orig'])
            db.rollback()
            db.close()
            return {
                "status":False,
                "message":errMsg,
            }

    def deleteById(id: int):
        try:
            db = Session(bind=engine,expire_on_commit=False)
            check = db.query(models.Privileges).filter(models.Privileges.id == id).first()
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

    def createPrivileges(body):
        try:
            db = Session(bind=engine,expire_on_commit=False)
            data = models.Privileges(
                                name=body.name,
                                created_at= ConfigDate.carbonDateTime()
                                )
            db.add(data)
            db.commit()
            db.close()
            return {
                "status":True,
                "message":"success add data users",
            }
        except SQLAlchemyError as e:
            errMsg = str(e.__dict__['orig'])
            db.rollback()
            db.close()
            return {
                "status":False,
                "message":errMsg,
            }

    def updatePrivileges(id,body):
        try:
            db = Session(bind=engine,expire_on_commit=False)
            data = db.query(models.Privileges).filter(models.Privileges.id == id)
            data.update({
                models.Privileges.name : body.name,
                models.Privileges.update_at : ConfigDate.carbonDate()
            })
            db.commit()
            db.close()
            return {
                "status":True,
                "message":"success add data users",
            }
        except SQLAlchemyError as e:
            errMsg = str(e.__dict__['orig'])
            db.rollback()
            db.close()
            return {
                "status":False,
                "message":errMsg,
            }
