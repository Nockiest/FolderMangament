from PIL import Image
import os

def create_image_collage(image_folder, output_path):
    # Get a list of all image files in the specified folder
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    if not image_files:
        print("No image files found in the specified folder.")
        return

    # Open the first image to get dimensions
    first_image_path = os.path.join(image_folder, image_files[0])
    first_image = Image.open(first_image_path)
    image_width, image_height = first_image.size

    # Create a new blank image to hold the collage
    collage = Image.new('RGB', (image_width * len(image_files), image_height))

    # Paste each image side by side into the collage
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)
        collage.paste(img, (i * image_width, 0))

    # Save the resulting collage image
    collage.save(output_path)

if __name__ == "__main__":
    # Specify the path to the folder containing image files
    image_folder_path = "./images"

    # Specify the output path for the collage image
    output_collage_path = "./collage.jpg"

    # Create the image collage
    create_image_collage(image_folder_path, output_collage_path)

    print(f"Image collage saved at: {output_collage_path}")