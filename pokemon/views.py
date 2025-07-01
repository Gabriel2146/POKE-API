from django.shortcuts import render
from .pokeapi_client import PokemonAPIClientFactory

def home(request):
    return render(request, 'pokemon/home.html')

def pokemon_detail(request, name_or_id):
    client = PokemonAPIClientFactory.get_client()
    pokemon = client.get_pokemon(name_or_id)
    context = {'pokemon': pokemon, 'name_or_id': name_or_id}
    return render(request, 'pokemon/pokemon_detail.html', context)
