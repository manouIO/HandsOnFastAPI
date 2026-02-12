from typing import Any
from fastapi.testclient import TestClient
from app import schemas, models
import pytest
from jose import jwt
from app.config import settings

@pytest.fixture()
def test_vote(test_posts, session):
    new_vote = models.Vote(post_id=test_posts[0].id, user_id=test_posts[0].owner_id) #vote for the first post by the owner of that post
    session.add(new_vote)
    session.commit()
    return new_vote

def test_vote_on_post(authorized_client: TestClient, test_posts: Any,test_vote):
    # authorized_client belongs to test_user, so here he is the one voting
    response = authorized_client.post("/vote", json={"post_id": test_posts[3].id, "dir": 1}) #voting for his own post, should be allowed
    assert response.status_code == 201


def test_vote_on_post_twice(authorized_client: TestClient, test_posts, test_vote): 
    # Now that test_vote is a parameter, it will run the fixture 
    # and add a vote for test_posts[0] to the database.

    response = authorized_client.post("/vote", json={"post_id": test_posts[0].id, "dir": 1})
    assert response.status_code == 409

def test_remove_vote(authorized_client: TestClient, test_posts, test_vote):
    response = authorized_client.post("/vote", json={"post_id": test_posts[0].id, "dir": 0})
    assert response.status_code == 201

def test_remove_nonexistent_vote(authorized_client: TestClient, test_posts):
    response = authorized_client.post("/vote", json={"post_id": test_posts[0].id, "dir": 0})
    assert response.status_code == 404

def test_vote_on_nonexistent_post(authorized_client: TestClient):
    response = authorized_client.post("/vote", json={"post_id": 9999, "dir": 1})
    assert response.status_code == 404

def test_vote_unauthorized_user(client: TestClient, test_posts):
    response = client.post("/vote", json={"post_id": test_posts[0].id, "dir": 1})
    assert response.status_code == 401