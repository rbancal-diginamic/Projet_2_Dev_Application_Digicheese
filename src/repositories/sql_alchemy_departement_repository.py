from typing import List

from sqlmodel import Session, select
from ..models.db_models.departement_db import DepartementDB
from ..repositories.abstract_repository import AbstractRepository


class SQLAlchemyDepartementRepository(AbstractRepository):
    """Repository for managing Departement entities in the database."""
    def __init__(self, session: Session):
        self.session = session

    def add(self, departement: dict) -> DepartementDB:
        pass

    def get_by_id(self, departement_id: int | None = None) -> DepartementDB | None:
        statement = select(DepartementDB).where(DepartementDB.d_id == departement_id)

        departement_db = self.session.exec(statement).first()
        if departement_db:
            return departement_db
        return None

    def get_all(self) -> List[DepartementDB]:
        statement = select(DepartementDB)
        departements_db = self.session.exec(statement).all()
        return [DepartementDB.model_validate(departement) for departement in departements_db]

    def update(self, departement: dict) -> DepartementDB | None:
        pass

    def delete(self, departement_id: DepartementDB.d_id) -> bool:
        pass
