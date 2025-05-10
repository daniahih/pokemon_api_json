import requests

API_BASE_URL = "https://pokeapi.co/api/v2"
POKEMON_LIST_ENDPOINT = f"{API_BASE_URL}/pokemon?limit=100000&offset=0"
resp = requests.get(POKEMON_LIST_ENDPOINT)
print(f"resp :{resp}")
response = resp.json().get('results',[])
print(f'response {response}')
# Using dict.get(key, default) is the idiomatic way to look up a key and supply a fallback if the key isn’t present.

# Here, if for some reason the API returns an object without "results", data.get("results", []) will give you an empty list ([]) instead of raising a KeyError.


