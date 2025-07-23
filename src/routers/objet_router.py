from fastapi import APIRouter

router = APIRouter(prefix="/client", tags=["Clients"])

@router.get("/client")
def get_clients():
    pass

@router.get("/client/{id}")
def get_clients_by_id(id : int):
    pass


@router.post("/client")
def create_client(client: dict):
    pass

@router.patch("/client/{id}")
def patch_client(id : int):
    pass

@router.delete("/client/{id}")
def delete_cleint(id : int):
    pass