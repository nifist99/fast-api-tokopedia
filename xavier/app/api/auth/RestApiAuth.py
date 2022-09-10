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
from xavier.app.helper.Utils import get_hashed_password,verify_password
from datetime import datetime, timedelta
from sqlalchemy.orm import Session, aliased
from xavier.dbconfig.ConnectionDB import Connection
from xavier.app.helper.JwtToken import AuthHandler


from xavier.app.model.UsersModel import body_auth_login,body_auth_register,UsersModel
from xavier.app.model.AccessToken import TokenModel

restAuth = APIRouter(prefix="/auth")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

auth_handler = AuthHandler()
@restAuth.post("/login")
async def login(body: body_auth_login):
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    email = UsersModel.getUsersByEmail(body.email)
    if email['status']==True:
        check = verify_password(body.password,email['data']['password'])
        if check == True:
            # token = create_access_token(body.email,expires_delta=access_token_expires)
            token = auth_handler.encode_token(body.email)
            # save token to database
            TokenModel.createToken(email['data']['id'],token['token'],token['expired_at'])
            respon={
                "status":True,
                "message":"Success Login",
                "code":200,
                "token":token['token'],
                "data":email['data']
            }
            return JSONResponse(content=respon,status_code=status.HTTP_200_OK)
        else:
            respon={
                "status":False,
                "message":"Password Wrong",
                "code":400
            }
            return JSONResponse(content=respon,status_code=status.HTTP_400_BAD_REQUEST)
    else:
        respon={
                "status":False,
                "message":email['message'],
                "code":400
            }
        return JSONResponse(content=respon,status_code=status.HTTP_400_BAD_REQUEST)

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

@restAuth.post("/logout")
async def logout(request : Request):
    req = await request.json()
    print(req)

         
            