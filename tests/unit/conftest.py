import pytest
from dependency_injector import providers

from src.hexagon.models.role import Role
from src.hexagon.models.user import User
from src.infrastructure.container import Container
from src.infrastructure.message_bus.in_memory_message_bus import InMemoryMessageBus
from src.infrastructure.storage.in_memory.in_memory_organization_accounts_repository import \
    InMemoryOrganizationAccountsRepository
from src.infrastructure.storage.in_memory.in_memory_organizations_repository import InMemoryOrganizationsRepository
from src.infrastructure.storage.in_memory.in_memory_roles_repository import InMemoryRolesRepository
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
    container.organizations_repository = providers.Singleton(InMemoryOrganizationsRepository)
    container.organization_accounts_repository = providers.Singleton(InMemoryOrganizationAccountsRepository)
    container.roles_repository = providers.Singleton(InMemoryRolesRepository)
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
def organizations_repository(test_app):
    return test_app.extra["container"].organizations_repository()


@pytest.fixture
def organization_accounts_repository(test_app):
    return test_app.extra["container"].organization_accounts_repository()


@pytest.fixture
def roles_repository(test_app):
    return test_app.extra["container"].roles_repository()


@pytest.fixture
def message_bus(test_app):
    return test_app.extra["container"].message_bus()


@pytest.fixture
def email_gateway(test_app):
    return test_app.extra["container"].email_gateway()


@pytest.fixture
def instance(instances_repository, roles_repository):
    instance = Instance(id="instance-1", name="test-instance")
    instances_repository.add(instance)
    roles_repository.add(Role(id="role-1", name="owner", instance_id=instance.id))
    return instance


@pytest.fixture
def owner_role(roles_repository, instance):
    roles_repository.get_by_name(instance_id=instance.id, name="owner")


@pytest.fixture
def user(users_repository, instance):
    user = User(id="user-1", email="test-email@email.com", instance_id=instance.id, hashed_password="hashed-password")
    users_repository.add(user)
    return user
