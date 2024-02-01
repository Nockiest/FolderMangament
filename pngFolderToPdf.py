from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os

def create_pdf_from_folder(input_folder, output_pdf_path):
    # Create a PDF file
    pdf_canvas = canvas.Canvas(output_pdf_path, pagesize=letter)

    # Iterate through all PNG files in the folder
    for file_name in sorted(os.listdir(input_folder)):
        if file_name.lower().endswith('.png'):
            # Construct the full path to the PNG file
            png_path = os.path.join(input_folder, file_name)

            # Open the PNG image using Pillow
            image = Image.open(png_path)

            # Set the size of the PDF page to match the image size
            pdf_canvas.setPageSize((image.width, image.height))

            # Draw the image onto the PDF canvas
            pdf_canvas.drawInlineImage(png_path, 0, 0, width=image.width, height=image.height)

            # Add a new page for the next image
            pdf_canvas.showPage()

    # Save the PDF file
    pdf_canvas.save()

if __name__ == "__main__":
    # Specify the path to the folder containing PNG images
    input_folder = "./images"

    # Specify the output path for the PDF
    output_pdf_path = "./output.pdf"

    # Create the PDF from the PNG images in the folder
    create_pdf_from_folder(input_folder, output_pdf_path)

    print(f"PDF created at: {output_pdf_path}")
