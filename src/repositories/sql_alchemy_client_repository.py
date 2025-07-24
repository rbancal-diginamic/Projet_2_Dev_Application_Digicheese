from typing import Optional, List

from sqlmodel import Session

from src.models.db_models.client_db import ClientDB
from src.models.schemas.clients.client_patch import ClientPatch
from src.models.schemas.clients.client_post import ClientPost
from src.repositories.client_repository import ClientRepository


class SQLAlchemyClientRepository(ClientRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, client: dict) -> ClientDB:
        client_db = ClientDB(**client)
        self.session.add(client_db)
        self.session.commit()
        return client_db

    def get_by_id(self, client_id: ClientDB.c_id) -> Optional[ClientDB]:
        statement = select(ClientDB).where(ClientDB.c_id == client_id)
        client_db = self.session.query(ClientDB).get(client_id)
        if client_db:
            return ClientDB(**client_db.model_dump())
        return None

    def get_by_name(self, client_nom: ClientDB.c_nom) -> Optional[ClientDB]:
        statement = select(client_db).where(ClientDB.c_nom == client.nom)
        client_db = self.session.exec(ClientDB).where(statement).first()
        if client_db:
            return client_db
        return None

    def get_all(self, session: Session) -> List[ClientDB]:
        clients_db = self.session.query(ClientDB).all()
        return [ClientDB.model_validate(c) for c in clients_db]

    def update(self, client: ClientPatch) -> None:
        client_db = self.session.query(ClientDB).get(client.id)
        if client_db:
            # FIXME : Contrôler la bonne exécution de l'update !
            ClientDB(**client.model_dump())
            self.session.commit()

    def delete(self, client_id: ClientDB.c_id) -> None:
        client_db = self.session.query(ClientDB).get(client_id)
        if client_db:
            self.session.delete(client_db)
            self.session.commit()
