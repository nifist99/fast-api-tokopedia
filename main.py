from typing import Union
from datetime import datetime, timedelta
import uvicorn
from fastapi import FastAPI
from backend.routes.route import auth

from backend.app.helper.Utils import create_access_token,create_refresh_token,verify_password,get_hashed_password,ACCESS_TOKEN_EXPIRE_MINUTES
# from routes.route import auth

app = FastAPI()

app.mount('/api/v1',auth)

if __name__ == '__main__':
    print(get_hashed_password('123'))
    print(verify_password('123','$2b$12$v6rqq955NiX6g3dUYq7gNuQlHxfZSyrv/Xk0UigLV82R/Sgx0JoEi'))
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        'niko', expires_delta=access_token_expires
    )
    print(access_token)
    uvicorn.run("main:app", host='localhost', port=8000, log_level="info", reload=True)
