from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class UsersBase(BaseModel):
    name: str
    email : str
    status: str
    privileges_id: int


class UsersCreate(UsersBase):
    created_at : datetime


class Users(UsersBase):
    id: int
    status: str

    class Config:
        orm_mode = True