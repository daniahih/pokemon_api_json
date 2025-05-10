def ask_user():
    """
    Prompts 'yes/no'; returns True on yes.
    """
    ans = input("Draw a Pokémon? (yes/no): ").strip().lower()
    return ans in ('yes', 'y')


def display_pokemon(details):
    """
    Nicely prints the Pokémon details.
    """
    print("\n--- Pokémon ---")
    print(f"ID: {details['id']}")
    print(f"Name: {details['name'].title()}")
    print(f"Height: {details['height']} dm")
    print(f"Weight: {details['weight']} hg")
    print(f"Base Exp: {details['base_experience']}")
    print(f"Types: {', '.join(details['types'])}")
    print(f"Abilities: {', '.join(details['abilities'])}")
    print("--------------\n")