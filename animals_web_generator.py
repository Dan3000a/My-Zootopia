import json
import html


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML list item."""
    output = ''
    output += '<li class="cards__item">\n'
    if "name" in animal_obj:
        output += f'  <div class="card__title">{html.escape(animal_obj["name"])}</div>\n'
    output += '  <p class="card__text">\n'
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += f'      <strong>Diet:</strong> {html.escape(animal_obj["characteristics"]["diet"])}<br/>\n'
    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        locations = " and ".join(map(html.escape, animal_obj["locations"]))
        output += f'      <strong>Location:</strong> {locations}<br/>\n'
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += f'      <strong>Type:</strong> {html.escape(animal_obj["characteristics"]["type"])}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


def generate_animal_html(animals_data):
    """Generates the HTML for all animals by using the serialize_animal function."""
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)  # Call the function for each animal
    return output


def main():
    """Main function to orchestrate loading data, generating HTML, and saving the file."""
    # Load JSON data
    animals_data = load_data('animals_data.json')

    # Generate the animals output
    animals_html = generate_animal_html(animals_data)

    # Read the HTML template
    template_file_path = "animals_template.html"
    with open(template_file_path, "r") as file:
        html_template = file.read()

    # Replace placeholder in the template with the generated animal HTML
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Write the final HTML to a new file
    output_file_path = "animals.html"
    with open(output_file_path, "w") as file:
        file.write(html_output)

    print(f"HTML file '{output_file_path}' generated successfully!")


if __name__ == "__main__":
    main()