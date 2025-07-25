from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_db

router = APIRouter(prefix="/client", tags=["Clients"])

@router.get("/")
def get_clients(session: Session = Depends(get_db)):
    pass

@router.get("/{id}")
def get_client_by_id(id: int, session: Session = Depends(get_db)):
    pass


@router.post("/")
def create_client(body: dict, session: Session = Depends(get_db)):
    pass

@router.patch("/{id}")
def patch_client(id: int, body: dict, session: Session = Depends(get_db)):
    pass

@router.delete("/{id}")
def delete_client(id: int, session: Session = Depends(get_db)):
    pass