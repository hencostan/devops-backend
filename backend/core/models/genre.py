import uuid
from django.db import models
from simple_history.models import HistoricalRecords
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE


class Genre(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def slugify(self):
        return self.name.replace(" ", "-").lower()
