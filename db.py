import os
import json
from constants import DB_PATH


def load_db(path=DB_PATH):
    """
    Loads cache from disk, warns on error.
    """
    if os.path.exists(path):
        try:
            with open(path) as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError):
            print(f"Warning: cannot read {path}, starting fresh.")
    return {}


def save_db(db, path=DB_PATH):
    """
    Saves cache to disk.
    """
    try:
        with open(path, 'w') as f:
            json.dump(db, f, indent=4)
    except IOError as e:
        print(f"Error writing {path}: {e}")