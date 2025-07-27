from sqlmodel import Session

from src.models.schemas.objetcond.objetcond_patch import ObjetCondPatch
from ..models.db_models.objetcond_db import ObjetCondDB
from ..models.schemas.objetcond.objetcond_post import ObjetCondPost
from ..repositories.sql_alchemy_objetcond_repository import SQLAlchemyObjetCondRepository


class ObjetCondService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyObjetCondRepository(session)

    def create_objetcond(self, objetcond: ObjetCondPost) -> ObjetCondDB:
        objetcond = objetcond.model_dump()
        return self.repository.add(objetcond)

    def get_objetcond_by_id(self, c_id: int | None = None) -> ObjetCondDB |None:
        return self.repository.get_by_id(c_id)

    def get_objetconds(self) -> list[ObjetCondDB]:
        return self.repository.get_all()

    def update_objetcond(self, objetcond_id: int, objetcond_body: ObjetCondPatch) -> ObjetCondDB | None :
        objetcond = objetcond_body.model_dump()
        return self.repository.update(objetcond_id, objetcond)

    def delete_objetcond(self, c_id: int | None = None) -> bool:
        objetcond = self.repository.get_by_id(c_id)
        if objetcond:
            self.repository.delete(objetcond)
            return True
        return False