import factory
import pytest

from tests.factories import PostFactory, CommentFactory
from blog.serializers import PostListSerializer


@pytest.mark.django_db
def test_list_view(client):
    posts = PostFactory.create_batch(5)
    CommentFactory.create_batch(10, post=factory.Iterator(posts))

    response = client.get("/api/post/")

    assert response.status_code == 200
    assert response.data == PostListSerializer(posts, many=True).data
