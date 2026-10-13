# avaliacao/forms.py
from django import forms
from .models import RespostaAvaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = RespostaAvaliacao
        fields = '__all__'
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'}),
            'q1_clareza': forms.RadioSelect(),
            'q3_tempo': forms.RadioSelect(),
            'q4_linguagem': forms.RadioSelect(),
            'q5_ists': forms.RadioSelect(),
            'q6_sugestao_opcao': forms.RadioSelect(),
            'q6_sugestao_texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Se tiver alguma sugestão, escreva aqui...'}),
        }

    # Esta função roda sempre que o formulário é criado
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Lista com o nome dos campos que têm as bolinhas de marcar
        campos_radio = ['q1_clareza', 'q3_tempo', 'q4_linguagem', 'q5_ists', 'q6_sugestao_opcao']
        
        for campo in campos_radio:
            opcoes_atuais = self.fields[campo].choices
            # Se a primeira opção for vazia, nós a excluímos da lista (pegamos do item 1 em diante)
            if opcoes_atuais and opcoes_atuais[0][0] in ('', None):
                self.fields[campo].choices = opcoes_atuais[1:]