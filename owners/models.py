from django.db import models
import uuid
class Owner(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11 ,unique=True)
    
