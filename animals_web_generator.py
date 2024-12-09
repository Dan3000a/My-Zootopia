import html
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.api-ninjas.com/v1/animals'
HEADERS = {'X-Api-Key': API_KEY}


def load_data(animal_name):
    """Fetches data from the API and returns it as a list of objects."""
    params = {'name': animal_name}
    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        parsed_result = response.json()
        print(f"Successfully fetched data for '{animal_name}': {len(parsed_result)} animals found.")
        return parsed_result

    print(f"Error with the request: {response.status_code}, Message: {response.text}")
    return []


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML list item."""
    output = '<li class="cards__item">\n'
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
    """Generates the HTML output for all animals."""
    return ''.join(serialize_animal(animal) for animal in animals_data)


def read_html_template(file_path):
    """Reads an HTML template file."""
    with open(file_path, "r", encoding="utf8") as file:
        return file.read()


def write_html_file(output_path, content):
    """Writes content to an HTML file."""
    with open(output_path, "w", encoding="utf8") as file:
        file.write(content)
    print(f"HTML file '{output_path}' generated successfully!")


def main():
    """Main function to orchestrate the API call, generate HTML, and save the file."""
    user_input = input('What animal are you looking for? ')
    animals_data = load_data(user_input.strip())

    if not animals_data:  # Check if data is available
        print("No data received. Please check the API or the query parameters.")
        return

    # Generate HTML for animals
    animals_html = generate_animal_html(animals_data)

    # Read the template file
    template_file_path = "animals_template.html"
    html_template = read_html_template(template_file_path)

    # Replace the placeholder with generated animal HTML
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Save the generated HTML file
    output_file_path = "animals.html"
    write_html_file(output_file_path, html_output)


if __name__ == "__main__":
    main()