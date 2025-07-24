from .bases import client
from .schemas.clients import client_patch, client_post
from .db_models import client_db

from .bases import objet
from .schemas.objet import objet_patch, objet_post
from .db_models import objet_db

from .bases import commande
from .schemas.commande import commande_patch, commande_post
from .db_models import commande_db