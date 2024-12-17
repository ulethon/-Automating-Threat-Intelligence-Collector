import json

def save_to_json(data, filename):
    """Utility function to save data to a JSON file"""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

def load_from_json(filename):
    """Utility function to load data from a JSON file"""
    with open(filename, 'r') as file:
        return json.load(file)
