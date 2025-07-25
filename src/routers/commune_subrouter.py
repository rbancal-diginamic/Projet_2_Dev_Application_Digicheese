from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from ..database import get_db
from ..services.commune_service import CommuneService

router = APIRouter(prefix="/commune", tags=["communes"])


@router.get("/{id}")
async def get_commune_by_id(id: int, session: Session = Depends(get_db)):
    commune = CommuneService(session).get_commune_by_id(id)
    if not commune:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune non trouvée")
    return JSONResponse(status_code=status.HTTP_200_OK, content=commune)


@router.get("/")
async def get_communes(session: Session = Depends(get_db)):
    communes = CommuneService(session).get_communes()
    if not communes:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Communes non trouvées")
    return JSONResponse(status_code=status.HTTP_200_OK, content=communes)
