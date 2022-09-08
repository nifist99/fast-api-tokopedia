from typing import List, Optional

from pydantic import BaseModel


class UsersBase(BaseModel):
    name: str
    price : float
    description: Optional[str] = None
    store_id: int


class UsersCreate(UsersBase):
    pass


class Users(UsersBase):
    id: int

    class Config:
        orm_mode = True
