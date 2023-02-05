import pytest

from tests.factories import PostFactory


@pytest.mark.django_db
def test_post_detail(client):
    post = PostFactory()

    response = client.get(f"/api/post/{post.pk}/")

    assert response.status_code == 200
    assert response.data["name"] == post.name
    assert response.data["text"] == post.text
    assert response.data["view_count"] == post.view_count + 1
