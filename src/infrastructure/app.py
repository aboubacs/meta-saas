import logging

from fastapi import FastAPI
import uvicorn

from src.infrastructure.container import Container
from src.infrastructure.setup import setup, setup_live_container


def init() -> FastAPI:
    container = Container()

    container.config.log_level.from_env("LOG_LEVEL", "INFO")

    str_level = container.config.log_level()
    numeric_level = getattr(logging, str_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % str_level)
    logging.basicConfig(level=numeric_level)
    logger = logging.getLogger(__name__)
    logger.info("Logging level is set to %s" % str_level.upper())

    app = FastAPI()

    return app, container


def start() -> None:
    """Start application"""
    logger = logging.getLogger(__name__)
    logger.info(f"MetaSaaS")
    app, container = init()
    setup_live_container(container)
    setup(app, container)
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )


if __name__ == "__main__":
    start()