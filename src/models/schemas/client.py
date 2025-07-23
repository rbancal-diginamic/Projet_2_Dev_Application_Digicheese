from pydantic import BaseModel
from typing import Optional


class Client(BaseModel):
    id: Optional[int] = None
    genre: str
    nom: str
    prenom: str
    adresse_1: str
    adresse_2: str
    adresse_3: str
    ville_id: int
    telephone: str
    email: str
    portable: str
    newsletter: bool