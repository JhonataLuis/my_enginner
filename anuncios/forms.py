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
            'descricao': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
        }    