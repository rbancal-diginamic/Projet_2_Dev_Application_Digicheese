from typing import List

from sqlmodel import Field, Relationship

from ..bases.commune import Commune
from ..bases.departement import Departement


class DepartementDB(Departement, table=True):
    __tablename__ = "d_departement"
    d_id: int | None = Field(default=None, primary_key=True)
    d_communes: List["Commune"] = Relationship(back_populates="departement")