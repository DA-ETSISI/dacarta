from django.db import models

eriquetas = {
    "Nl" : "No leido",
    "Tra" : "Tramitado",
    "NaT" : "No tramitable",
    "DA" : "General",
    "IgS" : "Igualdad",
    "AaE" : "Estudiantes",
    "Ca" : "Calidad",
    "Com" : "Comunicacion"
}

# Create your models here.
class carta(models.Model):
    asunto = models.CharField(max_length=100)
    texto = models.TextField(max_length=5000)
    etiqueta = models.CharField(max_length=100, choices=eriquetas, default="Nl")
    fecha = models.DateField(auto_now_add=True)


