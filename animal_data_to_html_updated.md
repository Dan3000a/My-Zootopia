
# **Python Project: Animal Data to HTML**

## **Overview**
This project demonstrates how to dynamically fetch, serialize, and transform animal data from an API into an HTML format using Python. The program takes user input to query specific animals from the API and integrates the fetched data into an HTML template.

---

## **Steps**

### **1. Python Code: Working with API and HTML**

#### Step 1: Fetching Data from API
- The `load_data` function queries the API for animal data based on user input:
```python
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
```
- **Purpose**: To retrieve animal data dynamically based on the user's input.

---

#### Step 2: Serializing Data into HTML
- The `serialize_animal` function formats a single animal's data into an HTML structure:
```python
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
```
- **Purpose**: Modularize the conversion of animal data into an HTML format.

---

#### Step 3: Generating HTML for All Animals
- The `generate_animal_html` function uses `serialize_animal` to generate HTML for all animals:
```python
def generate_animal_html(animals_data):
    """Generates the HTML output for all animals."""
    return ''.join(serialize_animal(animal) for animal in animals_data)
```
- **Purpose**: Combine all serialized animals into a single HTML structure.

---

#### Step 4: Integrating with an HTML Template
- The `read_html_template` function reads the HTML template file, and the placeholder `__REPLACE_ANIMALS_INFO__` is replaced with the generated animal HTML:
```python
def read_html_template(file_path):
    """Reads an HTML template file."""
    with open(file_path, "r", encoding="utf8") as file:
        return file.read()

html_template = read_html_template("animals_template.html")
html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
```

---

#### Step 5: Writing the Final HTML File
- The `write_html_file` function saves the final HTML content to a file:
```python
def write_html_file(output_path, content):
    """Writes content to an HTML file."""
    with open(output_path, "w", encoding="utf8") as file:
        file.write(content)
    print(f"HTML file '{output_path}' generated successfully!")
```
- **Purpose**: Save the dynamically generated HTML content into a file for viewing.

---

### **2. Main Function Workflow**
- The `main` function orchestrates the entire workflow:
  1. Fetch user input for the desired animal.
  2. Query the API for animal data.
  3. Generate the HTML structure for the fetched data.
  4. Read the HTML template and replace the placeholder.
  5. Save the final HTML to a file:
```python
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
```

---

### **Results**
1. The program dynamically fetches animal data from an API based on user input.
2. The fetched data is serialized into a clean HTML format and integrated into an existing template.
3. The final HTML is saved for viewing in a web browser.

---

### **Future Enhancements**
- Add support for caching API responses to improve performance.
- Enhance the HTML template for a more interactive user experience.
- Include error handling for network issues and invalid user input.

---

