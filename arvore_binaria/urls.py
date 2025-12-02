from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gerar/', views.gerar_arvore, name='gerar_arvore'),
    path('arvore/', views.ver_arvore, name='arvore'),
    path('acao/', views.executar_acao, name='acao'),
]