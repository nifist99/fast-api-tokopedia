
from typing import List
from venv import create
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sqlalchemy import insert

from migrations.UsersMigration import Users
from migrations.PrivilegesMigration import Privileges
from migrations.OauthAccessTokenMigration import Oauth
from ConnectionDB import Base,engine

from datetime import datetime

# create table atau migration

Oauth.metadata.create_all(engine)
Users.metadata.create_all(engine)
Privileges.metadata.create_all(engine)

    

