from typing import Union
from datetime import datetime, timedelta
import uvicorn
from fastapi import FastAPI, Request
from backend.routes.route import auth
# from routes.route import auth

app = FastAPI()

app.mount('/api/v1',auth)

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, log_level="info", reload=True)
