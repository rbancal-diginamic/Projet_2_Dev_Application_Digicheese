from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..services.role_service import RoleService

router = APIRouter(prefix="/role", tags=["Role"])

@router.get("/")
def get_role(session: Session = Depends(get_db)):
    return RoleService(session).get_role(session)

@router.get("/{name}")
def get_role_by_name(name: str, session: Session = Depends(get_db)):
    pass