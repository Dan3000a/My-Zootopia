# Animal Info Fetcher

A Python application that fetches animal data from an external API and generates an HTML file showcasing the animal information.

## Features
- Fetch data about animals using the [API Ninjas Animals API](https://api-ninjas.com).
- Serialize animal data into a user-friendly HTML format.
- Automatically generate and save an HTML file with the fetched data.

## Requirements
- Python 3.7+
- A valid API key for the API Ninjas Animals API.

## Dependencies
The following Python libraries are used:
- `requests`: For making HTTP requests to the API.
- `dotenv`: For managing environment variables.
- `html`: For escaping HTML content in Python.

You can install the required dependencies using:
```bash
pip install -r requirements.txt