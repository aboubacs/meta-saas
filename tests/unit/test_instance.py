import pytest

from src.hexagon.gateways.repositories.instances_repository import InstanceAlreadyExists
from src.hexagon.use_cases import instances_use_cases
from src.hexagon.use_cases.instances_commands import CreateInstanceCommand


def test_should_create_instance_with_the_right_name(instances_repository):
    instances_use_cases.create_instance(CreateInstanceCommand(id="1", name="test-instance"))
    instance = instances_repository.get("1")
    assert instance.id == "1"
    assert instance.name == "test-instance"


def test_should_raise_if_instance_id_already_exists(instances_repository):
    instances_use_cases.create_instance(CreateInstanceCommand(id="1", name="test-instance"))
    with pytest.raises(InstanceAlreadyExists):
        instances_use_cases.create_instance(CreateInstanceCommand(id="1", name="test-instance"))