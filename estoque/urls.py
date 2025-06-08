# estoque/urls.py

from django.urls import path
from . import views # Importa as views do nosso app

urlpatterns = [
    # A URL raiz ('') do nosso app vai chamar a view 'lista_produtos'
    path('', views.lista_produtos, name='lista_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produto/<int:produto_id>/movimento/', views.registrar_movimento, name='registrar_movimento'),
    path('relatorio/balanco/', views.relatorio_estoque, name='relatorio_estoque'),
    path('relatorio/historico/', views.relatorio_historico, name='relatorio_historico'),
    path('relatorio/balanco/pdf/', views.gerar_pdf_balanco, name='gerar_pdf_balanco'),
    path('produto/<int:produto_id>/excluir/', views.excluir_produto, name='excluir_produto'),
]