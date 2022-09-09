
from typing import List
from venv import create
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sqlalchemy import insert

from migrations.UsersMigration import Users
from migrations.PrivilegesMigration import Privileges
from migrations.OauthAccessTokenMigration import Oauth
from ConnectionDB import Base,engine

from app.helper.date import ConfigDate

# create table atau migration

Oauth.metadata.create_all(engine)
Users.metadata.create_all(engine)
Privileges.metadata.create_all(engine)

#seeder default data 

privileges = insert(Privileges).values(name='users', created_at=ConfigDate.carbonDateTime())

with engine.connect() as conn:
    result = conn.execute(privileges)
    conn.commit()

