# avaliacao/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail # Função nativa do Django para e-mails
from django.conf import settings
from .forms import AvaliacaoForm

# avaliacao/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import AvaliacaoForm

def formulario_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        
        if form.is_valid():
            nova_resposta = form.save() 
            
            assunto = f"Nova Avaliação de {nova_resposta.nome}"
            # O texto da mensagem foi atualizado, removendo a linha do telefone
            mensagem = f"""
            Você recebeu uma nova resposta no projeto!
            
            Dados do Usuário:
            Nome: {nova_resposta.nome}
            
            Respostas:
            1. Clareza YEMA: {nova_resposta.q1_clareza}
            3. Duração da atividade: {nova_resposta.q3_tempo}
            4. Linguagem: {nova_resposta.q4_linguagem}
            5. Aprendizado sobre ISTs: {nova_resposta.q5_ists}
            6. Sugestão: {nova_resposta.q6_sugestao_opcao}
            Detalhe da sugestão: {nova_resposta.q6_sugestao_texto}
            """
            
            send_mail(
                subject=assunto,
                message=mensagem,
                from_email='dharavitoria74@gmail.com', 
                recipient_list=['dharavitoria74@gmail.com'], 
                fail_silently=False,
            )
            
            return redirect('sucesso') 
            
    else:
        form = AvaliacaoForm()
        
    return render(request, 'avaliacao/formulario.html', {'form': form})

def pagina_sucesso(request):
    return render(request, 'avaliacao/sucesso.html')