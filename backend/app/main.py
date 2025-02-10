# backend/app/main.py
from app.api.v1.routers import api_router
from app.core.config import settings
from fastapi import FastAPI

from .api.dancers import router as dancers_router

app = FastAPI()
# app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)


# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()


# app.include_router(dancers_router, prefix="/api")
app.include_router(api_router, prefix="/api")
