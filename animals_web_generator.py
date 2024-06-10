import json

def load_data(file_path):
    """Function to load the JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def display_animal_data():
    """read and print the animal_data contents"""
    data = load_data("animals_data.json")
    for animal in data:
        if "name" in animal:
            print(f"Name: {animal['name']}")
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            print(f"Diet: {animal['characteristics']['diet']}")
        if "locations" in animal:
            print(f"Location: {animal['locations'][0]}")
        if "characteristics" in animal and "type" in animal["characteristics"]:
            print(f"Type: {animal['characteristics']['type']}")
        print()

display_animal_data()


