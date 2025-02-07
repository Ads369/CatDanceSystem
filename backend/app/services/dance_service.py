from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.dancer_repository import DancerRepository


class DancerService:
    @staticmethod
    async def register_dancer(db: AsyncSession, dancer_data: dict):
        return await DancerRepository.create_dancer(db, dancer_data)

    @staticmethod
    async def get_dancer_info(db: AsyncSession, dancer_id: int):
        return await DancerRepository.get_dancer(db, dancer_id)
