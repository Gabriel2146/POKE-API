from django.shortcuts import render
from .pokeapi_client import PokemonAPIClientFactory

def home(request):
    return render(request, 'pokemon/home.html')

def pokemon_list(request):
    page = int(request.GET.get('page', 1))
    limit = 20
    offset = (page - 1) * limit
    client = PokemonAPIClientFactory.get_client()
    try:
        data = client.get_pokemon_list(offset=offset, limit=limit)
        pokemons = data['results'] if data else []
        count = data['count'] if data else 0
        next_page = page + 1 if data and data.get('next') else None
        prev_page = page - 1 if page > 1 else None
        error = None
    except Exception as e:
        pokemons = []
        count = 0
        next_page = None
        prev_page = None
        error = 'Error al conectar con la API. Intenta más tarde.'
    context = {
        'pokemons': pokemons,
        'page': page,
        'next_page': next_page,
        'prev_page': prev_page,
        'count': count,
        'limit': limit,
        'error': error
    }
    return render(request, 'pokemon/pokemon_list.html', context)

def pokemon_detail(request, name_or_id):
    client = PokemonAPIClientFactory.get_client()
    try:
        pokemon = client.get_pokemon(name_or_id)
        error = None if pokemon else f'No se encontró información para "{name_or_id}".'
    except Exception as e:
        pokemon = None
        error = 'Error al conectar con la API. Intenta más tarde.'
    context = {'pokemon': pokemon, 'name_or_id': name_or_id, 'error': error}
    return render(request, 'pokemon/pokemon_detail.html', context)
