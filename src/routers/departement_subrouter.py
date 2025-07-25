from fastapi import APIRouter, Depends
from sqlmodel import Session

from ..database import get_db
from ..services.departement_service import DepartementService

router = APIRouter(prefix="/departement", tags=["Departements"])

@router.get("/{id}")
def get_departement_by_id(id: int, session: Session = Depends(get_db())):
    return DepartementService(session).get_departement_by_id(id)

@router.get("/")
def get_departements(session: Session = Depends(get_db)):
    return DepartementService(session).get_departements()