from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import dotenv_values,load_dotenv
from fastapi import HTTPException,Depends,status
from pydantic import BaseModel
from backend.dbconfig.migrations import UsersMigration as models
from backend.dbconfig.ConnectionDB import Connection,engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, aliased

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


