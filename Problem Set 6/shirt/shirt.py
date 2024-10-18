import sys
import os
from PIL import Image, ImageOps

def main():

    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isfile(input_path):
        sys.exit(f"Input file '{input_path}' does not exist.")

    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Input and output files must have .jpg, .jpeg, or .png extension.")

    if input_ext != output_ext:
        sys.exit("Input and output files must have the same extension.")

    try:
        input_image = Image.open(input_path)
        shirt_image = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt image not found.")

    size = shirt_image.size
    input_image = ImageOps.fit(input_image, size)

    input_image.paste(shirt_image, shirt_image)

    try:
        input_image.save(output_path)
    except Exception as e:
        sys.exit(f"Failed to save output image: {e}")

if __name__ == "__main__":
    main()
