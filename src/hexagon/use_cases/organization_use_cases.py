from dependency_injector.wiring import Provide

from src.hexagon.events.organization_events import OrganizationCreated
from src.hexagon.gateways.message_bus import MessageBus
from src.hexagon.models.organization import Organization
from src.hexagon.models.user import User
from src.hexagon.use_cases.organization_commands import CreateOrganizationCommand
from src.infrastructure.container import Container

organizations_repository = Provide[Container.organizations_repository]
message_bus: MessageBus = Provide[Container.message_bus]


def create_organization(command: CreateOrganizationCommand, user: User) -> None:
    organization = Organization(id=command.id, name=command.name, owner_user_id=user.id, instance_id=user.instance_id)
    organizations_repository.add(organization)
    message_bus.publish(OrganizationCreated(organization_id=organization.id, name=organization.name,
                                            owner_user_id=organization.owner_user_id,
                                            instance_id=user.instance_id))
