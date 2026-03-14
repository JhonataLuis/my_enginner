from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Anuncio, ImagemAnuncio
from .forms import AnuncioForm

# Create your views here.
def home(request):
    # Mostra todos os anuncios, do mais novo para o mais velho
    anuncios = Anuncio.objects.all().order_by('-data_criacao')

    return render(request, 'anuncios/home.html', {'anuncios': anuncios})
