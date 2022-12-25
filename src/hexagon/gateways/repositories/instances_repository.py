import abc

from src.hexagon.models.instance import Instance


class InstancesRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, instance_id: str) -> Instance:
        pass

    @abc.abstractmethod
    def add(self, instance: Instance) -> None:
        pass

    @abc.abstractmethod
    def update(self, instance: Instance) -> None:
        pass


class InstancesRepositoryErrors(Exception):
    pass


class InstanceAlreadyExists(InstancesRepositoryErrors):
    def __init__(self, instance_id: str):
        super().__init__(f"Instance with id {instance_id} already exists")