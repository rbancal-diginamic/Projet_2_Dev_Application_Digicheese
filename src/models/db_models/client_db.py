from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ClientDB(Base):
    __tablename__ = "d_client"
    c_id = Column(Integer, primary_key=True, index=True)
    c_genre = Column(String(8), nullable=True)
    c_nom = Column(String(40), nullable=True)
    c_prenom = Column(String(30), nullable=True)
    c_adresse_1 = Column(String(50), nullable=True)
    c_adresse_2 = Column(String(50), nullable=True)
    c_adresse_3 = Column(String(50), nullable=True)
    c_fk_ville_id = Column(Integer, nullable=True) # FIXME : Corriger le champs avec la FK
    c_telephone = Column(String(13), nullable=True)
    c_email = Column(String(255), nullable=True)
    c_portable = Column(String(13), nullable=True)
    c_newsletter = Column(Boolean, nullable=True)