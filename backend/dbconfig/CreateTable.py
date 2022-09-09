
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from migrations.UsersMigration import Users
from migrations.PrivilegesMigration import Privileges
from migrations.OauthAccessTokenMigration import Oauth
from migrations import engine

# create table

Oauth.metadata.create_all(engine)
Users.metadata.create_all(engine)
Privileges.metadata.create_all(engine)
