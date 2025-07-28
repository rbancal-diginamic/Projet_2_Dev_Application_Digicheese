from typing import List, TYPE_CHECKING
from sqlmodel import Field, Relationship

from ..bases.departement import DepartementBase
if TYPE_CHECKING:
    from .commune_db import CommuneDB


class DepartementDB(DepartementBase, table=True):
    __tablename__ = "d_departement"
    d_id: int | None = Field(default=None, primary_key=True)
    d_communes: List["CommuneDB"] = Relationship(back_populates="c_departement")