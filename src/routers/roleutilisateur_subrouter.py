from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.models.schemas.RoleUtilisateur.roleutilisateur_patch import RoleUtilisateurPatch
from src.models.schemas.RoleUtilisateur.roleutilisateur_post import RoleUtilisateurPost
from ..database import get_db
from ..services.roleutilisateur_service import RoleUtilisateurService

router = APIRouter(prefix="/roleutilisateur", tags=["RoleUtilisateurs"])

@router.get("/")
def get_roleutilisateurs(session: Session = Depends(get_db)):
    roleutilisateurs = RoleUtilisateurService(session).get_roleutilisateurs(session)
    if not roleutilisateurs:
        return "Aucun role d'utilisateur trouvé"
    return roleutilisateurs

@router.get("/{id}")
def get_roleutilisateur_by_id(id: int, session: Session = Depends(get_db)):
    roleutilisateur = RoleUtilisateurService(session).get_roleutilisateur_by_id(id)
    if not roleutilisateur:
        return "Le role d'utilisateur n'existe pas"
    return roleutilisateur

@router.get("/{name}")
def get_roleutilisateur_by_name(name: str, session: Session = Depends(get_db)):
    roleutilisateur = RoleUtilisateurService(session).get_roleutilisateur_by_name(name)
    if not roleutilisateur:
        return "Le role d'utilisateur n'existe pas"
    return roleutilisateur

@router.get("/{username}")
def get_roleutilisateur_by_username(username: str, session: Session = Depends(get_db)):
    roleutilisateur = RoleUtilisateurService(session).get_roleutilisateur_by_username(username)
    if not roleutilisateur:
        return "Le role d'utilisateur n'existe pas"
    return roleutilisateur

@router.post("/")
def create_roleutilisateur(body: dict, session: Session = Depends(get_db)):
    roleutilisateur_post = RoleUtilisateurPost().from_dict(body)
    roleutilisateur = RoleUtilisateurService(session).create_roleutilisateur(roleutilisateur_post)
    if not roleutilisateur:
        return "Le role d'utilisateur n'a pas été créé"
    return roleutilisateur

@router.patch("/{id}")
def patch_roleutilisateur(id: int, body: dict, session: Session = Depends(get_db)):
    roleutilisateur_patch = RoleUtilisateurPatch().from_dict(body)
    roleutilisateur = RoleUtilisateurService(session).update_roleutilisateur(roleutilisateur_patch)
    if not roleutilisateur:
        return "Le role d'utilisateur n'a pas été créé"
    return roleutilisateur

@router.delete("/{id}")
def delete_roleutilisateur(id: int, session: Session = Depends(get_db)):
    roleutilisateur = RoleUtilisateurService(session).delete_roleutilisateur(id)
    if not roleutilisateur:
        return "Le role d'utilisateur n'a pas été supprimé"
    return roleutilisateur