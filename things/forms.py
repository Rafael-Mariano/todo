from django.forms import ModelForm
from django import forms
from .models import Things

class ThingForm(forms.ModelForm):
    class Meta:
        model = Things
        fields = [
            "title",
            "description",
            "data"
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'})
        }
        # adicione o formato de data ao modelo
        localized_fields = ('data',)