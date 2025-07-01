import requests
from abc import ABC, abstractmethod

class PokemonAPIClientStrategy(ABC):
    """Interfaz Strategy para obtener datos de la PokeAPI."""
    @abstractmethod
    def get_pokemon(self, name_or_id):
        pass

class DefaultPokemonAPIClient(PokemonAPIClientStrategy):
    """Implementación por defecto para obtener datos de la PokeAPI."""
    BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'

    def get_pokemon(self, name_or_id):
        response = requests.get(f'{self.BASE_URL}{name_or_id}')
        if response.status_code == 200:
            return response.json()
        return None

class PokemonAPIClientFactory:
    """Factory para instanciar estrategias de consumo de la PokeAPI."""
    @staticmethod
    def get_client(strategy_name='default'):
        if strategy_name == 'default':
            return DefaultPokemonAPIClient()
        # Aquí se pueden agregar más estrategias
        raise ValueError('Estrategia no soportada')
