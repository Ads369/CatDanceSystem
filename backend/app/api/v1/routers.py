from fastapi import APIRouter

from app.api.v1.endpoints import dancer

api_router = APIRouter()
api_router.include_router(dancer.router, prefix="/users", tags=["users"])
