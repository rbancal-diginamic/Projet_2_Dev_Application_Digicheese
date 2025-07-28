from sqlmodel import Field
from ..bases.role import RoleBase

class RoleDB(RoleBase, table = True):
    __tablename__ = "d_role"
    r_id: int | None = Field(default=None, primary_key=True)