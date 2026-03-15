from django import forms
from .models import Anuncio, ImagemAnuncio

class AnuncioForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = [
            'titulo', 'descricao', 'preco', 'tipo_imovel',
            'endereco', 'cidade', 'estado', 'cep', 'quartos', 
            'banheiros', 'vagas_garagem', 'area_total'
        ]

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tipo_imovel': forms.Select(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'quartos': forms.NumberInput(attrs={'class': 'form-control'}),
            'banheiros': forms.NumberInput(attrs={'class': 'form-control'}),
            'vagas_garagem': forms.NumberInput(attrs={'class': 'form-control'}),
            'area_total': forms.NumberInput(attrs={'class': 'form-control'})
        }    