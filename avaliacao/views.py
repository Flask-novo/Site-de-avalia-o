# avaliacao/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail # Função nativa do Django para e-mails
from django.conf import settings
from .forms import AvaliacaoForm

def formulario_avaliacao(request):
    # Se o usuário clicou no botão de enviar (método POST)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        
        # Verifica se preencheu tudo certinho
        if form.is_valid():
            # 1. Salva no banco de dados
            nova_resposta = form.save() 
            
            # 2. Monta o texto do e-mail
            assunto = f"Nova Avaliação de {nova_resposta.nome}"
            mensagem = f"""
            Você recebeu uma nova resposta no projeto!
            
            Dados do Usuário:
            Nome: {nova_resposta.nome}
            Telefone: {nova_resposta.telefone}
            
            Respostas:
            1. Clareza YEMA: {nova_resposta.q1_clareza}
            3. Duração da atividade: {nova_resposta.q3_tempo}
            4. Linguagem: {nova_resposta.q4_linguagem}
            5. Aprendizado sobre ISTs: {nova_resposta.q5_ists}
            6. Sugestão: {nova_resposta.q6_sugestao_opcao}
            Detalhe da sugestão: {nova_resposta.q6_sugestao_texto}
            """
            
            # 3. Envia o e-mail
            send_mail(
                subject=assunto,
                message=mensagem,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['seu_email_que_vai_receber@gmail.com'], # Coloque seu e-mail aqui
                fail_silently=False,
            )
            
            # 4. Redireciona para uma tela de "Obrigado!"
            return redirect('sucesso') 
            
    # Se ele só está abrindo a página pela primeira vez (método GET)
    else:
        form = AvaliacaoForm()
        
    return render(request, 'avaliacao/formulario.html', {'form': form})

# View simples para a página de sucesso
def pagina_sucesso(request):
    return render(request, 'avaliacao/sucesso.html')
