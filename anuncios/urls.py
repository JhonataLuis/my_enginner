from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('anuncio/<int:id>/', views.detalhe_anuncio, name='detalhe_anuncio'),
    path('criar/', views.criar_anuncio, name='criar_anuncio'),
    path('detalhes/', views.detalhe_anuncio, name='detalhe_anuncio'),
    path('editConsult/<int:id>', views.editConsult, name='editConsult'),
    path('delete-imagem/<int:id>', views.delete_imagem, name='delete_imagem'),
    path('delete/<int:id>', views.delete, name='delete')
]