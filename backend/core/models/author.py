import uuid
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from simple_history.models import HistoricalRecords


class Author(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="author_profiles/", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        related_name="authors_created",
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        related_name="authors_updated",
        null=True,
        blank=True,
    )

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def name(self):
        return f"{self.first_name} {self.last_name}"

    name.short_description = "Author Name"
