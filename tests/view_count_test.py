import pytest

from tests.factories import PostFactory


@pytest.mark.django_db
def test_view_count_post(client):
	"""
		This test shows that view_count work only on detail post view
	"""

	post = PostFactory()

	response = client.get(f"/api/post/{post.pk}/")
	assert response.status_code == 200
	assert response.data["view_count"] == post.view_count + 1

	response = client.get(f"/api/post/")
	assert response.data[0]["view_count"] == post.view_count + 1

	response = client.get(f"/api/post/{post.pk}/")
	assert response.data["view_count"] == post.view_count + 2
