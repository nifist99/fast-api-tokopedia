from fastapi import APIRouter,FastAPI, Depends, HTTPException
# middleware
from backend.app.middleware.Middleware import admin,auth,guest

# api users
# from app.api.users.ApiUsersTokopedia import ApiUsersTokopedia

# api auth
from backend.app.api.auth.RestApiAuth import restAuth
from backend.app.api.users.RestApiUsers import restUsers


auth.include_router(restAuth)
auth.include_router








