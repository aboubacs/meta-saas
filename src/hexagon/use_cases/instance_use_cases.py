from dependency_injector.wiring import Provide

from src.hexagon.events.instance_events import InstanceCreated
from src.hexagon.gateways.message_bus import MessageBus
from src.hexagon.gateways.repositories.instances_repository import InstancesRepository
from src.hexagon.models.instance import Instance
from src.hexagon.use_cases.instance_commands import CreateInstanceCommand
from src.infrastructure.container import Container

instances_repository: InstancesRepository = Provide[Container.instances_repository]
message_bus: MessageBus = Provide[Container.message_bus]


def create_instance(create_instance_command: CreateInstanceCommand):
    instance = Instance(id=create_instance_command.id, name=create_instance_command.name)
    instances_repository.add(instance)
    message_bus.publish(InstanceCreated(instance_id=instance.id, name=instance.name))
