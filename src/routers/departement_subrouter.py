from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from ..database import get_db
from ..services.departement_service import DepartementService

router = APIRouter(prefix="/departement", tags=["Departements"])


@router.get("/{id}")
async def get_departement_by_id(id: int, session: Session = Depends(get_db)):
    departement = DepartementService(session).get_departement_by_id(id)
    if not departement:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Département non trouvé")
    return JSONResponse(status_code=status.HTTP_200_OK, content=departement)


@router.get("/")
async def get_departements(session: Session = Depends(get_db)):
    departements = DepartementService(session).get_departements()
    if not departements:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aucun département trouvé")
    return JSONResponse(status_code=status.HTTP_200_OK, content=departements)
