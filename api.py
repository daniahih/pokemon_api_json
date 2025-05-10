import sys
import requests
from constants import POKEMON_LIST_ENDPOINT


def fetch_pokemon_list():
    """
    Fetches a list of all Pokémon (name & URL).
    Exits on failure.
    """
    try:
        resp = requests.get(POKEMON_LIST_ENDPOINT)
        resp.raise_for_status()
        return resp.json().get("results", [])
    except requests.RequestException as e:
        print(f"Error fetching list: {e}")
        sys.exit(1)


def fetch_pokemon_details(url):
    """
    Fetches full JSON data for a given Pokémon URL.
    Returns None on failure.
    """
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()
       
    except requests.RequestException as e:
        print(f"Error fetching details: {e}")
        return None