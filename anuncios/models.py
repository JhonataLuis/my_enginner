from django.db import models
from django.contrib.auth.models import User
from django.utils import timizone
from PIL import Image

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome    
    
class Anuncio(models.Model):
    TIPO_IMOVEL = [
        ('AP', 'Apartamento'),
        ('CS', 'Casa'),
        ('CO', 'Comercial'),
        ('TE', 'Terreno'),
    ]    

    STATUS = [
        ('D', 'Disponível'),
        ('V', 'Vendido'),
        ('A', 'Alugado'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_imovel = models.CharField(max_length=2, choices=TIPO_IMOVEL)
    status = models.CharField(max_length=1, choices=STATUS, default='D')

    # Localização
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    # Características
    quartos = models.IntegerField(default=0)
    banheiros = models.IntegerField(default=0)
    vagas_garagem = models.IntegerField(default=0)
    area_total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    # Relacionamentos
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anuncios')

    # Controle
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-data_criacao']


    def __str__(self):
        return self.titulo    
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detalhe_anuncio', args=[str(self.id)])
    
class ImagemAnuncio(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='anuncios/%Y/%m/')
    ordem = models.IntegerField(default=0)    
    principal = models.BooleanField(default=False)

    class Meta:
        ordering = ['ordem']
        verbose_name ='Imagem do Anúncio'
        verbose_name_plural = 'Imagens do Anúncio'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)    

        # Redimensionar imagem se necessário
        if self.imagem:
            img_path = self.imagem.path
            img = Image.open(img_path)

            # Redimensionar para no máximo 1024x1024 mantendo proporção
            max_size = (1024, 1024)
            img.thumbnail(max_size, Image.Resanpling.LANCZOS)

            # Criar thumbnail
            thumb_size = (300, 200)
            thumb = img.copy()
            thumb.thumbnail(thumb_size, Image.Resanpling.LANCZOS)
            thumb_path = img_path.replace('.', '_thumb.')
            thumb.save(thumb_path, optimize=True, quality=85)

            img.save(img_path, optimize=True, quality=85)

    def __str__(self):
        return f"Imagem {self.ordem} - {self.anuncio.titulo}" 