from sqlmodel import Field
from ...bases.utilisateur import UtilisateurBase


class UtilisateurPost(UtilisateurBase):
    u_username: str | None = Field(max_length=50, nullable=True)