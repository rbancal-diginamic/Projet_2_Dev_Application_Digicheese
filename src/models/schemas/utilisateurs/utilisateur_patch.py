from sqlmodel import Field
from ...bases.utilisateur import UtilisateurBase


class UtilisateurPatch(UtilisateurBase):
    """Schéma Utilisateur pour modification en base de données"""
    u_username: str | None = Field(default=None, max_length=50, nullable=True)
