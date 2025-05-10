"""
constants.py
Application-wide constants for the Pokémon CLI app.
"""

API_BASE_URL = "https://pokeapi.co/api/v2"
POKEMON_LIST_ENDPOINT = f"{API_BASE_URL}/pokemon?limit=100000&offset=0"
DB_PATH = "pokemon_db.json"