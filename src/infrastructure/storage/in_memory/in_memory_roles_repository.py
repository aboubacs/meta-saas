from typing import Optional

from src.hexagon.gateways.repositories.roles_repository import RolesRepository, RoleIdAlreadyExists, RoleNameTaken
from src.hexagon.models.role import Role


class InMemoryRolesRepository(RolesRepository):
    def __init__(self):
        self.roles = {}

    def get(self, role_id: str) -> Optional[Role]:
        return self.roles.get(role_id)

    def get_by_name(self, instance_id: str, name: str) -> Optional[Role]:
        for role in self.roles.values():
            if role.name == name and role.instance_id == instance_id:
                return role
        return None

    def add(self, role: Role) -> None:
        if role.id in self.roles:
            raise RoleIdAlreadyExists(role.id)
        for role in self.roles.values():
            if role.name == role.name and role.instance_id == role.instance_id:
                raise RoleNameTaken(role.instance_id, role.name)
        self.roles[role.id] = role

    def update(self, role: Role) -> None:
        self.roles[role.id] = role
