from django.db import models

class Owner(models.Model):

    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11 ,unique=True)
    
