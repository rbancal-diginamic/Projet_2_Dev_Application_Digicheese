from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session
from src.models.schemas.utilisateurs.utilisateur_patch import UtilisateurPatch
from src.models.schemas.utilisateurs.utilisateur_post import UtilisateurPost
from ..database import get_db
from ..services.utilisateur_service import UtilisateurService

router = APIRouter(prefix="/utilisateurs", tags=["Utilisateurs"])

@router.get(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Get toutes les utilisateurs",
        description="Renvoie toutes les utilisateurs "       
)
async def get_utilisateurs(session: Session = Depends(get_db)):
    """Renvoie toutes les utilisateurs """
    utilisateurs = UtilisateurService(session).get_utilisateurs()
    if not utilisateurs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=["Aucun utilisateur trouvé"])
    return JSONResponse(status_code=status.HTTP_200_OK, content=[utilisateur.model_dump() for utilisateur in utilisateurs])

@router.get(
        "/{id}",
        status_code=status.HTTP_200_OK,
        summary="Get un utilisateur avec un id",
        description="Renvoie l'utilisateur'" 
        )
async def get_utilisateur_by_id(id: int, session: Session = Depends(get_db)):
    """Renvoie l'utilisateur """   
    utilisateur = UtilisateurService(session).get_utilisateur_by_id(id)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=["L'utilisateur n'existe pas"])
    return JSONResponse(status_code=status.HTTP_200_OK, content=utilisateur.model_dump())

@router.get(
        "/{name}",
        status_code=status.HTTP_200_OK,
        summary="Get une utilisateur avec un nom",
        description="Renvoie l'utilisateur "       
)
async def get_utilisateur_by_name(name: str, session: Session = Depends(get_db)):
    """Renvoie l'utilisateur """     
    utilisateur = UtilisateurService(session).get_utilisateur_by_name(name)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=["L'utilisateur n'existe pas"])
    return JSONResponse(status_code=status.HTTP_200_OK, content=utilisateur.model_dump())

@router.get(
        "/{username}",
        status_code=status.HTTP_200_OK,
        summary="Get un utilisateur avec un prénom",
        description="Renvoie l'utilisateur "    
)
async def get_utilisateur_by_username(username: str, session: Session = Depends(get_db)):
    """Renvoie l'utilisateur """     
    utilisateur = UtilisateurService(session).get_utilisateur_by_username(username)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=["L'utilisateur n'existe pas"])
    return JSONResponse(status_code=status.HTTP_200_OK, content=utilisateur.model_dump())

@router.post(
        "/",
        status_code=status.HTTP_201_CREATED,
        summary="Post pour un utilisateur",
        description="Créé un utilisateur "
)
async def create_utilisateur(body: UtilisateurPost, session: Session = Depends(get_db)):
    """Créé un utilisateur """    
    try:
        utilisateur = UtilisateurService(session).create_utilisateur(body)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=utilisateur.model_dump())
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=["Un paramètre obligatoire n'est pas renseigné: [u_username]"])
    
@router.patch(
        "/{id}",
        status_code=status.HTTP_200_OK,
        summary="Patch pour un utilisateur",
        description="mise à jour pour un utilisateur " 
)
async def patch_utilisateur(id: int, body: UtilisateurPatch, session: Session = Depends(get_db)):
    """mise à jour pour un utilisateur"""     
    try:
        utilisateur = UtilisateurService(session).update_utilisateur(id, body)
        return JSONResponse(status_code=status.HTTP_200_OK, content=utilisateur.model_dump())
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@router.delete(
        "/{id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete pour un utilisateur",
        description="suppression pour un utilisateur "        
)
async def delete_utilisateur(id: int, session: Session = Depends(get_db)):
    utilisateur = UtilisateurService(session).delete_utilisateur(id)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(status_code=status.HTTP_200_OK, content="L'utilisateur a été supprimé")