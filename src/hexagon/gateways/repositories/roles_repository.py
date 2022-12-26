import abc
from typing import Optional

from src.hexagon.models.role import Role


class RolesRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, role_id: str) -> Optional[Role]:
        ...

    @abc.abstractmethod
    def get_by_name(self, instance_id: str, name: str) -> Optional[Role]:
        ...

    @abc.abstractmethod
    def add(self, role: Role) -> None:
        ...

    @abc.abstractmethod
    def update(self, role: Role) -> None:
        ...


class RolesRepositoryExceptions(Exception):
    pass


class RoleIdAlreadyExists(RolesRepositoryExceptions):
    def __init__(self, role_id: str):
        super().__init__(f"Role with id {role_id} already exists")


class RoleNameTaken(RolesRepositoryExceptions):
    def __init__(self, instance_id: str, name: str):
        super().__init__(f"Role with name {name} already exists in instance {instance_id}")
