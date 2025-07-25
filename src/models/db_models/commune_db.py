from sqlmodel import Field, Relationship
from ..bases.commune import Commune
from ..bases.departement import Departement


class CommuneDB(Commune, table=True):
    __tablename__ = "d_commune"
    c_id: int | None = Field(default=None, primary_key=True)
    c_fk_departement_id: int = Field(foreign_key="d_departement.d_id", nullable=False)
    c_departement: Departement | None = Relationship(back_populates="commune")