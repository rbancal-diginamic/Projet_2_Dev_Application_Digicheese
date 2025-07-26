from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..services.role_service import RoleService

router = APIRouter(prefix="/role", tags=["Role"])

@router.get("/{id}")
def get_role_by_name(id: int, session: Session = Depends(get_db)):
    role = RoleService(session).get_role_by_id(id)

@router.get("/{name}")
def get_role_by_name(name: str, session: Session = Depends(get_db)):
    role = RoleService(session).get_role_by_name(name)

@router.get("/")
def get_role(session: Session = Depends(get_db)):
    return RoleService(session).get_role(session)