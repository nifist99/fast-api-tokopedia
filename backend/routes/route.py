from fastapi import APIRouter,FastAPI, Depends, HTTPException
# middleware
from app.middleware.Middleware import admin,auth,guest

# api users
# from app.api.users.ApiUsersTokopedia import ApiUsersTokopedia

# api auth
from app.api.auth.RestApiAuth import restAuth
from app.api.users.RestApiUsers import restUsers


auth.include_router(restAuth)
auth.include_router








