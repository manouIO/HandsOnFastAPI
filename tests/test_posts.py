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
    #assert post_list[0].Post.owner.id == test_posts[0].owner_id
    #assert post_list[0].Post.title == test_posts[0].title

def test_unauthorized_user_get_all_posts(client: TestClient,test_posts: Any):
    response = client.get("/sqlalchemy/posts")
    assert response.status_code == 401

def test_unauthorized_user_get_post_by_id(client: TestClient,test_posts: Any):
    response = client.get(f"/sqlalchemy/posts/{test_posts[0].id}")
    assert response.status_code == 401

def test_get_post_by_id_not_exist(authorized_client: TestClient,test_posts: Any):
    response = authorized_client.get(f"/sqlalchemy/posts/9999")
    assert response.status_code == 404

def test_get_post_by_id(authorized_client: TestClient,test_posts: Any):
    response = authorized_client.get(f"/sqlalchemy/posts/{test_posts[0].id}")
    def validate(post):
        return schemas.PostOut(**post)
    post_out = validate(response.json())
    assert response.status_code == 200
    assert post_out.Post.id == test_posts[0].id
    assert post_out.Post.title == test_posts[0].title


@pytest.mark.parametrize("title, content, published", [
    ("New Post", "Content of the new post", True),
    ("Another Post", "Content of another post", False),
    ("Third Post", "Content of the third post", True)
])
def test_create_post(authorized_client: TestClient,test_user, title, content, published):
    response = authorized_client.post("/sqlalchemy/posts", json={"title": title, "content": content, "published": published})
    post_out = schemas.Post(**response.json())
    assert response.status_code == 201
    assert post_out.title == title
    assert post_out.content == content
    assert post_out.published == published
    assert post_out.owner.id == test_user['id']


def test_create_post_default_published(authorized_client: TestClient,test_user):
    response = authorized_client.post("/sqlalchemy/posts", json={"title": "Default Published Post", "content": "Content of the default published post"})
    post_out = schemas.Post(**response.json())
    assert response.status_code == 201
    assert post_out.title == "Default Published Post"
    assert post_out.content == "Content of the default published post"
    assert post_out.published == True
    assert post_out.owner.id == test_user['id']

def unauthorized_user_create_post(client: TestClient,test_user):
    response = client.post("/sqlalchemy/posts", json={"title": "Unauthorized Post", "content": "Content of the unauthorized post"})
    assert response.status_code == 401

def test_unhauthorized_user_delete_post(client: TestClient,test_posts: Any):
    response = client.delete(f"/sqlalchemy/posts/{test_posts[0].id}")
    assert response.status_code == 401

def test_delete_post_not_exist(authorized_client: TestClient,test_posts: Any):
    response = authorized_client.delete(f"/sqlalchemy/posts/9999")
    assert response.status_code == 404

def test_delete_post_success(authorized_client: TestClient,test_posts: Any):
    # 1. Store the ID in a plain integer variable first
    post_id=test_posts[0].id

    #2. perform the deletion
    response = authorized_client.delete(f"/sqlalchemy/posts/{test_posts[0].id}")
    assert response.status_code == 204
    #3. verify that the post has been deleted using the stored ID
    get_response = authorized_client.get(f"/sqlalchemy/posts/{post_id}")
    assert get_response.status_code == 404

def test_delete_others_post(authorized_client_2: TestClient,test_posts: Any):
    # authorized_client_2 belongs to test_user_2 (user2@gmail.com)
    # test_posts[0] was created by test_user (maryse@gmail.com)

    response = authorized_client_2.delete(f"/sqlalchemy/posts/{test_posts[0].id}")

    # This should return a 403 Forbidden, not a 401 or a 204
    assert response.status_code == 403


    #Now let's do the test update post

def test_update_post(authorized_client: TestClient,test_posts: Any):
    post_id = test_posts[0].id
    data={"title": "Updated Title", 
          "content": "Updated Content", 
          "published": True}
    response = authorized_client.put(f"/sqlalchemy/posts/{post_id}", json=data)
    assert response.status_code == 200
    updated_post = schemas.Post(**response.json())
    assert updated_post.title == "Updated Title"
    assert updated_post.content == "Updated Content"
    assert updated_post.published == True

def test_update_post_not_exist(authorized_client: TestClient,test_posts: Any):
    data={"title": "Updated Title", 
          "content": "Updated Content", 
          "published": True}
    response = authorized_client.put(f"/sqlalchemy/posts/9999", json=data) 
    assert response.status_code == 404

def test_update_others_post(authorized_client_2: TestClient,test_posts: Any):
# authorized_client_2 belongs to test_user_2 
# test_posts[0] was created by test_user 
    post_id = test_posts[0].id 
    data={"title": "Updated Title", "content": "Updated Content", "published": True} 
    response = authorized_client_2.put(f"/sqlalchemy/posts/{post_id}", json=data) 
    assert response.status_code == 403

def test_unauthorized_user_update_post(client: TestClient,test_posts: Any):
    post_id = test_posts[0].id
    data={"title": "Updated Title", "content": "Updated Content", "published": True}
    response = client.put(f"/sqlalchemy/posts/{post_id}", json=data)
    assert response.status_code == 401