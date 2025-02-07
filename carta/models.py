from django.db import models
from gestionada import models as mdls

ESTADO = (
    ("NoLeido", "No leido"),
    ("Leido", "Leido"),
    ("NoTramitable", "No tramitable"),
)

# Create your models here.
class carta(models.Model):
    asunto = models.CharField(max_length=100)
    texto = models.TextField(max_length=5000)
    subdelegacion = models.ForeignKey(mdls.Subdelegacion, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=100, choices=ESTADO, default="NoLeido")
    fecha = models.DateField(auto_now_add=True)


