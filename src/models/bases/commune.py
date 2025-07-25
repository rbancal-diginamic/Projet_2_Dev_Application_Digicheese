from sqlmodel import SQLModel, Field


class CommuneBase(SQLModel):
    c_ville: str | None = Field(default=None, max_length=50, nullable=True)
    c_code_postal: str | None = Field(default=None, max_length=5, nullable=True)
