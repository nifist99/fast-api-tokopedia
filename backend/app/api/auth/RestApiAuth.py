from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status,APIRouter,Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from uuid import uuid4
from backend.app.helper.Utils import get_hashed_password


restAuth = APIRouter(prefix="/auth")

class body_auth_login(BaseModel):       
    email: str
    password : str

class body_auth_register(BaseModel):
    name : str       
    email: str
    password : str

@restAuth.post("/login")
async def login(email: str = Form(), password: str = Form()):
    return "message"

@restAuth.post("/register")
async def register(email: str = Form(),name : str = Form(), password: str = Form(), privileges_id: str = Form()):
    return {
                "name": name,
                "email":email,
                "password":get_hashed_password(password),
                "privileges_id":id
            }

@restAuth.post("/forget")
async def forget():
    return "message"
