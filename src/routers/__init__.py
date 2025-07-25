from fastapi import APIRouter
from .client_subrouter import router as client_router
from .objet_subrouter import router as objet_router
from .commande_subrouter import router as commande_router
from .departement_subrouter import router as departement_router
from .commune_subrouter import router as commune_router


global_router = APIRouter()
global_router.include_router(client_router, tags=["client"])
global_router.include_router(objet_router, tags=["object"])
global_router.include_router(objet_router, tags=["commande"])
global_router.include_router(departement_router, tags=["departement"])
global_router.include_router(commune_router, tags=["commune"])