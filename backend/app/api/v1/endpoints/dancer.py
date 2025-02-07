from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.schemas.dancer import DancerCreate, DancerResponse
from app.db.session import get_db
from app.services.dance_service import DancerService

router = APIRouter()


@router.post("/", response_model=DancerResponse)
async def register_dancer(dancer: DancerCreate, db: AsyncSession = Depends(get_db)):
    return await DancerService.register_dancer(db, dancer.dict())


@router.get("/{dancer_id}", response_model=DancerResponse)
async def get_dancer(dancer_id: int, db: AsyncSession = Depends(get_db)):
    return await DancerService.get_dancer_info(db, dancer_id)
