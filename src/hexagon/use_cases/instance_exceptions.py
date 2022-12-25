class InstanceUseCasesExceptions(Exception):
    pass


class InstanceDoesNotExist(InstanceUseCasesExceptions):
    def __init__(self, instance_id: str):
        super().__init__(f"Instance with id {instance_id} does not exist")