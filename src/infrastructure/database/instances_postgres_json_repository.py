from src.hexagon.gateways.repositories.instances_repository import InstancesRepository
from src.hexagon.models.instance import Instance


class InstancesPostgresJsonRepository(InstancesRepository):
    def get(self, instance_id: str) -> Instance:
        raise NotImplementedError()

    def add(self, instance: Instance) -> None:
        raise NotImplementedError()

    def update(self, instance: Instance) -> None:
        raise NotImplementedError()