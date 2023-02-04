import pytest
from datetime import date

from blog.models import Post


@pytest.mark.django_db
def test_post_detail(client):
    post = Post.objects.create(
        name="Test_name",
        text="test_text",
    )

    expected_response = {
        "id": post.pk,
        "name": "Test_name",
        "text": "test_text",
        "comments": [],
        "created_at": date.today().strftime("%Y-%m-%d"),
        "view_count": 1,
    }

    response = client.get(f"/post/{post.pk}/")

    assert response.status_code == 200
    assert response.data == expected_response
