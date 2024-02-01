from PIL import Image
import os

def compile_images(input_folder, output_folder, images_per_row=2, images_per_column=5):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all image files in the input folder
    image_files = [f for f in sorted(os.listdir(input_folder)) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Track the current row and column
    current_row = 0
    current_col = 0

    # Iterate through the image files and compile them
    for i, image_file in enumerate(image_files):
        # Open the current image using Pillow
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)

        # Create a new composite image if it's the start of a new set of 10 images
        if i % (images_per_row * images_per_column) == 0:
            compiled_image = Image.new("RGB", (image.width * images_per_row, image.height * images_per_column))

            # Reset the current row and column
            current_row = 0
            current_col = 0

        # Paste the current image onto the composite image
        compiled_image.paste(image, (current_col * image.width, current_row * image.height))

        # Move to the next column
        current_col += 1

        # Move to the next row if the end of the row is reached
        if current_col == images_per_row:
            current_col = 0
            current_row += 1

        # Save the compiled image when a set of 10 images is completed
        if (i + 1) % (images_per_row * images_per_column) == 0 or i == len(image_files) - 1:
            compiled_image_path = os.path.join(output_folder, f"compiled_image_{i + 1}.png")
            compiled_image.save(compiled_image_path)
            print(f"Compiled image saved: {compiled_image_path}")

if __name__ == "__main__":
    # Specify the path to the folder containing input images
    input_folder = "./input_images"

    # Specify the path to the folder where compiled images will be saved
    output_folder = "./output_compiled_images"

    # Set the number of images per row and column
    images_per_row = 1
    images_per_column = 5

    # Compile the images
    compile_images(input_folder, output_folder, images_per_row, images_per_column)
