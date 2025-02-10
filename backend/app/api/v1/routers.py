from app.api.v1.endpoints import users
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(router=users.router, prefix="/users", tags=["users"])
