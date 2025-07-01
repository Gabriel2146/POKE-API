from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pokemons/', views.pokemon_list, name='pokemon_list'),
    path('pokemon/<str:name_or_id>/', views.pokemon_detail, name='pokemon_detail'),
]
