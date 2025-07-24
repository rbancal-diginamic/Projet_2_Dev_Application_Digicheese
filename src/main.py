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

from .models import client_db

from .routers import global_router

app = FastAPI()
app.include_router(global_router)
SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}