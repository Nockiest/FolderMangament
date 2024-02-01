import os
import easyocr
from PIL import Image

def extract_text_from_images(folder_path):
    # Create the output folder if it doesn't exist
    output_folder = "./text_output"
    os.makedirs(output_folder, exist_ok=True)

    # Create an OCR reader
    reader = easyocr.Reader(['en'])

    # Get a list of all image files in the specified folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Iterate through each image file
    for i, image_file in enumerate(image_files, 1):
        # Construct the full path to the image file
        image_path = os.path.join(folder_path, image_file)

        # Open the image using Pillow
        image = Image.open(image_path)

        # Use easyocr to extract text from the image
        results = reader.readtext(image)

        # Extracted text from results
        extracted_text = '\n'.join([result[1] for result in results])

        # Create a text file with the extracted text
        text_output_path = os.path.join(output_folder, f"text_{i}.txt")
        with open(text_output_path, "w", encoding="utf-8") as text_file:
            text_file.write(extracted_text)

        print(f"Text extracted from {image_file} and saved to {text_output_path}")

if __name__ == "__main__":
    # Specify the path to the folder containing image files
    image_folder_path = "./images"

    # Extract text from images in the specified folder
    extract_text_from_images(image_folder_path)
