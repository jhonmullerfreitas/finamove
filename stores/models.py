from django.db import models
import uuid

class Store(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        "owners.Owner",
        on_delete=models.CASCADE,
        related_name="stores"
    )
    balance = models.FloatField(null=True, blank=True, default=0)
    