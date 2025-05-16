# Third-party imports
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

# Project imports
from bookmarks.models import Bookmark


@pytest.mark.django_db
def test_valid_bookmark_is_created() -> None:
    url: str = reverse("bookmarks-list")

    data: dict = {
        "title": "Google",
        "url": "https://www.google.com",
    }

    client: APIClient = APIClient()
    response: Response = client.post(url, data, format="json")
    bookmark: Bookmark = Bookmark.objects.get()

    assert response.status_code == status.HTTP_201_CREATED
    assert bookmark.title == data["title"]
    assert bookmark.url == data["url"]


@pytest.mark.django_db
def test_invalid_bookmark_is_not_created_missing_url() -> None:
    url: str = reverse("bookmarks-list")

    data: dict = {
        "title": "Google is not here man",
    }

    client: APIClient = APIClient()
    response: Response = client.post(url, data, format="json")

    with pytest.raises(Bookmark.DoesNotExist):
        bookmark: Bookmark = Bookmark.objects.get()  # noqa: F841

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_invalid_bookmark_is_not_created_missing_title() -> None:
    url: str = reverse("bookmarks-list")

    data: dict = {
        "url": "https://www.google.com",
    }

    client: APIClient = APIClient()
    response: Response = client.post(url, data, format="json")

    with pytest.raises(Bookmark.DoesNotExist):
        bookmark: Bookmark = Bookmark.objects.get()  # noqa: F841

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_invalid_bookmark_is_not_created_invalid_fields() -> None:
    url: str = reverse("bookmarks-list")

    data: dict = {
        "bleep": "bloop",
        "foo": "bar",
    }

    client: APIClient = APIClient()
    response: Response = client.post(url, data, format="json")

    with pytest.raises(Bookmark.DoesNotExist):
        bookmark: Bookmark = Bookmark.objects.get()  # noqa: F841

    assert response.status_code == status.HTTP_400_BAD_REQUEST
