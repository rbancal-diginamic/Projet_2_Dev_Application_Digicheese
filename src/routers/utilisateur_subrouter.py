from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session
from src.models.schemas.utilisateurs.utilisateur_patch import UtilisateurPatch
from src.models.schemas.utilisateurs.utilisateur_post import UtilisateurPost
from ..database import get_db
from ..services.utilisateur_service import UtilisateurService

router = APIRouter(prefix="/utilisateurs", tags=["Utilisateurs"])

@router.get("/")
async def get_utilisateurs(session: Session = Depends(get_db)):
    utilisateurs = UtilisateurService(session).get_utilisateurs()
    if not utilisateurs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aucun utilisateur trouvé")
    return JSONResponse(status_code=status.HTTP_200_OK, content=[utilisateur.model_dump() for utilisateur in utilisateurs])

@router.get("/{id}")
async def get_utilisateur_by_id(id: int, session: Session = Depends(get_db)):
    utilisateur = UtilisateurService(session).get_utilisateur_by_id(id)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="L'utilisateur n'existe pas")
    return JSONResponse(status_code=status.HTTP_200_OK, content=utilisateur.model_dump())

@router.get("/{name}")
async def get_utilisateur_by_name(name: str, session: Session = Depends(get_db)):
    utilisateur = UtilisateurService(session).get_utilisateur_by_name(name)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="L'utilisateur n'existe pas")
    return JSONResponse(status_code=status.HTTP_200_OK, content=utilisateur.model_dump())

@router.get("/{username}")
async def get_utilisateur_by_username(username: str, session: Session = Depends(get_db)):
    utilisateur = UtilisateurService(session).get_utilisateur_by_username(username)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="L'utilisateur n'existe pas")
    return JSONResponse(status_code=status.HTTP_200_OK, content=utilisateur.model_dump())

@router.post("/")
async def create_utilisateur(body: UtilisateurPost, session: Session = Depends(get_db)):
    try:
        utilisateur_post = UtilisateurPost.model_validate(body)
        utilisateur = UtilisateurService(session).create_utilisateur(utilisateur_post)
        if not utilisateur:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="L'utilisateur n'a pas été créé")
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=utilisateur.model_dump())
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
@router.patch("/{id}")
async def patch_utilisateur(id: int, body: UtilisateurPatch, session: Session = Depends(get_db)):
    try:
        utilisateur_patch = UtilisateurPatch.model_validate(body)
        utilisateur = UtilisateurService(session).update_utilisateur(id, utilisateur_patch)
        if not utilisateur:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="L'utilisateur n'existe pas")
        return JSONResponse(status_code=status.HTTP_200_OK, content=utilisateur.model_dump())
    except Exception(BaseException):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@router.delete("/{id}")
async def delete_utilisateur(id: int, session: Session = Depends(get_db)):
    utilisateur = UtilisateurService(session).delete_utilisateur(id)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(status_code=status.HTTP_200_OK, content="L'utilisateur a été supprimé")