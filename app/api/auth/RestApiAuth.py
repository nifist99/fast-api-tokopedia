from fastapi import APIRouter, Depends, HTTPException


restAuth = APIRouter(prefix="/auth")

@restAuth.get("/login")
async def login():
    return "message"

@restAuth.get("/register")
async def register(id : int):
    return "message"

@restAuth.put("/forget")
async def forget():
    return "message"
