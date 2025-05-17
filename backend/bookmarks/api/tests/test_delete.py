# Third-party imports
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

# Project imports
from bookmarks.models import Bookmark


@pytest.mark.django_db
def test_can_delete_bookmark() -> None:
    bookmark: Bookmark = Bookmark.objects.create(
        title="Google", url="https://www.google.com"
    )

    url: str = reverse("bookmarks-detail", args=[bookmark.id])

    client: APIClient = APIClient()
    response: Response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert len(Bookmark.objects.all()) == 0
