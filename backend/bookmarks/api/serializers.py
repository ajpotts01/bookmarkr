# Third-party imports
from rest_framework import serializers

# Project imports
from bookmarks.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model: type = Bookmark
        fields: list[str] = ["id", "title", "url", "created_at", "updated_at"]
        read_only_fields: tuple[str] = ("id", "created_at", "updated_at")
