from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('anuncio/<int:pk>/', views.detalhe_anuncio, name='detalhe_anuncio'),
    path('criar/', views.criar_anuncio, name='criar_anuncio'),
    path('detalhes/', views.detalhe_anuncio, name='detalhe_anuncio')
]