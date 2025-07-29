from sqlmodel import Field, SQLModel


class RoleUtilisateurDB(SQLModel, table=True):
    """Schéma de la table RoleUtilisateur représentée en base de données"""
    __tablename__ = "d_utilisateur_role"

    r_utilisateur_id: int | None = Field(default=None, foreign_key="d_utilisateur.u_id", primary_key=True)
    r_role_id: int | None = Field(default=None, foreign_key="d_role.r_id", primary_key=True)