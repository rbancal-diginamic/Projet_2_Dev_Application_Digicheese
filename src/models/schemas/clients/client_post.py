from sqlmodel import Field
from ...bases.client import ClientBase


class ClientPost(ClientBase):
    """Schéma Client pour création en base de données"""
    c_fk_ville_id: int | None = Field(default=None, foreign_key="d_communes.id", nullable=True)
