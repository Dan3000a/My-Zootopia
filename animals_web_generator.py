import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')
"""original code:
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
"""

# Step 1: Read the HTML template
template_file_path = "animals_template.html"
with open(template_file_path, "r") as file:
    html_template = file.read()

# Step 2: Generate the animals output (from your previous step)
output = ""  # Example output generation
for animal in animals_data:
    if "name" in animal:
        output += f"Name: {animal['name']}\n"
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}\n"
    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"Location: {animal['locations'][0]}\n"
    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}\n"
    output += "\n"

# Step 3: Replace the placeholder in the template
html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 4: Write the final HTML to a new file
output_file_path = "animals.html"

with open(output_file_path, "w") as file:
    file.write(html_output)

print(f"HTML file '{output_file_path}' generated successfully!")