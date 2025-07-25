
from typing import Optional, List

from sqlmodel import Session, select
from ..models.db_models.objet_db import ObjetDB
from ..repositories.abstract_repository import AbstractRepository



class SQLAlchemyObjetRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, objet: dict) -> ObjetDB:
        objet_db = ObjetDB(**objet)
        self.session.add(objet_db)
        self.session.commit()
        return objet_db

    def get_by_id(self, objet_id: int) -> Optional[ObjetDB]:
        statement = select(ObjetDB).where(ObjetDB.o_id == objet_id)
        objet_db = self.session.exec(statement).first()
        if objet_db:
            return objet_db
        return None

    def get_all(self) -> List[ObjetDB] | None:
        statement = select(ObjetDB)
        objet_dbs = self.session.exec(statement).all()
        if objet_dbs:
            return [ObjetDB.model_validate(objet) for objet in objet_dbs]
        return None

    def update(self, objet: dict) -> None:
        statement= select(ObjetDB).where(ObjetDB.o_id==objet["o_id"])
        objet_db = self.session.exec(statement).first()
        if objet_db:
            ObjetDB(**objet.model_dump())
            self.session.commit()

    def delete(self, objet_id: int) -> None:
        statement= select(ObjetDB).where(ObjetDB.o_id == objet_id)
        objet_db = self.session.exec(statement).first()
        if objet_db:
            self.session.delete(objet_db)
            self.session.commit()
