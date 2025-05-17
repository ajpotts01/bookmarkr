# Third-party imports
from django.db.models.query import QuerySet
from rest_framework import generics

from bookmarks.api.serializers import BookmarkSerializer
from bookmarks.models import Bookmark

# from rest_framework.response import Response
# from rest_framework.views import APIView


class BookmarkList(generics.ListCreateAPIView):
    queryset: QuerySet = Bookmark.objects.all()
    serializer_class: type = BookmarkSerializer


class BookmarkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset: QuerySet = Bookmark.objects.all()
    serializer_class: type = BookmarkSerializer
