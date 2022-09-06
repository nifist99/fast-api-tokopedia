from fastapi import APIRouter, Depends, HTTPException


ApiUsersTokopedia = APIRouter(prefix="/tokopedia")

@ApiUsersTokopedia.get("/all")
async def all():
    return "message"

@ApiUsersTokopedia.get("/detail/{id}")
async def detail(id : int):
    return "message"

@ApiUsersTokopedia.put("/update")
async def update():
    return "message"

@ApiUsersTokopedia.post("/save")
async def save():
    return "message"

@ApiUsersTokopedia.get("/delete/{id}")
async def delete(id : int):
    return "message"