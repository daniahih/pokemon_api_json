from db import load_db, save_db
from api import fetch_pokemon_list, fetch_pokemon_details
from utils import get_random_pokemon, extract_relevant_fields
from ui import ask_user, display_pokemon


def main():
    db = load_db()
    pokemon_list = fetch_pokemon_list()

    while ask_user():
        name, url = get_random_pokemon(pokemon_list)

        if name in db:
            print(f"Already drew {name.title()}:")
            display_pokemon(db[name])
        else:
            print(f"New Pokémon: {name.title()}! Fetching...")
            data = fetch_pokemon_details(url)
            if data:
                details = extract_relevant_fields(data)
                db[name] = details
                save_db(db)
                display_pokemon(details)
            else:
                print("Couldn’t fetch details.")

    print("Goodbye! Thanks for playing.")


if __name__ == '__main__':
    main()