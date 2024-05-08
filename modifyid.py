
from bs4 import BeautifulSoup, NavigableString
import json
import re

def add_span_ids_and_create_json(html_file, json_file):
    # Load the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Dictionary to store span ids and their exact text content
    span_data = {}

    # Find all span tags
    spans = soup.find_all('span')
    # Loop through each span, assign an ID, and collect text
    for index, span in enumerate(spans, start=1):
        span_id = f"light_{index}"
        span['id'] = span_id
        # Initialize an empty string to collect direct text
        direct_text = ''
        # Check each child of the span; if it's a direct text node, add it
        for content in span.contents:
            if isinstance(content, NavigableString):
                direct_text += content
        # Clean the direct text: lower case, remove special characters except whitespace
        direct_text = re.sub(r'[^\w\s]', '', direct_text.lower())
        span_data[span_id] = direct_text

    # Write the changes back to the HTML file
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    # Create and write the JSON data
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(span_data, file, indent=4)

# Replace 'yourfile.html' with the path to your HTML file
# Example usage
add_span_ids_and_create_json('light.html', 'light.json')
