from enum import Enum


class Role(Enum):
    OWNER = 1
    ADMIN = 2
    MEMBER = 3

    def is_owner(self):
        return self == Role.OWNER

    def is_admin(self):
        return self in [Role.OWNER, Role.ADMIN]