
### 1. Python Code: Working with JSON and HTML (Detailed)

#### Step 1: Importing Data
- Initially, JSON data was imported from a file (`animals_data.json`) using a `load_data` function.
- This function reads the file and converts it into a Python dictionary:
```python
def load_data(file_path):
    # Reads a JSON file and returns it as a dictionary.
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')
```
- **Purpose**: To access structured data for further processing.

---

#### Step 2: Querying JSON Data
- The JSON data contains animal details such as name, diet, location, and type. The data is accessed and validated using conditions:
```python
for animal in animals_data:
    if "name" in animal:
        print(animal["name"])
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        print(animal["characteristics"]["diet"])
    if "locations" in animal and len(animal["locations"]) > 0:
        print(animal["locations"][0])
    if "characteristics" in animal and "type" in animal["characteristics"]:
        print(animal["characteristics"]["type"])
    print("
")
```
- **Purpose**: Ensure only available data is accessed to avoid errors.

---

#### Step 3: Serializing Data
- A function (`serialize_animal`) was introduced to format a single animal's data into an HTML structure:
```python
def serialize_animal(animal_obj):
    # Serializes a single animal into an HTML list element.
    output = '<li class="cards__item">
'
    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>
'
    output += '  <p class="card__text">
'
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += f'      <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>
'
    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        locations = " and ".join(animal_obj["locations"])
        output += f'      <strong>Location:</strong> {locations}<br/>
'
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += f'      <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>
'
    output += '  </p>
'
    output += '</li>
'
    return output
```
- **Purpose**: Make the code modular so any changes in the HTML structure can be implemented in one place.

---

#### Step 4: Generating HTML
- The `serialize_animal` function is used to iterate through all animals and create a complete HTML list:
```python
def generate_animal_html(animals_data):
    # Generates the HTML output for all animals.
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output

animals_html = generate_animal_html(animals_data)
```

---

#### Step 5: Integrating into an HTML Template
- An existing HTML template (`animals_template.html`) is read. The placeholder `__REPLACE_ANIMALS_INFO__` is replaced with the serialized animal data:
```python
with open("animals_template.html", "r") as file:
    html_template = file.read()

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
```

---

#### Step 6: Saving the Generated HTML
- The resulting HTML file is written to `animals.html`:
```python
with open("animals.html", "w") as file:
    file.write(html_output)
```

---

#### Step 7: Transition to API Data
- Instead of relying on a local JSON file, the program was updated to fetch animal data from an API:
```python
def load_data(animal_name):
    params = {'name': animal_name}
    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        parsed_result = response.json()
        print(f"Successfully fetched data for '{animal_name}': {len(parsed_result)} animals found.")
        return parsed_result
    else:
        print(f"Request error: {response.status_code}, Message: {response.text}")
        return []
```

#### Step 8: Dynamically Fetching Animal Data
- The program was modified to take user input for the desired animal and fetch its details from the API:
```python
user_input = input('What animal are you looking for? ')
animals_data = load_data(user_input.strip())
```

#### Step 9: Testing and Debugging
- The script was executed to ensure correct generation of the `animals.html` file.
- The new functionality was verified with dynamic user input and API calls.

---

### **Results**
- **Initial JSON Approach**: Successfully imported, queried, and transformed local JSON data into HTML.
- **API Integration**: The program now dynamically fetches data from an API based on user input, enhancing functionality and flexibility.
