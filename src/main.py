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

# tags_metadata=[]

app = FastAPI()
# FIXME : Supprimer la 1ere ligne pour la PROD
SQLModel.metadata.drop_all(bind=engine)
SQLModel.metadata.create_all(bind=engine)
app.include_router(global_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
