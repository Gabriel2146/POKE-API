# Pokédex Django WebApp

Proyecto web desarrollado con Django y Django REST Framework que consume la API pública [PokeAPI](https://pokeapi.co/) para mostrar información de Pokémon. Incluye buenas prácticas de desarrollo, principios SOLID (SRP y OCP), y patrones de diseño Factory y Strategy.

## Características
- Interfaz web moderna y responsiva para buscar Pokémon por nombre o ID.
- Consumo de la API REST pública de PokeAPI.
- Arquitectura basada en principios SOLID y patrones de diseño.
- Código documentado y siguiendo PEP 8.
- Control de versiones recomendado con Git.

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd POKE API
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # En Windows
   # source venv/bin/activate  # En Linux/Mac
   ```

3. **Instala las dependencias:**
   ```bash
   pip install django djangorestframework requests
   ```

4. **Aplica migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

6. **Accede a la aplicación:**
   - Página de inicio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Detalle de Pokémon: [http://127.0.0.1:8000/pokemon/pikachu/](http://127.0.0.1:8000/pokemon/pikachu/)

## Endpoints principales

- `/` — Página de inicio con formulario de búsqueda.
- `/pokemon/<name_or_id>/` — Detalle de Pokémon por nombre o ID (HTML).

## Estructura de carpetas principal

```
POKE API/
├── pokeapi_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── pokemon/
│   ├── views.py
│   ├── pokeapi_client.py
│   ├── templates/
│   │   └── pokemon/
│   │       ├── home.html
│   │       └── pokemon_detail.html
│   └── ...
├── manage.py
└── README.md
```

## Principios y patrones aplicados
- **SRP (Single Responsibility Principle):** Cada clase y función tiene una única responsabilidad.
- **OCP (Open/Closed Principle):** El cliente de la API permite extensión mediante estrategias.
- **Factory Pattern:** Para instanciar la estrategia de consumo de la API.
- **Strategy Pattern:** Para definir diferentes formas de consumir la API.

## Contribución
1. Haz un fork del repositorio.
2. Crea una rama para tu feature o fix: `git checkout -b mi-feature`.
3. Realiza tus cambios y haz commit: `git commit -am 'Agrega mi feature'`.
4. Haz push a tu rama: `git push origin mi-feature`.
5. Abre un Pull Request.

## Licencia
Este proyecto está bajo la licencia MIT.

## Créditos
- [PokeAPI](https://pokeapi.co/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
