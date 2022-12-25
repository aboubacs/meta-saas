from fastapi import FastAPI
from dependency_injector import providers

from src.infrastructure.container import Container
from src.infrastructure.database.instances_postgres_json_repository import InstancesPostgresJsonRepository


def setup_live_container(container: Container):
    container.instances_repository = providers.Singleton(InstancesPostgresJsonRepository)


def setup(app: FastAPI, container: Container) -> None:
    # Add other controllers here
    # app.include_router(todo_controller.router)

    app.extra["container"] = container

    # Inject dependencies
    container.wire(
        packages=[
            "src.hexagon.use_cases",
        ]
    )
