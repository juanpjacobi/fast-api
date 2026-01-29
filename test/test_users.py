from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == test_user.username
    assert response.json()['first_name'] == test_user.first_name
    assert response.json()['last_name'] == test_user.last_name
    assert response.json()['email'] == test_user.email
    assert response.json()['role'] == test_user.role
    assert response.json()['phone_number'] == test_user.phone_number


def test_changepassword_success(test_user):
    response = client.put("/users/change_password", json={"password": "test", "new_password": "test123"})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_changepassword_fail(test_user):
    response = client.put("/users/change_password", json={"password": "test123", "new_password": "test123"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Verification Failed'}

def test_change_phonenumber_success(test_user):
    response = client.put("/users/phone_number", json={"phone_number": "test123"})
    assert response.status_code == status.HTTP_204_NO_CONTENT
