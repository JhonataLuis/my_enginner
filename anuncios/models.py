from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

# Create your models here.
class Anuncio(models.Model):
    TIPO_IMOVEL = [
        ('AP', 'Apartamento'),
        ('CS', 'Casa'),
        ('CO', 'Comercial'),
        ('TE', 'Terreno'),
    ]    

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_imovel = models.CharField(max_length=2, choices=TIPO_IMOVEL)

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

    # Controle
    data_criacao = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.titulo    
    
    
class ImagemAnuncio(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='anuncios/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)    

        # Redimensionar imagem se necessário
        if self.imagem:
           img_path = self.imagem.path
           img = Image.open(img_path)

           # Redimensionar para no máximo 800x600
           if img.height > 600 or img.width > 800:
               output_size = (800, 600)
               img.thumbnail(output_size)
               img.save(img_path) 