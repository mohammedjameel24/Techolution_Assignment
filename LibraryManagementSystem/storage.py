# storage.py
import json

def save_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_from_json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
