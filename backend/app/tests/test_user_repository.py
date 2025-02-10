import pytest
from app.db.models.user import User
from app.db.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate

@pytest.fixture
def user_repository(db):
    return UserRepository(db)

def test_create_user(user_repository):
    user_data = UserCreate(name="Test User", description="Test Description")
    user = user_repository.create_user(user_data)
    assert user.id is not None
    assert user.name == "Test User"
    assert user.description == "Test Description"

def test_get_user(user_repository):
    user_data = UserCreate(name="Test User", description="Test Description")
    user = user_repository.create_user(user_data)
    fetched_user = user_repository.get_user(user.id)
    assert fetched_user.id == user.id
    assert fetched_user.name == "Test User"

def test_update_user(user_repository):
    user_data = UserCreate(name="Test User", description="Test Description")
    user = user_repository.create_user(user_data)
    update_data = UserUpdate(name="Updated User")
    updated_user = user_repository.update_user(user.id, update_data)
    assert updated_user.name == "Updated User"

def test_delete_user(user_repository):
    user_data = UserCreate(name="Test User", description="Test Description")
    user = user_repository.create_user(user_data)
    deleted_user = user_repository.delete_user(user.id)
    assert deleted_user.id == user.id
    assert user_repository.get_user(user.id) is None
