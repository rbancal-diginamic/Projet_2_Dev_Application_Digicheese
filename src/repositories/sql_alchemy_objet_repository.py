
from typing import Optional, List
from sqlmodel import Session, select

from ..models.db_models.client_db import ObjetDB
from ..repositories.abstract_repository import AbstractRepository



class SQLAlchemyObjetRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, objet: dict) -> ObjetDB:
        objet_db = ObjetDB(**objet)
        self.session.add(objet_db)
        self.session.commit()

    def get_by_id(self, objet_id: ObjetDB.o_id) -> Optional[ObjetDB]:
        statement = select(ObjetDB).where(ObjetDB.c_id == objet_id)
        objet_db = self.session.exec(statement).first()
        if objet_db:
            return objet_db
        return None
    
    def get_by_name(self, client_nom: ObjetDB.o_nom) -> Optional[ObjetDB]:
        statement = select(ObjetDB).where(ObjetDB.c_nom == objet_nom)
        objet_db = self.session.exec(statement).first()
        if objet_db:
            return objet_db
        return None

    def get_all(self) -> List[ObjetDB]:
        objet_db = self.session.query(ObjetDB).all()
        return [ObjetDB.model_validate(c) for c in objet_db]

   def update(self, objet: dict) -> None:
        objet_db = self.session.query(ObjetDB).get(objet.id)
        if objet_db:
            # FIXME : Contrôler la bonne exécution de l'update !
            ObjetDB(**objet.model_dump())
            self.session.commit()

    def delete(self, objet_id: ObjetDB.c_id) -> None:
        objet_db = self.session.query(ObjetDB).get(objet_id)
        if objet_db:
            self.session.delete(objet_db)
            self.session.commit()
