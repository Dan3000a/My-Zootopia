
### 1. Python-Code: Arbeiten mit JSON und HTML (detaillierter)

#### Schritt 1: Daten importieren
- Die JSON-Daten wurden mit einer Funktion `load_data` aus der Datei `animals_data.json` geladen. 
- Der Code liest die Datei und wandelt sie in ein Python-Dictionary um:
```python
def load_data(file_path):
    # Lädt eine JSON-Datei und gibt sie als Dictionary zurück.
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')
```
- **Zweck**: Ermöglicht den Zugriff auf strukturierte Daten, die später verarbeitet werden.

---

#### Schritt 2: Datenabfragen aus JSON
- Die JSON-Daten enthalten Informationen über Tiere, wie Name, Ernährungsweise, Standort und Typ. Der Zugriff erfolgte durch Iteration und Bedingungsprüfung:
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
    print("\n")
```
- **Zweck**: Nur vorhandene Daten werden abgefragt und ausgegeben, um Fehler zu vermeiden.

---

#### Schritt 3: Serialisierung der Daten
- Zur besseren Organisation wurde die Funktion `serialize_animal` eingeführt, die die Daten eines einzelnen Tieres in eine HTML-Struktur umwandelt:
```python
def serialize_animal(animal_obj):
    # Serialisiert ein einzelnes Tier in ein HTML-Listenelement.
    output = '<li class="cards__item">\n'
    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += f'      <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        locations = " and ".join(animal_obj["locations"])
        output += f'      <strong>Location:</strong> {locations}<br/>\n'
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += f'      <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output
```

- **Zweck**: Der Code wird modularer, und Änderungen an der HTML-Struktur müssen nur in einer Funktion vorgenommen werden.

---

#### Schritt 4: HTML-Generierung
- Die `serialize_animal`-Funktion wurde verwendet, um alle Tiere zu iterieren und die Ergebnisse zu einer vollständigen HTML-Liste zusammenzuführen:
```python
def generate_animal_html(animals_data):
    # Generiert die HTML-Ausgabe für alle Tiere.
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output

animals_html = generate_animal_html(animals_data)
```

---

#### Schritt 5: Integration ins HTML-Template
- Ein bestehendes HTML-Template (`animals_template.html`) wurde gelesen. Der Platzhalter `__REPLACE_ANIMALS_INFO__` wurde durch die generierten Tierdaten ersetzt:
```python
with open("animals_template.html", "r") as file:
    html_template = file.read()

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
```

---

#### Schritt 6: Generiertes HTML speichern
- Die resultierende HTML-Datei wurde in `animals.html` geschrieben:
```python
with open("animals.html", "w") as file:
    file.write(html_output)
```

---

#### Schritt 7: Tests und Debugging
- Das Skript wurde ausgeführt, um sicherzustellen, dass die Datei `animals.html` korrekt generiert wurde.
- Fehler wurden durch kleine Anpassungen in den Funktionen und Datenabfragen behoben.

---

#### Ergebnis
- **JSON-Daten wurden erfolgreich eingelesen, verarbeitet und in HTML überführt**.
- Das Endprodukt (`animals.html`) ist eine dynamische Liste von Tieren, die aus den JSON-Daten generiert wurde.

---

