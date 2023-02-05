import pytest
from tests.factories import PostFactory


@pytest.mark.django_db
def test_post_create(client):

    post = PostFactory()

    response = client.post("/api/post/", post.__dict__)

    assert response.status_code == 201
    assert response.data["name"] == post.name
    assert response.data["text"] == post.text
    assert response.data["view_count"] == post.view_count
