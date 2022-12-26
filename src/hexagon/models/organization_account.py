from dataclasses import dataclass


@dataclass
class OrganizationAccount:
    organization_id: str
    user_id: str
    role_id: str
