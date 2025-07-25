from sqlmodel import Session

from ..models.db_models.commune_db import CommuneDB
from ..repositories.sql_alchemy_commune_repository import SQLAlchemyCommuneRepository


class CommuneService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyCommuneRepository(session)

    def get_commune_by_id(self, commmune_id: int | None = None) -> CommuneDB:
        return self.repository.get_by_id(commmune_id)

    def get_communes(self):
        return self.repository.get_all()