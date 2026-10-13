# avaliacao/models.py
from django.db import models

class RespostaAvaliacao(models.Model):
    # Campos de Identificação
    nome = models.CharField(max_length=150, verbose_name="Nome completo")

    # Opções para as perguntas
    OPCOES_Q1 = [('Excelente', 'Excelente'), ('Boa', 'Boa'), ('Regular', 'Regular'), ('Ruim', 'Ruim')]
    OPCOES_Q3 = [('Muito adequado', 'Muito adequado'), ('Adequado', 'Adequado'), ('Curto', 'Curto'), ('Longo', 'Longo')]
    OPCOES_Q4 = [('Sim, foi muito fácil', 'Sim, foi muito fácil'), ('Sim, foi razoável', 'Sim, foi razoável'), ('Não, foi difícil', 'Não, foi difícil'), ('Não tenho certeza', 'Não tenho certeza')]
    OPCOES_Q5 = [('Sim, totalmente', 'Sim, totalmente'), ('Sim, em parte', 'Sim, em parte'), ('Não', 'Não'), ('Não tenho certeza', 'Não tenho certeza')]
    OPCOES_Q6 = [('Sim', 'Sim'), ('Não', 'Não'), ('Talvez', 'Talvez')]

    # Campos do questionário
    q1_clareza = models.CharField(max_length=50, choices=OPCOES_Q1, verbose_name="1. Como você avalia a clareza da explicação sobre o que é o TEMA?")
    q3_tempo = models.CharField(max_length=50, choices=OPCOES_Q3, verbose_name="2. Como você avalia o tempo de duração da atividade?")
    q4_linguagem = models.CharField(max_length=50, choices=OPCOES_Q4, verbose_name="3. A linguagem utilizada foi de fácil compreensão?")
    q5_ists = models.CharField(max_length=50, choices=OPCOES_Q5, verbose_name="4. A atividade ajudou você a aprender algo novo sobre as ISTs?")
    q6_sugestao_opcao = models.CharField(max_length=10, choices=OPCOES_Q6, verbose_name="5. Você tem alguma sugestão para melhorar as próximas atividades?")
    q6_sugestao_texto = models.TextField(blank=True, null=True, verbose_name="Se sim, qual?")

    # Retorna o nome da pessoa no painel de administração
    def __str__(self):
        return f"Avaliação de {self.nome}"