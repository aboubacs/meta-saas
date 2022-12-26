import pytest
from dependency_injector import providers

from src.infrastructure.container import Container
from src.infrastructure.message_bus.in_memory_message_bus import InMemoryMessageBus
from src.infrastructure.storage.in_memory.in_memory_users_repository import InMemoryUsersRepository
from src.infrastructure.setup import setup
from src.infrastructure.storage.in_memory.in_memory_instances_repository import InMemoryInstancesRepository
from src.hexagon.models.instance import Instance
from tests.fakes.spy_email_gateway import SpyEmailGateway


@pytest.fixture
def unit_test_container():
    container = Container()
    container.instances_repository = providers.Singleton(InMemoryInstancesRepository)
    container.users_repository = providers.Singleton(InMemoryUsersRepository)
    container.message_bus = providers.Singleton(InMemoryMessageBus)
    container.email_gateway = providers.Singleton(SpyEmailGateway)
    yield container
    container.unwire()


@pytest.fixture(autouse=True)
def use_in_memory_repositories(test_app, unit_test_container):
    setup(test_app, unit_test_container)


@pytest.fixture
def instances_repository(test_app):
    return test_app.extra["container"].instances_repository()


@pytest.fixture
def users_repository(test_app):
    return test_app.extra["container"].users_repository()


@pytest.fixture
def message_bus(test_app):
    return test_app.extra["container"].message_bus()


@pytest.fixture
def email_gateway(test_app):
    return test_app.extra["container"].email_gateway()


@pytest.fixture
def instance(instances_repository):
    instance = Instance(id="1", name="test-instance")
    instances_repository.add(instance)
    return instance
