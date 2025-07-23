from models.bases.client import ClientBase
from sqlalchemy import Integer, Column, String


class ClientPatch(ClientBase):
    c_nom = Column(String(40), nullable=True)
    c_prenom = Column(String(30), nullable=True)
    c_fk_ville_id = Column(Integer, nullable=True)  # FIXME : Corriger le champs avec la FK