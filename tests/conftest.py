from fastapi.testclient import TestClient
from app.main import app
from app import schemas, models
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.oauth2 import create_access_token
from app.database import get_db, Base
import pytest


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}\
:{settings.database_password}@{settings.database_hostname}\
:{settings.database_port}/{settings.database_name}_test" #use a separate database for testing


engine = create_engine(SQLALCHEMY_DATABASE_URL) #connects to the database

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #creates a session


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine) #drop the tables before the tests to ensure a clean slate
    Base.metadata.create_all(bind=engine) #create the tables before the tests
    db = TestingSessionLocal()
    try:
        yield db
    finally:       
        db.close()
    


@pytest.fixture()
def client(session):
    def override_get_db():
        yield session
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear() # Cleans up after the test is done

@pytest.fixture()
def test_user(client: TestClient):
    user_data = {"email": "maryse@gmail.com", "password": "password123"}
    response = client.post("/sqlalchemy/users", json=user_data)
    assert response.status_code == 201
    new_user = schemas.UserOut(**response.json())
    user_dict = new_user.model_dump()
    user_dict['password'] = user_data['password']
    return user_dict #return the user data as a dictionary for use in other tests

@pytest.fixture
def test_user_2(client):
    user_data = {"email": "user2@gmail.com", "password": "password1234"}
    res = client.post("/sqlalchemy/users", json=user_data)
    assert res.status_code == 201
    new_user = schemas.UserOut(**res.json())
    user_dict = new_user.model_dump()
    user_dict['password'] = user_data['password']
    return user_dict #return the user data as a dictionary for use in other tests

@pytest.fixture
def authorized_client_2(client, test_user_2):
    # This client is logged in as the second user
    token = create_access_token(data={"user_id": test_user_2['id']})
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture()
def token(test_user):
    return create_access_token({"user_id": test_user['id']})

@pytest.fixture()
def authorized_client(client: TestClient, token: str):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture()
def test_posts(test_user, test_user_2, session):
    posts_data = [
        {"title": "First Post", "content": "Content of the first post", "owner_id": test_user['id']},
        {"title": "Second Post", "content": "Content of the second post", "owner_id": test_user['id']},
        {"title": "Third Post", "content": "Content of the third post", "owner_id": test_user['id']},
        {"title": "Fourth Post", "content": "Content of the fourth post", "owner_id": test_user_2['id']},
        {"title": "Fifth Post", "content": "Content of the fifth post", "owner_id": test_user_2['id']},
        {"title": "Sixth Post", "content": "Content of the sixth post", "owner_id": test_user_2['id']}
    ]
    

    def create_post_model(post):
        return models.Post(**post)
    
    # This FORCES the map to execute for every item in posts_data
    post_models = list(map(create_post_model, posts_data)) #it is like f(x) where f=create_post_model, for x in posts_data
    session.add_all(post_models)
    session.commit()

    #instead of map, we can also use list comprehension
    # post_models = [create_post_model(post) for post in posts_data]
    # session.add_all(post_models)
    # session.commit()

    # IMPORTANT: You must return the data here!
    return session.query(models.Post).all()