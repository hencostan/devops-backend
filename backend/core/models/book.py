import uuid
from django.db import models
from simple_history.models import HistoricalRecords
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Book(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    edition = models.CharField(max_length=100, null=True, blank=True)
    cover_image = models.ImageField(upload_to="book_covers/", null=True, blank=True)
    isbn = models.CharField(
        max_length=13,
        unique=True,
        null=True,
        blank=True,
        help_text="International Standard Book Number (ISBN)",
    )
    publisher = models.CharField(max_length=255, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    authors = models.ManyToManyField(
        "core.Author",
        related_name="books",
        blank=True,
    )
    genres = models.ManyToManyField(
        "core.Genre",
        related_name="books",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        related_name="books_created",
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        related_name="books_updated",
        null=True,
        blank=True,
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def slugify(self):
        slug = self.name.replace(" ", "-").lower()
        if self.edition:
            slug += f"-{self.edition.replace(' ', '-').lower()}"
        return slug
