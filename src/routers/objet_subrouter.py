from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from models.schemas.objets.objet_patch import ObjetPatch
from models.schemas.objets.objet_post import ObjetPost

from ..database import get_db
from ..services.objet_service import ObjetService

router = APIRouter(prefix="/objet", tags=["Objet"])

@router.get("/")
async def get_objets(session: Session = Depends(get_db)):
    objets = ObjetService(session).get_objets()
    if not objets:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aucun objet trouvé")
    return JSONResponse(status_code=status.HTTP_200_OK, content=objets)


@router.get("/{id}")
async def get_objet_by_id(id: int, session: Session = Depends(get_db)):
    objet = ObjetService(session).get_objet_by_id(id)
    if not objet:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="L'objet n'existe pas")
    return JSONResponse(status_code=status.HTTP_200_OK, content=objet)


@router.post("/")
async def create_objet(body: dict, session: Session = Depends(get_db)):
    try:
        objet_post = ObjetPost.model_validate(body)
        objet = ObjetService(session).create_objet(objet_post)
        if not objet:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="L' objet n'a pas été créé")
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=objet)
    except Exception(BaseException):
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@router.patch("/{id}")
async def patch_objet(id: int, body: dict, session: Session = Depends(get_db)):
    try:
        objet_patch = ObjetPatch.model_validate(body)
        objet = ObjetService(session).update_objet(id, objet_patch)
        if not objet:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="L'objet n'existe pas")
        return JSONResponse(status_code=status.HTTP_200_OK, content=objet)
    except Exception(BaseException):
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
@router.delete("/{id}")
async def delete_objet(id: int, session: Session = Depends(get_db)):
    objet = ObjetService(session).delete_objet(id)
    if not objet:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(status_code=status.HTTP_200_OK, content="L'objet' a été supprimé")