from fastapi import APIRouter,FastAPI, Depends, HTTPException,Request


class Auth:
    async def getBody(request: Request, call_next):
        body = await request.body()
        print(body)
        response = await call_next(request)
        return response