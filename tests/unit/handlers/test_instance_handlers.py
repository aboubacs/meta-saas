from src.hexagon.events.instance_events import InstanceCreated


def test_instance_created_event_should_create_default_roles(message_bus, roles_repository, user):
    message_bus.publish(InstanceCreated(instance_id="instance-1", name="test-instance"))
    """instance_role = roles_repository.get(instance_id="instance-1", )
    assert instance_role
    assert instance_role.instance_id == "1"
    assert instance_role.role == "owner"
    """