from typing import List
from sqlmodel import Session, select

from ..models.db_models.commune_db import CommuneDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyCommuneRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, commune: dict) -> CommuneDB:
        pass

    def get_by_id(self, commune_id: int | None = None) -> CommuneDB | None:
        statement = select(CommuneDB).where(CommuneDB.c_id == commune_id)

        commune_db = self.session.exec(statement).first()
        if commune_db:
            return commune_db
        return None

    def get_all(self) -> List[CommuneDB]:
        statement = select(CommuneDB)
        communes_db = self.session.exec(statement).all()
        return [CommuneDB.model_validate(commune) for commune in communes_db]

    def update(self, commune_id: int, commune_body: dict) -> CommuneDB | None:
        pass

    def delete(self, commune_id: int | None = None) -> bool:
        pass
