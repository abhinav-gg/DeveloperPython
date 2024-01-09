# Import necessary modules
from PIL import Image
import math
import requests

ASCII = " .:-=+*#%@"

def get_image(link = "https://img.freepik.com/free-photo/blue-house-with-blue-roof-sky-background_1340-25953.jpg"):
    image_path = link
    # Download image from internet
    image = Image.open(requests.get(image_path, stream=True).raw)
    return image

def convert(image, size: int = None):
    def get_ascii(pixel):
        # Get grayscale value of pixel
        grayscale = (pixel[0] + pixel[1] + pixel[2]) // 3
        # rescale from 0 to 9
        rescaled = math.floor(grayscale / 256 * len(ASCII))
        # Return ascii character
        return ASCII[rescaled]
    
    if size:
        # Resize image
        image = image.resize((size, size//3))
    ascii = []
    for y in range(image.height):
        row =""
        for x in range(image.width):
            # Get the pixel at the position
            pixel = image.getpixel((x, y))
            # Add to the ascii string
            row += get_ascii(pixel)
        ascii.append(row)
    return ascii

def display(ascii):
    print("\n".join(ascii))