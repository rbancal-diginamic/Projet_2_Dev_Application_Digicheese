from fastapi import APIRouter
from .subrouters import client_subrouter, objet_subrouter

global_router = APIRouter()
global_router.include_router(client_subrouter, tags=["client"])
global_router.include_router(objet_subrouter, tags=["object"])