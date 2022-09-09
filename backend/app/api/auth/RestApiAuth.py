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
from backend.app.helper.Utils import get_hashed_password


restAuth = APIRouter(prefix="/auth")

class body_auth_login(BaseModel):       
    email: EmailStr
    password : str

class body_auth_register(BaseModel):
    name : str       
    email: EmailStr
    password : str


@restAuth.post("/login")
async def login(email: str = Form(), password: str = Form()):
    return {
                "email":email,
                "password":password
            }

@restAuth.post("/register")
async def register(email: str = Form(),name : str = Form(), password: str = Form(), privileges_id: str = Form()):
    return {
                "name": name,
                "email":email,
                "password":get_hashed_password(password),
                "privileges_id":id
            }

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
async def logout(request : Request,respone : Response):
    req = await request.json()
    respone.status_code = status.HTTP_400_BAD_REQUEST
    return {
        "status":True,
        "code":respone.status_code,
        "message":"success logout",
        "data":req
    }
         
            