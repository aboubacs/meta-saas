from fastapi import FastAPI
from dependency_injector import providers

from src.infrastructure.container import Container
from src.infrastructure.storage.database.instances_postgres_json_repository import InstancesPostgresJsonRepository
from src.hexagon.handlers import wiring


def setup_live_container(container: Container):
    container.instances_repository = providers.Singleton(InstancesPostgresJsonRepository)


def setup(app: FastAPI, container: Container) -> None:
    # Add other controllers here
    # app.include_router(todo_controller.router)

    container.config.jwt_algorithm.from_env("JWT_ALGORITHM", "HS256")
    container.config.jwt_secret_key.from_env("JWT_SECRET_KEY", "secret")

    app.extra["container"] = container

    # Inject dependencies
    container.wire(
        packages=[
            "src.hexagon.use_cases",
            "src.hexagon.handlers",
            "src.hexagon.gateways",
            "src.hexagon.services",
        ]
    )
    wiring.wire(container.message_bus())
