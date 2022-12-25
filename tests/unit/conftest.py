import pytest
from dependency_injector import providers

from src.infrastructure.container import Container
from src.infrastructure.in_memory.in_memory_users_repository import InMemoryUsersRepository
from src.infrastructure.setup import setup
from src.infrastructure.in_memory.in_memory_instances_repository import InMemoryInstancesRepository
from src.hexagon.models.instance import Instance


@pytest.fixture
def container_with_in_memory_repositories():
    container = Container()
    container.instances_repository = providers.Singleton(InMemoryInstancesRepository)
    container.users_repository = providers.Singleton(InMemoryUsersRepository)
    yield container
    container.unwire()


@pytest.fixture(autouse=True)
def use_in_memory_repositories(test_app, container_with_in_memory_repositories):
    setup(test_app, container_with_in_memory_repositories)


@pytest.fixture
def instances_repository(test_app):
    return test_app.extra["container"].instances_repository()


@pytest.fixture
def users_repository(test_app):
    return test_app.extra["container"].users_repository()


@pytest.fixture
def instance(instances_repository):
    instance = Instance(id="1", name="test-instance")
    instances_repository.add(instance)
    return instance
