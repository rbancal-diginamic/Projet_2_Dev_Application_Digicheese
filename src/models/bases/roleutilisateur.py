from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field


class RoleUtilisateurBase(SQLModel):
    r_utilisateur_id: int | None = Field(default=None, foreign_key="d_utilisateur.u_id", primary_key=True)
    r_role_id: int | None = Field(default=None, foreign_key="d_role.r_id", primary_key=True)