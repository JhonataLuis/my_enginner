from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Anuncio, ImagemAnuncio
from .forms import AnuncioForm

# Create your views here.

# Função para listar e mostrar todos os anúncios
def home(request):
    # Busca e filtros
    query = request.GET.get('q', '')
    tipo = request.GET.get('tipo','')
    cidade = request.GET.get('cidade', '')

    anuncios = Anuncio.objects.filter(ativo=True, status_imovel='DISPONIVEL')

    # busca geral
    if query:
        anuncios = anuncios.filter(
             Q(titulo__icontains=query) |
             Q(descricao__icontains=query) |
             Q(endereco__icontains=query)
        )
    # tipo de imóvel
    if tipo:
        anuncios = anuncios.filter(tipo_imovel=tipo)

    # cidade
    if cidade:
         anuncios = anuncios.filter(cidade__icontains=cidade)    

        # Mostra todos os anuncios, do mais novo para o mais velho
    anuncios = anuncios.order_by('-data_criacao')

    context = {
             'anuncios': anuncios,
             'total_anuncios': anuncios.count(),
        }

    return render(request, 'home.html', context)
        #return render(request, 'home.html', {'anuncios': anuncios})

# Função para consultar os detalhes do anúncio
def detalhe_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    imagens = anuncio.imagens.all()
    return render(request, 'detalhe_anuncio.html', {'anuncio': anuncio, 'imagens': imagens})

# Função para cadastrar um novo anúncio
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
                return redirect('detalhe_anuncio', id=anuncio.id) 
        else:
            form = AnuncioForm()

        return render(request, 'criar_anuncio.html', {'form':form})   

# Função para consultar/editar um anúncio
def editConsult(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)

    if request.method == "POST":
        form = AnuncioForm(request.POST, instance=anuncio)

        if form.is_valid():
             form.save()

             # Adicionar novas imagens enviadas
             imagens = request.FILES.getlist('imagens')
             for imagem in imagens:
                  ImagemAnuncio.objects.create(
                       anuncio=anuncio,
                       imagem=imagem
                  )

             messages.success(request, "Anúncio atualizado com sucesso!")
             return redirect('detalhe_anuncio', id=anuncio.id)  

    else:

            form = AnuncioForm(instance=anuncio)

    return render(request, 'edit.html', {
          'form': form, 
          'anuncio': anuncio
          })

# Deletar imagem do anúncio
def delete_imagem(request, id):
     imagem = get_object_or_404(ImagemAnuncio, id=id)
     anuncio_id = imagem.anuncio_id
     imagem.delete()

     messages.success(request, "Imagem removida com sucesso!")

     return redirect('editConsult', id=anuncio_id)

# Função para deletar um anúncio
def delete(request, id):
     
    anuncio = get_object_or_404(Anuncio, id=id)

    if request.method == "GET":
        anuncio.delete()
        messages.success(request, "Anúncio excluído com sucesso!")

        return redirect('home.html')
        
    return render(request, 'home.html', {'anuncio': anuncio})


# Função buscar cidades ex: Terreno, Casa, etc.
def buscar_cidades(request):
     
     termo = request.GET.get('term', '')
     if termo:
          cidades = Anuncio.objects.filter(
               cidade_icontains=termo
          ).values_list('cidade', flat=True).distinct()[:10]
          return JsonResponse(list(cidades), safe=False)
     return JsonResponse([], safe=False)

