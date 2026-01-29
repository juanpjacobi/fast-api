from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
import pytest
from ..models import Todos, Users
from ..routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args = {"check_same_thread": False},
    poolclass = StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {"username": "test", "id": 1, "user_role": "admin"}        

client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(title="Test Todo", description="Test Description", priority=1, complete=False, owner_id=1)
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM todos;"))
        conn.commit()

@pytest.fixture
def test_user():
    user = Users(
        username="test",
        first_name="test",   
        last_name="test",
        email="test",
        role="admin",
        phone_number="test",     
        hashed_password=bcrypt_context.hash("test"))
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM users;"))
        conn.commit()