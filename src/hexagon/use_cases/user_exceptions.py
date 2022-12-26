class UserUseCasesExceptions(Exception):
    pass


class UserDoesNotExist(UserUseCasesExceptions):
    def __init__(self, user_id: str):
        super().__init__(f"User with id {user_id} does not exist")


class UserAlreadyActivated(UserUseCasesExceptions):
    def __init__(self, user_id: str):
        super().__init__(f"User with id {user_id} is already activated")


class InvalidActivationToken(UserUseCasesExceptions):
    def __init__(self, user_id: str):
        super().__init__(f"Invalid activation token for user with id {user_id}")