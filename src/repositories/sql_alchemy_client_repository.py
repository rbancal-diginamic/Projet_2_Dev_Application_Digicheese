from typing import Optional, List
from sqlalchemy.orm import Session
from models.schemas.clients.client_patch import ClientPatch
from models.schemas.clients.client_post import ClientPost
from repositories.client_repository import ClientRepository
from models.db_models.client_db import ClientDB


class SQLAlchemyClientRepository(ClientRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, client: ClientPost) -> None:
        client_db = ClientDB(**client.model_dump())
        self.session.add(client_db)
        self.session.commit()

    def get_by_id(self, client_id: ClientDB.c_id) -> Optional[ClientDB]:
        client_db = self.session.query(ClientDB).get(client_id)
        if client_db:
            return ClientDB(**client_db.model_dump())
        return None

    def get_by_name(self, client_nom: ClientDB.c_nom) -> Optional[ClientDB]:
        client_db = self.session.query(ClientDB).where(ClientDB.c_nom == client_nom).first()
        if client_db:
            return ClientDB(**client_db.model_dump())
        return None

    def get_all(self) -> List[ClientDB]:
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
