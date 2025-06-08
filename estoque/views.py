# estoque/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Produto, Movimento
from .forms import ProdutoForm, MovimentoForm
from datetime import date
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.conf import settings

# View para a página inicial, que lista os produtos
def lista_produtos(request):
    """
    Busca todos os produtos no banco de dados e os exibe em uma página.
    """
    # Busca todos os objetos do modelo Produto no banco de dados
    produtos = Produto.objects.all()
    
    # Cria um "contexto" que é um dicionário para enviar os dados para o template
    contexto = {
        'produtos': produtos
    }
    
    # Renderiza o template 'lista_produtos.html', passando o contexto com os produtos
    return render(request, 'estoque/lista_produtos.html', contexto)

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            # Usamos commit=False para pegar o objeto antes de salvar definitivamente
            produto = form.save(commit=False)
            
            # Salvamos o produto primeiro para que ele tenha um ID
            produto.save() 
            
            # ----- LÓGICA ADICIONADA -----
            # Se uma quantidade inicial foi informada, cria um movimento de entrada
            if produto.quantidade > 0:
                Movimento.objects.create(
                    produto=produto,
                    tipo='E',
                    quantidade=produto.quantidade,
                    data_hora=date.today() # <-- AQUI ESTÁ A CORREÇÃO
                )
            # --------------------------------

            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    
    contexto = {'form': form}
    return render(request, 'estoque/adicionar_produto.html', contexto)


def registrar_movimento(request, produto_id):
    """
    Registra um movimento (entrada ou saída) para um produto específico.
    """
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        form = MovimentoForm(request.POST)
        if form.is_valid():
            movimento = form.save(commit=False)
            movimento.produto = produto

            # Lógica para atualizar o estoque
            if movimento.tipo == 'E': # Entrada
                produto.quantidade += movimento.quantidade
            elif movimento.tipo == 'S': # Saída
                # Verifica se há estoque suficiente
                if produto.quantidade >= movimento.quantidade:
                    produto.quantidade -= movimento.quantidade
                else:
                    contexto_erro = {
                        'form': form,
                        'produto': produto,
                        'erro': 'Estoque insuficiente para realizar a saída.'
                    }
                    return render(request, 'estoque/registrar_movimento.html', contexto_erro)
            
            # Atualiza a data da última movimentação do produto
            produto.data_ultima_movimentacao = movimento.data_hora
            
            # Salva as alterações
            produto.save()
            movimento.save()
            
            return redirect('lista_produtos')
    else:
        form = MovimentoForm()

    contexto = {
        'form': form,
        'produto': produto
    }
    return render(request, 'estoque/registrar_movimento.html', contexto)

def relatorio_historico(request):
    """
    Exibe o histórico de todos os movimentos de entrada e saída.
    """
    # Busca todos os movimentos, ordenados pela data mais recente (-data_hora)
    # O .select_related('produto') otimiza a busca, evitando múltiplas consultas ao banco de dados
    movimentos = Movimento.objects.all().select_related('produto').order_by('-data_hora')
    
    contexto = {
        'movimentos': movimentos
    }
    
    return render(request, 'estoque/relatorio_historico.html', contexto)

def relatorio_estoque(request):
    """
    Exibe a lista de todos os produtos para fins de balanço de estoque.
    """
    produtos = Produto.objects.order_by('nome')
    contexto = {
        'produtos': produtos,
        'now': timezone.now()
    }
    return render(request, 'estoque/relatorio_estoque.html', contexto)

def gerar_pdf_balanco(request):
    """
    Gera um relatório em PDF com a lista de produtos para balanço.
    """
    produtos = Produto.objects.order_by('nome')

# --- LÓGICA PARA ACHAR A LOGO ---
    # Este é o caminho para a sua pasta 'static' que definimos no settings.py
    static_dir = settings.STATICFILES_DIRS[0]
    # Este é o caminho completo para a imagem da logo
    logo_path = os.path.join(static_dir, 'img/logo.png')
    # --------------------------------

    contexto = {
        'produtos': produtos,
        'now': timezone.now(),
        'logo_path': logo_path  # Passamos o caminho da logo para o template
    }
    
    # Pega o template que criamos
    template_path = 'estoque/relatorio_pdf.html'
    template = get_template(template_path)
    
    # Renderiza o HTML com o contexto
    html = template.render(contexto)

    # Cria o PDF
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        # Se não houver erro, retorna o PDF como um anexo para download
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="balanco_estoque.pdf"'
        return response
        
    return HttpResponse("Erro ao gerar PDF", status=400)

    # estoque/views.py
def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    
    contexto = {'produto': produto}
    return render(request, 'estoque/excluir_produto_confirm.html', contexto)