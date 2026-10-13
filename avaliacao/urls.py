# avaliacao/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_avaliacao, name='formulario'),
    path('sucesso/', views.pagina_sucesso, name='sucesso'),
]