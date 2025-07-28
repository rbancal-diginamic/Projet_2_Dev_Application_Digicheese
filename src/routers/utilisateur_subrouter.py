from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.models.schemas.utilisateurs.utilisateur_patch import UtilisateurPatch
from src.models.schemas.utilisateurs.utilisateur_post import UtilisateurPost
from ..database import get_db
from ..services.utilisateur_service import UtilisateurService

router = APIRouter(prefix="/utilisateurs", tags=["Utilisateurs"])

@router.get("/")
def get_utilisateurs(session: Session = Depends(get_db)):
    utilisateurs = UtilisateurService(session).get_utilisateurs()
    if not utilisateurs:
        return "Aucun utilisateurs trouvé"
    return utilisateurs

@router.get("/{id}")
def get_utilisateur_by_id(id: int, session: Session = Depends(get_db)):
    utilisateur = UtilisateurService(session).get_utilisateur_by_id(id)
    if not utilisateur:
        return "L'utilisateurs n'existe pas"
    return utilisateur

@router.get("/{name}")
def get_utilisateur_by_name(name: str, session: Session = Depends(get_db)):
    utilisateur = UtilisateurService(session).get_utilisateur_by_name(name)
    if not utilisateur:
        return "L'utilisateurs n'existe pas"
    return utilisateur

@router.get("/{username}")
def get_utilisateur_by_username(username: str, session: Session = Depends(get_db)):
    utilisateur = UtilisateurService(session).get_utilisateur_by_username(username)
    if not utilisateur:
        return "L'utilisateurs n'existe pas"
    return utilisateur

@router.post("/")
def create_utilisateur(body: UtilisateurPost, session: Session = Depends(get_db)):
    utilisateur_post = UtilisateurPost().from_dict(body)
    utilisateur = UtilisateurService(session).create_utilisateur(utilisateur_post)
    if not utilisateur:
        return "L'utilisateurs n'a pas été créé"
    return utilisateur

@router.patch("/{id}")
def patch_utilisateur(id: int, body: dict, session: Session = Depends(get_db)):
    utilisateur_patch = UtilisateurPatch().from_dict(body)
    utilisateur = UtilisateurService(session).update_utilisateur(utilisateur_patch)
    if not utilisateur:
        return "L'utilisateurs n'a pas été créé"
    return utilisateur

@router.delete("/{id}")
def delete_utilisateur(id: int, session: Session = Depends(get_db)):
    utilisateur = UtilisateurService(session).delete_utilisateur(id)
    if not utilisateur:
        return "L'utilisateurs n'a pas été supprimé"
    return utilisateur