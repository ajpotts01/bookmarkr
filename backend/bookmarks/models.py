# Standard lib imports
import uuid

# Third-party imports
from django.db import models


class Bookmark(models.Model):
    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4
    )
    title: models.CharField = models.CharField(max_length=150)
    url: models.URLField = models.URLField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural: str = "bookmarks"

    def __str__(self) -> str:
        return f"{self.title} ({self.url})"
