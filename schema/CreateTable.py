
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from migration.UsersMigration import Users
from migration.PrivilegesMigration import Privileges
from migration.OauthAccessTokenMigration import Oauth
from migration import engine

# create table

Oauth.metadata.create_all(engine)
Users.metadata.create_all(engine)
Privileges.metadata.create_all(engine)
