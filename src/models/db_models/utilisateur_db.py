from typing import List
from sqlmodel import Field, Relationship
from src.models.bases import role, roleutilisateur
from ..bases.utilisateur import UtilisateurBase


class UtilisateurDB(UtilisateurBase, table=True):
    __tablename__ = "d_utilisateur"
    u_id: int | None = Field(default=None, primary_key=True)

    u_role: List["role"] = Relationship(backpopulates="r_utilisateur", link_model=roleutilisateur)