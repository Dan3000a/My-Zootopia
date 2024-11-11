import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
    if "name" in animal:
        print(animal["name"])
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        print(animal["characteristics"]["diet"])
    if "locations" in animal and len(animal["locations"]) > 0:  # Making sure "locations" is a list with entries
        print(animal["locations"][0])
    if "characteristics" in animal and "type" in animal["characteristics"]:
        print(animal["characteristics"]["type"])
    print("\n")


