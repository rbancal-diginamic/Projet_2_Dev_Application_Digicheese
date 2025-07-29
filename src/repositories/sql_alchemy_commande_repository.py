from typing import Optional, List
from sqlmodel import Session, select
from ..models.db_models.commande_db import CommandeDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyCommandeRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, commande: dict) -> CommandeDB:
        commande_db = CommandeDB(**commande)
        self.session.add(commande_db)
        self.session.commit()
        self.session.refresh(commande_db)
        return commande_db

    def get_by_id(self, commande_id: int) -> Optional[CommandeDB]:
        statement = select(CommandeDB).where(CommandeDB.c_id == commande_id)
        commande_db = self.session.exec(statement).first()
        if commande_db:
            return commande_db
        return None

    def get_all(self) -> List[CommandeDB] | None:
        statement = select(CommandeDB)
        commandes_dbs = self.session.exec(statement).all()
        if commandes_dbs:
            return [CommandeDB.model_validate(statement) for commande in commandes_dbs]
        return None

    def update(self, commande_id: int, commande_body: dict) -> CommandeDB | None:
        statement = select(CommandeDB).where(CommandeDB.c_id == commande_id)
        commande_db = self.session.exec(statement).first()
        if commande_db:
            for key, value in commande_body.items():
                setattr(commande_db, key, value)
            self.session.commit()
            self.session.refresh(commande_db)
            return commande_db
        return None

    def delete(self, commande_id: int | None = None) -> bool:
        statement = select(CommandeDB).where(CommandeDB.c_id == commande_id)
        commande_db = self.session.exec(statement).first()
        if not commande_db:
            return False
        self.session.delete(commande_db)
        self.session.commit()
        return True
