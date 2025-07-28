from .bases import departement, commune, client, commande, objet, role, utilisateur
from .db_models import departement_db, commune_db, objet_db, commande_db, client_db, role_db, utilisateur_db

from .schemas.clients import client_patch, client_post
from .schemas.objet import objet_patch, objet_post
from .schemas.commande import commande_patch, commande_post
from .schemas.role import role_patch, role_post
from .schemas.utilisateur import utilisateur_patch, utilisateur_post