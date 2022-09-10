from typing import Union
from datetime import datetime, timedelta
import uvicorn
from fastapi import FastAPI, Request
from backend.routes.route import app
# from routes.route import auth


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
