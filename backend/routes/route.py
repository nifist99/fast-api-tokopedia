from sys import prefix
from fastapi import APIRouter,FastAPI, Depends, HTTPException,Request, Header,Response
# middleware
from backend.app.middleware.Middleware import admin,auth,guest
from fastapi.middleware.cors import CORSMiddleware
from backend.app.middleware.Authenticate import Auth
import time
from typing import Callable
from fastapi.routing import APIRoute,APIWebSocketRoute
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from jose.exceptions import JOSEError

#model

from backend.app.model.UsersModel import UsersModel

# api auth
from backend.app.api.auth.RestApiAuth import restAuth
from backend.app.api.ApiPrivileges import restPrivileges

from backend.app.helper.JwtToken import AuthHandler

auth_handler = AuthHandler()

app = FastAPI()
api_router_guest = APIRouter()
api_router_auth = APIRouter(dependencies=[Depends(auth_handler.auth_wrapper)])

origins = [
    "https://localhost",
    "http://localhost",
    "https://localhost:8000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router_guest.include_router(restAuth)

api_router_auth.include_router(restPrivileges)

app.include_router(api_router_auth,prefix="/api/v1")
app.include_router(api_router_guest,prefix="/api/v1")








