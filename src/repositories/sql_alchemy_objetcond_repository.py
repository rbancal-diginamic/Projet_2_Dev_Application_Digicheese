from typing import List
from sqlmodel import Session, select

from ..models.db_models.objetcond_db import ObjetCondDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyObjetCondRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, objetcond: dict) -> ObjetCondDB:
        objetcond_db = ObjetCondDB(**objetcond)
        self.session.add(objetcond_db)
        self.session.commit()
        self.session.refresh(objetcond_db)
        return objetcond_db

    def get_by_id(self, objetcond_id: int | None = None) -> ObjetCondDB | None:
        statement = select(ObjetCondDB)
        statement.where(ObjetCondDB.c_id == objetcond_id)

        objetcond_db = self.session.exec(statement).first()
        if objetcond_db:
            return objetcond_db
        return None


    def get_all(self) -> List[ObjetCondDB]:
        statement = select(ObjetCondDB)
        objetconds_db = self.session.exec(statement).all()
        return [ObjetCondDB.model_validate(objetcond) for objetcond in objetconds_db]

    def update(self, objetcond_id: int, objetcond_body: dict) -> ObjetCondDB | None:
        statement = select(ObjetCondDB)
        statement.where(ObjetCondDB.c_id == objetcond_id)

        objetcond_db = self.session.exec(statement).first()
        if objetcond_db:
            for key, value in objetcond_body.items():
                setattr(objetcond_db, key, value)
            self.session.commit()
            self.session.refresh(objetcond_db)
            return objetcond_db
        return None

    def delete(self, objetcond_id: int | None = None) -> bool:
        statement = select(ObjetCondDB)
        statement.where(ObjetCondDB.c_id == objetcond_id)

        objetcond_db = self.session.exec(statement).first()
        if objetcond_db:
            self.session.delete(objetcond_db)
            self.session.commit()
            return True
        return False
