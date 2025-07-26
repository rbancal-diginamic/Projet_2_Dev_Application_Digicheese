from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field


class RoleBase(SQLModel):
    r_nom: str | None = Field(default=None, max_length=25, nullable=True)