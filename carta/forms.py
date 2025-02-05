from django import forms
from .models import carta

class CartaForm(forms.ModelForm):
    class Meta:
        model = carta
        fields = ["asunto", "texto"]
