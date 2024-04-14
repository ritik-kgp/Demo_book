# from bs4 import BeautifulSoup
# import re

# # Define the path to your HTML file
# html_file_path = 'Introduction_to_graphs.html'

# # Function to modify the CSS content
# def modify_css(css_content):
#     # Broad pattern to match various class names and CSS properties, including font-size
#     pattern = r'(\.[\w\d]+)\{(\w+-spacing|width|height|left|bottom|font-size):\s*([-\d.]+)px;'
    
#     # Use re.sub with a lambda function for replacement to apply calc() to the values
#     modified_css = re.sub(
#         pattern,
#         lambda m: f"{m.group(1)}{{ {m.group(2)}: calc(var(--scale-factor) * {m.group(3)}px);",
#         css_content
#     )
    
#     return modified_css

# # Open and read the HTML file
# with open(html_file_path, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # Parse the HTML
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all <style> tags
# style_tags = soup.find_all('style')

# for style in style_tags:
#     # Modify the CSS content and replace the old content
#     modified_css = modify_css(style.string)
#     style.string.replace_with(modified_css)

# # Write the modified HTML back to the file (or a new file if you prefer)
# with open('Introduction_to_graphs.html', 'w', encoding='utf-8') as file:
#     file.write(str(soup))



from bs4 import BeautifulSoup
import re
import os

# List of HTML file paths
html_files =['hehd101.html']


# Function to modify the CSS content
def modify_css(css_content):
    # Broad pattern to match various class names and CSS properties, including font-size
    pattern = r'(\.[\w\d]+)\{(\w+-spacing|width|height|left|bottom|font-size):\s*([-\d.]+)px;'
    
    # Use re.sub with a lambda function for replacement to apply calc() to the values
    modified_css = re.sub(
        pattern,
        lambda m: f"{m.group(1)}{{ {m.group(2)}: calc(var(--scale-factor) * {m.group(3)}px);",
        css_content
    )
    
    return modified_css

# Function to process each HTML file
def process_html_file(html_file_path):
    # Open and read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <style> tags
    style_tags = soup.find_all('style')

    for style in style_tags:
        # Modify the CSS content and replace the old content
        modified_css = modify_css(style.string)
        style.string.replace_with(modified_css)

    # Write the modified HTML back to the file
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# Process each file in the list
for html_file in html_files:
    process_html_file(html_file)

