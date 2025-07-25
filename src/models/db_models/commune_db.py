from sqlmodel import Field, Relationship
from ..bases.commune import CommuneBase
from ..bases.departement import DepartementBase


class CommuneDB(CommuneBase, table=True):
    __tablename__ = "d_commune"
    c_id: int | None = Field(default=None, primary_key=True)
    c_fk_departement_id: int = Field(foreign_key="d_departement.d_id", nullable=False)
    c_departement: DepartementBase | None = Relationship(back_populates="commune")
