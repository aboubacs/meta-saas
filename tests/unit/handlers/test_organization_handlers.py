from src.hexagon.events.organization_events import OrganizationCreated


def test_organization_created_event_should_create_an_organization_account(message_bus, organization_accounts_repository,
                                                                          user, roles_repository):
    message_bus.publish(
        OrganizationCreated(organization_id="organization-1", name="test-organization", owner_user_id=user.id,
                            instance_id=user.instance_id))
    organization_account = organization_accounts_repository.get(organization_id="organization-1", user_id=user.id)
    assert organization_account
    assert organization_account.organization_id == "organization-1"
    assert organization_account.user_id == user.id
    assert organization_account.role_id == roles_repository.get_by_name(instance_id="instance-1", name="owner").id
