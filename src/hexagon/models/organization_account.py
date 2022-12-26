from dataclasses import dataclass

from src.hexagon.types.role import Role


@dataclass
class OrganizationAccount:
    organization_id: str
    user_id: str
    role: Role
