from importlib.resources import contents
from jose import jwt, JWTError,ExpiredSignatureError
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, aliased
from xavier.dbconfig.migrations import UsersMigration as models
from xavier.dbconfig.ConnectionDB import Connection,engine
from dotenv import dotenv_values,load_dotenv
from fastapi import HTTPException,Depends,status
from pydantic import BaseModel
from typing import Union, Any

config = dotenv_values(".env")

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30 
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30 
ALGORITHM = config['ALGORITHM']
JWT_SECRET_KEY = config['SECRET_KEY']     
JWT_REFRESH_SECRET_KEY = config['SECRET_KEY'] 

class TokenData(BaseModel):
    email: Union[str, None] = None

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = JWT_SECRET_KEY

    def get_user(self,email: str):
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

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, email):
        expired_at = datetime.utcnow() + timedelta(days=30, minutes=5)
        payload = {
            'exp':expired_at ,
            'iat': datetime.utcnow(),
            'sub': email
        }
        token = jwt.encode(
                    payload,
                    self.secret,
                    algorithm=ALGORITHM
                )
        return {
            "token": token,
            "expired_at":expired_at
        }


    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except ExpiredSignatureError:
            respon={
                "status":False,
                'code':401,
                "message":"Token has expired"
            }
            raise HTTPException(status_code=401, detail=respon)
        except JWTError as e:
            respons={
                "status":False,
                'code':401,
                "message":"Invalid token"
            }
            raise HTTPException(status_code=401, detail=respons)
            
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)