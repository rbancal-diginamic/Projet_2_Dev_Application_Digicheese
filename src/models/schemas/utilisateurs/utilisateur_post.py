from sqlmodel import Field
from ...bases.utilisateur import UtilisateurBase


class UtilisateurPost(UtilisateurBase):
    """Schéma Utilisateur pour création en base de données"""
    u_username: str | None = Field(max_length=50, nullable=True)
