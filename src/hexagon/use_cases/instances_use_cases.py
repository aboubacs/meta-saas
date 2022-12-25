from dependency_injector.wiring import Provide

from src.hexagon.gateways.repositories.instances_repository import InstancesRepository
from src.hexagon.models.instance import Instance
from src.hexagon.use_cases.instances_commands import CreateInstanceCommand
from src.infrastructure.container import Container

instances_repository: InstancesRepository = Provide[Container.instances_repository]

def create_instance(create_instance_command: CreateInstanceCommand):
    instance = Instance(id=create_instance_command.id, name=create_instance_command.name)
    instances_repository.add(instance)