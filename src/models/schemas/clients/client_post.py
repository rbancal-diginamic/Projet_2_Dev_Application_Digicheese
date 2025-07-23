from models.bases.client import ClientBase
from sqlalchemy import Integer, Column


class ClientPost(ClientBase):
    c_fk_ville_id = Column(Integer, nullable=True)  # FIXME : Corriger le champs avec la FK