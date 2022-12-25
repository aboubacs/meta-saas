from dependency_injector import providers, containers

from src.hexagon.gateways.repositories.instances_repository import InstancesRepository
from src.hexagon.gateways.repositories.users_repository import UsersRepository


class Container(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    instances_repository = providers.Dependency(instance_of=InstancesRepository)
    users_repository = providers.Dependency(instance_of=UsersRepository)
