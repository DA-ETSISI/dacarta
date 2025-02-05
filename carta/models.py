from django.db import models

# Create your models here.
class carta(models.Model):
    asunto = models.CharField(max_length=100)
    texto = models.TextField(max_length=5000)