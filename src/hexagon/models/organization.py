from dataclasses import dataclass


@dataclass
class Organization:
    id: str
    name: str
    owner_user_id: str
    instance_id: str