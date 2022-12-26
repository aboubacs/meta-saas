import pytest

from src.hexagon.events.instance_events import InstanceCreated
from src.hexagon.gateways.repositories.instances_repository import InstanceIdAlreadyExists
from src.hexagon.use_cases.instance_use_cases import create_instance
from src.hexagon.use_cases.instance_commands import CreateInstanceCommand


def test_should_create_instance_with_the_right_name(instances_repository):
    create_instance(CreateInstanceCommand(id="instance-1", name="test-instance"))
    instance = instances_repository.get("instance-1")
    assert instance.id == "instance-1"
    assert instance.name == "test-instance"


def test_should_raise_if_instance_id_already_exists(instances_repository):
    create_instance(CreateInstanceCommand(id="instance-1", name="test-instance"))
    with pytest.raises(InstanceIdAlreadyExists):
        create_instance(CreateInstanceCommand(id="instance-1", name="test-instance"))


def test_should_emit_instance_created_event(message_bus):
    create_instance(CreateInstanceCommand(id="instance-1", name="test-instance"))
    assert message_bus.messages
    assert isinstance(message_bus.messages[0], InstanceCreated)
    assert message_bus.messages[0].instance_id == "instance-1"
    assert message_bus.messages[0].name == "test-instance"
