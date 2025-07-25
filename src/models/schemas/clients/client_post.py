from sqlmodel import Field
from ...bases.client import ClientBase


class ClientPost(ClientBase):
    c_fk_ville_id: int | None = Field(default=None, foreign_key="d_communes.id", nullable=True)
