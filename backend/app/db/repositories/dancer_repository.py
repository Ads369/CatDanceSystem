from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.models import Dancer


class DancerRepository:
    @staticmethod
    async def get_dancer(db: AsyncSession, dancer_id: int):
        result = await db.execute(select(Dancer).filter(Dancer.id == dancer_id))
        return result.scalars().first()

    @staticmethod
    async def create_dancer(db: AsyncSession, dancer_data: dict):
        dancer = Dancer(**dancer_data)
        db.add(dancer)
        await db.commit()
        await db.refresh(dancer)
        return dancer
