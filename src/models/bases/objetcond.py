from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field


class ObjetCond(SQLModel, table=True):
    """Table représentant la relation entre les objets et les conditionnements."""

    #o_idrelcond: int | None = Field(default=None, primary_key=True, index=True)
    o_quantite_objet_debut: int = Field(default=0)
    o_quantite_objet_fin: int = Field(default=0)
    #o_codobj: int | None = Field(default=None, foreign_key="t_objet.codobj", nullable=True)
    #o_codcond: int | None = Field(default=None, foreign_key="t_conditionnement.idcondit", nullable=True)
    
    #objets: Objet | None = Relationship(back_populates="condit")
    #condit: Conditionnement | None = Relationship(back_populates="objets")
