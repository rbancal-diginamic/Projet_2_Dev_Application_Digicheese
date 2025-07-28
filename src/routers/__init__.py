from fastapi import APIRouter
from .client_subrouter import router as client_router
from .objet_subrouter import router as objet_router
from .commande_subrouter import router as commande_router
from .departement_subrouter import router as departement_router
from .commune_subrouter import router as commune_router
from .role_subrouter import router as role_router
from .utilisateur_subrouter import router as utilisateur_router
from .conditionnement_subrouter import router as conditionnement_router

global_router = APIRouter()
global_router.include_router(client_router)
global_router.include_router(objet_router)
global_router.include_router(commande_router)
global_router.include_router(departement_router)
global_router.include_router(commune_router)
global_router.include_router(role_router)
global_router.include_router(utilisateur_router)
global_router.include_router(conditionnement_router)
