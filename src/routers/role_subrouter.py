from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from ..models.schemas.roles.role_patch import RolePatch
from ..models.schemas.roles.role_post import RolePost
from ..database import get_db
from ..services.role_service import RoleService

router = APIRouter(prefix="/roles", tags=["Role"])

@router.get("/{id}")
def get_role_by_name(id: int, session: Session = Depends(get_db)):
    role = RoleService(session).get_role_by_id(id)
    if not role:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=["Le role n'existe pas"])
    return JSONResponse(status_code=status.HTTP_200_OK, content=role)

@router.get("/{name}")
def get_role_by_name(name: str, session: Session = Depends(get_db)):
    role = RoleService(session).get_role_by_name(name)
    if not role:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=["Le role n'existe pas"])
    return JSONResponse(status_code=status.HTTP_200_OK, content=role)

@router.get("/")
def get_role(session: Session = Depends(get_db)):
    role = RoleService(session).get_role()
    if not role:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=["Les roles n'existent pas"])
    return JSONResponse(status_code=status.HTTP_200_OK, content=role)


@router.post("/")
async def create_role(body: RolePost, session: Session = Depends(get_db)):
    try:
        role_post = RolePost.model_validate(body)
        role = RoleService(session).create_role(role_post)
        if not role:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Le role n'a pas été créé")
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=role)
    except Exception(BaseException):
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.patch("/{id}")
async def patch_role(id: int, body: RolePatch, session: Session = Depends(get_db)):
    try:
        role_patch = RolePatch.model_validate(body)
        role = RoleService(session).update_role(id, role_patch)
        if not role:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le role n'existe pas")
        return JSONResponse(status_code=status.HTTP_200_OK, content=role)
    except Exception(BaseException):
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.delete("/{id}")
async def delete_role(id: int, session: Session = Depends(get_db)):
    role = RoleService(session).delete_role(id)
    if not role:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Le role a été supprimé")
