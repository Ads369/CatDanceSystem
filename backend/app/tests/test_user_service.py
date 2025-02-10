from unittest.mock import Mock

import pytest
from app.schemas.user import UserCreate, UserUpdate
from app.services.user_service import UserService


@pytest.fixture
def mock_user_repository(mocker):
    return mocker.Mock()


@pytest.fixture
def user_service(mock_user_repository):
    return UserService(mock_user_repository)


def test_create_user(user_service, mock_user_repository):
    user_data = UserCreate(name="Test User", description="Test Description")
    mock_user_repository.create_user.return_value = user_data
    result = user_service.create_user(user_data)
    assert result == user_data
    mock_user_repository.create_user.assert_called_once_with(user_data)


def test_get_user(user_service, mock_user_repository):
    mock_user_repository.get_user.return_value = {"id": 1, "name": "Test User"}
    result = user_service.get_user(1)
    assert result == {"id": 1, "name": "Test User"}
    mock_user_repository.get_user.assert_called_once_with(1)
