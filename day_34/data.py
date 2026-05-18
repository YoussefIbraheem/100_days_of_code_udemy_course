import requests
import html

# Set query parameters for Trivia question API
query_params = {"amount": 10, "type": "boolean"}

# Make request to Trivia question API
response = requests.get("https://opentdb.com/api.php", params=query_params)
response.encoding = "utf-8"

# Parse response JSON data
question_data = response.json()["results"]
