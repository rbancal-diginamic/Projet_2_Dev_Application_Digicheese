from sqlalchemy import Column, String, Boolean
from sqlmodel import SQLModel


class ClientBase(SQLModel):
    c_genre = Column(String(8), nullable=True)
    c_nom = Column(String(40))
    c_prenom = Column(String(30))
    c_adresse_1 = Column(String(50), nullable=True)
    c_adresse_2 = Column(String(50), nullable=True)
    c_adresse_3 = Column(String(50), nullable=True)
    c_telephone = Column(String(13), nullable=True)
    c_email = Column(String(255), nullable=True)
    c_portable = Column(String(13), nullable=True)
    c_newsletter = Column(Boolean, nullable=True)