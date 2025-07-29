from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from ..models import ClientDB
from ..models.schemas.clients.client_patch import ClientPatch
from ..models.schemas.clients.client_post import ClientPost
from ..database import get_db
from ..services.client_service import ClientService

router = APIRouter(prefix="/client", tags=["Clients"])


@router.get("/{id}")
async def get_client_by_id(id: int, session: Session = Depends(get_db)):
    client = ClientService(session).get_client_by_id(id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=["Le client n'existe pas"])
    return JSONResponse(status_code=status.HTTP_200_OK, content=client)


@router.get("/")
async def get_clients(session: Session = Depends(get_db)):
    clients = ClientService(session).get_clients()
    if not clients:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=[])
    return JSONResponse(status_code=status.HTTP_200_OK, content=[client.model_dump() for client in clients])


@router.post("/")
async def create_client(body: ClientPost, session: Session = Depends(get_db)):
    try:
        client = ClientService(session).create_client(body)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=client.model_dump())
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=["Un paramètre obligatoire n'est pas renseigné: [c_nom, c_prenom]"])


@router.patch("/{id}")
async def patch_client(id: int, body: ClientPatch, session: Session = Depends(get_db)):
    try:
        client_patch = ClientPatch.model_validate(body)
        client = ClientService(session).update_client(id, client_patch)
        if not client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le client n'existe pas")
        return JSONResponse(status_code=status.HTTP_200_OK, content=client)
    except Exception(BaseException):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.delete("/{id}")
async def delete_client(id: int, session: Session = Depends(get_db)):
    client = ClientService(session).delete_client(id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Le client a été supprimé")
