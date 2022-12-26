from dependency_injector import providers, containers

from src.hexagon.gateways.email_gateway import EmailGateway
from src.hexagon.gateways.message_bus import MessageBus
from src.hexagon.gateways.repositories.instances_repository import InstancesRepository
from src.hexagon.gateways.repositories.users_repository import UsersRepository


class Container(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    instances_repository = providers.Dependency(instance_of=InstancesRepository)
    users_repository = providers.Dependency(instance_of=UsersRepository)
    message_bus = providers.Dependency(instance_of=MessageBus)
    email_gateway = providers.Dependency(instance_of=EmailGateway)