import pytest

from src.hexagon.gateways.repositories.instances_repository import InstanceIdAlreadyExists
from src.hexagon.use_cases.instance_use_cases import create_instance
from src.hexagon.use_cases.instance_commands import CreateInstanceCommand


def test_should_create_instance_with_the_right_name(instances_repository):
    create_instance(CreateInstanceCommand(id="1", name="test-instance"))
    instance = instances_repository.get("1")
    assert instance.id == "1"
    assert instance.name == "test-instance"


def test_should_raise_if_instance_id_already_exists(instances_repository):
    create_instance(CreateInstanceCommand(id="1", name="test-instance"))
    with pytest.raises(InstanceIdAlreadyExists):
        create_instance(CreateInstanceCommand(id="1", name="test-instance"))
