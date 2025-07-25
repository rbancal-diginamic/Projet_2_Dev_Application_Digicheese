from fastapi import APIRouter, Depends
from sqlmodel import Session

from ..database import get_db
from ..services.commune_service import CommuneService

router = APIRouter(prefix="/commune", tags=["communes"])

@router.get("/{id}")
def get_commune_by_id(id: int, session: Session = Depends(get_db)):
    return CommuneService(session).get_commune_by_id(id)

@router.get("/")
def get_communes(session: Session = Depends(get_db)):
    return CommuneService(session).get_communes()