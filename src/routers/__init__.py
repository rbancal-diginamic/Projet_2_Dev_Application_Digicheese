from fastapi import APIRouter
from .client_subrouter import router as client_router
from .objet_subrouter import router as objet_router

global_router = APIRouter()
global_router.include_router(client_router, tags=["client"])
global_router.include_router(objet_router, tags=["object"])