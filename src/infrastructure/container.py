from dependency_injector import providers, containers

from src.hexagon.gateways.repositories.instances_repository import InstancesRepository


class Container(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    instances_repository = providers.Dependency(instance_of=InstancesRepository)
