import yaml
from fastapi import FastAPI
from reverse_proxy.app.router import api_router
from reverse_proxy.app.config import init_config


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=api_router)
    init_config()
    return app
