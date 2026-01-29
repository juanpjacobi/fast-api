from .utils import *
from ..routers.auth import get_db, authenticate_user, create_access_token, SECRET_KEY, ALGORITHM, get_current_user
from datetime import timedelta
from jose import jwt
from fastapi import status, HTTPException


app.dependency_overrides[get_db] = override_get_db


def test_authenticate_user(test_user):
    db = TestingSessionLocal()
    authenticated_user = authenticate_user(test_user.username, "test", db)
    assert authenticated_user is not None
    assert authenticated_user.username == test_user.username

    non_existing_user = authenticate_user("non_existing_user", "test", db)
    assert non_existing_user is False

    wrong_password_user = authenticate_user(test_user.username, "wrong_password", db)
    assert wrong_password_user is False

def test_create_access_token(test_user):
    token = create_access_token(test_user.username, test_user.id, test_user.role, timedelta(minutes=20))
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_signature": False})
    assert decoded_token["sub"] == test_user.username
    assert decoded_token["id"] == test_user.id
    assert decoded_token["role"] == test_user.role

def test_get_current_user_valid_token():
    encode = {"sub": "test", "id": 1, "role": "admin"}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    response = get_current_user(token)
    assert response["username"] == "test"
    assert response["id"] == 1
    assert response["user_role"] == "admin"

def test_get_current_user_missing_payload():
    encode = {"role": "user"}  # Missing 'sub' and 'id'
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token)
    assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
 
