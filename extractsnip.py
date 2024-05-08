import fitz  # PyMuPDF
from PIL import Image, ImageDraw
import json

with open('jsonData_sci.json', 'r') as file:
    overlayData = json.load(file)

def extract_image_from_pdf(file_path, page_number, rect):
    doc = fitz.open(file_path)
    page = doc.load_page(page_number - 1)  # page numbers start from 0
    clip = fitz.Rect(rect)  # rect is a tuple (x1, y1, x2, y2)
    pix = page.get_pixmap(clip=clip)  # renders the cropped area
    output_image = f"output_image_page_{page_number}.png"
    pix.save(output_image)
    doc.close()
    return output_image

def add_translucent_rectangle(image_path, top_left, bottom_right, output_path):
    # Open the original image
    with Image.open(image_path) as im:
        # Create a transparent overlay
        overlay = Image.new('RGBA', im.size, (255, 0, 255, 0))  # Full transparency
        # Get the drawing context for the overlay
        draw = ImageDraw.Draw(overlay)
        # Define the color and opacity for the rectangle
        # In this case, purple with 128 out of 255 opacity
        rectangle_color = (128, 0, 128, 128)
        # Draw the rectangle on the overlay
        draw.rectangle((top_left, bottom_right), fill=rectangle_color)
        # Composite the original image with the overlay
        combined = Image.alpha_composite(im.convert('RGBA'), overlay)
        # Save the result
        combined.save(output_path, 'PNG')

multiplier = 1.0
# Get the data for the first image overlay
 
image_overlay = overlayData["light"][2]

# First, extract the image from the PDF
file_path = 'light.pdf'
page_number = image_overlay["pageNumber"]
rect = (image_overlay["imageLeft"] , image_overlay["imageTop"], 
        image_overlay["imageLeft"] + image_overlay["width"], 
        image_overlay["imageTop"] + image_overlay["height"])

# This function call will return the path to the extracted image
extracted_image_path = extract_image_from_pdf(file_path, page_number, rect)

# Now, add the translucent rectangle to the extracted image

top_left = (380/multiplier - image_overlay["imageLeft"], 89/multiplier - image_overlay["imageTop"])
bottom_right = (543/multiplier - image_overlay["imageLeft"], 223/multiplier - image_overlay["imageTop"])


add_translucent_rectangle(extracted_image_path, top_left, bottom_right, f"highlighted_image_page_{page_number}.png")
