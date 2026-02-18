from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }

    def save(self, commit=True):
        # Guardar el autor
        autor = super().save(commit=False)
       
    
        if commit:
            autor.save()
        return autor