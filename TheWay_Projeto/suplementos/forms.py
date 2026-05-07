from django import forms
from .models import ConsultaSuplemento

class SuplementoForm(forms.ModelForm):
    class Meta:
        model = ConsultaSuplemento
        fields = ['nome', 'peso', 'altura']