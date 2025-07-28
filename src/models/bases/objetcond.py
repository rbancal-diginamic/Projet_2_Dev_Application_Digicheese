from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field


class ObjetCondBase(SQLModel):
    """Table représentant la relation entre les objets et les conditionnements."""

    o_quantite_objet_debut: int = Field(default=0)
    o_quantite_objet_fin: int = Field(default=0)
    #o_codobj: int | None = Field(default=None, foreign_key="t_objet.codobj", nullable=True)
    #o_codcond: int | None = Field(default=None, foreign_key="t_conditionnement.idcondit", nullable=True)
    
    #objets: Objet | None = Relationship(back_populates="condit")
    #condit: Conditionnement | None = Relationship(back_populates="objets")
