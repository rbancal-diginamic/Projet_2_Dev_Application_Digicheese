from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..services.objet_service import ObjetService

router = APIRouter(prefix="/objet", tags=["Objet"])

@router.get("/")
def get_objets(session: Session = Depends(get_db)):
    return ObjetService(session).get_objets()

@router.get("/{id}")
def get_objet_by_id(id: int, session: Session = Depends(get_db)):
    pass


@router.post("/")
def create_objet(body: dict, session: Session = Depends(get_db)):
    pass

@router.patch("/{id}")
def patch_objet(id: int, body: dict, session: Session = Depends(get_db)):
    pass

@router.delete("/{id}")
def delete_objet(id: int, session: Session = Depends(get_db)):
    pass