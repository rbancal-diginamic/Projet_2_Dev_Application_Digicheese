from .bases import client, role, utilisateur
from .schemas.clients import client_patch, client_post
from .db_models import client_db

from .bases import departement, commune, departement, commande, objet
from .db_models import departement_db, commune_db, objet_db, commande_db, client_db, role_db, utilisateur_db
from .schemas.objet import objet_patch, objet_post
from .schemas.commande import commande_patch, commande_post
from .schemas.role import role_patch, role_post
from .schemas.utilisateur import utilisateur_patch, utilisateur_post