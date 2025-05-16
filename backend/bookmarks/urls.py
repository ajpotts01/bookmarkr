# Third-party imports
from django.urls import path

# Project imports
from bookmarks.api.views import BookmarkDetail, BookmarkList

urlpatterns = [
    path(
        "api/bookmarks/",
        BookmarkList.as_view(),
        name="bookmarks-list",
    ),
    path(
        "api/bookmarks/<uuid:pk>/",
        BookmarkDetail.as_view(),
        name="bookmarks-detail",
    ),
]
