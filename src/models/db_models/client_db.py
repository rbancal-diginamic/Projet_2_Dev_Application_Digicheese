from sqlmodel import Field
from ..bases.client import ClientBase


class ClientDB(ClientBase, table=True):
    __tablename__ = "d_client"
    c_id: int | None = Field(default=None, primary_key=True)
    c_fk_ville_id: int | None = Field(default=None, foreign_key="d_commune.c_id", nullable=True)
