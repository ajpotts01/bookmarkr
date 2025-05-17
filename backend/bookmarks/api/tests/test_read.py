# Third-party imports
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

# Project imports
from bookmarks.models import Bookmark


@pytest.mark.django_db
def test_bookmarks_are_listed() -> None:
    url: str = reverse("bookmarks-list")
    google: Bookmark = Bookmark.objects.create(
        title="Google", url="https://www.google.com"
    )
    bing: Bookmark = Bookmark.objects.create(
        title="Bing", url="https://www.bing.com"
    )
    yahoo: Bookmark = Bookmark.objects.create(
        title="Yahoo!", url="https://www.yahoo.com"
    )

    client: APIClient = APIClient()
    response: Response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3
    assert response.data[0]["title"] == google.title
    assert response.data[1]["title"] == bing.title
    assert response.data[2]["title"] == yahoo.title
    assert response.data[0]["url"] == google.url
    assert response.data[1]["url"] == bing.url
    assert response.data[2]["url"] == yahoo.url


@pytest.mark.django_db
def test_bookmark_is_retrievable_by_id() -> None:
    bookmark: Bookmark = Bookmark.objects.create(
        title="Google", url="https://www.google.com"
    )
    url: str = reverse("bookmarks-detail", args=[bookmark.id])

    client: APIClient = APIClient()
    response: Response = client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == bookmark.title
    assert response.data["url"] == bookmark.url
