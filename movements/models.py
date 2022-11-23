from django.db import models
from django.utils import timezone

import uuid

class Movement(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    document = models.FileField()
    registered_at = models.DateTimeField(default=timezone.now)

    