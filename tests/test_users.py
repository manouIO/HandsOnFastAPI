from typing import Any
from fastapi.testclient import TestClient
from app import schemas
import pytest
from jose import jwt
from app.config import settings

# def test_root(client):
#     response = client.get("/")
#     print(response.json().get("message"))
#     assert response.status_code == 200
#     assert response.json() == {"message":"Now it is time to deploy!"}



def test_create_user(client: TestClient):
    response = client.post("/sqlalchemy/users", json={"email": "manou2@gmail.com", "password": "password1232"})
    print(response.json())
    new_user = schemas.UserOut(**response.json())
    assert response.status_code == 201
    assert new_user.email== "manou2@gmail.com"

def test_login_user(client: TestClient,test_user: dict[str, Any]):
    response = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_response = schemas.Token(**response.json())
    payload = jwt.decode(login_response.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_response.token_type == "bearer"
    assert response.status_code == 200
   
@pytest.mark.parametrize("email, password, status_code", [
      ('wrongemail@gmail.com', 'password123', 403),  # Incorrect email
        ("maryse@gmail.com", "wrongpassword", 403),  # Incorrect password
        ("maryse@gmail.com","password123", 200),  # Correct credentials] 
        (None, "password123", 422),  # Missing email
        ("maryse@gmail.com", None, 422)  # Missing password
    ])
def test_incorrect_login(client, test_user,email,password, status_code):
    response = client.post("/login", data={"username": email, "password": password})
    assert response.status_code == status_code 
    #assert response.json().get('detail') == "Invalid Credentials"