from .bases import client, role, utilisateur
from .schemas.clients import client_patch, client_post
from .schemas.role import role_patch, role_post
from .schemas.utilisateur import utilisateur_patch, utilisateur_post
from .db_models import client_db, role_db, utilisateur_db