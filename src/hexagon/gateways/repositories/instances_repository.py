import abc
from typing import Optional

from src.hexagon.models.instance import Instance


class InstancesRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, instance_id: str) -> Optional[Instance]:
        ...

    @abc.abstractmethod
    def add(self, instance: Instance) -> None:
        ...

    @abc.abstractmethod
    def update(self, instance: Instance) -> None:
        ...


class InstancesRepositoryExceptions(Exception):
    pass


class InstanceIdAlreadyExists(InstancesRepositoryExceptions):
    def __init__(self, instance_id: str):
        super().__init__(f"Instance with id {instance_id} already exists")