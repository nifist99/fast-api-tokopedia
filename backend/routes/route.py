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

# api users
# from app.api.users.ApiUsersTokopedia import ApiUsersTokopedia

#model

from backend.app.model.UsersModel import UsersModel
from backend.app.helper.Utils import get_current_user

# api auth
from backend.app.api.auth.RestApiAuth import restAuth
from backend.app.api.ApiPrivileges import restPrivileges

class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)
            print(f"route duration: {duration}")
            print(f"route response: {response}")
            print(f"route response headers: {response.headers}")
            return response

        return custom_route_handler

class BarierJwt(APIRoute):

    async def get_token_auth_header(request: Request):
        print(request.headers)
        return True

app = FastAPI()
app.router.route_class = TimedRoute
app.router.route_class = BarierJwt
api_router = APIRouter()

@app.middleware("http")
async def get_token_auth_header(request: Request):
        print(request.headers)
        return request.headers

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

# @app.middleware("http")
# async def root(request: Request,call_next,authorization: str = Header(None)):
#     try:
#         decoded = get_current_user(authorization)
#         print(decoded)
#         if decoded.status == True:
#             response = await call_next(request)
#             print(response)
#         else:
#             return {
#                 "message":"Unauthorized Access!",
#                 "status":False,
#                 "code":400
#                 }
#         # here we can add code to check the user (by email)
#         # e.g. select the user from the DB and see its permissions
#     except:
#         return {
#                 "message":"Unauthorized Access!",
#                 "status":False,
#                 "code":400
#                 }
#     # in this example we'll simply return the person entity from the request body
#     # after adding a "checked"
#     return response

api_router.include_router(restAuth)

api_router.include_router(restPrivileges)

app.include_router(api_router,prefix="/api/v1")

# guest.include_router(restAuth)
# auth.include_router(restPrivileges)

# app.mount('/api/v1',guest)
# app.mount('/api/v1',auth)








