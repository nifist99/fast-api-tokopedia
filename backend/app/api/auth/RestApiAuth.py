from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status,APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from uuid import uuid4


restAuth = APIRouter(prefix="/auth")

@restAuth.get("/login")
async def login():
    return "message"

@restAuth.get("/register")
async def register(id : int):
    return "message"

@restAuth.put("/forget")
async def forget():
    return "message"
