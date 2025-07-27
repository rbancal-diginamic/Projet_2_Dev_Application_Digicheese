from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from ..models.schemas.objetconds.objetcond_patch import ObjetCondPatch
from ..models.schemas.objetconds.objetcond_post import ObjetCondPost
from ..database import get_db
from ..services.objetcond_service import ObjetCondService

router = APIRouter(prefix="/objetcond", tags=["ObjetConds"])


@router.get("/{id}")
async def get_objetcond_by_id(id: int, session: Session = Depends(get_db)):
    objetcond = ObjetCondService(session).get_objetcond_by_id(id)
    if not objetcond:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le objetcond n'existe pas")
    return JSONResponse(status_code=status.HTTP_200_OK, content=objetcond)


@router.get("/")
async def get_objetconds(session: Session = Depends(get_db)):
    objetconds = ObjetCondService(session).get_objetconds()
    if not objetconds:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aucun objetcond trouvé")
    return JSONResponse(status_code=status.HTTP_200_OK, content=objetconds)


@router.post("/")
async def create_objetcond(body: ObjetCondPost, session: Session = Depends(get_db)):
    try:
        objetcond_post = ObjetCondPost.model_validate(body)
        objetcond = ObjetCondService(session).create_objetcond(objetcond_post)
        if not objetcond:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Le objetcond n'a pas été créé")
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=objetcond)
    except Exception(BaseException):
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.patch("/{id}")
async def patch_objetcond(id: int, body: ObjetCondPatch, session: Session = Depends(get_db)):
    try:
        objetcond_patch = ObjetCondPatch.model_validate(body)
        objetcond = ObjetCondService(session).update_objetcond(id, objetcond_patch)
        if not objetcond:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="L'objetcond n'existe pas")
        return JSONResponse(status_code=status.HTTP_200_OK, content=objetcond)
    except Exception(BaseException):
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.delete("/{id}")
async def delete_objetcond(id: int, session: Session = Depends(get_db)):
    objetcond = ObjetCondService(session).delete_objetcond(id)
    if not objetcond:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(status_code=status.HTTP_200_OK, content="L'objetcond a été supprimé")
