import pytest

from src.hexagon.events.organization_events import OrganizationCreated
from src.hexagon.gateways.repositories.organizations_repository import OrganizationIdAlreadyExists
from src.hexagon.use_cases.organization_commands import CreateOrganizationCommand
from src.hexagon.use_cases.organization_use_cases import create_organization


@pytest.fixture
def command():
    return CreateOrganizationCommand(id="1", name="test-organization")


def test_should_create_organization_with_the_right_name_and_owner_id(organizations_repository, command, user):
    create_organization(command, user)
    organization = organizations_repository.get("1")
    assert organization.id == "1"
    assert organization.name == "test-organization"
    assert organization.owner_user_id == user.id


def test_should_raise_if_organization_id_already_exists(organizations_repository, command, user):
    create_organization(command, user)
    with pytest.raises(OrganizationIdAlreadyExists):
        create_organization(command, user)


def test_should_emit_organization_created_event(message_bus, user, command):
    create_organization(command, user)
    assert message_bus.messages
    assert isinstance(message_bus.messages[0], OrganizationCreated)
    assert message_bus.messages[0].id == "1"
    assert message_bus.messages[0].name == "test-organization"
    assert message_bus.messages[0].owner_user_id == user.id
