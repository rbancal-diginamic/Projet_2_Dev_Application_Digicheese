from typing import Optional, List

from sqlmodel import Session, select
from ..models.db_models.departement_db import DepartementDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyDepartementRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, departement: dict) -> DepartementDB:
        departement_db = DepartementDB(**departement)
        self.session.add(departement_db)
        self.session.commit()
        return departement_db

    def get_by_id(self, departement_id: int) -> Optional[DepartementDB]:
        statement = select(DepartementDB).where(DepartementDB.d_id == departement_id)
        departement_db = self.session.exec(statement).first()
        if departement_db:
            return departement_db
        return None

    def get_all(self) -> List[DepartementDB] | None:
        statement = select(DepartementDB)
        departement_dbs = self.session.exec(statement).all()
        if departement_dbs:
            return [DepartementDB.model_validate(departement) for departement in departement_dbs]
        return None

    def update(self, departement: dict) -> None:
        statement = select(DepartementDB).where(DepartementDB.d_id == departement["d_id"])
        departement_db = self.session.exec(statement).first()
        if departement_db:
            DepartementDB(**departement.model_dump())
            self.session.commit()

    def delete(self, departement_id: int) -> None:
        statement = select(DepartementDB).where(DepartementDB.d_id == departement_id)
        departement_db = self.session.exec(statement).first()
        if departement_db:
            self.session.delete(departement_db)
            self.session.commit()
