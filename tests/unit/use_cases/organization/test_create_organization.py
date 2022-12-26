import pytest

from src.hexagon.gateways.repositories.organizations_repository import OrganizationIdAlreadyExists
from src.hexagon.use_cases.organization_commands import CreateOrganizationCommand
from src.hexagon.use_cases.organization_use_cases import create_organization


def test_should_create_organization_with_the_right_name_and_owner_id(organizations_repository, user):
    create_organization(CreateOrganizationCommand(id="1", name="test-organization", owner_user_id=user.id))
    organization = organizations_repository.get("1")
    assert organization.id == "1"
    assert organization.name == "test-organization"
    assert organization.owner_user_id == user.id


def test_should_raise_if_organization_id_already_exists(organizations_repository, user):
    create_organization(CreateOrganizationCommand(id="1", name="test-organization", owner_user_id=user.id))
    with pytest.raises(OrganizationIdAlreadyExists):
        create_organization(CreateOrganizationCommand(id="1", name="test-organization", owner_user_id=user.id))