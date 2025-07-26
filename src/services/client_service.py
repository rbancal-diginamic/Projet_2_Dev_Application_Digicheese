from sqlmodel import Session

from ..models.schemas.clients.client_patch import ClientPatch
from ..models.db_models.client_db import ClientDB
from ..models.schemas.clients.client_post import ClientPost
from ..repositories.sql_alchemy_client_repository import SQLAlchemyClientRepository


class ClientService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyClientRepository(session)

    def __traitement(self, client: dict) -> dict:
        client['c_nom'] = client["c_nom"].upper()
        client['c_prenom'] = client["c_prenom"].capitalize()
        return client

    def create_client(self, client_body: ClientPost) -> ClientDB:
        client = client_body.model_dump()
        client = self.__traitement(client)
        return self.repository.add(client)

    def get_client_by_id(self, client_id: int | None = None) -> ClientDB | None:
        return self.repository.get_by_id(client_id)

    def get_client_by_name(self, name: str) -> ClientDB | None:
        return self.repository.get_by_name(name)

    def get_clients(self) -> list[ClientDB]:
        return self.repository.get_all()

    def update_client(self, client_id: int, client_body: ClientPatch) -> ClientDB | None:
        client = client_body.model_dump()
        return self.repository.update(client_id, client)

    def delete_client(self, c_id: int | None = None) -> bool:
        client = self.repository.get_by_id(c_id)
        if client:
            self.repository.delete(client)
            return True
        return False
