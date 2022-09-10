from typing import Union
from datetime import datetime, timedelta
import uvicorn
from fastapi import FastAPI, Request
from backend.routes.route import auth
# from routes.route import auth
from backend.app.helper.Utils import verify_password,get_hashed_password

app = FastAPI()

app.mount('/api/v1',auth)

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, log_level="debug", reload=True)
