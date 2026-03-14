from django import forms
from .models import Anuncio, ImagemAnuncio

class AnuncioForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = [
            'titulo', 'descricao', 'preco', 'tipo_imovel',
            'endereco', 'cidade', 'quartos', 'banheiros', 'area_total'
        ]

        widgets = {
            
        }    