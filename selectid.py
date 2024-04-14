# import json
# import re

# def preprocess(text):
#     """Remove all non-alphanumeric characters and convert text to lowercase."""
#     return re.sub(r'\W+', '', text).lower()

# def find_matching_keys(json_file, query):
#     # Load JSON data from the file
#     with open(json_file, 'r', encoding='utf-8') as file:
#         json_data = json.load(file)

#     # Normalize the query to a sequence of characters
#     query = list(preprocess(query))
#     keys = sorted(json_data.keys(), key=lambda x: int(x.split('_')[1]))

#     start_key_index = 0  # Track where the match starts
#     query_index = 0  # Current index in the query to match
#     matching_keys = []

#     # Iterate over each key
#     for i, key in enumerate(keys):
#         text = list(preprocess(json_data[key]))  # Convert text to list of characters
#         print(key,text)
#         # Check characters in the current key's text
#         for char in text:
            
#             if char == query[query_index]:  # Match found for the current query character
#                 query_index += 1  # Move to the next character in the query
#                 if query_index == 1:  # First match in this key
#                     start_key_index = i
#                 if query_index == len(query):  # All characters matched
#                     return keys[start_key_index:i+1]
#             else:
#                 # Reset if any character mismatches in the middle of a match
#                 if query_index > 0:
#                     query_index = 0
#                     break  # Restart matching from the next key

#     return []

# json_file = 'hehd101.json'
# query_one = "all i could to ease it out gently in the end i used brute force i struck it sharply with the side of my fist and the drawer flew open to reveal a shallow space underneath a secret drawer"
# result_keys_one = find_matching_keys(json_file, query_one)
# print("Matching keys:", result_keys_one)

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
query_one = "re calling out to us from acrossno man’s land, “Happy Christmas, Tommy! HappyChristmas!” When we had got over the surprise, some ofus shouted back, “Same to you, Fritz! Same to you!” Ithought that would be that. We all did. But then suddenlyone of them was up there in his grey greatcoat and wavinga white flag. “Don’t shoot, lads!” someone shouted. Andno one did. Then there was another Fritz up on theparapet, and another. “Keep your heads down,” I told themen, “it’s a trick.” But it wasn’t.One of the Germans was waving a bottle above hishead. “It is Christmas Day, Tommy. We have schnapps.We have sausage. We meet you? Yes?” By this time therewere dozens of them walking towards us across no man’sland and not a rifle between them. Little Private Morriswas the first up. “Come on, boys. What are we waitingfor?” And then there was no stopping them. I was theofficer. I should have stopped them there and then, Isuppose, but the truth is that it never even occurred tome I should. All along their line and ours I could seemen walking slowly towards one another, grey coats,khaki coats meeting in the middle. "
result_keys_one = find_matching_keys(json_file, query_one)
print("Matching keys:", result_keys_one)



