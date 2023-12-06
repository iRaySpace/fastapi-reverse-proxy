import requests
from fastapi.routing import APIRouter
from reverse_proxy.domain.dto import LoginDto
from reverse_proxy.app.config import get_config


api_router = APIRouter()


@api_router.post("/login")
def process_api(data: LoginDto):
    response = requests.post(get_config('url'), json=data.dict())
    return response.json()
