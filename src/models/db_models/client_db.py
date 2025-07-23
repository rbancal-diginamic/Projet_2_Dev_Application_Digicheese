from sqlalchemy import Column, Integer, String, Boolean
from models.bases.client import ClientBase


class ClientDB(ClientBase, table=True):
    __tablename__ = "d_client"
    c_id = Column(Integer, primary_key=True, index=True)
    c_fk_ville_id = Column(Integer, nullable=True) # FIXME : Corriger le champs avec la FK