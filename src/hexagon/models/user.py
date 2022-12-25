from dataclasses import dataclass


@dataclass
class User:
    instance_id: str
    id: str
    email: str
    hashed_password: str
    verified: bool = False
