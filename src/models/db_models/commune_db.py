from sqlmodel import Field, Relationship

from ..bases.commune import CommuneBase
from .departement_db import DepartementDB


class CommuneDB(CommuneBase, table=True):
    """Schéma de la table Commune représentée en base de données"""
    __tablename__ = "d_commune"
    c_id: int | None = Field(default=None, primary_key=True)
    c_fk_departement_id: int = Field(foreign_key="d_departement.d_id", nullable=True)
    c_departement: DepartementDB | None = Relationship(back_populates="d_communes")
