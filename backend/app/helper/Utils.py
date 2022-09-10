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

config = dotenv_values(".env")

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30 # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30 # 7 days
ALGORITHM = config['ALGORITHM']
JWT_SECRET_KEY = config['SECRET_KEY']     # should be kept secret
JWT_REFRESH_SECRET_KEY = config['SECRET_KEY']      # should be kept secret


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None


class User(BaseModel):
    email: Union[str, None] = None
    status: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

def get_user(email: str):
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


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return {
                "token":encoded_jwt,
                "expired_at":expires_delta
            }

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return {
                "token":encoded_jwt,
                "expired_at":expires_delta
            }

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        status=False,
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = get_user(email=token_data.email)
    if user['status'] != True:
        raise credentials_exception
    return {
        "status":True,
        "code":200,
        "message":"success autentication",
        "data":user
    }

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.status:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user