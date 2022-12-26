from src.hexagon.events.instance_events import InstanceCreated


def test_instance_created_event_should_create_default_roles(message_bus, roles_repository, instance):
    roles_repository.clear()
    message_bus.publish(InstanceCreated(instance_id=instance.id, name=instance.name))
    assert_role_exists(instance, "owner", roles_repository)
    assert_role_exists(instance, "admin", roles_repository)
    assert_role_exists(instance, "member", roles_repository)
    assert_role_exists(instance, "billing_manager", roles_repository)


def assert_role_exists(instance, role_name, roles_repository):
    owner_role = roles_repository.get_by_name(instance_id=instance.id, name=role_name)
    assert owner_role
    assert owner_role.name == role_name
    assert owner_role.instance_id == instance.id
