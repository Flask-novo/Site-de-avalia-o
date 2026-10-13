# avaliacao/forms.py
from django import forms
from .models import RespostaAvaliacao

# Aqui criamos um formulário baseado no nosso Modelo de Banco de Dados
class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = RespostaAvaliacao
        fields = '__all__' # Pega todos os campos que criamos no models.py