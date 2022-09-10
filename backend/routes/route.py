from sys import prefix
from fastapi import APIRouter,FastAPI, Depends, HTTPException
# middleware
from backend.app.middleware.Middleware import admin,auth,guest
from fastapi.middleware.cors import CORSMiddleware

# api users
# from app.api.users.ApiUsersTokopedia import ApiUsersTokopedia

# api auth
from backend.app.api.auth.RestApiAuth import restAuth
from backend.app.api.ApiPrivileges import restPrivileges

app = FastAPI(prefix="api/v1")

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

app.include_router(restAuth)
app.include_router(restPrivileges)

# guest.include_router(restAuth)
# auth.include_router(restPrivileges)

# app.mount('/api/v1',guest)
# app.mount('/api/v1',auth)








