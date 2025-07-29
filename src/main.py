from fastapi import FastAPI
from sqlmodel import SQLModel

from .database import engine
# from .models import (
#     Departement,
#     Commune,
#     Client,
#     Commande,
#     Conditionnement,
#     Objet,
#     ObjetCond,
#     Detail,
#     DetailObjet,
#     Enseigne,
#     Poids,
#     Role,
#     Utilisateur,
#     RoleUtilisateur
# )

from .models import (
    DepartementDB,
    CommuneDB,
    ClientDB,
    ConditionnementDB,
    CommandeDB,
    ObjetDB,
    RoleDB,
    UtilisateurDB
)

from .routers import global_router

tags_metadata = [
    {
        "name": "Clients",
        "description": "Opérations sur la table Client.",

    },
    {
        "name": "Commandes",
        "description": "Opérations sur la table Commandes.",

    },
        {
        "name": "Objets",
        "description": "Opérations sur la table Objets",

    },
        {
        "name": "Departements",
        "description": "Opérations sur la table Departements.",

    },
        {
        "name": "communes",
        "description": "Opérations sur la table communes.",

    },
        {
        "name": "Role",
        "description": "Opérations sur la table Role.",

    },
        {
        "name": "Utilisateurs",
        "description": "Opérations sur la table Utilisateurs.",

    },
        {
        "name": "Conditionnements",
        "description": "Opérations sur la table Conditionnements.",

    }

    ]
app = FastAPI(openapi_tags=tags_metadata)
# FIXME : Supprimer la 1ere ligne pour la PROD
# SQLModel.metadata.drop_all(bind=engine)
SQLModel.metadata.create_all(bind=engine)
app.include_router(global_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
