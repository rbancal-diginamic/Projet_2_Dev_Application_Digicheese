from sqlmodel import Session

from ..models.db_models.departement_db import DepartementDB
from ..repositories.sql_alchemy_departement_repository import SQLAlchemyDepartementRepository


class DepartementService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyDepartementRepository(session)

    def get_departement_by_id(self, departement_id: int | None = None) -> DepartementDB:
        return self.repository.get_by_id(departement_id)

    def get_departements(self) -> list[DepartementDB]:
        return self.repository.get_all()