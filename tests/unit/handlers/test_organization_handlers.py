from src.hexagon.events.organization_events import OrganizationCreated


def test_organization_created_event_should_create_an_organization_account(message_bus, organization_accounts_repository,
                                                                          user):
    message_bus.publish(OrganizationCreated(id="1", name="test-organization", owner_user_id=user.id))
    organization_account = organization_accounts_repository.get(organization_id="1", user_id=user.id)
    assert organization_account
    assert organization_account.role.is_owner()
