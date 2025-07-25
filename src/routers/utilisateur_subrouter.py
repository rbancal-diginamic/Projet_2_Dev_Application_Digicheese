from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..services.utilisateur_service import UtilisateurService

router = APIRouter(prefix="/utilisateur", tags=["Utilisateurs"])

@router.get("/")
def get_utilisateurs(session: Session = Depends(get_db)):
    return UtilisateurService(session).get_utilisateurs(session)

@router.get("/{id}")
def get_utilisateur_by_id(id: int, session: Session = Depends(get_db)):
    pass

@router.get("/{username}")
def get_utilisateur_by_username(username: str, session: Session = Depends(get_db)):
    pass

@router.post("/")
def create_utilisateur(body: dict, session: Session = Depends(get_db)):
    pass

@router.patch("/{id}")
def patch_utilisateur(id: int, body: dict, session: Session = Depends(get_db)):
    pass

@router.delete("/{id}")
def delete_utilisateur(id: int, session: Session = Depends(get_db)):
    pass