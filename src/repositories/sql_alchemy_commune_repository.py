from typing import Optional, List

from sqlmodel import Session, select

from ..models.db_models.commune_db import CommuneDB
from ..repositories.abstract_repository import AbstractRepository


class CommuneRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, commune: dict) -> CommuneDB:
        commune_db = CommuneDB(**commune)
        self.session.add(commune_db)
        self.session.commit()
        return commune_db

    def get_by_id(self, commune_id: int) -> Optional[CommuneDB]:
        statement = select(CommuneDB).where(CommuneDB.c_id == commune_id)
        commune_db = self.session.exec(statement).first()
        if commune_db:
            return commune_db
        return None

    def get_all(self) -> List[CommuneDB] | None:
        statement = select(CommuneDB)
        commune_dbs = self.session.exec(statement).all()
        if commune_dbs:
            return [CommuneDB.model_validate(commune) for commune in commune_dbs]
        return None

    def update(self, commune: dict) -> None:
        statement = select(CommuneDB).where(CommuneDB.c_id == commune["c_id"])
        commune_db = self.session.exec(statement).first()
        if commune_db:
            CommuneDB(**commune.model_dump())
            self.session.commit()

    def delete(self, commune_id: int) -> None:
        statement = select(CommuneDB).where(CommuneDB.c_id == commune_id)
        commune_db = self.session.exec(statement).first()
        if commune_db:
            self.session.delete(commune_db)
            self.session.commit()
            