from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Anuncio, ImagemAnuncio

class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Nome')
    last_name = forms.CharField(max_length=30, required=True, label='Sobrenome')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']