from ConnectionDB import Base,engine

# keterangan tabel

from migrations.OauthAccessTokenMigration import Oauth
from migrations.PrivilegesMigration import Privileges
from migrations.UsersMigration import Users

# delete data

Oauth.metadata.drop_all(engine)
Privileges.metadata.drop_all(engine)
Users.metadata.drop_all(engine)