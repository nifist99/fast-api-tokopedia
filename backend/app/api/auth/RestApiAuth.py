# package modul
from datetime import datetime, timedelta
from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status,APIRouter,Form, Request,Response,exception_handlers
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr,ValidationError, validator
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from backend.app.helper.Utils import get_hashed_password,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES
from backend.app.validation.UsersValidate import UsersValidate
from datetime import datetime, timedelta
from sqlalchemy.orm import Session, aliased
from backend.dbconfig.ConnectionDB import Connection


from backend.app.model.UsersModel import body_auth_login,body_auth_register,UsersModel

restAuth = APIRouter(prefix="/auth")


@restAuth.post("/login")
async def login(email: str = Form(), password: str = Form()):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
                "email":email,
                "password":get_hashed_password(password),
                "token" : create_access_token(email,expires_delta=access_token_expires)
            }

@restAuth.post("/register")
async def register(body: body_auth_register):
    try:
        check = UsersModel.createUsers(body)
        if check['status']==True:
            respone={
                "status":True,
                "message":check['message'],
                "code"  : 200
            }
            return JSONResponse(content=respone, status_code=status.HTTP_200_OK)
        else:
            respone={
                "status":False,
                "message":check['message'],
                "code"  : 400
            }
            return JSONResponse(content=respone, status_code=status.HTTP_400_BAD_REQUEST)
    except ValidationError as e:
        errMsg = str(e.__dict__['orig'])
        respone = {
            "status"  :False,
            "code"    : 400,
            "message" : errMsg
        }

        return JSONResponse(content=respone, status_code=status.HTTP_400_BAD_REQUEST)

@restAuth.post("/forget")
async def forget(request : Request,respone : Response):
        respone.status_code = status.HTTP_200_OK
        return {
                    "status": True, 
                    "code"  :respone.status_code,
                    "message":"success send password to email",
                    "data"  : register
                }

# fixs respon api

@restAuth.post("/logout")
async def logout(request : Request,respone : Response , register = body_auth_register):
    req = await request.json()

    print(req)

    exit()
    if(validate['status']):
        respone.status_code = status.HTTP_200_OK
        return {
            "status":True,
            "code":respone.status_code,
            "message":validate['message'],
            "data":req
        }
    else:
        respone.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status":False,
            "code":respone.status_code,
            "message":validate['message'],
        }
         
            