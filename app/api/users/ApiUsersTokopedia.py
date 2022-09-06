from fastapi import APIRouter, Depends, HTTPException


ApiTokopedia = APIRouter(prefix="/tokopedia")

@ApiTokopedia.get("/all")
async def all():
    return "message"

@ApiTokopedia.get("/detail/{id}")
async def detail(id : int):
    return "message"

@ApiTokopedia.put("/update")
async def update():
    return "message"

@ApiTokopedia.post("/save")
async def save():
    return "message"

@ApiTokopedia.get("/delete/{id}")
async def delete(id : int):
    return "message"