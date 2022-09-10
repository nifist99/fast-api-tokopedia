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
from datetime import datetime, timedelta
from sqlalchemy.orm import Session, aliased
from xavier.dbconfig.ConnectionDB import Connection

from xavier.app.model.PrivilegesModel import PrivilegesModel,body_privileges

restPrivileges = APIRouter(prefix="/privileges")

@restPrivileges.get("/")
async def index():
    return "message"

@restPrivileges.get("/edit/{id}")
async def edit(id : int):
    return "message"

@restPrivileges.post("/create")
async def create(body: body_privileges):
    return "message"

@restPrivileges.get("/update/{id}")
async def update(body: body_privileges,id : int):
    return "message"

@restPrivileges.get("/delete/{id}")
async def delete(id : int):
    return "message"



