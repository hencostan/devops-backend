from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from safedelete.models import SOFT_DELETE_CASCADE
from simple_history.models import HistoricalRecords


class User(AbstractUser):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    history = HistoricalRecords(excluded_fields=["last_login", "is_active"])

    def __str__(self):
        return self.username
