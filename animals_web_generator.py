import json
import html


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load JSON data
animals_data = load_data('animals_data.json')

def generate_animal_html():
    """Generates the HTML for the animals list."""
    output = ''  # Initialize an empty string to hold the serialized HTML
    for animal_data in animals_data:
        # Start a new list item
        output += '<li class="cards__item">\n'

        # Add animal title (name)
        if "name" in animal_data:
            output += f'  <div class="card__title">{html.escape(animal_data["name"])}</div>\n'

        # Add animal details in a paragraph
        output += '  <p class="card__text">\n'
        if "characteristics" in animal_data and "diet" in animal_data["characteristics"]:
            output += f'      <strong>Diet:</strong> {html.escape(animal_data["characteristics"]["diet"])}<br/>\n'
        if "locations" in animal_data and len(animal_data["locations"]) > 0:
            locations = " and ".join(map(html.escape, animal_data["locations"]))
            output += f'      <strong>Location:</strong> {locations}<br/>\n'
        if "characteristics" in animal_data and "type" in animal_data["characteristics"]:
            output += f'      <strong>Type:</strong> {html.escape(animal_data["characteristics"]["type"])}<br/>\n'
        output += '  </p>\n'

        # End the list item
        output += '</li>\n'

    return output


# Generate the animals output
animals_html = generate_animal_html()

# Replace placeholder and write to file
with open("animals_template.html", "r") as file:
    html_template = file.read()

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

with open("animals.html", "w") as file:
    file.write(html_output)

print("HTML file 'animals.html' generated successfully!")