import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse("home")
    response = client.get(reverse(url))
    assert response.status_code == 200
    assert response.content == b"Hello, world. You're at the blog index."
    
    # assert len(response.context["object_list"]) == 10
    # assert "post_list.html" in [t.name for t in response.templates]