import time
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,APIRouter, Request

admin = FastAPI()

auth  = FastAPI()

guest = FastAPI()

origins = [
    "https://localhost",
    "http://localhost",
    "https://localhost:8000",
    "http://localhost:8000",
]

admin.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

guest.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

auth.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)