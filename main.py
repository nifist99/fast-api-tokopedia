from typing import Union
from datetime import datetime, timedelta
import uvicorn
from fastapi import FastAPI, Request
from xavier.routes.route import app


if __name__ == '__main__':
    uvicorn.run("run:app", reload=True)
