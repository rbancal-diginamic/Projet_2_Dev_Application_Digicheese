from sqlmodel import Session

from src.models.schemas.objets.objet_patch import ObjetPatch
from ..models.db_models.objet_db import ObjetDB
from ..models.schemas.objets.objet_post import ObjetPost
from ..repositories.sql_alchemy_objet_repository import SQLAlchemyObjetRepository


class ObjetService:
    """Service to do treatments on Objet entities before commit in database."""
    def __init__(self, session: Session):
        self.repository = SQLAlchemyObjetRepository(session)

    def create_objet(self, objet: ObjetPost) -> ObjetDB:
        objet = objet.model_dump()
        return self.repository.add(objet)

    def get_objet_by_id(self, o_id: int | None = None) -> ObjetDB |None:
        return self.repository.get_by_id(o_id)

    def get_objets(self) -> list[ObjetDB]:
        return self.repository.get_all()

    def update_objet(self, objet_id: int, objet_body: ObjetPatch) -> ObjetDB | None :
        objet = objet_body.model_dump(exlude_unset=True)
        return self.repository.update(objet_id, objet)

    def delete_objet(self, o_id: int | None = None) -> bool:
        objet = self.repository.get_by_id(o_id)
        if objet:
            self.repository.delete(objet)
            return True
        return False