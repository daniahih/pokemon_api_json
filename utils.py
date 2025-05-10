import random


def get_random_pokemon(pokemon_list):
    """
    Returns a (name, url) tuple chosen at random.
    """
    choice = random.choice(pokemon_list)
    return choice['name'], choice['url']


def extract_relevant_fields(data):
    """
    Strips out only the fields we care about.
    """
    return {
        'id': data.get('id'),
        'name': data.get('name'),
        'height': data.get('height'),
        'weight': data.get('weight'),
        'base_experience': data.get('base_experience'),
        'types': [t['type']['name'] for t in data.get('types', [])],
        'abilities': [a['ability']['name'] for a in data.get('abilities', [])]
    }