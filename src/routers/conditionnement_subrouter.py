from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from ..models.schemas.conditionnements.conditionnement_patch import ConditionnementPatch
from ..models.schemas.conditionnements.conditionnement_post import ConditionnementPost
from ..database import get_db
from ..services.conditionnement_service import ConditionnementService

router = APIRouter(prefix="/conditionnement", tags=["Conditionnements"])


@router.get("/{id}")
async def get_conditionnement_by_id(id: int, session: Session = Depends(get_db)):
    conditionnement = ConditionnementService(session).get_conditionnement_by_id(id)
    if not conditionnement:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le conditionnement n'existe pas")
    return JSONResponse(status_code=status.HTTP_200_OK, content=conditionnement)


@router.get("/")
async def get_conditionnements(session: Session = Depends(get_db)):
    conditionnements = ConditionnementService(session).get_conditionnements()
    if not conditionnements:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aucun conditionnement trouvé")
    return JSONResponse(status_code=status.HTTP_200_OK, content=conditionnements)


@router.post("/")
async def create_conditionnement(body: ConditionnementPost, session: Session = Depends(get_db)):
    try:
        conditionnement_post = ConditionnementPost.model_validate(body)
        conditionnement = ConditionnementService(session).create_conditionnement(conditionnement_post)
        if not conditionnement:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Le conditionnement n'a pas été créé")
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=conditionnement)
    except Exception(BaseException):
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.patch("/{id}")
async def patch_conditionnement(id: int, body: ConditionnementPatch, session: Session = Depends(get_db)):
    try:
        conditionnement_patch = ConditionnementPatch.model_validate(body)
        conditionnement = ConditionnementService(session).update_conditionnement(id, conditionnement_patch)
        if not conditionnement:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le conditionnement n'existe pas")
        return JSONResponse(status_code=status.HTTP_200_OK, content=conditionnement)
    except Exception(BaseException):
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.delete("/{id}")
async def delete_conditionnement(id: int, session: Session = Depends(get_db)):
    conditionnement = ConditionnementService(session).delete_conditionnement(id)
    if not conditionnement:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Le conditionnement a été supprimé")
