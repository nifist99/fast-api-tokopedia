# import from package

from datetime import date, datetime
from sqlalchemy.orm import Session, aliased
from fastapi import APIRouter, Depends, status
from backend.app.helper.Utils import get_current_user,ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.responses import JSONResponse
# import from file python

from backend.dbconfig.migrations import OauthAccessTokenMigration as models
from backend.dbconfig.ConnectionDB import Connection,engine
from pydantic import BaseModel, EmailStr,ValidationError, validator
from sqlalchemy.exc import SQLAlchemyError
from dotenv import dotenv_values,load_dotenv
config = dotenv_values(".env")
#helper
from backend.app.helper.date import ConfigDate

class TokenModel:
    def createToken(users_id,token,expired_at):
        try:
            db = Session(bind=engine,expire_on_commit=False)
            data = models.Oauth(
                                users_id=users_id,
                                name="JWT", 
                                token=token, 
                                screet_key=config['SECRET_KEY'],
                                expired_at=expired_at,
                                created_at= ConfigDate.carbonDateTime()
                                )
            db.add(data)
            db.commit()
            db.close()
            return {
                "status":True,
                "message":"Barier : "+data.token,
            }
        except SQLAlchemyError as e:
            errMsg = str(e.__dict__['orig'])
            db.rollback()
            db.close()
            return {
                "status":False,
                "message":errMsg,
            }