from typing import List
from sqlmodel import Field, Relationship

from .commune_db import CommuneDB
from ..bases.departement import DepartementBase


class DepartementDB(DepartementBase, table=True):
    __tablename__ = "d_departement"
    d_id: int | None = Field(default=None, primary_key=True)
    d_communes: List["CommuneDB"] = Relationship(back_populates="departement")