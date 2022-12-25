from typing import Optional

from src.hexagon.gateways.repositories.instances_repository import InstancesRepository, InstanceIdAlreadyExists
from src.hexagon.models.instance import Instance


class InMemoryInstancesRepository(InstancesRepository):
    def __init__(self):
        self.instances = {}

    def get(self, instance_id: str) -> Optional[Instance]:
        return self.instances.get(instance_id)

    def add(self, instance: Instance) -> None:
        if instance.id in self.instances:
            raise InstanceIdAlreadyExists(instance.id)
        self.instances[instance.id] = instance

    def update(self, instance: Instance) -> None:
        self.instances[instance.id] = instance

