import json
import re

def preprocess(text):
    """Remove all non-alphanumeric characters and convert text to lowercase."""
    return re.sub(r'\W+', '', text).lower()

def find_matching_keys(json_file, query):
    # Load JSON data from the file
    with open(json_file, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # Normalize the query to a sequence of characters
    normalized_query = preprocess(query)
    keys = sorted(json_data.keys(), key=lambda x: int(x.split('_')[1]))

    # Concatenate all texts with their keys, skipping empty entries
    full_text = ''
    index_map = []  # Maps character index in full_text to key index
    for key in keys:
        text = preprocess(json_data[key])
        if text:  # Append only if the text is not empty
            full_text += text
            index_map.extend([key] * len(text))  # Map each character to its key

    # Find the start position of the query in the full text
    start_pos = full_text.find(normalized_query)
    if start_pos == -1:
        return []  # Query not found

    # Find the range of keys that encompass the query
    start_key = index_map[start_pos]
    end_key = index_map[start_pos + len(normalized_query) - 1]

    # Collect and return the range of keys from start to end
    start_index = keys.index(start_key)
    end_index = keys.index(end_key)
    return keys[start_index:end_index + 1]

# Example usage:
json_file = 'tbcpitw.json'
query_one = " a secret drawer. There was something inthere. I reached in and took out a small black tin box.Sello-taped to the top of it was a piece of lined notepaper,and written on it in shakyhandwriting: “Jim’slast letter, receivedJanuary 25, 1915.To be buried withme when thetime comes"
result_keys_one = find_matching_keys(json_file, query_one)
print("Matching keys:", result_keys_one)



