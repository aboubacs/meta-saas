from dependency_injector.wiring import Provide

from src.hexagon.events.organization_events import OrganizationCreated
from src.hexagon.gateways.repositories.organization_accounts_repository import OrganizationAccountsRepository
from src.hexagon.models.organization_account import OrganizationAccount
from src.hexagon.types.role import Role
from src.infrastructure.container import Container

organization_accounts_repository: OrganizationAccountsRepository = Provide[Container.organization_accounts_repository]


def create_owner_organization_account(organization_created_event: OrganizationCreated) -> None:
    organization_account = OrganizationAccount(
        organization_id=organization_created_event.id,
        user_id=organization_created_event.owner_user_id,
        role=Role.OWNER,
    )
    organization_accounts_repository.add(organization_account)
