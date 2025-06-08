# estoque/forms.py

from django import forms
from .models import Produto, Movimento

class ProdutoForm(forms.ModelForm):
    """
    Formulário para criar ou editar um Produto, baseado no modelo Produto.
    """
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: detergente'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'nome': 'Nome do Produto',
            'quantidade': 'Quantidade Inicial em Estoque',
        }

class MovimentoForm(forms.ModelForm):
    """
    Formulário para criar um Movimento (entrada ou saída).
    """
    class Meta:
        model = Movimento
        # Os campos que o usuário irá preencher
        fields = ['data_hora', 'tipo', 'quantidade']

        widgets = {
            'data_hora': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade a ser movimentada'}),
        }

        labels = {
            'data_hora': 'Data do Movimento',
            'tipo': 'Tipo de Movimento',
            'quantidade': 'Quantidade',
        }