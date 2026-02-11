from typing import Any
from fastapi.testclient import TestClient
from app import schemas
import pytest
from jose import jwt
from app.config import settings



def test_get_all_posts(authorized_client: TestClient,test_posts: Any):
    response = authorized_client.get("/sqlalchemy/posts")
    #print(response.json())
    def validate(post):
        return schemas.PostOut(**post)
    post_list = list(map(validate, response.json()))
    assert isinstance(post_list, list)
    assert len(post_list) == len(test_posts)
    assert response.status_code == 200
    assert post_list[0].Post.owner.id == test_posts[0].owner_id
    #assert post_list[0].Post.title == test_posts[0].title

def test_unauthorized_user_get_all_posts(client: TestClient,test_posts: Any):
    response = client.get("/sqlalchemy/posts")
    assert response.status_code == 401