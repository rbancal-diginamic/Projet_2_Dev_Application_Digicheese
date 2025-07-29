from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from ..models.schemas.objets.objet_patch import ObjetPatch
from ..models.schemas.objets.objet_post import ObjetPost
from ..database import get_db
from ..services.objet_service import ObjetService

router = APIRouter(prefix="/objets", tags=["Objets"])

@router.get(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Get toutes les objets",
        description="Renvoie toutes les objets "
)
async def get_objets(session: Session = Depends(get_db)):
    """Renvoie les objets """
    objets = ObjetService(session).get_objets()
    if not objets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aucun objets trouvé")
    return JSONResponse(status_code=status.HTTP_200_OK, content=objets)


@router.get(
        "/{id}",
        status_code=status.HTTP_200_OK,
        summary="Get un objet avec un id",
        description="Renvoie l'objet " 
)
async def get_objet_by_id(id: int, session: Session = Depends(get_db)):
    """Renvoie l'objet """   
    objet = ObjetService(session).get_objet_by_id(id)
    if not objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="L'objets n'existe pas")
    return JSONResponse(status_code=status.HTTP_200_OK, content=objet)


@router.post(
        "/",
        status_code=status.HTTP_201_CREATED,
        summary="Post pour un objet",
        description="Créé un objet "        
)
async def create_objet(body: dict, session: Session = Depends(get_db)):
    """Créé un objet """
    try:
        objet_post = ObjetPost.model_validate(body)
        objet = ObjetService(session).create_objet(objet_post)
        if not objet:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="L' objets n'a pas été créé")
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=objet)
    except Exception(BaseException):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@router.patch(
        "/{id}",
        status_code=status.HTTP_200_OK,
        summary="Patch pour un objet",
        description="mise à jour pour un objet"     
)
async def patch_objet(id: int, body: dict, session: Session = Depends(get_db)):
    """mise à jour pour un objet"""  
    try:
        objet_patch = ObjetPatch.model_validate(body)
        objet = ObjetService(session).update_objet(id, objet_patch)
        if not objet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="L'objets n'existe pas")
        return JSONResponse(status_code=status.HTTP_200_OK, content=objet)
    except Exception(BaseException):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
@router.delete(
        "/{id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete pour un objet",
        description="suppression pour un objet "   
)
async def delete_objet(id: int, session: Session = Depends(get_db)):
    """suppression pour un objet """
    objet = ObjetService(session).delete_objet(id)
    if not objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(status_code=status.HTTP_200_OK, content="L'objets' a été supprimé")