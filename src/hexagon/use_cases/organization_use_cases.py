from dependency_injector.wiring import Provide

from src.hexagon.models.organization import Organization
from src.hexagon.use_cases.organization_commands import CreateOrganizationCommand
from src.infrastructure.container import Container

organizations_repository = Provide[Container.organizations_repository]


def create_organization(command: CreateOrganizationCommand) -> None:
    organization = Organization(id=command.id, name=command.name, owner_user_id=command.owner_user_id)
    organizations_repository.add(organization)
