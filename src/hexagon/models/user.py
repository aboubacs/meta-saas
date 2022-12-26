from dataclasses import dataclass


@dataclass
class User:
    instance_id: str
    id: str
    email: str
    hashed_password: str
    activated: bool = False

    def activate(self):
        self.activated = True
