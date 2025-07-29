from typing import List, TYPE_CHECKING
from sqlmodel import Field, Relationship

from ..bases.utilisateur import UtilisateurBase

from .roleutilisateur_db import RoleUtilisateurDB

if TYPE_CHECKING:
    from ..db_models import RoleDB


class UtilisateurDB(UtilisateurBase, table=True):
    """Schéma de la table Utilisateur représentée en base de données"""
    __tablename__ = "d_utilisateur"
    u_id: int | None = Field(default=None, primary_key=True)

    u_roles: List["RoleDB"] = Relationship(back_populates="r_utilisateurs", link_model=RoleUtilisateurDB)
