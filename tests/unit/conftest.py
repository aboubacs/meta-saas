import pytest
from dependency_injector import providers

from src.infrastructure.container import Container
from src.infrastructure.setup import setup
from tests.dummies.in_memory_instances_repository import InMemoryInstancesRepository


@pytest.fixture
def container_with_in_memory_repositories():
    container = Container()
    container.instances_repository = providers.Singleton(InMemoryInstancesRepository)
    yield container
    container.unwire()


@pytest.fixture(autouse=True)
def use_in_memory_repositories(test_app, container_with_in_memory_repositories):
    setup(test_app, container_with_in_memory_repositories)


@pytest.fixture
def instances_repository(test_app):
    return test_app.extra["container"].instances_repository()