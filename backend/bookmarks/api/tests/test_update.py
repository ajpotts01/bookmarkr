# Third-party imports
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

# Project imports
from bookmarks.models import Bookmark


@pytest.mark.django_db
def test_bookmark_can_have_title_changed() -> None:
    bookmark: Bookmark = Bookmark.objects.create(
        title="Google", url="https://www.google.com"
    )

    url: str = reverse("bookmarks-detail", args=[bookmark.id])

    data: dict = {
        "title": "Something other than Google",
    }

    client: APIClient = APIClient()
    response: Response = client.patch(url, data=data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == data["title"]


@pytest.mark.django_db
def test_bookmark_can_have_url_changed() -> None:
    bookmark: Bookmark = Bookmark.objects.create(
        title="Google", url="https://www.bing.com"
    )

    url: str = reverse("bookmarks-detail", args=[bookmark.id])

    data: dict = {
        "url": "https://www.google.com",
    }

    client: APIClient = APIClient()
    response: Response = client.patch(url, data=data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["url"] == data["url"]


@pytest.mark.django_db
def test_bookmark_can_have_full_update() -> None:
    bookmark: Bookmark = Bookmark.objects.create(
        title="Google", url="https://www.google.com"
    )

    url: str = reverse("bookmarks-detail", args=[bookmark.id])

    data: dict = {
        "title": "Bing",
        "url": "https://www.bing.com",
    }

    client: APIClient = APIClient()
    response: Response = client.put(url, data=data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == data["title"]
    assert response.data["url"] == data["url"]


@pytest.mark.django_db
def test_bookmark_can_reject_full_update_data_missing() -> None:
    bookmark: Bookmark = Bookmark.objects.create(
        title="Google", url="https://www.google.com"
    )

    url: str = reverse("bookmarks-detail", args=[bookmark.id])

    data: dict = {
        "url": "https://www.bing.com",
    }

    client: APIClient = APIClient()
    response: Response = client.put(url, data=data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
