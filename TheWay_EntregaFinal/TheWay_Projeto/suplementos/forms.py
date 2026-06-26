from django import forms
from .models import ConsultaSuplemento

class SuplementoForm(forms.ModelForm):
    class Meta:
        model = ConsultaSuplemento
        fields = ['nome', 'peso', 'altura']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo', 'minlength': '3'}),
            'peso': forms.NumberInput(attrs={'placeholder': 'Ex: 75.5', 'min': '20', 'max': '300', 'step': '0.1'}),
            'altura': forms.NumberInput(attrs={'placeholder': 'Ex: 1.75', 'min': '1.0', 'max': '2.5', 'step': '0.01'}),
        }
        labels = {
            'nome': 'Nome',
            'peso': 'Peso (kg)',
            'altura': 'Altura (m)',
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if len(nome) < 3:
            raise forms.ValidationError("Nome deve ter pelo menos 3 caracteres.")
        return nome

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso is None or peso < 20 or peso > 300:
            raise forms.ValidationError("Peso deve estar entre 20 kg e 300 kg.")
        return peso

    def clean_altura(self):
        altura = self.cleaned_data.get('altura')
        if altura is None or altura < 1.0 or altura > 2.5:
            raise forms.ValidationError("Altura deve estar entre 1,00 m e 2,50 m.")
        return altura
