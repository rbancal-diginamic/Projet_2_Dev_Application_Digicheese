from sqlmodel import Session

from src.models.schemas.conditionnements.conditionnement_patch import ConditionnementPatch
from ..models.db_models.conditionnement_db import ConditionnementDB
from ..models.schemas.conditionnements.conditionnement_post import ConditionnementPost
from ..repositories.sql_alchemy_conditionnement_repository import SQLAlchemyConditionnementRepository


class ConditionnementService:
    """Service to do treatments on Conditionnement entities before commit in database."""
    def __init__(self, session: Session):
        self.repository = SQLAlchemyConditionnementRepository(session)

    def create_conditionnement(self, conditionnement: ConditionnementPost) -> ConditionnementDB:
        conditionnement = conditionnement.model_dump()
        return self.repository.add(conditionnement)

    def get_conditionnement_by_id(self, c_id: int | None = None) -> ConditionnementDB |None:
        return self.repository.get_by_id(c_id)

    def get_conditionnements(self) -> list[ConditionnementDB]:
        return self.repository.get_all()

    def update_conditionnement(self, conditionnement_id: int, conditionnement_body: ConditionnementPatch) -> ConditionnementDB | None :
        conditionnement = conditionnement_body.model_dump(exlude_unset=True)
        return self.repository.update(conditionnement_id, conditionnement)

    def delete_conditionnement(self, c_id: int | None = None) -> bool:
        conditionnement = self.repository.get_by_id(c_id)
        if conditionnement:
            self.repository.delete(conditionnement)
            return True
        return False