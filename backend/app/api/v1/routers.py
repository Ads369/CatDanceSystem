from app.api.v1.endpoints import dancer
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(router=dancer.router, prefix="/users", tags=["users"])
