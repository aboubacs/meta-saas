from src.hexagon.gateways.repositories.instances_repository import InstancesRepository, InstanceAlreadyExists
from src.hexagon.models.instance import Instance


class InMemoryInstancesRepository(InstancesRepository):
    def __init__(self):
        self.instances = {}

    def get(self, instance_id: str) -> Instance:
        return self.instances[instance_id]

    def add(self, instance: Instance) -> None:
        if instance.id in self.instances:
            raise InstanceAlreadyExists(instance.id)
        self.instances[instance.id] = instance

    def update(self, instance: Instance) -> None:
        self.instances[instance.id] = instance

