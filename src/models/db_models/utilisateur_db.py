from typing import List
from sqlmodel import Field, Relationship
from src.models.bases.role import RoleBase
from src.models.db_models.roleutilisateur_db import RoleUtilisateurDB
from ..bases.utilisateur import UtilisateurBase


class UtilisateurDB(UtilisateurBase, table=True):
    __tablename__ = "d_utilisateur"
    u_id: int | None = Field(default=None, primary_key=True)

    u_role: List["RoleBase"] = Relationship(back_populates="r_utilisateur", link_model=RoleUtilisateurDB)