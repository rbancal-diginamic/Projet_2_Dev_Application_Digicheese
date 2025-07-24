from typing import Optional, List
from sqlmodel import Session, select

from ..models.db_models.client_db import ClientDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyClientRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, client: dict) -> ClientDB:
        client_db = ClientDB(**client)
        self.session.add(client_db)
        self.session.commit()
        return client_db

    def get_by_id(self, client_id: ClientDB.c_id) -> Optional[ClientDB]:
        statement = select(ClientDB).where(ClientDB.c_id == client_id)
        client_db = self.session.exec(statement).first()
        if client_db:
            return client_db
        return None

    def get_by_name(self, client_nom: ClientDB.c_nom) -> Optional[ClientDB]:
        statement = select(ClientDB).where(ClientDB.c_nom == client_nom)
        client_db = self.session.exec(statement).first()
        if client_db:
            return client_db
        return None

    def get_all(self) -> List[ClientDB]:
        clients_db = self.session.query(ClientDB).all()
        return [ClientDB.model_validate(c) for c in clients_db]

    def update(self, client: dict) -> None:
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
