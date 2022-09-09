from fastapi import APIRouter, Depends, HTTPException


restUsers = APIRouter(prefix="/users")

@restUsers.get("/")
async def index():
    return "message"

@restUsers.get("/detail/{id}")
async def detail(id : int):
    return "message"

@restUsers.post("/save")
async def save():
    return "message"

@restUsers.put("/update")
async def update():
    return "message"

@restUsers.get("/delete/{id}")
async def delete(id : int):
    return "message"
