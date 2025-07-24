from sqlmodel import Field
from ..bases.objet import ObjetBase


class ObjetDB(ObjetBase, table=True):
    __tablename__ = "d_objet"
    o_id: int | None = Field(default=None, primary_key=True)
    # FIXME : Décommenter après avoir créer les autres tables !
    # condit: List["ObjetCond"] = Relationship(back_populates="objets" A VOIR par la suite