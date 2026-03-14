from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Anuncio, ImagemAnuncio
from .forms import AnuncioForm

# Create your views here.
def home(request):
    # Mostra todos os anuncios, do mais novo para o mais velho
    anuncios = Anuncio.objects.all().order_by('-data_criacao')

    return render(request, 'home.html', {'anuncios': anuncios})

def detalhe_anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    imagens = anuncio.imagens.all()
    return render(request, 'detalhe_anuncio.html', {'anuncio': anuncio, 'imagens': imagens})

def criar_anuncio(request):

        if request.method == 'POST':
            form = AnuncioForm(request.POST, request.FILES)


            if form.is_valid():
                anuncio = form.save()

                # Processar as imagens enviadas
                imagens = request.FILES.getlist('imagens')
                
                for imagem in imagens:
                    ImagemAnuncio.objects.create(
                        anuncio=anuncio,
                        imagem=imagem
                    )

                messages.success(request, 'Anúncio criado com sucesso!')
                return redirect('detalhe_anuncio', pk=anuncio.pk) 
        else:
            form = AnuncioForm()

        return render(request, 'criar_anuncio.html', {'form':form})   
