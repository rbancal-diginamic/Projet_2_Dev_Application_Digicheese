from typing import List
from sqlmodel import Session, select

from ..models.db_models.conditionnement_db import ConditionnementDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyConditionnementRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, conditionnement: dict) -> ConditionnementDB:
        conditionnement_db = ConditionnementDB(**conditionnement)
        self.session.add(conditionnement_db)
        self.session.commit()
        self.session.refresh(conditionnement_db)
        return conditionnement_db

    def get_by_id(self, conditionnement_id: int | None = None) -> ConditionnementDB | None:
        statement = select(ConditionnementDB).where(ConditionnementDB.c_id == conditionnement_id)

        conditionnement_db = self.session.exec(statement).first()
        if conditionnement_db:
            return conditionnement_db
        return None


    def get_all(self) -> List[ConditionnementDB]:
        statement = select(ConditionnementDB)
        conditionnements_db = self.session.exec(statement).all()
        return [ConditionnementDB.model_validate(conditionnement) for conditionnement in conditionnements_db]

    def update(self, conditionnement_id: int, conditionnement_body: dict) -> ConditionnementDB | None:
        statement = select(ConditionnementDB).where(ConditionnementDB.c_id == conditionnement_id)

        conditionnement_db = self.session.exec(statement).first()
        if conditionnement_db:
            for key, value in conditionnement_body.items():
                setattr(conditionnement_db, key, value)
            self.session.commit()
            self.session.refresh(conditionnement_db)
            return conditionnement_db
        return None

    def delete(self, conditionnement_id: int | None = None) -> bool:
        statement = select(ConditionnementDB).where(ConditionnementDB.c_id == conditionnement_id)

        conditionnement_db = self.session.exec(statement).first()
        if conditionnement_db:
            self.session.delete(conditionnement_db)
            self.session.commit()
            return True
        return False
