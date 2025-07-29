from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from ..models.schemas.commandes.commande_patch import CommandePatch
from ..models.schemas.commandes.commande_post import CommandePost
from ..database import get_db
from ..services.commande_service import CommandeService

router = APIRouter(prefix="/commande", tags=["Commandes"])


@router.get(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Get toutes les commandes",
        description="Renvoie toutes les commandes "
)
async def get_commandes(session: Session = Depends(get_db)):
    """Renvoie toutes les commandes """
    commandes = CommandeService(session).get_commandes()
    if not commandes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aucunne commandes trouvée")
    content = []
    for commande in commandes:
        commande = commande.model_dump()
        if "c_date_commande" in commande and isinstance(commande["c_date_commande"], datetime):
            commande['c_date_commande'] = commande['c_date_commande'].strftime("%d/%m/%Y")
        content.append(commande)
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)


@router.get(
        "/{id}",
        status_code=status.HTTP_200_OK,
        summary="Get une commande avec un id",
        description="Renvoie la commande "        
)
async def get_commande_by_id(id: int, session: Session = Depends(get_db)):
    """Renvoie la commande """    
    commande = CommandeService(session).get_commande_by_id(id)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="La commandes n'existe pas")
    commande = commande.model_dump()
    commande['c_date_commande'] = commande['c_date_commande'].strftime("%d/%m/%Y")
    return JSONResponse(status_code=status.HTTP_200_OK, content=commande)


@router.post(
        "/",
        status_code=status.HTTP_201_CREATED,
        summary="Post pour une commande",
        description="Créé une commande "

)
async def create_commande(body: CommandePost, session: Session = Depends(get_db)):
    """Créé une commande """
    try:
        commande_post = CommandePost.model_validate(body)
        commande = CommandeService(session).create_commande(commande_post)
        if not commande:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                detail="La commandes n'a pas été créée")
        commande = commande.model_dump()
        commande['c_date_commande'] = datetime.isoformat(commande['c_date_commande'])
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=commande)
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.patch(
        "/{id}",
        status_code=status.HTTP_200_OK,
        summary="Patch pour une commande",
        description="mise à jour pour une commande "       
)
async def patch_commande(id: int, body: CommandePatch, session: Session = Depends(get_db)):
    """mise à jour pour une commande"""    
    try:
        commande = CommandeService(session).update_commande(id, body)
        commande = commande.model_dump()
        commande['c_date_commande'] = commande['c_date_commande'].strftime("%d/%m/%Y")
        return JSONResponse(status_code=status.HTTP_200_OK, content=commande)
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.delete(
        "/{id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete pour une commande",
        description="suppression pour une commande "       
)
async def delete_commande(id: int, session: Session = Depends(get_db)):
    """suppression pour une commande """
    commande = CommandeService(session).delete_commande(id)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, 
                        content="La commade a été supprimée")
