from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..services.commande_service import CommandeService

router = APIRouter(prefix="/client", tags=["Clients"])

@router.get("/")
def get_commandes(session: Session = Depends(get_db)):
    return CommandeService(session).get_commandes()

@router.get("/{id}")
def get_commande_by_id(id: int, session: Session = Depends(get_db)):
    pass


@router.post("/")
def create_commande(body: dict, session: Session = Depends(get_db)):
    pass

@router.patch("/{id}")
def patch_commande(id: int, body: dict, session: Session = Depends(get_db)):
    pass

@router.delete("/{id}")
def delete_commande(id: int, session: Session = Depends(get_db)):
    pass