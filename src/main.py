from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, select, Session

from .database import get_db, engine
from .models import (
    Departement,
    Commune,
    Client,
    Commande,
    Conditionnement,
    Objet,
    ObjetCond,
    Detail,
    DetailObjet,
    Enseigne,
    Poids,
    Role,
    Utilisateur,
    RoleUtilisateur
)

from .routers import global_router

app = FastAPI()
app.include_router(global_router)
SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}