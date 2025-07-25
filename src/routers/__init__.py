from fastapi import APIRouter
from .client_subrouter import router as client_router
from .objet_subrouter import router as objet_router
from .role_subrouter import router as role_router
from .utilisateur_subrouter import router as utilisateur_router

global_router = APIRouter()
global_router.include_router(client_router, tags=["client"])
global_router.include_router(objet_router, tags=["object"])
global_router.include_router(role_router, tags=["role"])
global_router.include_router(utilisateur_router, tags=["utilisateur"])