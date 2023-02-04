import pytest
from datetime import date


@pytest.mark.django_db
def test_post_create(client):

	expected_response = {
	    "id": 2,
	    "name": "Test_name",
	    "text": "test_text",
	    "comments": [],
	    "created_at": date.today().strftime("%Y-%m-%d"),
	    "view_count": 0
	}

	response = client.post("/post/", data={
		"name": "Test_name",
		"text": "test_text"})

	assert response.status_code == 201
	assert response.data == expected_response
