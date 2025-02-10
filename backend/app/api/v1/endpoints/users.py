from app.db.repositories.user_repository import UserRepository
from app.db.session import get_db
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.user_service import UserService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


def get_user_service(db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    return UserService(user_repository)


@router.post("/", response_model=User)
def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service),
):
    return service.create_user(user)


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, service: UserService = Depends(get_user_service)):
    db_user = service.get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=User)
def update_user(
    user_id: int,
    user: UserUpdate,
    service: UserService = Depends(get_user_service),
):
    return service.update_user(user_id, user)


@router.delete("/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    service.delete_user(user_id)
    return {"message": "User deleted"}
