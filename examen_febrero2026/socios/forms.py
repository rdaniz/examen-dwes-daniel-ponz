from django import forms
from .models import Disco

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ['titulo', 'formato', 'año', 'discografica', 'num_pistas', 'genero']
        widgets = {
            'año': forms.NumberInput(attrs={'min': 1500, 'max': 2100}),
            'num_pistas': forms.NumberInput(attrs={'min': 1})
        }