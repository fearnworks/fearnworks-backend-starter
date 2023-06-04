import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.auth import create_access_token
from app.db.session import SessionLocal
from app import crud

client = TestClient(app)


def test_get_current_user():
    # Create a user to test with
    # Create a UserCreate object with the required fields
    user_create = UserCreate(
        email="test@example.com",
        password="password",
        first_name="Test",
        surname="User",
        is_superuser=False,
    )
    session = SessionLocal()
    # Call the create function with the UserCreate object
    user = crud.user.create(db=session, obj_in=user_create)
    # Generate a JWT token for the user
    access_token = create_access_token(data={"sub": user.email})
    print(access_token)
    # Make a request to the API with the token
    response = client.get("/users/me", headers={"Authorization": f"Bearer {access_token}"})

    # Check that the response is successful and contains the correct user data
    assert response.status_code == 200
    assert response.json()["email"] == user.email
    assert response.json()["full_name"] == user.full_name
    assert response.json()["is_active"] == user.is_active
    assert response.json()["is_superuser"] == user.is_superuser