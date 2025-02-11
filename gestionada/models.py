from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Subdelegacion(models.Model):
    name = models.CharField(max_length=200, blank=False)
    date = models.DateField(auto_now_add=True)

class DaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subdelegacion = models.ForeignKey(Subdelegacion, on_delete=models.SET_NULL, null=True)
    notificacion = models.IntegerField(default=0)
