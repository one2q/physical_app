import pytest

from tests.factories import PostFactory, CommentFactory


@pytest.mark.django_db
def test_list_posts_comments_ordering(client):
    post = PostFactory()
    comment_1 = CommentFactory(post=post)
    comment_2 = CommentFactory(post=post)

    response = client.get("/post/")
    response_data = response.json()

    assert response_data[0]["comments"]["pk"] == comment_2.pk
